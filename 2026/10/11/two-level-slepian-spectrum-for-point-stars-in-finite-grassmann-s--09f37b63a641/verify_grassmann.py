"""Exact finite-field subspace enumeration and numerical singular-value checks.
Only standard-library and NumPy are needed. Finite calculations corroborate but do not replace the analytic proof.
"""
from itertools import combinations, product
import numpy as np

def points(n,p):
    out=[]
    for j in range(n):
        for tail in product(range(p),repeat=n-j-1):
            v=[0]*j+[1]+list(tail)
            out.append(tuple(v))
    return out

def normalize(v,p):
    for x in v:
        if x%p:
            inv=pow(int(x),-1,p)
            return tuple((int(y)*inv)%p for y in v)
    return None

def grass(n,k,p):
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for vals in product(range(p),repeat=len(free)):
            rows=[[0]*n for _ in range(k)]
            for i,c in enumerate(piv):rows[i][c]=1
            for (i,j),a in zip(free,vals):rows[i][j]=a
            pts=set()
            for coeff in product(range(p),repeat=k):
                v=[sum(coeff[i]*rows[i][j] for i in range(k))%p for j in range(n)]
                pp=normalize(v,p)
                if pp is not None:pts.add(pp)
            yield pts

def qint(j,p):return (p**j-1)//(p-1)

def check(n,k,p):
    pts=points(n,p); index={a:i for i,a in enumerate(pts)}
    sub=list(grass(n,k,p))
    A=np.zeros((len(sub),len(pts)),dtype=float)
    chosen=[]
    for row,S in enumerate(sub):
        for a in S:A[row,index[a]]=1
        if (1,)+(0,)*(n-1) in S:chosen.append(row)
    gram=A.T@A
    u,L=np.linalg.eigh(gram)
    assert np.min(u)>1e-7,(n,k,p,'full rank',np.min(u))
    invsqrt=(L/u**0.5)@L.T
    M=invsqrt@(A[chosen].T@A[chosen])@invsqrt
    eig=np.linalg.eigvalsh((M+M.T)/2)
    v=qint(n,p); vprime=qint(n-1,p)
    target=np.array([0]*(v-vprime)+[qint(k-1,p)/qint(n-2,p)]*(vprime-1)+[1.0])
    assert len(eig)==len(target)
    err=max(abs(eig-target))
    assert err<3e-10,(n,k,p,err,eig,target)
    assert len(sub)*qint(k,p)==len(chosen)*len(pts)
    return len(sub),len(chosen),v,err
def mult4(a,b):
    z=0
    while b:
        if b&1:z^=a
        a<<=1
        if a&4:a^=7
        b>>=1
    return z

def gf4_normalize(v):
    for a in v:
        if a:
            inv=next(b for b in range(1,4) if mult4(a,b)==1)
            return tuple(mult4(inv,x) for x in v)
    return None

def check_gf4(n,k):
    p=4
    pts=[]
    for j in range(n):
        for tail in product(range(p),repeat=n-j-1):pts.append(tuple([0]*j+[1]+list(tail)))
    pi={a:i for i,a in enumerate(pts)}
    subs=[]
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for vals in product(range(p),repeat=len(free)):
            rows=[[0]*n for _ in range(k)]
            for i,c in enumerate(piv):rows[i][c]=1
            for (i,j),a in zip(free,vals):rows[i][j]=a
            S=set()
            for coeff in product(range(p),repeat=k):
                v=[]
                for j in range(n):
                    z=0
                    for i in range(k):z ^= mult4(coeff[i],rows[i][j])
                    v.append(z)
                t=gf4_normalize(v)
                if t is not None:S.add(t)
            subs.append(S)
    A=np.zeros((len(subs),len(pts)))
    chosen=[]
    for row,S in enumerate(subs):
        for a in S:A[row,pi[a]]=1
        if (1,)+(0,)*(n-1) in S:chosen.append(row)
    gram=A.T@A
    eigen,vecs=np.linalg.eigh(gram)
    assert eigen.min()>1e-8
    invsqrt=(vecs/eigen**0.5)@vecs.T
    M=invsqrt@(A[chosen].T@A[chosen])@invsqrt
    eig=np.linalg.eigvalsh((M+M.T)/2)
    v=qint(n,p); vp=qint(n-1,p)
    target=np.array([0]*(v-vp)+[qint(k-1,p)/qint(n-2,p)]*(vp-1)+[1.])
    err=max(abs(eig-target))
    assert err<1e-10,(n,k,p,err)
    return len(subs),len(chosen),v,err

if __name__=='__main__':
    cases=[(4,2,2),(4,3,2),(5,2,2),(5,3,2),(5,4,2),(6,2,2),(6,3,2),(4,2,3),(4,3,3),(5,2,3)]
    for n,k,p in cases:
        B,Bs,v,err=check(n,k,p)
        print('CASE n=%s k=%s q=%s B=%s star=%s points=%s eig_maxerr=%.3g'%(n,k,p,B,Bs,v,err))
    B,Bs,v,err=check_gf4(4,2)
    print("CASE n=4 k=2 q=4 B=%s star=%s points=%s eig_maxerr=%.3g"%(B,Bs,v,err))
    print('VERIFY_OK cases=%s prime_power_GF4=true exact_projective_point_enumeration=true'%(len(cases)+1))
