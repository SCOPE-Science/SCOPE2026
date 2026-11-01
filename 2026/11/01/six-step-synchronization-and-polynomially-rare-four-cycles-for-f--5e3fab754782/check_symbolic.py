#!/usr/bin/env python3
"""Exhaustive finite-alphabet proof and exponential generating-function identity.
No external dependencies. Run: python3 check_symbolic.py.
"""
from itertools import product
from collections import defaultdict
from math import factorial

PAIRS = ((0,0), (0,1), (0,2), (1,1), (1,2), (2,2))
WEIGHTS = (1,2,2,1,2,1)
IDX={p:i for i,p in enumerate(PAIRS)}

def next_cap(v):
    blink=min(2,sum(v[i]*(p[0]==1)+(v[i]*(p[1]==1)) for i,p in enumerate(PAIRS)))
    def advance(a, partner):
        return (a+1) if a<2 else (2 if blink>int(partner==1) else 0)
    out=[0]*6
    for i,(a,b) in enumerate(PAIRS):
        j=IDX[tuple(sorted((advance(a,b),advance(b,a))))]
        out[j]=min(2,out[j]+v[i])
    return tuple(out)

def trap(s):
    return s[2]==s[4]==1 and s[0]==s[1]==s[3]==0

def uniform(s):
    return sum(v!=0 for v in s)==1 and bool(s[0] or s[3] or s[5])

def outcome(v):
    s=v
    for t in range(7):
        if trap(s):
            assert t==0, ('new trap entered',v,t)
            return (4,0)
        if uniform(s):return (3,t)
        if t<6:s=next_cap(s)
    raise AssertionError(('uncategorized',v,s))

# Polynomial in y=exp(z), z, represented as map (degree_y, degree_z)->integer.
def add(P,Q):
    R=P.copy()
    for k,v in Q.items():R[k]=R.get(k,0)+v
    return {k:v for k,v in R.items() if v}
def mul(P,Q):
    out=defaultdict(int)
    for (a,b),x in P.items():
        for (c,d),y in Q.items():out[a+c,b+d]+=x*y
    return {k:v for k,v in out.items() if v}

def choices(w):
    return ({(0,0):1},{(0,1):w},{(w,0):1,(0,0):-1,(0,1):-w})

GEN={}
count=0
for v in product(range(3),repeat=6):
    # n>=2, so the empty state and 1-pair states are not needed.
    if sum(v)<2:continue
    category=outcome(v)
    p={(0,0):1}
    for s,w in zip(v,WEIGHTS):p=mul(p,choices(w)[s])
    GEN[category]=add(GEN.get(category,{}),p)
    count+=1

# The coefficients are the exact EGFs of labelled initial configurations.
EXPECTED={
 (3,0):{(1,0):3,(0,1):-3,(0,0):-3},
 (3,1):{(4,0):1,(1,1):-2,(1,0):-2,(0,0):1},
 (3,2):{(9,0):1,(4,1):-6,(4,0):-2,(1,2):4,(1,1):4,(1,0):1},
 (3,3):{(4,0):1,(1,1):-2,(1,0):-2,(0,0):1},
 (3,4):{(1,1):2,(0,1):-2},
 (3,5):{(4,1):4,(1,2):-4,(1,1):-2,(0,1):-2},
 (3,6):{(4,1):2,(1,2):-4,(0,1):-2},
 (4,0):{(1,2):4},
}
assert count==3**6-7, count
assert set(GEN)==set(EXPECTED)
for key in EXPECTED:
    assert GEN[key]==EXPECTED[key], (key,GEN[key],EXPECTED[key])
# Verify that the union of all nonempty class series equals exp(9z)-1-9z.
whole={}
for v in GEN.values():whole=add(whole,v)
assert whole=={(9,0):1,(0,0):-1,(0,1):-9},whole

# Independently check the generating-function coefficients for n>=2.
def coefficient(P,n):
    answer=0
    for (r,k),a in P.items():
        if k<=n:
            if r==0 and n>k:continue
            answer+=a*(factorial(n)//factorial(n-k))*(r**(n-k))
    return answer
for n in range(2,21):
    cnt={key:coefficient(P,n) for key,P in GEN.items()}
    assert sum(cnt.values())==9**n,(n,cnt)
    assert cnt[(4,0)]==4*n*(n-1)
    assert all(v>=0 for v in cnt.values())
print('SYMBOLIC_PASS: all 722 capped states, exact eight EGFs, n=2..20 coefficients')
print('GENERATOR_POLYNOMIALS: y=exp(z), cycle/entry-time categories')
for key in sorted(EXPECTED):print(key, sorted(EXPECTED[key].items()))
