"""Deterministic exact checks for uniform recursive-tree path/leaf moments."""
from fractions import Fraction as Q
from itertools import product
from math import factorial

def enumerate_moments(n):
    total=0; leaves=0; joint=0; leaf_depth=0; sq_leaves=0
    num=0
    # n vertices: parent of i in 1..i-1
    for parents in product(*(range(1,i) for i in range(2,n+1))):
        depth=[0]*(n+1)
        out=[0]*(n+1)
        for i,k in enumerate(parents,2):
            depth[i]=1+depth[k]
            out[k]+=1
        t=sum(depth);l=sum(1 for i in range(1,n+1) if not out[i]);a=sum(depth[i] for i in range(1,n+1) if not out[i])
        total+=t; leaves+=l; joint+=l*t; leaf_depth+=a; sq_leaves+=l*l; num+=1
    assert num==factorial(n-1)
    return (Q(total,num),Q(leaves,num),Q(joint,num),Q(leaf_depth,num),Q(sq_leaves,num))

def moments_closed(n):
    H=sum((Q(1,k) for k in range(1,n+1)),Q())
    t=n*(H-1)
    l=Q(n,2)
    a=Q(n,2)*H-Q(n,4)
    cov=-Q(n-2,4)
    return t,l,t*l+cov,a

checks=0
for n in range(2,10):
    t,l,tl,a,l2=enumerate_moments(n)
    et,el,etl,ea=moments_closed(n)
    assert (t,l,tl,a)==(et,el,etl,ea),(n,(t,l,tl,a),(et,el,etl,ea))
    checks+=4
    assert l2-l*l==(Q(n,12) if n>=3 else 0)
    checks+=1

# Independent moment recurrences checked across many n, plus martingale identities.
for n in range(2,500):
    t,l,tl,a=moments_closed(n)
    tt,ll,ttl,aa=moments_closed(n+1)
    assert tt==t+1+t/n; checks+=1
    assert ll==l+1-l/n; checks+=1
    assert aa==(1-Q(1,n))*a+1+t/n; checks+=1
    assert ttl==tl+t+l+1+(t-l-a)/n; checks+=1
    assert (ttl-tt*ll)-(tl-t*l)==-Q(1,4);checks+=1

print('EXACT_OK',checks,'assertions; enumerated n=2..9, 499 recurrence transitions')
