#!/usr/bin/env python3
"""Reproducible integer certificate for optimal double-coalition partitions of bicliques.

No external Python dependencies. Blocks and shore occupancies are unordered.
"""
from collections import Counter
from math import comb, factorial


def is_double_dominating(a, b, r, s):
    """Exact double domination predicate for a subset of K_(r,s)."""
    return a >= 1 and b >= 1 and (a == r or b >= 2) and (b == s or a >= 2)


def maximum(r, s):
    assert 3 <= r <= s
    return s + 1 if r <= 5 else r + s - 4


def profiles(r, s):
    """Exhaust all possible excess-support profiles at the known optimum.

    If a partition has n-e blocks, all nonsingleton blocks contribute
    precisely e to the sum of (block_size-1). Enumerate every such multiset.
    Unused vertices are *forced* singleton blocks, so no case is omitted.
    """
    e = r + s - maximum(r, s)
    options = [(a, t-a) for t in range(2, e+2)
               for a in range(t+1) if a <= r and t-a <= s]
    options.sort()
    result = set()

    def visit(idx, spare, ra, sb, chosen):
        if spare == 0:
            p = list(chosen) + [(1, 0)] * ra + [(0, 1)] * sb
            if all(not is_double_dominating(a, b, r, s) for a, b in p):
                if all(any(i != j and is_double_dominating(a+c, b+d, r, s)
                           for j, (c, d) in enumerate(p))
                       for i, (a, b) in enumerate(p)):
                    result.add(tuple(sorted(chosen)))
            return
        for j in range(idx, len(options)):
            a, b = options[j]
            cost = a + b - 1
            if cost <= spare and a <= ra and b <= sb:
                visit(j, spare-cost, ra-a, sb-b, chosen + [(a,b)])

    visit(0, e, r, s, [])
    return result


def expected(r, s):
    x = set()
    if r <= 5:
        x.add(((r, 0),))
        for a in range(2, r):
            x.add(tuple(sorted([(a, 1)] + ([(r-a, 0)] if r-a > 1 else []))))
    if s == r and s <= 5:
        x.add(((0, s),))
        for b in range(2, s):
            x.add(tuple(sorted([(1, b)] + ([(0, s-b)] if s-b > 1 else []))))
    if r >= 5 and s >= 5:
        x.add(tuple(sorted([(1,2), (2,1)])))
    return x


def count_signature(r, s, sig):
    """Orbit-stabilizer count for unlabeled blocks of labeled vertices."""
    remaining_a = r - sum(a for a,b in sig)
    remaining_b = s - sum(b for a,b in sig)
    all_types = Counter(sig)
    all_types[(1,0)] += remaining_a
    all_types[(0,1)] += remaining_b
    denominator = 1
    for (a,b), multiplicity in all_types.items():
        denominator *= (factorial(a)*factorial(b))**multiplicity * factorial(multiplicity)
    numerator = factorial(r)*factorial(s)
    assert numerator % denominator == 0
    return numerator//denominator


def predicted_count(r, s):
    assert 3 <= r <= s
    ahub = sum(comb(r, a) for a in range(2,r))
    total = (1+s*ahub) if r <= 5 else 0
    if s == r and s <= 5:
        total += 1+r*sum(comb(s,b) for b in range(2,s))
    if r >= 5:
        total += 9*comb(r,3)*comb(s,3)
    return total


def direct_count(r, s):
    """Independent brute force of set partitions of labeled vertices.

    Restricted growth strings enumerate each unlabeled partition exactly once.
    For small graphs only; does NOT call the occupancy-profile enumerator.
    """
    n = r+s
    target = maximum(min(r,s),max(r,s))
    membership = [0]*n
    neighborhoods = [({i} | (set(range(r,n)) if i < r else set(range(r)))) for i in range(n)]
    def graph_dd(vertices):
        return all(len(N & vertices) >= 2 for N in neighborhoods)
    num = 0
    def visit(pos, k):
        nonlocal num
        if k+n-pos < target or k > target:
            return
        if pos == n:
            if k != target: return
            blocks = [set() for _ in range(k)]
            for v,t in enumerate(membership): blocks[t].add(v)
            if any(graph_dd(b) for b in blocks):return
            if all(any(i!=j and graph_dd(b | other)
                       for j, other in enumerate(blocks))
                   for i, b in enumerate(blocks)):
                num+=1
            return
        for q in range(min(k+1, target)):
            membership[pos]=q
            visit(pos+1,k+(q==k))
    membership[0]=0
    visit(1,1)
    return num


def main():
    checked=0
    for r in range(3,11):
        for s in range(r,15):
            got = profiles(r,s)
            ex = expected(r,s)
            assert got == ex,(r,s,got^ex)
            count = sum(count_signature(r,s,sig) for sig in got)
            want = predicted_count(r,s)
            assert count == want,(r,s,count,want)
            checked += 1
    # All exceptional pairs requiring a bounded finite-case proof,
    # together with some additional independent direct-set checks.
    small=[(3,3),(3,4),(4,4),(4,5),(4,6),(5,5),(5,6),(5,7),(5,8)]
    for r,s in small:
        assert profiles(r,s) == expected(r,s)
    for r,s in [(3,3),(3,4),(4,4),(5,5)]:
        n = direct_count(r,s)
        assert n == predicted_count(r,s),(r,s,n,predicted_count(r,s))
    print('VERIFY_OK',checked,'exact occupancy parameter pairs;',
          len(small),'finite exceptional parameter pairs;',
          4,'independent labeled-partition enumerations')
    print('K_3,3:',predicted_count(3,3),'K_4,4:',predicted_count(4,4),
          'K_5,5:',predicted_count(5,5),'K_6,6:',predicted_count(6,6))

if __name__=='__main__': main()
