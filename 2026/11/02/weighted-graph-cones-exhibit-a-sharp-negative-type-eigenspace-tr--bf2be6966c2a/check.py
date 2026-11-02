"""Independent finite-matrix and spectral checks for a weighted graph-cone negative-type theorem.

Requires numpy; constructs powered distance matrices from graph edges and
computes the eigenvalues of their restrictions to zero-sum vectors.
These finite tests do not establish the all-graph theorem.
"""
import math
import itertools
import numpy as np
from scipy.optimize import brentq
import sympy as sp

def hamming(d, q):
    vertices = list(itertools.product(range(q), repeat=d))
    n=len(vertices)
    A=np.zeros((n,n),dtype=float)
    for i in range(n):
        for j in range(i):
            if sum(a!=b for a,b in zip(vertices[i],vertices[j]))==1:
                A[i,j]=A[j,i]=1
    return A

def cycle(n):
    A=np.zeros((n,n))
    for j in range(n):
        A[j,(j+1)%n]=A[(j+1)%n,j]=1
    return A

def circulant(n,steps):
    A=np.zeros((n,n))
    for i in range(n):
        for t in steps: A[i,(i+t)%n]=A[(i+t)%n,i]=1
    return A

def petersen():
    pairs=list(itertools.combinations(range(5),2))
    n=len(pairs); A=np.zeros((n,n))
    for i,x in enumerate(pairs):
        for j,y in enumerate(pairs):
            if i<j and set(x).isdisjoint(y): A[i,j]=A[j,i]=1
    return A

def restrictions(A,h,p):
    N=A.shape[0]
    D=np.zeros((N+1,N+1))
    D[:N,:N]=A+(2*h)**p*(np.ones((N,N))-np.eye(N)-A)
    D[:N,N]=D[N,:N]=h**p
    # A basis of coefficients of zero sum is [e_i-e_hub].
    R=np.vstack([np.eye(N),-np.ones((1,N))])
    gram=R.T@D@R
    return np.linalg.eigvalsh(gram)

def check(A,label):
    N=len(A)
    k=np.sum(A[0]); assert np.max(abs(np.sum(A,axis=1)-k))<1e-12
    s=-np.linalg.eigvalsh(A)[0]; assert s>=2-1e-10
    mult=np.sum(abs(np.linalg.eigvalsh(A)+s)<1e-7)
    pc=math.log2(2*N*s/(s*(N-1)-k))
    hc=(s/(s-1))**(1/pc)/2
    assert .5<hc<1
    def f(p,h):return k+(N-1-k)*(2*h)**p-2*N*h**p
    for h in [.5,(.5+hc)/2,hc,(1+hc)/2,1.]:
        p0=brentq(lambda p:f(p,h),.001,20)
        p1=float('inf') if h==.5 else math.log(s/(s-1))/math.log(2*h)
        p=min(p0,p1)
        eig=restrictions(A,h,p)
        tol=2e-6
        expected=(1 if h<=hc+1e-10 else 0)+(mult if h>=hc-1e-10 else 0)
        nullity=sum(abs(eig)<tol)
        assert nullity==expected,(label,h,p,nullity,expected,eig[:5])
        assert eig[-1]<tol
        for ptry in [p*.8,p*.92]: assert restrictions(A,h,ptry)[-1]<-1e-7
        assert restrictions(A,h,p*1.05)[-1]>1e-7
        if h==hc: assert abs(p-pc)<1e-9
    # At the crossover, powered distances are rational when s is integral.
    # This exact reconstruction checks the critical nullity without a floating tolerance.
    if abs(s-round(s))<1e-9 and N<=27:
        si=int(round(s)); ki=int(round(k))
        c=sp.Rational(si,si-1)
        b=sp.Rational(si*(N-1)-ki,2*N*(si-1))
        raw=sp.zeros(N,N)
        for i in range(N):
            for j in range(N):
                if i!=j:raw[i,j]=1 if A[i,j] else c
        G=sp.Matrix(N,N,lambda i,j:raw[i,j]-2*b)
        rank=G.rank()
        assert N-rank==mult+1,(label,'exact rational rank',rank)
    print(label, 'N',N,'degree',int(k),'s',round(s,9),'m',int(mult),'h_cross',round(hc,9),'p_cross',round(pc,9),'PASS')

if __name__=='__main__':
    for d,q in [(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)]:check(hamming(d,q),f'H({d},{q})')
    check(cycle(4),'C4')
    check(cycle(6),'C6')
    check(petersen(),'Petersen')
    for n in [7,10,11]:check(circulant(n,[1,2]),f'C{n}(1,2)')
    print('CHECK_OK: twelve adjacency-matrix families, five cone weights each, independent centered spectral reconstructions and exact-rational crossover ranks')
