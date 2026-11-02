#!/usr/bin/env python3
"""Finite checks of the primitive-pair distribution for B_n(-2); Python standard library."""
from collections import deque
from math import gcd

A = ((-2, 0), (1, 1))
B = ((1, 1), (0, -2))

def action(M, x, m):
    return ((M[0][0]*x[0]+M[0][1]*x[1])%m,
            (M[1][0]*x[0]+M[1][1]*x[1])%m)

def factors(m):
    n=m;p=2;res=[]
    while p*p<=n:
        if n%p==0:
            res.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:res.append(n)
    return res

def expected_size(m):
    ans=m*m
    for p in factors(m):ans=ans//(p*p)*(p*p-1)
    return ans

def stern_values(N):
    b=[0]*(N+2);b[1]=1
    for n in range(2,N+2):
        if n%2==0:b[n]=-2*b[n//2]
        else:b[n]=b[n//2]+b[n//2+1]
    return b

# Check that the exact integer recurrence agrees with leading-1 binary matrix updates.
N=50000
b=stern_values(N)
for n in range(1,N+1):
    x=(1,-2)
    for bit in bin(n)[3:]:
        if bit=='0':x=(-2*x[0],x[0]+x[1])
        else:x=(x[0]+x[1],-2*x[1])
    assert x==(b[n],b[n+1]),(n,x,b[n:n+2])

# The finite directed graph is proved irreducible symbolically in RESULT.md;
# this breadth-first check is only finite corroboration of its orbit claim.
mods=[m for m in range(3,62,2)] + [65,75,81,99,105,121]
seen_total=0
for m in mods:
    origin=(1%m,(-2)%m)
    seen={origin}; q=deque([origin])
    while q:
        u=q.popleft()
        for mat in (A,B):
            v=action(mat,u,m)
            assert gcd(v[0],v[1],m)==1
            if v not in seen:seen.add(v);q.append(v)
    expected={(u,v) for u in range(m) for v in range(m) if gcd(u,v,m)==1}
    assert seen==expected,(m,len(seen),len(expected))
    assert len(seen)==expected_size(m)
    assert action(A,(0,1),m)==(0,1)
    seen_total+=len(seen)

# Check exact marginals from the primitive-pair formula, independent of BFS.
for m in mods:
    size=expected_size(m)
    for r in range(m):
        actual=sum(gcd(r,v,m)==1 for v in range(m))
        pred=m
        for p in factors(m):
            if r%p==0:pred=pred//p*(p-1)
        assert actual==pred,(m,r,actual,pred)
        assert size>0
print('VERIFY_OK recurrence_indices=%d moduli=%d primitive_states=%d' % (N,len(mods),seen_total))
