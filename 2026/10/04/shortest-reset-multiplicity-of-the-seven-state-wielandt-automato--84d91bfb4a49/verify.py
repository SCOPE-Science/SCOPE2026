#!/usr/bin/env python3
from collections import deque, defaultdict
from math import comb

N=7
# States are 1..7.  Both letters advance along 1->2->...->7;
# at 7, b closes the 7-cycle to 1 and a takes the shortcut to 2.
def image(mask, letter):
    out=0
    for s in range(1,N+1):
        if mask & (1<<(s-1)):
            if s < N:
                t=s+1
            else:
                t=2 if letter=='a' else 1
            out |= 1<<(t-1)
    return out

def padd(p,q):
    r=[0]*max(len(p),len(q))
    for i,x in enumerate(p): r[i]+=x
    for i,x in enumerate(q): r[i]+=x
    return r

def shift(p): return [0]+p

full=(1<<N)-1
# Route 1: forward BFS plus generating-polynomial DP on shortest paths.
dist={full:0}; poly={full:[1]}; Q=deque([full])
first_single=None
while Q:
    S=Q.popleft(); d=dist[S]
    if first_single is not None and d>=first_single: continue
    for c in ('a','b'):
        T=image(S,c); cand=shift(poly[S]) if c=='a' else poly[S]
        if T not in dist:
            dist[T]=d+1; poly[T]=cand[:]; Q.append(T)
        elif dist[T]==d+1:
            poly[T]=padd(poly[T],cand)
        if T and T&(T-1)==0 and first_single is None:
            first_single=d+1
mins=[(s,dist[1<<(s-1)],poly[1<<(s-1)]) for s in range(1,N+1) if (1<<(s-1)) in dist]
best=min(d for s,d,p in mins)
targets=[(s,p) for s,d,p in mins if d==best]
assert best==31, best
assert [s for s,p in targets]==[2], targets
P=targets[0][1]
expected=[0]*6+[comb(20,k) for k in range(21)]
assert P==expected, (P,expected)
assert sum(P)==2**20

# Route 2: reverse-distance optimal-DAG recursion, independent of Route 1's polynomial accumulation.
allm=range(1,1<<N)
rev=defaultdict(list)
for S in allm:
    for c in ('a','b'):
        rev[image(S,c)].append((S,c))
target=1<<(2-1)
rd={target:0}; Q=deque([target])
while Q:
    T=Q.popleft()
    for S,c in rev[T]:
        if S not in rd:
            rd[S]=rd[T]+1; Q.append(S)
assert rd[full]==31
memo={target:[1]}
def rec(S):
    if S in memo:return memo[S]
    r=[0]
    for c in ('a','b'):
        T=image(S,c)
        if T in rd and rd[T]==rd[S]-1:
            z=rec(T); z=shift(z) if c=='a' else z
            r=padd(r,z)
    memo[S]=r; return r
P2=rec(full)
assert P2==expected
# Sanity check the published witness (a b^(n-2))^(n-2) a.
w=('a'+'b'*(N-2))*(N-2)+'a'
S=full
for c in w:S=image(S,c)
assert len(w)==31 and S==target
print('VERIFY_OK length=31 target=2 total=1048576 polynomial=z^6(1+z)^20 nonzero_subsets=127')
