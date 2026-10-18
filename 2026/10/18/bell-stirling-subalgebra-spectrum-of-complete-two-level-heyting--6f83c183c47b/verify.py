#!/usr/bin/env python3
"""Finite independent checks for complete-two-level Heyting subalgebras.

Run with Python 3: python verify.py. No external packages are required.
This is a finite test, not a substitute for the general proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def stirling(n, k):
    if n == k == 0: return 1
    if k < 0 or k > n or n == 0: return 0
    return stirling(n-1,k-1) + k*stirling(n-1,k)

def bell(n):
    return sum(stirling(n,k) for k in range(n+1))

def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(seq, mx):
        if len(seq) == n:
            yield tuple(seq)
            return
        for x in range(mx+2):
            seq.append(x)
            yield from rec(seq,max(mx,x))
            seq.pop()
    yield from rec([0],0)

def canonical_kernel(rgs):
    d={}; z=[]
    for val in rgs:
        if val not in d: d[val]=len(d)
        z.append(d[val])
    return tuple(z)

def permitted(pi,a,b):
    lower=set(pi[:a]); upper=set(pi[a:]); cross=lower & upper
    return (not cross) or (len(upper)==1)

def upset_algebra(a,b):
    n=a+b; full=(1<<n)-1; upper=full ^ ((1<<a)-1)
    cones=[(1<<i)|upper if i<a else (1<<i) for i in range(n)]
    up=tuple(x for x in range(1<<n) if all(not (x>>i&1) or (x&cones[i])==cones[i] for i in range(n)))
    assert 0 in up and full in up and len(up)==(1<<a)+(1<<b)-1
    index={u:k for k,u in enumerate(up)}
    imp=lambda x,y:sum(1<<i for i in range(n) if (x&cones[i]&~y)==0)
    clos=[]
    for x in up:
        clos.append([(index[x&y],index[x|y],index[imp(x,y)]) for y in up])
    return up,clos

def enumerate_subalgebras(a,b):
    up,ops=upset_algebra(a,b); z=len(up)
    must=(1<<0) | (1<<(z-1))
    good=set()
    for sel in range(1<<z):
        if sel&must!=must:continue
        ids=[i for i in range(z) if (sel>>i)&1]
        if any(not ((sel>>target)&1) for i in ids for j in ids for target in ops[i][j]):continue
        good.add(frozenset(up[i] for i in ids))
    return good

def kernel_from_set(S,n):
    sig=[tuple(bool(u>>i&1) for u in sorted(S)) for i in range(n)]
    return canonical_kernel(sig)

def theoretical_subalgebras(a,b):
    up,_=upset_algebra(a,b)
    out={}
    for pi in partitions(a+b):
        if not permitted(pi,a,b):continue
        sub=frozenset(u for u in up if all(((u>>i)&1)==((u>>j)&1) for i in range(a+b) for j in range(i+1,a+b) if pi[i]==pi[j]))
        assert kernel_from_set(sub,a+b)==pi,(a,b,pi)
        assert pi not in out
        out[pi]=sub
    return out

def predicted_sizes(a,b):
    hist=Counter()
    for i in range(a+1):hist[(1<<i)+1]+=stirling(a+1,i+1)
    for i in range(a+1):
        for j in range(2,b+1):hist[(1<<i)+(1<<j)-1]+=stirling(a,i)*stirling(b,j)
    return +hist

tests=0; subalgebras=0; partition_tests=0
for a,b in product(range(1,4),range(1,4)):
    actual=enumerate_subalgebras(a,b)
    prediction=theoretical_subalgebras(a,b)
    assert actual==set(prediction.values()),('family mismatch',a,b)
    hist=Counter(map(len,actual))
    assert hist==predicted_sizes(a,b),('rank mismatch',a,b,hist,predicted_sizes(a,b))
    assert len(actual)==bell(a+1)+bell(a)*(bell(b)-1)
    assert len(prediction)==len(actual)
    assert len(set(prediction.values()))==len(actual)
    # Kernel refinement in partition space agrees with reverse inclusion in subalgebra space.
    for p1,s1 in prediction.items():
        for p2,s2 in prediction.items():
            # If p1 is coarser than p2, the corresponding algebra is smaller.
            coarse=all(p2[i]!=p2[j] or p1[i]==p1[j] for i in range(a+b) for j in range(i+1,a+b))
            assert (s1 <= s2)==coarse,('inclusion mismatch',a,b,p1,p2)
            partition_tests+=1
    # Direct maximal subalgebra census and Frattini intersection.
    n=a+b
    maximal=[s for s in actual if len(s)<len(max(actual,key=len)) and not any(s<t and len(t)<len(max(actual,key=len)) for t in actual)]
    expected_max=comb(a,2)+comb(b,2) if b>=2 else comb(a+1,2)
    assert len(maximal)==expected_max,(a,b,expected_max,len(maximal))
    if maximal:
        inter=set.intersection(*map(set,maximal))
        full=(1<<n)-1; upper=full ^ ((1<<a)-1)
        target={0,upper,full} if b>=2 else {0,full}
        assert inter==target,(a,b,inter,target)
    tests+=1; subalgebras+=len(actual)
    print(f'CHECK_OK a={a} b={b} size={len(actual)} hist={dict(sorted(hist.items()))}')
print(f'VERIFY_OK families={tests} exhaustive_subalgebras={subalgebras} kernel_order_pairs={partition_tests}')
