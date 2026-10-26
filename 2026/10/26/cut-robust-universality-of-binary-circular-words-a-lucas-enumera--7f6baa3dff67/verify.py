#!/usr/bin/env python3
"""Independent exhaustive checks for robust cyclic binary subsequence universality."""
from itertools import product
from math import comb

def greedy_index(w):
    seen=set(); count=0
    for x in w:
        seen.add(x)
        if len(seen)==2:
            count+=1; seen.clear()
    return count

def explicit_index(w):
    s={''}
    for a in w:
        s |= {u+a for u in tuple(s)}
    k=0
    while all(''.join(a) in s for a in product('01',repeat=k+1)):
        k+=1
    return k

def perfect_parity(w):
    n=len(w)
    x=[int(w[i]!=w[(i+1)%n]) for i in range(n)]
    if all(x): return True
    # start from a zero and scan all 1 runs
    i=x.index(0)
    seq=x[i+1:]+x[:i]
    streak=0
    for t in seq:
        if t:
            streak+=1
        else:
            if streak%2:return False
            streak=0
    return streak%2==0

def odd_run_bad_cuts(w):
    n=len(w)
    t=[int(w[i]!=w[(i+1)%n]) for i in range(n)]
    if all(t):return 0
    ix=t.index(0)
    x=t[ix+1:]+t[:ix+1]
    lengths=[]
    count=0
    for z in x:
        if z:count+=1
        elif count:
            lengths.append(count)
            count=0
    return sum((r+1)//2 for r in lengths if r%2)

def expected(n,k):
    if k>n//2:return 0
    if k==0:return 2
    return 2*n*comb(n-k,k)//(n-k)- (2 if n==2*k else 0)

# Independently propagate weighted closed-walk traces of [[1,1],[u,0]].
trace0={0:2}
trace1={0:1}
def trace_poly(n):
    p,q=trace0,trace1
    if n==0:return p
    for _ in range(2,n+1):
        z=dict(q)
        for k,v in p.items():z[k+1]=z.get(k+1,0)+v
        p,q=q,z
    return q

for n in range(1,19):
    hist={}
    exceptions=0
    for w in product('01',repeat=n):
        inds=[greedy_index(w[i:]+w[:i]) for i in range(n)]
        mn=min(inds); mx=max(inds)
        assert mx-mn<=1,(n,w,inds)
        robust=(mn==mx)
        assert sum(v==mx-1 for v in inds)==odd_run_bad_cuts(w),(n,w,inds)
        assert robust==perfect_parity(w),(n,w,inds)
        if n<=9:
            assert inds==[explicit_index(w[i:]+w[:i]) for i in range(n)], (n,w,inds)
        if robust:hist[mx]=hist.get(mx,0)+1
    for k in range(n//2+1):
        assert hist.get(k,0)==expected(n,k),(n,k,hist,expected(n,k))
        walk_count=2*trace_poly(n).get(k,0)-(2 if k>=1 and n==2*k else 0)
        assert hist.get(k,0)==walk_count,(n,k,walk_count,hist)
    Lprev,Lcurr=2,1
    for i in range(2,n+1):Lprev,Lcurr=Lcurr,Lprev+Lcurr
    L=1 if n==1 else Lcurr
    assert sum(hist.values())==2*(L-(n%2==0)),(n,hist,L)
    print(n,sum(hist.values()),hist)
print('VERIFY_OK exhaustive_binary_words=',(1<<19)-2,'explicit_subsequences_n=1..9','distribution_n=1..18', 'weighted_transfer_trace_n=1..18', 'bad_cut_positions=checked')
