"""Reproduce the double-cone reversible-mixing spectral formula and its optimum.
Run with Python 3 and numpy/scipy: python verify.py.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import linprog


def cycle(n):
    A=np.zeros((n,n))
    for i in range(n):
        A[i,(i+1)%n]=A[(i+1)%n,i]=1
    return A


def clique(n):
    return np.ones((n,n))-np.eye(n)


def biclique(m):
    n=2*m
    A=np.zeros((n,n)); A[:m,m:]=1;A[m:,:m]=1
    return A


def cube(d):
    n=1<<d
    A=np.zeros((n,n))
    for i in range(n):
        for bit in range(d):
            A[i,i^(1<<bit)]=1
    return A


def petersen():
    A=np.zeros((10,10))
    for i in range(5):
        for u,v in ((i,(i+1)%5),(i+5,((i+2)%5)+5),(i,i+5)):
            A[u,v]=A[v,u]=1
    return A


def triangular_graph(m):
    pairs=[(i,j) for i in range(m) for j in range(i+1,m)]
    n=len(pairs); A=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            if len(set(pairs[i])&set(pairs[j])):
                A[i,j]=A[j,i]=1
    return A


def rook_graph(m):
    n=m*m; A=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            if i//m==j//m or i%m==j%m: A[i,j]=A[j,i]=1
    return A


def eigen_params(A):
    n=len(A)
    d=A.sum(axis=1)
    assert np.max(np.abs(d-d[0]))<1e-12
    r=d[0]
    L=np.diag(d)-A
    w=np.linalg.eigvalsh(L)
    assert w[1]>1e-10
    lo,hi=w[1],w[-1]
    q=min(2/(lo+hi),1/r)
    kappa=max(abs(1-q*lo),abs(1-q*hi))
    return n,r,lo,hi,q,kappa


def optimum(A):
    n,r,u,v,q,k=eigen_params(A)
    if k <= 1/(n-1):
        a=1/(n+1)
    elif k < 2/(n-2):
        a=(1+k)/(n+2+2*k)
    else:
        a=1/n
    b=(1-2*a)*q
    s=max(abs(1-n*a),abs(1-(n+2)*a),k*(1-2*a))
    return a,b,s


def matrix(A,a,b):
    n=len(A)
    R=np.zeros((n+2,n+2))
    R[:2,:2]=np.eye(2)*(1-n*a)
    R[:2,2:]=a;R[2:,:2]=a
    R[2:,2:]=b*A
    for j in range(n):
        R[j+2,j+2]=1-2*a-b*sum(A[j])
    return R


def lap_critical(A):
    n,r,u,v,q,k=eigen_params(A)
    # minimize t s.t. +/- each group eigenvalue <=t
    # format a,b,t; inequalities c dot (a,b,t) <=rhs
    cons=[];rhs=[]
    def add(c,rhs0): cons.append(c);rhs.append(rhs0)
    for c in (n,n+2):
        add([-c,0,-1],-1);add([c,0,-1],1)
    for ll in (u,v):
        add([-2,-ll,-1],-1);add([2,ll,-1],1)
    add([n,0,0],1)
    add([2,r,0],1)
    lp=linprog([0,0,1],A_ub=cons,b_ub=rhs,bounds=[(0,None),(0,None),(0,None)],method='highs')
    assert lp.success,lp.message
    return lp.x


def randomized_bound(A,s,seed):
    rng=np.random.default_rng(seed)
    n=len(A)
    edges=np.argwhere(np.triu(A,1)>0)
    edges=[(i,j) for i in range(2,n+2) for j in range(i+1,n+2) if A[i-2,j-2]]+[(i,j) for i in range(2) for j in range(2,n+2)]
    N=n+2
    for _ in range(35):
        X=np.zeros((N,N))
        vals=rng.uniform(0.01,1.0,len(edges))
        for (i,j),v in zip(edges,vals): X[i,j]=X[j,i]=v
        # scaling ensures each diagonal holding probability nonnegative
        X*=float(rng.uniform(.03,1))/np.max(X.sum(axis=1))
        np.fill_diagonal(X,1-X.sum(axis=1))
        eig=np.linalg.eigvalsh(X)
        assert max(abs(eig[:-1]))>=s-2e-9, (eig,s)


if __name__=='__main__':
    cases=[]
    for n in range(3,22): cases.append((f'C{n}',cycle(n)))
    for n in range(3,10): cases.append((f'K{n}',clique(n)))
    for m in range(2,7): cases.append((f'K{m},{m}',biclique(m)))
    for d in range(2,6): cases.append((f'Q{d}',cube(d)))
    cases.append(('Petersen',petersen()))
    for m in range(6,10): cases.append((f'T({m})',triangular_graph(m)))
    for m in range(5,8): cases.append((f'R({m})',rook_graph(m)))
    eig_tests=0;lp_tests=0;random_tests=0;clipped_tests=0
    for idx,(name,A) in enumerate(cases):
        n,r,u,v,q,k=eigen_params(A)
        a,b,s=optimum(A)
        if q < 2/(u+v)-1e-12: clipped_tests+=1
        X=matrix(A,a,b)
        assert np.max(np.abs(X.sum(axis=1)-1))<1e-12
        assert X.min()>=-1e-12
        eig=np.linalg.eigvalsh(X)
        expected=sorted([1,1-n*a,1-(n+2)*a]+[1-2*a-b*w for w in np.linalg.eigvalsh(np.eye(n)*r-A)[1:]])
        assert np.max(np.abs(eig-expected))<3e-12,(name,eig,expected)
        assert abs(max(abs(eig[:-1]))-s)<2e-11,(name,s,eig)
        eig_tests+=1
        aa,bb,ss=lap_critical(A)
        assert abs(ss-s)<2e-8,(name,s,ss)
        lp_tests+=1
        if idx<12 or (n<=12 and idx%3==0):
            randomized_bound(A,s,idx+813)
            random_tests+=35
    # Exact characteristic polynomials of three rational cycle instances.
    exact=0
    for n,a,b in [(3,sp.Rational(1,4),sp.Rational(1,6)),
                  (4,sp.Rational(1,5),sp.Rational(1,5)),
                  (6,sp.Rational(1,6),sp.Rational(4,15))]:
        C=sp.zeros(n,n)
        for i in range(n):
            C[i,(i+1)%n]=C[(i+1)%n,i]=1
        M=sp.zeros(n+2,n+2)
        for i in range(2):
            M[i,i]=1-n*a
            for j in range(2,n+2):
                M[i,j]=M[j,i]=a
        for i in range(n):
            M[i+2,i+2]=1-2*a-2*b
            for j in range(n):
                if C[i,j]: M[i+2,j+2]=b
        eig=M.eigenvals()
        base=(2*sp.eye(n)-C).eigenvals()
        expected={}
        for x in [sp.Integer(1),1-n*a,1-(n+2)*a]:
            expected[x]=expected.get(x,0)+1
        zero_count=base.pop(sp.Integer(0),0)
        assert zero_count==1
        for ll,mult in base.items():
            z=1-2*a-b*ll
            expected[z]=expected.get(z,0)+mult
        assert eig==expected,(n,eig,expected)
        exact+=1
    print('PASS',len(cases),'spectral matrices,',lp_tests,'independent 3-variable LPs,',random_tests,'unrestricted asymmetric feasible allocations,',exact,'exact characteristic spectra,',clipped_tests,'clipped base-edge minimax cases')
    for name,A in cases[:9]:
        n,r,u,v,q,k=eigen_params(A)
        print(name,'kappa',round(k,9),'a',round(optimum(A)[0],9),'b',round(optimum(A)[1],9),'SLEM',round(optimum(A)[2],9))
