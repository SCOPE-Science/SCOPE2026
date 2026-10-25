#!/usr/bin/env python3
"""Finite exhaustive certificate for complete multipartite excitable dynamics.

Only the mathematical model and verification tests are represented here.
"""
from itertools import product
from collections import Counter
from math import comb


def update(parts):
    flags = [1 in part for part in parts]
    total = sum(flags)
    return tuple(tuple(2 if v == 1 else 0 if v == 2 else
                       (1 if total - flags[i] else 0) for v in part)
                 for i, part in enumerate(parts))


def rotate(parts):
    return tuple(tuple((v+1) % 3 for v in part) for part in parts)


def zero(parts):
    return all(all(v == 0 for v in part) for part in parts)


def phase(parts):
    seen = {}
    state = parts
    while state not in seen:
        seen[state] = len(seen)
        state = update(state)
    return seen[state], len(seen)-seen[state]


def finite_quotient_certificate():
    hist = Counter()
    size = 0
    for caps in product((0, 1, 3), repeat=7):
        if sum(caps) < 3:
            continue
        # Counts 3 stand for any number >= 2 of identical part-supports.
        parts = tuple(tuple(c for c in range(3) if mask & (1 << c))
                      for mask, count in enumerate(caps, 1)
                      for _ in range(count))
        states = [parts]
        for _ in range(7):
            states.append(update(states[-1]))
        assert states[7] == states[4]
        assert zero(states[4]) or states[5] == rotate(states[4])
        d, p = phase(parts)
        masks = [sum(1 << c for c in part) for part in parts]
        assert good_supports(masks) == (d == 0 and not zero(parts))
        assert d <= 4 and p in (1, 3)
        hist[(d, p)] += 1
        size += 1
    assert size == 2158
    assert hist == Counter({(0, 3): 1969, (2, 3): 42, (3, 3): 42,
                            (1, 3): 38, (2, 1): 21, (1, 1): 19,
                            (3, 1): 19, (4, 3): 4, (4, 1): 3,
                            (0, 1): 1})
    return size, hist


def omega(m, mask):
    colors = [i for i in range(3) if mask & (1 << i)]
    s = len(colors)
    return sum((-1)**(s-j) * comb(s, j) * j**m
               for j in range(s+1))


def good_supports(masks):
    return all(
        any((masks[j] & (1 << ((c+1) % 3))) and j != i
            for j in range(len(masks)))
        for i, mask in enumerate(masks)
        for c in range(3) if mask & (1 << c)
    )


def periodic_count(sizes):
    total = 1
    for masks in product(range(1,8), repeat=len(sizes)):
        if good_supports(masks):
            ways = 1
            for n, mask in zip(sizes,masks):
                ways *= omega(n,mask)
            total += ways
    return total


def tripartite_polynomial(sizes):
    assert len(sizes) == 3
    a = [2**n-2 for n in sizes]
    b = [3**n-3*2**n+3 for n in sizes]
    from itertools import combinations
    P = 7+6*sum(a)+9*sum(a[i]*a[j] for i,j in combinations(range(3),2))
    P += 15*a[0]*a[1]*a[2]
    P += 3*sum(b[i]*b[j] for i,j in combinations(range(3),2)) + b[0]*b[1]*b[2]
    P += 3*sum(a[i]*b[j] for i in range(3) for j in range(3) if i!=j)
    P += 6*sum(a[i]*a[j]*b[k] for k in range(3)
               for i,j in [tuple(v for v in range(3) if v != k)])
    P += 3*sum(a[i]*b[j]*b[k] for i in range(3)
               for j,k in [tuple(v for v in range(3) if v != i)])
    return P


def direct_check(sizes):
    total = 0
    periodic = 0
    max_depth = 0
    for flat in product(range(3),repeat=sum(sizes)):
        parts = []
        off=0
        for n in sizes:
            parts.append(tuple(flat[off:off+n]));off += n
        parts = tuple(parts)
        d,p=phase(parts)
        assert d<=4 and p in (1,3)
        if d==0:
            periodic += 1
            assert zero(parts) or update(parts) == rotate(parts)
        if d>max_depth:max_depth=d
        total += 1
    assert total==3**sum(sizes)
    assert periodic == periodic_count(sizes)
    if len(sizes)==3:
        assert periodic == tripartite_polynomial(sizes)
    assert max_depth == (4 if max(sizes)>=2 else 3)
    assert (periodic-1)%3 == 0
    return total,periodic,max_depth


def main():
    q,h=finite_quotient_certificate()
    cases=[(1,1,1),(2,1,1),(1,2,3),(2,2,2),
           (1,1,1,1),(2,1,1,1),(2,2,1,1), (1,1,1,1,1)]
    total=0;record=[]
    for case in cases:
        n,p,d=direct_check(case)
        total+=n
        record.append((case,p,d))
    # Every ordinary signed 3-cycle contains 3 distinct configurations.
    print('VERIFY_OK quotient_classes=',q,
          'depth_period_histogram=',sorted(h.items()),
          'direct_configurations=',total,'cases=',record)

if __name__=='__main__':
    main()
