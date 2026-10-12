#!/usr/bin/env python3
"""Standalone exact checks for finite-chain Alex correspondence and enumeration.
Python 3 standard library only. No external datasets required.
"""
from itertools import product
from functools import lru_cache


def eventual_orbit_minimum(mapping, source):
    seen = set()
    x = source
    m = x
    while x not in seen:
        seen.add(x)
        if x < m:
            m = x
        x = mapping[x]
    return m


def alex_holds_all_valuations(mapping):
    """Independently interpret closure + eventuality on every atom valuation."""
    n = len(mapping)
    for subset in range(1 << n):
        # E(P) = {x : f^t(x) in P for some t >=0}
        event = [False] * n
        for x in range(n):
            seen = set()
            y = x
            while y not in seen:
                seen.add(y)
                if subset & (1 << y):
                    event[x] = True
                    break
                y = mapping[y]
        # C(E(P)) = downclosure, i.e. exists y >= x with E(P)(y)
        # E(C(P)) = eventual visit to a point <= some p in P.
        for x in range(n):
            left = any(event[y] for y in range(x, n))
            right = False
            seen = set()
            y = x
            while y not in seen:
                seen.add(y)
                if any(subset & (1 << z) for z in range(y, n)):
                    right = True
                    break
                y = mapping[y]
            if left and not right:
                return False
    return True


def tree_decomposition_condition(mapping):
    """Independently enumerate the exact interval-rooted-tree condition."""
    n = len(mapping)
    q = [eventual_orbit_minimum(mapping, x) for x in range(n)]
    roots = [i for i in range(n) if q[i] == i]
    assert roots and roots[0] == 0
    for j, r in enumerate(roots):
        end = roots[j+1] if j+1 < len(roots) else n
        if mapping[r] < r:
            return False
        for x in range(r+1, end):
            if not (r <= mapping[x] < end):
                return False
            seen=set()
            z=x
            while z != r and z not in seen and r <= z < end:
                seen.add(z)
                z=mapping[z]
            if z != r:
                return False
    return True


def compositions(total):
    if total == 0:
        yield ()
    else:
        for first in range(1, total+1):
            for rest in compositions(total-first):
                yield (first,) + rest


def rooted_trees(block_size):
    return 1 if block_size == 1 else block_size ** (block_size - 2)


def count_by_compositions(n):
    result=0
    for parts in compositions(n):
        start=0
        weight=1
        for length in parts:
            weight *= (n-start)*rooted_trees(length)
            start += length
        result += weight
    return result


def count_by_dp(n):
    @lru_cache(None)
    def from_position(start):
        if start == n:
            return 1
        return (n-start)*sum(rooted_trees(length)*from_position(start+length)
                             for length in range(1,n-start+1))
    return from_position(0)


def main():
    known = [1,4,24,188,1825,21420,299572,4932880,94435713,2073167150]
    for n in range(1,11):
        dp = count_by_dp(n)
        comp = count_by_compositions(n)
        assert dp == comp == known[n-1], (n,dp,comp)
    print('DP_COMPOSITIONS_MATCH',known)
    for n in range(1,8):
        hits=0
        for f in product(range(n), repeat=n):
            q=tuple(eventual_orbit_minimum(f,x) for x in range(n))
            expected=all(q[i]<=q[i+1] for i in range(n-1))
            trees=tree_decomposition_condition(f)
            assert expected == trees,(n,f,q,'tree')
            if n<=5:
                semantic=alex_holds_all_valuations(f)
                assert expected == semantic,(n,f,q,'semantics')
            hits += expected
        assert hits == count_by_dp(n),(n,hits,count_by_dp(n))
        print('EXHAUSTIVE',n,'all_maps',n**n,'accepted',hits,
              'all_valuations',n<=5)
    # Example of map satisfying Alex but violating temporal continuity.
    assert alex_holds_all_valuations((1,0))
    assert not (1<=0)  # f(0)=1 > f(1)=0
    # First failing case and its singleton witness.
    f=(0,1,0)
    assert not alex_holds_all_valuations(f)
    assert [eventual_orbit_minimum(f,x) for x in range(3)]==[0,1,0]
    print('VERIFY_OK')

if __name__=='__main__':
    main()
