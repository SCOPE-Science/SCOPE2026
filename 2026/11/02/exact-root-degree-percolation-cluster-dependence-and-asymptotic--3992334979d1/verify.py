"""Exact checks for recursive-tree root cluster and original root degree."""
from fractions import Fraction as F
from itertools import product
from math import factorial

def rising(x,k):
    y=F(1)
    for j in range(k):y*=x+j
    return y

def binom(x,k):
    y=F(1)
    for j in range(k):y*=x-j
    return y/factorial(k)

def mul(A,B,N):
    C=[F(0)]*(N+1)
    for j,a in enumerate(A):
        for k,b in enumerate(B[:N-j+1]):C[j+k]+=a*b
    return C

def formula(n,p,u,z):
    N=n-1
    # Expand the proposed closed bivariate generating derivative to x^N.
    a=[rising(z*(1-p),j)/factorial(j) for j in range(N+1)]
    h=[F(0)]+[u*binom(p,j)*((-1)**j) for j in range(1,N+1)]
    B=[F(0)]*(N+1)
    H=[F(1)]+[F(0)]*N
    for k in range(N+1):
        c=((-1)**k)*rising(z,k)/factorial(k)
        for j in range(N+1):B[j]+=c*H[j]
        H=mul(H,h,N)
    return u*mul(a,B,N)[N]

def dp(n,p):
    state={(1,0):F(1)}
    for size in range(1,n):
        nxt={}
        def add(key,pr):nxt[key]=nxt.get(key,F(0))+pr
        for (r,k),w in state.items():
            add((r+1,k+1),w*p/size)
            add((r,k+1),w*(1-p)/size)
            add((r+1,k),w*p*(r-1)/size)
            add((r,k),w*(size-1-p*(r-1))/size)
        state=nxt
        assert sum(state.values())==1
    return state

def exhaustive(n,p):
    # Directly enumerate independent parent choices and edge retentions.
    hist={}
    den=factorial(n-1)
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        deg=sum(v==1 for v in parents)
        for bits in product((0,1),repeat=n-1):
            connected={1}
            for j,(par,edge) in enumerate(zip(parents,bits),2):
                if edge and par in connected:connected.add(j)
            r=len(connected)
            wt=F(1,den)
            for edge in bits:wt*=p if edge else 1-p
            hist[r,deg]=hist.get((r,deg),F(0))+wt
    return hist

def exact_cov(n,p):
    a=F(1)
    for j in range(1,n):a*=1+p/j
    s=sum((F(1,j)-1/(j+p) for j in range(1,n)), F(0))
    return a*(1-s)-1

checks=0
for p in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
    for n in range(1,10):
        P=dp(n,p)
        checks+=1
        ER=sum(w*r for (r,k),w in P.items())
        EK=sum(w*k for (r,k),w in P.items())
        ERK=sum(w*r*k for (r,k),w in P.items())
        assert ERK-ER*EK==exact_cov(n,p),(n,p,ERK-ER*EK,exact_cov(n,p));checks+=1
        assert (ERK-ER*EK>0) == (F(0)<p<F(1) and n>=3);checks+=1
        for u,z in [(F(1),F(1)),(F(2),F(3)),(F(3,2),F(4,3)),(F(5,4),F(7,3))]:
            moment=sum(w*(u**r)*(z**k) for (r,k),w in P.items())
            assert moment==formula(n,p,u,z),(n,p,u,z,moment,formula(n,p,u,z));checks+=1
        if n<=6:
            assert {k:v for k,v in P.items() if v}=={k:v for k,v in exhaustive(n,p).items() if v},(n,p);checks+=1
print(f'PASS {checks} exact assertions; includes independent full parent/edge enumeration through n=6')
