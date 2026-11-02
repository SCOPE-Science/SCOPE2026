#!/usr/bin/env python3
"""Direct finite-field tests for the linear local/2-local Heisenberg theorem.
Runs with Python 3 standard library only. The theorem is proved in RESULT.md.
"""
from itertools import product
from random import Random


def rrref(a, p):
    a=[[(v%p) for v in row] for row in a]
    if not a:return a,[],0
    w=len(a[0]); piv=[]; row=0
    for col in range(w):
        i=next((i for i in range(row,len(a)) if a[i][col]%p),None)
        if i is None: continue
        a[row],a[i]=a[i],a[row]
        z=pow(a[row][col],-1,p)
        a[row]=[v*z%p for v in a[row]]
        for k in range(len(a)):
            if k != row and a[k][col]%p:
                z=a[k][col]
                a[k]=[(b-z*c)%p for b,c in zip(a[k],a[row])]
        piv.append(col);row+=1
        if row==len(a):break
    return a,piv,row

def rank(a,p):return rrref(a,p)[2]
def nullspace(a,n,p):
    r,pivs,_=rrref(a,p)
    out=[]
    for f in range(n):
        if f in pivs:continue
        v=[0]*n;v[f]=1
        for i,c in enumerate(pivs):v[c]=(-r[i][f])%p
        out.append(v)
    return out

