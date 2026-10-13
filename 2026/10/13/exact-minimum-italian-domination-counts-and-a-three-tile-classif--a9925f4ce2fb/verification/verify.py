"""Reproduce exact minimum Italian domination multiplicities for ladders.
Python 3 standard library only; immutable vertex order column-major (top,bottom).
"""
from itertools import product
from collections import defaultdict

SYMS=list(product(range(3),repeat=2))
Z=(0,0)
def feasible(p,s,t):
    return all(s[i]!=0 or s[1-i]+p[i]+t[i]>=2 for i in (0,1))
def delta(s):return s[0]+s[1]-1

def potential(p,s):
    if p==Z:return -2 if s in ((1,2),(2,1),(2,2)) else -1
    if p in ((0,1),(1,0)):return -1
    return 0

states=[(p,s) for p in SYMS for s in SYMS]
zeroadj={u:[] for u in states}
feasible_n=zerocost_n=0
for p,s,t in product(SYMS, repeat=3):
    if not feasible(p,s,t):continue
    feasible_n+=1
    rc=delta(s)+potential(p,s)-potential(s,t)
    assert rc>=0,(p,s,t,rc)
    if rc==0:
        zerocost_n+=1
        zeroadj[p,s].append((s,t))
assert feasible_n==666 and zerocost_n==161
# Trim zero-reduced-cost network between permitted boundary pairs.
start={(Z,s) for s in SYMS if potential(Z,s)==-1}
end={(s,Z) for s in SYMS if potential(s,Z)==-1}
def reach(src,forward=True):
    adj=zeroadj if forward else {u:[] for u in states}
    if not forward:
        for u,L in zeroadj.items():
            for v in L:adj[v].append(u)
    stack=list(src);seen=set(stack)
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    return seen
trim=reach(start)&reach(end,False)
expect={
 (Z,Z):[], (Z,(0,1)):[((0,1),(1,0))], (Z,(1,0)):[((1,0),(0,1))],
 (Z,(1,2)):[((1,2),Z)], (Z,(2,1)):[((2,1),Z)],
 ((0,1),Z):[(Z,(2,1))],
 ((0,1),(0,1)):[((0,1),(1,0))],
 ((0,1),(1,0)):[((1,0),Z),((1,0),(0,1)),((1,0),(1,0))],
 ((1,0),Z):[(Z,(1,2))],
 ((1,0),(0,1)):[((0,1),Z),((0,1),(0,1)),((0,1),(1,0))],
 ((1,0),(1,0)):[((1,0),(0,1))],
 ((1,2),Z):[(Z,(1,0))], ((2,1),Z):[(Z,(0,1))],
}
assert trim==set(expect)
for u in trim:
    assert set(zeroadj[u])&trim==set(expect[u]),(u,zeroadj[u],expect[u])
# Independent full-coloring enumeration from vertex-neighborhood definition.
def bruteforce(n):
    N=2*n
    nbr=[set() for _ in range(N)]
    for i in range(n):
        a=2*i;b=a+1;nbr[a].add(b);nbr[b].add(a)
        if i:
            for off in (0,1):
                x=2*i+off;y=x-2;nbr[x].add(y);nbr[y].add(x)
    hist=defaultdict(int)
    for f in product(range(3),repeat=N):
        if all(f[i] or sum(f[j] for j in nbr[i])>=2 for i in range(N)):
            hist[sum(f)]+=1
    return min(hist),hist[min(hist)]

def dp(n):
    d={(Z,s):1 for s in SYMS}
    for pos in range(n):
        nd=defaultdict(int)
        targets=SYMS if pos<n-1 else (Z,)
        for (p,s),c in d.items():
            for t in targets:
                if feasible(p,s,t):nd[(s,t)]+=c
        d=nd
    # For exact count only use weighted counts: second DP with weights.
    counts={(Z,s,sum(s)):1 for s in SYMS}
    for pos in range(n):
        nc=defaultdict(int)
        for (p,s,w),ct in counts.items():
            for t in (SYMS if pos<n-1 else (Z,)):
                if feasible(p,s,t):
                    ww=w+(sum(t) if pos<n-1 else 0)
                    if ww<=n:nc[(s,t,ww)]+=ct
        counts=nc
    return sum(v for (p,s,w),v in counts.items() if w==n)

comps=[1]
for m in range(1,32):
    comps.append(sum(comps[m-d] for d in (1,2,5) if m>=d))
for n in range(2,28):
    calc=dp(n);expectation=2*comps[n-2]
    assert calc==expectation,(n,calc,expectation)
for n in range(2,7):
    mn,mult=bruteforce(n)
    assert (mn,mult)==(n,2*comps[n-2]),(n,mn,mult,2*comps[n-2])
print('VALID: 729 local cases; 666 feasible; 161 zero-cost; 13 trimmed states and all transitions.')
print('VALID: exhaustive independent vertex-label enumeration for n=2..6.')
print('VALID: transfer DP and compositions agree for n=2..27.')
print('FIRST_VALUES: '+', '.join(f'{n}:{2*comps[n-2]}' for n in range(2,18)))
