"""Numerical checks of the complete-multipartite heat derivative norm formulas."""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def graph(parts):
    n=sum(parts)
    idx=np.repeat(range(len(parts)),parts)
    adj=(idx[:,None]!=idx[None,:]).astype(float)
    return np.diag(adj.sum(axis=1))-adj

def profile(parts,t):
    n=sum(parts)
    return 2*max((n-m)/m*((m-1)*np.exp(-(n-m)*t)+np.exp(-n*t)) for m in parts)

def exact_rows(parts,t):
    n=sum(parts)
    return np.concatenate([np.full(m,2*(n-m)/m*((m-1)*np.exp(-(n-m)*t)+np.exp(-n*t))) for m in parts])

checks=0
for n in range(2,15):
    for a in range(1,n):
        for b in range(1,n-a+1):
            z=n-a-b
            if z<0:continue
            parts=([a,b] if z==0 else [a,b,z])
            if min(parts)<1:continue
            L=graph(parts)
            for t in (0,1e-6,.002,.013,.1,.3,1,3):
                M=L@expm(-t*L)
                rows=np.sum(abs(M),axis=1)
                target=exact_rows(parts,t)
                assert np.max(abs(rows-target))<1e-8,(parts,t,rows,target)
                assert abs(np.linalg.norm(M,ord=np.inf)-profile(parts,t))<1e-8
                assert t*profile(parts,t)<=2*(n-1)/(np.e*n)+2e-12
                checks+=3
for n in range(3,30):
    for small in range(1,n-1):
        for big in range(small+1,n):
            def h(m,t):
                return (n-m)/m*(1+(m-1)*np.exp(m*t))
            root=brentq(lambda t: np.log(h(big,t))-np.log(h(small,t)), 0,20,xtol=1e-12)
            assert root>0 and h(small,root*0.99)>h(big,root*0.99) and h(small,root*1.01)<h(big,root*1.01)
            checks+=1
ex1=[2,4,4,4,6]
ex2=[2,2,4,6,6]
assert sum(ex1)==sum(ex2)==20
for t in np.linspace(0,1,71):
    assert abs(profile(ex1,t)-profile(ex2,t))<1e-14
    checks+=1
assert not np.allclose(np.sort(np.linalg.eigvalsh(graph(ex1))),np.sort(np.linalg.eigvalsh(graph(ex2))))
checks+=1
# Correct equality evaluated at t=1/n:
for n in range(2,50):
    assert abs(profile([1,n-1],1/n)/n-2*(n-1)/(np.e*n))<1e-13
    checks+=1
print('PASS',checks)
