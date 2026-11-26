"""Exact local and global checks for two Gr(2,6) secant instances.

NumPy proposes centers and preconditioners; all certificate inequalities
after rationalization use rational arithmetic, not floating-point tolerances.
Run with Python 3, NumPy and SymPy.
"""
import itertools as it
from fractions import Fraction as Q
import math
import numpy as np

A=[[Q(-7,5)+Q(2,5)*i+Q(2,25)*j for j in range(4)] for i in range(8)]
B=[g[:] for g in A]
B[3]=list(map(Q,['6/25','13/50','7/25','3/10']))
B[4]=list(map(Q,['1/25','4/25','11/25','3/5']))
B[5][0]=Q(61,100)

def interval_check(G):
    assert len(G)==8 and all(g==sorted(g) and len(g)==4 for g in G)
    assert len(set(it.chain.from_iterable(G)))==32
    return [(i,j) for i,j in it.combinations(range(8),2) if max(G[i][0],G[j][0])<min(G[i][-1],G[j][-1])]

P=list(it.combinations(range(6),2)); PI={e:i for i,e in enumerate(P)}
def rows(G):
    for g in G:
        p=[Q(1)]
        for t in g: p=[v-t*w for v,w in zip([Q(0)]+p,p+[Q(0)])]
        a,b=p+[Q(0)],[Q(0)]+p
        yield [a[i]*b[j]-a[j]*b[i] for i,j in P]

def reduced(M,p):
    rank=0;piv=[]
    for col in range(len(M[0])):
        pivot=next((r for r in range(rank,len(M)) if M[r][col]),None)
        if pivot is None: continue
        M[rank],M[pivot]=M[pivot],M[rank]; inv=pow(M[rank][col],-1,p)
        M[rank]=[x*inv%p for x in M[rank]]
        for r,row in enumerate(M):
            if r!=rank and row[col]:
                z=row[col]; M[r]=[(a-z*b)%p for a,b in zip(row,M[rank])]
        piv.append(col);rank+=1
        if rank==len(M): break
    return piv

def exclude_infinity(R):
    p=1009
    M=[[x.numerator*pow(x.denominator,-1,p)%p for x in r] for r in R]+[[1]+[0]*14]
    piv=reduced(M,p); assert len(piv)==9
    free=[j for j in range(15) if j not in piv]
    L=[[int(j==k) for k in free] for j in range(15)]
    for j,k in enumerate(piv): L[k]=[-M[j][col]%p for col in free]
    quad=[]
    for a,b,c,d in it.combinations(range(6),4):
        D={}
        for sign,e,f in [(1,(a,b),(c,d)),(-1,(a,c),(b,d)),(1,(a,d),(b,c))]:
            for i,x in enumerate(L[PI[e]]):
                for j,y in enumerate(L[PI[f]]):
                    key=tuple(sorted((i,j)));D[key]=(D.get(key,0)+sign*x*y)%p
        quad.append(D)
    mon4=list(it.combinations_with_replacement(range(6),4)); idx={m:i for i,m in enumerate(mon4)}
    mat=[]
    for D in quad:
        for mi in it.combinations_with_replacement(range(6),2):
            row=[0]*len(mon4)
            for mj,v in D.items(): row[idx[tuple(sorted(mi+mj))]]=v
            mat.append(row)
    rank=len(reduced(mat,p));print('chart complement: GF',p,'ranks',len(piv),rank,'size',len(mon4),flush=True)
    assert rank==len(mon4)==126

def chart(R):
    C=[];L=[];H=[]
    for row in R:
        D=dict(zip(P,row)); C.append(D[0,1])
        L.append([-D[1,i] for i in range(2,6)]+[D[0,i] for i in range(2,6)])
        h=[[Q(0)]*8 for _ in range(8)]
        for i,j in it.combinations(range(4),2):
            h[i][j+4]=h[j+4][i]=D[i+2,j+2]/2
            h[j][i+4]=h[i+4][j]=-D[i+2,j+2]/2
        H.append(h)
    return C,L,H

def float_functions(pol):
    C,L,H=(np.array(x).astype(float) for x in pol)
    return (lambda x: C+L@x+np.einsum('kij,i,j->k',H,x,x),
            lambda x: L+2*np.einsum('kij,j->ki',H,x))