def B(v,w,p):
    d=len(v)-1; s=0
    for i in range(d//2):
        s += v[2*i]*w[2*i+1]-v[2*i+1]*w[2*i]
    return s%p

def derive_basis(r,p):
    d=2*r; n=d+1; C=[]
    # Variables are columns of the n by n matrix, flattened row-major.
    for j in range(n):
        for k in range(j+1,n):
            x=[int(i==j) for i in range(n)]; y=[int(i==k) for i in range(n)]
            coeff=B(x,y,p)
            for t in range(n):
                row=[0]*(n*n)
                # D([e_j,e_k]) - [D(e_j),e_k]-[e_j,D(e_k)]
                row[t*n+d]=(coeff if t==d else 0)
                if t==d:
                    for a in range(n):
                        row[a*n+j]-=B([int(h==a) for h in range(n)], y,p)
                        row[a*n+k]-=B(x,[int(h==a) for h in range(n)],p)
                C.append(row)
    return nullspace(C,n*n,p)

def mat_apply(A,x,p):
    n=len(x)
    return tuple(sum(A[i*n+j]*x[j] for j in range(n))%p for i in range(n))

def belongs(E, x,y,fx,fy,p):
    if not E:return not any(fx+fy)
    vectors=[mat_apply(D,x,p)+mat_apply(D,y,p) for D in E]
    a=[[v[i] for v in vectors] for i in range(len(x)*2)]
    target=list(fx)+list(fy)
    return rank(a,p)==rank([row+[z] for row,z in zip(a,target)],p)

def is_csp(A,d,p):
    v=[[int(k==i) for k in range(d)] for i in range(d)]
    def f(i,j):
        av=[sum(A[a*d+b]*v[i][b] for b in range(d))%p for a in range(d)]
        aw=[sum(A[a*d+b]*v[j][b] for b in range(d))%p for a in range(d)]
        return (B(av+[0],v[j]+[0],p)+B(v[i]+[0],aw+[0],p))%p
    scal=f(0,1)
    return all(f(i,j)==scal*B(v[i]+[0],v[j]+[0],p)%p for i in range(d) for j in range(d))

def classify(A,r,p):
    d=2*r;n=d+1
    center=all(A[i*n+d]==0 for i in range(d))
    block=[A[i*n+j] for i in range(d) for j in range(d)]
    csp=center and is_csp(block,d,p)
    # Since omega(e1,f1)=1, any conformal symplectic B has multiplier
    # omega(B e1,f1)+omega(e1,B f1), not merely trace on V when r>1.
    v=[int(i==0) for i in range(d)];w=[int(i==1) for i in range(d)]
    av=[block[i*d] for i in range(d)];aw=[block[i*d+1] for i in range(d)]
    mu=(B(av+[0],w+[0],p)+B(v+[0],aw+[0],p))%p
    return center,csp,csp and A[d*n+d]%p==mu

def exact_small(p):
    r=1; n=3; E=derive_basis(r,p); assert len(E)==6
    xx=list(product(range(p),repeat=n))
    if p==2:
        # Exhaustively check all 512 linear maps by the *definition*.
        cases=list(product(range(p),repeat=n*n))
    else:
        rng=Random(117);cases=[tuple(rng.randrange(p) for _ in range(n*n)) for _ in range(80)]
    for A in cases:
        center,csp,der=classify(A,r,p)
        local_by_def=all(belongs(E,x,(0,)*n,mat_apply(A,x,p),(0,)*n,p) for x in xx)
        assert local_by_def==center,(p,A,'local')
        for x in xx:
            for y in xx:
                # For p=2 all matrices; for p=3 sampled maps, checked all pairs.
                good=belongs(E,x,y,mat_apply(A,x,p),mat_apply(A,y,p),p)
                assert good or not center,(p,A,x,y,'2local')
                # If map is not center preserving, pair (z,0) is a witness.
        assert center==csp
        assert der == (center and A[8] == (A[0]+A[4])%p)
    print('H3_F%d_%d_MAPS_ALL_PAIRS_OK'%(p,len(cases)))

def sampled_five():
    p=2;r=2;n=5;E=derive_basis(r,p);assert len(E)==15,len(E)
    xx=list(product(range(p),repeat=n));rng=Random(99)
    for k in range(18):
        # Construct uniformly selected block A, center-preserving in all cases.
        A=[rng.randrange(p) for _ in range(n*n)]
        for i in range(n-1):A[i*n+n-1]=0
        center,csp,der=classify(A,r,p)
        assert center
        # Exhaustive local (all 32 inputs) using linear-algebraic feasibility.
        for x in xx:
            assert belongs(E,x,(0,)*n,mat_apply(A,x,p),(0,)*n,p)
        # Evaluate all ordered pairs and compare with csp criterion.
        two=True
        for x in xx:
            for y in xx:
                good=belongs(E,x,y,mat_apply(A,x,p),mat_apply(A,y,p),p)
                if not good:two=False
                if csp:assert good,(k,x,y,'false negative')
        assert two==csp,(k,two,csp)
    # Direct construction of a basis of csp(V): solve B^T J+J B=mu J.
    d=2*r; nvar=d*d+1; eq=[]
    V=[[int(a==i) for a in range(d)] for i in range(d)]
    for i in range(d):
        for j in range(i+1,d):
            row=[0]*nvar
            for u in range(d):
                row[u*d+i] += B([int(z==u) for z in range(d)]+[0],V[j]+[0],p)
                row[u*d+j] += B(V[i]+[0],[int(z==u) for z in range(d)]+[0],p)
            row[-1] = -B(V[i]+[0],V[j]+[0],p)
            eq.append(row)
    cpbasis=nullspace(eq,nvar,p)
    assert len(cpbasis)==11
    for k in range(10):
        cs=[rng.randrange(p) for _ in cpbasis]
        Bmat=[sum(c*v[t] for c,v in zip(cs,cpbasis))%p for t in range(d*d)]
        A=[0]*(n*n)
        for i in range(d):
            for j in range(d):A[i*n+j]=Bmat[i*d+j]
            A[d*n+i]=rng.randrange(p)
        A[d*n+d]=rng.randrange(p)
        center,csp,der=classify(A,r,p)
        assert center and csp
        for x in xx:
            for y in xx:
                assert belongs(E,x,y,mat_apply(A,x,p),mat_apply(A,y,p),p)
    print('H5_F2_18_ARBITRARY_AND_10_CSP_32X32_PAIRS_OK')

if __name__=='__main__':
    exact_small(2)
    exact_small(3)
    sampled_five()
    print('HEISENBERG_LINEAR_LOCAL_2LOCAL_OK')
