#!/usr/bin/env python3
"""Exact verification of the eight-class Stern dyadic residue generating functions.

No nonstandard dependencies; integer arithmetic and 48-state complete certificates.
"""
from collections import deque
from fractions import Fraction

MOD = 8
STATES = [(a,b) for a in range(8) for b in range(8) if a % 2 or b % 2]
assert len(STATES) == 48
INDEX = {s:i for i,s in enumerate(STATES)}
NEXT = []
for a,b in STATES:
    NEXT.append((INDEX[(a,(a+b)%8)], INDEX[((a+b)%8,b)]))

# Each group stores Q_j(T), numerator P_j(T), all in ascending coefficients.
def mul(f,g):
    o = [0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):o[i+j]+=x*y
    return o

def prod(*factors):
    v=[1]
    for f in factors:v=mul(v,list(f))
    return v

L1 = [1,-1]; LP=[1,1]; L2=[1,-2]
Q0 = prod(L1,LP,L2,[1,-1,2],[1,0,-1,0,4])
Q1 = prod(L1,LP,L2,[1,0,1],[1,-2,3,-4,4])
Q2 = prod(L1,L1,LP,L2,[1,-1,2])
Q4 = prod(LP,L2,[1,-1,2],[1,0,-1,0,4])
Q=[Q0,Q1,Q2,Q1,Q4,Q1,Q2,Q1]
N=[
[1,-2,0,2,-1,-6,6,0,-8],
[0,1,-2,2,-4,1,6,-8,12,-16],
[0,0,1,-2,1,0,-2],
[0,0,0,2,-4,4,-4,2,4,-8],
[0,0,0,0,2],
[0,0,0,0,2,-2,2,-2,-4,8],
[0,0,0,0,0,0,2],
[0,0,0,0,0,4,-8,12,-12,16],
]
assert all(q[0]==1 and len(q)>=len(n) for q,n in zip(Q,N))

# Row-vector A powers: (w A)_i = sum of w at both descendants.
def row_mul(w):
    return [w[a]+w[b] for a,b in NEXT]

# The reciprocity Q(T) = T^d D(1/T) gives the row annihilator.
def certify_row(q,j,shift=0):
    coefficients=list(reversed(q))
    v=[int(a==j) for a,b in STATES]
    for _ in range(shift): v=row_mul(v)
    total=[0]*48
    for c in coefficients:
        for k in range(48):total[k]+=c*v[k]
        v=row_mul(v)
    return all(x==0 for x in total)

for j in range(8):
    if j != 4: assert certify_row(Q[j],j, int(j in (1,2,3,5,6,7))), ('row certificate',j)
# At residue 4 a one-factor stronger row identity holds; its shorter
# scalar recurrence is certified from the first nine values below.
assert certify_row(Q0,4)

# All states are reachable from (0,1), and the directed graph is strongly connected.
origin=INDEX[(0,1)]
reverse=[[] for _ in STATES]
for a,(i,j) in enumerate(NEXT):reverse[i].append(a);reverse[j].append(a)
for use_reverse in (False,True):
    seen={origin};todo=deque([origin])
    while todo:
        k=todo.popleft()
        for v in (reverse[k] if use_reverse else NEXT[k]):
            if v not in seen:seen.add(v);todo.append(v)
    assert len(seen)==48
assert NEXT[INDEX[(0,1)]][0]==INDEX[(0,1)]  # self loop -> aperiodic
assert all(sum(int(v==j) for a,b in NEXT for v in (a,b))==2 for j in range(48))

# State distributions, compared independently with direct enumeration.
v=[0]*48;v[origin]=1
H=[]
for r in range(19):
    h=[0]*8
    for k,(a,b) in enumerate(STATES):h[a]+=v[k]
    assert sum(h)==2**r
    H.append(h)
    w=[0]*48
    for k,(i,j) in enumerate(NEXT):w[i]+=v[k];w[j]+=v[k]
    v=w

# Verify all eight generating-function numerators from 18 terms.
for j in range(8):
    q=Q[j]; d=len(q)-1
    for r in range(18):
        val=sum(q[k]*H[r-k][j] for k in range(min(r,d)+1))
        valN=N[j][r] if r<len(N[j]) else 0
        assert val==valN, (j,r,val,valN)

# For residue four, P0 recurrence plus first nine terms implies Q4
# recurrence globally, as Q0=(1-T)Q4.
assert mul(Q4,L1)==Q0

# Independent direct Stern-value recurrence, never using transfer states.
s=[0,1]
for n in range(2,2**18):
    s.append(s[n//2] if n%2==0 else s[n//2]+s[n//2+1])
for r in range(18):
    direct=[0]*8
    for val in s[:2**r]:direct[val%8]+=1
    assert direct==H[r],('direct census',r)

# Check rational-function denominators are reduced via rational polynomial gcd.
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def divrem(a,b):
    a=list(map(Fraction,a));b=trim(list(map(Fraction,b)))
    while len(a)>=len(b) and any(a):
        f=a[-1]/b[-1];sh=len(a)-len(b)
        for i,v in enumerate(b):a[sh+i]-=f*v
        trim(a)
    return trim(a)

def gcdpoly(a,b):
    a=list(map(Fraction,a));b=list(map(Fraction,b))
    while any(b):a,b=b,divrem(a,b)
    return trim(a)
for j in range(8):
    g=gcdpoly(Q[j],N[j])
    assert len(g)==1,('uncancelled roots',j,g)

print('VERIFY_OK states=48 residues=8 row_certificates=8 direct_levels=18 last_depth=17')
print('INITIAL_DISTRIBUTIONS r=0..8:',H[:9])
print('DENOMINATOR_DEGREES', [len(q)-1 for q in Q])
