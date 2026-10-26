"""Reproduce sample spectral-gap values for hub cones; not a proof of global optimality."""
import math
import numpy as np

def cycle(n):
    return [(i,(i+1)%n) for i in range(n)]

def cube(k):
    return [(i,i^(1<<b)) for i in range(1<<k) for b in range(k) if i < (i^(1<<b))]

def analyze(n,edges,budget=1.0):
    d=2*len(edges)//n
    assert len(edges)*2 == n*d
    L=np.zeros((n,n))
    for u,v in edges:
        L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    g=np.linalg.eigvalsh(L)[1]
    beta=2*g/d
    if beta>1+1e-9:
        s=beta*budget/(n*(n+beta))
        t=2*budget/(d*(n+beta))
        theoretical=(n+1)*beta*budget/(n*(n+beta))
    else:
        s=budget/n; t=0.0; theoretical=budget/n
    L2=np.zeros((n+1,n+1))
    for v in range(n):
        L2[0,0]+=s;L2[v+1,v+1]+=s;L2[0,v+1]-=s;L2[v+1,0]-=s
    for u,v in edges:
        L2[u+1,u+1]+=t;L2[v+1,v+1]+=t;L2[u+1,v+1]-=t;L2[v+1,u+1]-=t
    observed=np.linalg.eigvalsh(L2)[1]
    assert abs(theoretical-observed)<1e-9,(n,beta,theoretical,observed)
    assert abs(n*s+len(edges)*t-budget)<1e-9
    ss=np.linspace(0,budget/n,1001)
    objective=np.minimum((n+1)*ss,ss+g*(budget-n*ss)/len(edges))
    assert max(objective)<theoretical+1e-9
    return n,d,round(beta,10),round(theoretical,10),round(s,10),round(t,10)

if __name__=='__main__':
    for n in range(3,15): print('cycle',analyze(n,cycle(n)))
    for k in range(2,7): print('cube',k,analyze(1<<k,cube(k)))
    print('Complete graph',analyze(8,[(i,j) for i in range(8) for j in range(i+1,8)]))