def centers(pol,is_A):
    F,J=float_functions(pol); rng=np.random.default_rng(321); saved=[]
    real=rng.uniform(-3,3,(2200,8)); nonreal=rng.standard_normal((2200,8))+1j*rng.standard_normal((2200,8))
    # Interleave real and complex starts for the overlapping instance.
    starts=real if is_A else (x for pair in zip(real,nonreal) for x in pair)
    for x in starts:
        for _ in range(60):
            try: step=np.linalg.solve(J(x),F(x))
            except np.linalg.LinAlgError: break
            x=x-step
            if np.max(np.abs(step))<2e-11:
                if all(np.max(np.abs(x-y))>1e-4 for y in saved): saved.append(x)
                break
        if len(saved)==14: return saved
    raise RuntimeError(len(saved))

from sympy import QQ_I
Z=QQ_I
def upper(x):
    # rigorous absolute-value upper endpoint, in multiples of 10^-30
    a=x.x*x.x+x.y*x.y; d=10**30
    return Q(math.isqrt((int(a.numerator)*d*d)//int(a.denominator))+1,d) if a else Q(0)

def rat(x):
    d=10**12
    return Z(QQ_I.dom(int(round(x.real*d)),d),QQ_I.dom(int(round(x.imag*d)),d))

def certify(pol,X,alpha_limit):
    C,L,H=([Z.convert(c) for c in pol[0]],[[Z.convert(c) for c in row] for row in pol[1]],[[[Z.convert(c) for c in row] for row in mat] for mat in pol[2]])
    _,Jfloat=float_functions(pol)
    pairs=[(i,j) for i in range(8) for j in range(8)]
    rad=Q(1,10**6); covered=[]; mx=[Q(0)]*3
    for t in X:
        if max(abs(x.imag) for x in t)<1e-6: t=t.real
        x=list(map(rat,t)); Y=[[rat(v) for v in row] for row in np.linalg.inv(Jfloat(t))]
        J=[[L[k][i]+2*sum((H[k][i][j]*x[j] for j in range(8)),Z.zero) for i in range(8)] for k in range(8)]
        F=[C[k]+sum((L[k][i]*x[i] for i in range(8)),Z.zero)+sum((H[k][i][j]*x[i]*x[j] for i,j in pairs),Z.zero) for k in range(8)]
        def matmult(row,col): return sum((u*v for u,v in zip(row,col)),Z.zero)
        E=[[Z.convert(int(i==j))-matmult(Y[i],[J[k][j] for k in range(8)]) for j in range(8)] for i in range(8)]
        e=max(sum(map(upper,row)) for row in E)
        beta=max(upper(matmult(row,F)) for row in Y)
        h=max(sum(upper(matmult(row,[H[k][i][j] for k in range(8)])) for i,j in pairs) for row in Y)
        lip=e+2*rad*h
        assert lip<1 and beta+lip*rad<rad
        alpha2=8*beta*h/(1-e)**2
        assert alpha2<alpha_limit
        mx=[max(v,w) for v,w in zip(mx,[beta,lip,alpha2])]
        covered.append(x)
    assert len(covered)==14
    def q(p): return Q(int(p.numerator),int(p.denominator))
    def lower(z): return max(abs(q(z.x)),abs(q(z.y)))
    sep=min(max(lower(a-b) for a,b in zip(x,y)) for x,y in it.combinations(covered,2))
    assert sep>2*rad
    real=[x for x in covered if all(not v.y for v in x)]
    non=[x for x in covered if x not in real]
    assert all(max(abs(q(z.y)) for z in x)>rad for x in non)
    print('local:', len(real),len(non), 'max beta, contraction bound, alpha2',list(map(float,mx)), 'sup norm separation lower',float(sep),flush=True)
    return len(real),len(non)

if __name__=='__main__':
    assert interval_check(A)==[] and interval_check(B)==[(3,4)]
    assert B[3][-1]-B[3][0]==Q(3,50) and B[4][0]<B[3][0]<B[3][-1]<B[4][-1]
    for G in [A,B]:
        R=list(rows(G));exclude_infinity(R);pol=chart(R)
        assert certify(pol,centers(pol,G is A),Q(43,10**10) if G is A else Q(12,1000))==((14,0) if G is A else (12,2))
