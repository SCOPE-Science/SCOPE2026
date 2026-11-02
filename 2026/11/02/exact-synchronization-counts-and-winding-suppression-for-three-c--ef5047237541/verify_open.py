#!/usr/bin/env python3
"""Direct CCA and transfer comparison on finite open ladders."""
from itertools import product

M=((3,2,1),(2,3,2),(1,2,3))

def transfer(n):
    v=(1,1,1)
    for _ in range(n-1):
        v=tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
    return 3*sum(v)

def direct(n):
    neighbors=[]
    for p in range(2):
        for i in range(n):
            xs=[(1-p)*n+i]
            if i>0:xs.append(p*n+i-1)
            if i+1<n:xs.append(p*n+i+1)
            neighbors.append(tuple(xs))
    ans=0
    for raw in product(range(3),repeat=2*n):
        x=raw
        for _ in range(n):
            y=list(x)
            for j,v in enumerate(x):
                if any(x[k]==(v+1)%3 for k in neighbors[j]):
                    y[j]=(v+1)%3
            x=tuple(y)
        if len(set(x))==1: ans+=1
    return ans

for n in (2,3,4,5,6):
    a,b=transfer(n),direct(n)
    print(n,a,b,a==b,flush=True)
    assert a==b
print('PASS')
