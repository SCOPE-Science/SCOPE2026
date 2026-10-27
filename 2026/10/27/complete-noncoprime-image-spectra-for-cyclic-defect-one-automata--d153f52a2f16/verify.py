#!/usr/bin/env python3
"""Exhaustive, self-contained checks for cyclic defect-one image spectra."""
from collections import deque
from functools import lru_cache
from math import comb, factorial, gcd

def direct_images(n, d):
    full = (1 << n) - 1
    seen = {full}
    todo = deque([full])
    while todo:
        s = todo.popleft()
        rot = ((s << 1) & full) | (s >> (n-1))
        merge = (s & ~1) | ((1 << d) if s & 1 else 0)
        for t in (rot, merge):
            if t not in seen:
                seen.add(t)
                todo.append(t)
    return seen

def expected_images(n, d):
    g = gcd(n, d)
    return {s for s in range(1, 1 << n) if all(any((s >> j) & 1 for j in range(r, n, g)) for r in range(g))}

def chain_lengths(n, d, surviving):
    h = {j for j in range(n) if not (surviving >> j) & 1}
    if not h:
        return []
    # Each missing d-orbit is split into chains by surviving states.
    heads = [j for j in h if (j-d) % n not in h]
    lens = []
    for j in heads:
        z = 0
        while j in h:
            z += 1
            j = (j+d) % n
        lens.append(z)
    assert sum(lens) == len(h), (n, d, surviving)
    return lens

def count_valid_deletion_orders(n, d, survivors):
    missing = ((1 << n)-1) ^ survivors
    @lru_cache(None)
    def go(remaining):
        if not remaining:
            return 1
        total=0
        x=remaining
        while x:
            low = x & -x
            j=low.bit_length()-1
            # Delete j only if its destination j+d is still present.
            if not (remaining >> ((j+d) % n)) & 1:
                total += go(remaining ^ low)
            x ^= low
        return total
    return go(missing)

pairs=0; tested_membership=0; orders=0
for n in range(2, 13):
    for d in range(n):
        got=direct_images(n,d)
        expected=expected_images(n,d)
        assert got == expected, (n,d,sorted(got^expected))
        g=gcd(n,d)
        m=n//g
        assert len(got)==(2**m-1)**g, (n,d)
        assert min(x.bit_count() for x in got)==g
        for k in range(g,n+1):
            actual=sum(s.bit_count()==k for s in got)
            predicted=sum((-1)**t*comb(g,t)*comb(n-t*m,k) for t in range(g+1) if n-t*m>=k)
            assert actual==predicted, (n,d,k,actual,predicted)
        pairs+=1; tested_membership+=1<<n
        if n<=9:
            for surviving in expected:
                if d:
                    lengths=chain_lengths(n,d,surviving)
                    pred=factorial(n-surviving.bit_count())
                    denom=1
                    for q in lengths:denom*=factorial(q)
                    pred//=denom
                    actual=count_valid_deletion_orders(n,d,surviving)
                    assert actual==pred, (n,d,surviving,actual,pred)
                    orders+=1
                else:
                    assert surviving == (1<<n)-1
print(f'VERIFY_OK: exact power-automaton images / polynomial coefficients: {pairs} (n,d) cases; {tested_membership} tested possible subsets.')
print(f'VERIFY_OK: independent recursive contraction-order counts: {orders} reachable image cases for n<=9.')
for n,d in ((6,2),(10,4),(11,5)):
    g=gcd(n,d); m=n//g
    print(f'SAMPLE n={n}, d={d}: gcd={g}, orbit_size={m}, image_count={(2**m-1)**g}, min_rank={g}')
print('SAMPLE n=10,d=4,S={0,1}: canonical 8-deletion order count =', count_valid_deletion_orders(10,4,(1<<0)|(1<<1)))
