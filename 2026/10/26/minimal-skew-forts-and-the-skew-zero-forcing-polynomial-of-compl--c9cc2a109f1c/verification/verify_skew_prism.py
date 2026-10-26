#!/usr/bin/env python3
"""Independent exhaustive checker for the stated mathematical claim.
Uses exact integer masks, the defining forcing rule, and graph adjacency.
No external data or packages are required.
"""
from collections import Counter
from math import comb


def graph(n):
    return [sum(1 << j for j in range(n) if j != i) | (1 << (n+i))
            for i in range(n)] + [sum(1 << (n+j) for j in range(n) if j != i) | (1 << i)
            for i in range(n)]


def success(n, white):
    adj = graph(n)
    while white:
        target = 0
        for nb in adj:
            x = nb & white
            if x and x & (x-1) == 0:
                target = x
                break
        if not target:
            return False
        white ^= target
    return True


def stalled(n, white):
    return white != 0 and all((nb & white).bit_count() != 1 for nb in graph(n))


def white_formula(n):
    if n == 3:
        return {0:1,1:6,2:15,3:20,4:12}
    d=Counter()
    for k in range(n+1): d[k] += 2*comb(n,k)
    d[0] -= 1
    for b in range(1,n-1): d[b+1] += 2*n*comb(n,b)
    d[2] -= n*n
    d[n] += 2*n*(n-1)
    for b in range(2,n-1):
        d[b+2] += 2*comb(n,2)*(comb(n,b)-comb(n-2,b-2))
    d[4] -= comb(n,2)*(comb(n,2)-1)
    return {k:v for k,v in d.items() if v}


def min_stalled_predicate(n, white):
    a={i for i in range(n) if white & (1<<i)}
    b={i for i in range(n) if white & (1<<(n+i))}
    aa,bb,cc=len(a),len(b),len(a&b)
    if aa==bb==2 and cc==2:return True
    if n>=4 and ((aa==1 and bb==n-1 and cc==0) or (bb==1 and aa==n-1 and cc==0)):return True
    if n>=5 and aa==bb==3 and cc<=1:return True
    return False


def check():
    checks=0
    for n in range(3,9):
        observed=Counter(); observed_forts=set(); successful=set()
        for w in range(1<<(2*n)):
            good=success(n,w)
            observed[w.bit_count()] += good
            if good:successful.add(w)
            if stalled(n,w): observed_forts.add(w)
            checks+=1
        expected=white_formula(n)
        assert {k:v for k,v in observed.items() if v} == expected, (n,expected,observed)
        minimal = {w for w in observed_forts if not any(v!=w and (v&w)==v for v in observed_forts)}
        proposed = {w for w in range(1,1<<(2*n)) if min_stalled_predicate(n,w)}
        assert minimal == proposed,(n,len(minimal),len(proposed),list(minimal^proposed)[:3])
        for w in range(1<<(2*n)):
            contains = any((w&v)==v for v in minimal)
            assert (w in successful) != contains,(n,w)
            checks+=1
        degree=max(expected)
        if n==3: assert degree==4 and expected[4]==12
        elif n==4:assert degree==n and expected[n]==56
        else:assert degree==n and expected[n]==2*n**3-3*n*n+n+2
        assert min(v.bit_count() for v in minimal)==4
        print('n=',n,'skew forcing polynomial coefficient sequence blue size ascending:',
              [observed[2*n-k] for k in range(2*n+1)],
              ' minimal skew forts=',len(minimal),' Zminus=',2*n-degree)
    print('VERIFY_OK subset_rule_and_obstruction_checks=',checks)

if __name__=='__main__':check()
