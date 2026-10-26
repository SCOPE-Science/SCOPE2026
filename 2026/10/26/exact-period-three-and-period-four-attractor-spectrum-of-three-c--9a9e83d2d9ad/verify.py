#!/usr/bin/env python3
"""Exact finite support quotient and independent labeled-state checks for 3-CCA on K_{a,b}."""
from itertools import product
from collections import Counter
from math import comb

Q = (0, 1, 2)
SUPPORTS = tuple(frozenset(i for i in Q if mask & (1 << i)) for mask in range(1, 8))
STATES = tuple(product(SUPPORTS, repeat=2))

def support_step(state):
    a, b = state
    return (frozenset(((i + 1) % 3 if (i + 1) % 3 in b else i) for i in a),
            frozenset(((i + 1) % 3 if (i + 1) % 3 in a else i) for i in b))

def eventually_periodic_and_depth(s):
    trail, first = [], {}
    v = s
    while v not in first:
        first[v] = len(trail)
        trail.append(v)
        v = support_step(v)
    return frozenset(trail[first[v]:]), first[v]

all_cyclic = set()
for s in STATES:
    all_cyclic.update(eventually_periodic_and_depth(s)[0])
expected_cyclic = {
    (a,b) for a,b in STATES
    if (len(a)==len(b)==1 and a==b)
    or (len(a)==len(b)==2 and a!=b)
    or (len(a)==len(b)==3)
}
assert all_cyclic == expected_cyclic and len(all_cyclic)==10
M = [[[0]*3 for _ in range(3)] for _ in range(3)]
for s in STATES:
    v, depth = s, 0
    while v not in all_cyclic:
        v = support_step(v)
        depth += 1
    assert depth <= 2
    M[depth][len(s[0])-1][len(s[1])-1] += 1
expected_M = (
    ((3,0,0),(0,6,0),(0,0,1)),
    ((6,3,0),(3,3,3),(0,3,0)),
    ((0,6,3),(6,0,0),(3,0,0)),
)
assert tuple(tuple(tuple(row) for row in layer) for layer in M) == expected_M

# Verify exact return permutations on the supports that remain periodic.
def represented_period(A, B):
    av = {x:x for x in A}; bv={x:x for x in B}
    original=(tuple(sorted(av.items())), tuple(sorted(bv.items())))
    for t in range(1,13):
        olda=set(av.values()); oldb=set(bv.values())
        na={x:((v+1)%3 if (v+1)%3 in oldb else v) for x,v in av.items()}
        nb={x:((v+1)%3 if (v+1)%3 in olda else v) for x,v in bv.items()}
        av,bv=na,nb
        if (tuple(sorted(av.items())), tuple(sorted(bv.items())))==original:
            return t
    raise AssertionError('No return')
for s in all_cyclic:
    predicted = 1 if len(s[0])==1 else (4 if len(s[0])==2 else 3)
    assert represented_period(*s) == predicted

# Independent direct implementation on labeled vertices, not using support_step.
def full_step(x,a,b):
    out = list(x)
    for i in range(a):
        successor=(x[i]+1)%3
        if any(x[j]==successor for j in range(a,a+b)):
            out[i]=successor
    for i in range(a,a+b):
        successor=(x[i]+1)%3
        if any(x[j]==successor for j in range(a)):
            out[i]=successor
    return tuple(out)

def onto(k,n):
    return sum((-1)**j*comb(k,j)*(k-j)**n for j in range(k+1))

def expected(a,b):
    A2,B2=onto(2,a),onto(2,b)
    A3,B3=onto(3,a),onto(3,b)
    d0=3+6*A2*B2+A3*B3
    d1=6+3*(A2+B2)+3*A2*B2+3*(A2*B3+A3*B2)
    d2=6*(A2+B2)+3*(A3+B3)
    return d0,d1,d2,{1:3,3:A3*B3,4:6*A2*B2}

seen_configurations=0
parameter_pairs=[]
for a in range(1,8):
    for b in range(1,8):
        if a+b>7 and (a,b)!=(4,4):
            continue
        depth_count=Counter(); period_count=Counter()
        for x in product(Q,repeat=a+b):
            x=tuple(x)
            cur=x
            first={}
            t=0
            while cur not in first:
                first[cur]=t
                cur=full_step(cur,a,b)
                t+=1
                if t>20:raise AssertionError(('Long orbit',a,b,x))
            depth=first[cur]
            period=t-depth
            assert depth<=2 and period in (1,3,4)
            depth_count[depth]+=1
            if depth==0:period_count[period]+=1
            seen_configurations+=1
        d0,d1,d2,ps=expected(a,b)
        assert tuple(depth_count[i] for i in (0,1,2))==(d0,d1,d2),(a,b,depth_count,(d0,d1,d2))
        assert dict(period_count)=={k:v for k,v in ps.items() if v},(a,b,period_count,ps)
        assert d0+d1+d2==3**(a+b)
        parameter_pairs.append((a,b))

print('SUPPORT_STATES=49')
print('RECURRENT_SUPPORT_STATES=10')
print('SUPPORT_DEPTH_MATRICES:', expected_M)
print('PERIODS=', {1:3,3:1,4:6}, '(support states)')
print('FULL_PARAMETER_PAIRS=',len(parameter_pairs))
print('FULL_CONFIGURATIONS=',seen_configurations)
print('EXACT_F14_EQUALS_F2_AND_RECURRENT_COUNTS=PASS')
print('CHECKS=PASS')
