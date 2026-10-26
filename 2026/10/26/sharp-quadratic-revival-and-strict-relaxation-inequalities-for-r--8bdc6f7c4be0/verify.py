"""Finite reproducibility checks for the transposition-walk revival/relaxation theorem."""
import math
import itertools
from functools import lru_cache
import numpy as np
from scipy.linalg import expm

@lru_cache(None)
def partitions(n, top=None):
    if n==0:
        return ((),)
    if top is None: top=n
    return tuple((x,)+p for x in range(min(n,top),0,-1) for p in partitions(n-x,x))

def content(part):
    return sum(j-i for i,row in enumerate(part) for j in range(row))

def dimension(part):
    hooks=[]
    for i,row in enumerate(part):
        for j in range(row):
            hooks.append(row-j+sum(1 for r in part[i+1:] if r>j))
    return math.factorial(sum(part))//math.prod(hooks)

count=0
for n in range(2,19):
    C=n*(n-1)//2
    pts=partitions(n)
    gaps=[C-content(p) for p in pts if p!=(n,)]
    g=math.gcd(*gaps)
    expected=(2 if n==2 else 3 if n==3 else 2 if n==4 else 1)
    assert g==expected,(n,g)
    assert sum(dimension(p)**2 for p in pts)==math.factorial(n)
    for p in pts:
        assert abs(content(p))<=C
    count+=3

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
for n in (3,4):
    els=list(itertools.permutations(range(n)))
    index={p:i for i,p in enumerate(els)}
    e=index[tuple(range(n))]
    C=n*(n-1)//2
    H=np.zeros((len(els),len(els)))
    for i in range(n):
        for j in range(i+1,n):
            tau=list(range(n));tau[i],tau[j]=tau[j],tau[i];tau=tuple(tau)
            for k,p in enumerate(els):
                H[index[compose(tau,p)],k]+=1/C
    assert np.linalg.norm(H-H.T)<1e-12
    d=np.zeros(len(els));d[e]=1
    t=1.23;gamma=.7
    classical=expm(gamma*t*(H-np.eye(len(els))))@d
    u=1/len(els)
    D0=sum((classical-u)**2)
    T=(2*math.pi if n==3 else 6*math.pi)
    for s in [0,.02,.2,.9,3,T/2,T,T+.09,2*T]:
        U=expm(-1j*s*H)
        Q=abs(U@d)**2
        mixed=abs(U)**2@classical
        D=sum((mixed-u)**2)
        assert D<=D0+3e-11,(n,s,D,D0)
        equal=min(abs(s-round(s/T)*T),T)>1e-7
        if equal: assert D<D0-1e-9,(n,s,D,D0)
        else: assert abs(D-D0)<1e-9
        assert abs(sum(Q)-1)<1e-10
        count+=4
    assert np.linalg.norm(expm(-1j*T*H)-np.eye(len(els)))<1e-9
    count+=1
    delta=.002
    U=expm(-1j*delta*H)
    mixed=abs(U)**2@classical
    D=sum((mixed-u)**2)
    expected=(2/(C*math.factorial(n)))*sum(dimension(p)**2*(1-content(p)/C)*math.exp(-2*gamma*t*(1-content(p)/C)) for p in partitions(n) if p!=(n,))
    assert abs((D0-D)/delta**2-expected)<1e-4,(n,(D0-D)/delta**2,expected)
    count+=1
print('PASS',count,'finite checks; n=2..18 content gcd + Plancherel; n=3,4 matrix dynamics, exact periods, strictness and curvature')
