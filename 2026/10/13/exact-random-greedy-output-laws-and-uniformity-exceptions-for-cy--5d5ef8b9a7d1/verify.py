#!/usr/bin/env python3
"""Exact finite checks for random-priority greedy maximal independent sets on cycles.
Only standard-library exact rational arithmetic is used.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from itertools import permutations


def transform(poly):
    """Apply (Af)(u) = integral_0^1 (1-min(u,v)) f(v) dv."""
    s = sum((c / Q(i + 1) for i, c in enumerate(poly)), Q(0))
    out = [Q(0)] * (len(poly) + 2)
    out[0], out[1] = s, -s
    for i,c in enumerate(poly):
        out[i + 2] += c / Q((i+1)*(i+2))
    return out


def phi_values(max_a):
    f = [Q(1), Q(-1)]
    out=[]
    for _ in range(max_a+1):
        out.append(sum((c/Q((i+1)*(i+2)) for i,c in enumerate(f)),Q(0)))
        f = transform(f)
    return out


def trace_values(max_k):
    """Tr(A**k), via -z D'(z)/D(z), D=cosh(sqrt(z))-sqrt(z)*sinh(sqrt(z))."""
    d = [Q(1-2*j, factorial(2*j)) for j in range(max_k+1)]
    t = [Q(0)] * (max_k+1)
    for k in range(1,max_k+1):
        t[k] = -k*d[k] - sum((d[j]*t[k-j] for j in range(1,k)),Q(0))
    return t


def maximal_masks(n):
    allmask = (1<<n)-1
    edges = [(i, (i+1)%n) for i in range(n)]
    closed = [(1<<i) | (1<<((i-1)%n)) | (1<<((i+1)%n)) for i in range(n)]
    for mask in range(1,1<<n):
        if any((mask>>a&1) and (mask>>b&1) for a,b in edges):
            continue
        if all(mask & nb for nb in closed):
            yield mask


def profile(n,mask):
    indexes=[i for i in range(n) if mask>>i&1]
    gaps=[((indexes[(i+1)%len(indexes)]-v)%n or n) for i,v in enumerate(indexes)]
    return gaps


def predicted(n,mask,ph,t):
    gaps=profile(n,mask)
    assert all(g in (2,3) for g in gaps)
    if 3 not in gaps:
        return t[len(gaps)]
    start=gaps.index(3)
    rotated=gaps[start+1:]+gaps[:start+1]
    blocks=[]; block=0
    for gap in rotated:
        if gap==2:block+=1
        else:blocks.append(block);block=0
    assert block==0
    assert len(blocks)==gaps.count(3)
    res=Q(1)
    for a in blocks:res*=ph[a]
    return res


def direct_probability(n,mask):
    closed=[(1<<i)|(1<<((i-1)%n))|(1<<((i+1)%n)) for i in range(n)]
    full=(1<<n)-1
    @lru_cache(None)
    def rec(active, target):
        if not active:
            return Q(int(target==0))
        result=Q(0)
        m=target
        while m:
            bit=m&-m;v=bit.bit_length()-1;m-=bit
            result+=rec(active&~closed[v],target&~bit)
        return result/active.bit_count()
    return rec(full,mask)


def greedy_mask(n,ordering):
    selected=0
    for v in ordering:
        if not selected & ((1<<((v-1)%n)) | (1<<((v+1)%n))):
            selected|=1<<v
    return selected


def main():
    phi=phi_values(22)
    traces=trace_values(22)
    assert phi[:5] == [Q(1,3),Q(1,5),Q(1,7),Q(8,81),Q(34,495)],phi[:5]
    assert phi[0]*phi[2]-phi[1]**2 == Q(4,525)
    assert traces[3:6]==[Q(1,3),Q(7,30),Q(17,105)]
    rows=0; total_masks=0
    for n in range(3,19):
        pm={}
        total=Q(0)
        for mask in maximal_masks(n):
            predicted_p=predicted(n,mask,phi,traces)
            direct_p=direct_probability(n,mask)
            assert predicted_p == direct_p,(n,mask,predicted_p,direct_p)
            pm[mask]=predicted_p
            total+=predicted_p
            rows+=1
        assert total ==1,(n,total)
        assert (len(set(pm.values()))==1) == (n in {3,4,5,7}),(n,pm)
        total_masks+=len(pm)
        print('CYCLE_OK n=%d outcomes=%d distinct_probabilities=%d' %(n,len(pm),len(set(pm.values()))))
    permutation_tests=0
    for n in range(3,9):
        from collections import Counter
        freq=Counter(greedy_mask(n,pi) for pi in permutations(range(n)))
        for mask,count in freq.items():
            assert Q(count,factorial(n)) == predicted(n,mask,phi,traces)
        assert len(freq)==len(list(maximal_masks(n)))
        permutation_tests += factorial(n)
    print('VERIFY_OK exact_outcomes=%d cycles=16 permutation_orders=%d phi_0_2=%s,%s,%s trace4=%s gap=%s' % (rows,permutation_tests,phi[0],phi[1],phi[2],traces[4],phi[0]*phi[2]-phi[1]**2))

if __name__=='__main__':main()
