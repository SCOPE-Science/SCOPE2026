#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, Counter
from math import comb

def sig_direct(w):
    n=len(w)
    # literal multiset of binary substring compositions for lengths 1 and 2:
    # a composition is (#0,#1); keep length labels implicitly through the sum.
    c=Counter()
    for L in (1,2):
        if L>n: continue
        for i in range(n-L+1):
            u=w[i:i+L]
            c[(u.count('0'),u.count('1'))]+=1
    return tuple(sorted(c.items()))

def runs(w):
    if not w: return (0,0)
    r0=r1=0
    prev=None
    for ch in w:
        if ch!=prev:
            if ch=='0': r0+=1
            else: r1+=1
            prev=ch
    return r0,r1

def sig_params(w):
    z=w.count('0'); o=len(w)-z
    r0,r1=runs(w)
    a=z-r0 if z else 0
    b=o-r1 if o else 0
    mixed=max(0,r0+r1-1)
    # counts of (1,0),(0,1),(2,0),(1,1),(0,2)
    return (z,o,a,mixed,b)

def Q(n):
    if n%2==0:
        m=n//2; return 3*m*m-2*m+2
    m=(n-1)//2; return 3*m*m+m+2

def predicted_class_size(n,z,r0,r1):
    o=n-z
    if z==0 or o==0:
        return 1
    if r0==r1:
        k=r0
        return 2*comb(z-1,k-1)*comb(o-1,k-1)
    if r0==r1+1:
        k=r1
        return comb(z-1,k)*comb(o-1,k-1)
    if r1==r0+1:
        k=r0
        return comb(z-1,k-1)*comb(o-1,k)
    return 0


def predicted_singletons(n):
    out={'0'*n,'1'*n}
    if n>=3:
        out.add('0'+'1'*(n-2)+'0')
        out.add('1'+'0'*(n-2)+'1')
    if n>=5 and n%2==1:
        out.add(('01'*((n+1)//2))[:n])
        out.add(('10'*((n+1)//2))[:n])
    return out

def feasible_count(n):
    # independent direct count of feasible triples, optimized by summing allowed r1 ranges
    s=2
    for z in range(1,n):
        o=n-z
        for r0 in range(1,z+1):
            s += max(0, min(o,r0+1)-max(1,r0-1)+1)
    return s

def closed_sum(n):
    return 2 + sum(n-2*k+1 for k in range(1,n//2+1)) + 2*sum(n-2*k for k in range(1,(n-1)//2+1))

words_checked=0
classes_checked=0
for n in range(1,17):
    by_lit=defaultdict(list)
    by_param=defaultdict(list)
    for bits in product('01', repeat=n):
        w=''.join(bits); words_checked+=1
        by_lit[sig_direct(w)].append(w)
        by_param[sig_params(w)].append(w)
    assert len(by_lit)==Q(n),(n,len(by_lit),Q(n))
    assert len(by_param)==Q(n)
    # The literal composition multiset and the run-parameter signature define identical partitions.
    lit_partition={frozenset(v) for v in by_lit.values()}
    param_partition={frozenset(v) for v in by_param.values()}
    assert lit_partition==param_partition
    singleton_words={v[0] for v in by_param.values() if len(v)==1}
    assert singleton_words==predicted_singletons(n),(n,singleton_words,predicted_singletons(n))
    # Every class obeys the exact positive-composition formula.
    for key,ws in by_param.items():
        z,o,a,t,b=key
        r0=z-a if z else 0
        r1=o-b if o else 0
        assert t==max(0,r0+r1-1)
        assert len(ws)==predicted_class_size(n,z,r0,r1),(n,key,len(ws),predicted_class_size(n,z,r0,r1))
        classes_checked+=1

for n in range(1,501):
    assert feasible_count(n)==Q(n)==closed_sum(n),(n,feasible_count(n),Q(n),closed_sum(n))
    if n>=2:
        assert Q(n)-Q(n-1)==(3*(n-1))//2

print(f'VERIFY_OK words={words_checked} n=1..16 classes={classes_checked} formulas_n<=500')
