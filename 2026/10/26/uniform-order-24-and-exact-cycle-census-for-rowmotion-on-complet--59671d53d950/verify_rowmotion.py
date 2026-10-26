#!/usr/bin/env python3
"""Finite-state certificate for rowmotion on incidence posets of K_{2,n}.

Requires Python >=3.9 and the standard library only. No external data.
Run: python3 verify_rowmotion.py
"""
from collections import Counter
from math import comb, lcm

# A column type records (leaf-in-ideal, first edge-in-ideal,
# second edge-in-ideal). An edge in the ideal forces its endpoints in.
COLUMN = ((0, 0, 0), (1, 0, 0), (1, 1, 0),
          (1, 0, 1), (1, 1, 1))
BY_VECTOR = {x: i for i, x in enumerate(COLUMN)}


def alphabet(h):
    return frozenset(i for i, (c, e0, e1) in enumerate(COLUMN)
                     if not (e0 and not (h & 1))
                     and not (e1 and not (h & 2)))


def column_step(h, x):
    c, e0, e1 = COLUMN[x]
    d0 = int(bool(h & 1) and bool(c) and not bool(e0))
    d1 = int(bool(h & 2) and bool(c) and not bool(e1))
    cp = int(not c or d0 or d1)
    return BY_VECTOR[(cp, d0, d1)]


def support_step(state):
    h, support = state
    image = frozenset(column_step(h, x) for x in support)
    hp = 0
    for i in range(2):
        if not (h & (1 << i)) or any(COLUMN[x][i + 1] for x in image):
            hp |= 1 << i
    assert image and image <= alphabet(hp)
    return (hp, image)


def support_orbits():
    universe = set()
    for h in range(4):
        a = sorted(alphabet(h))
        for bits in range(1, 1 << len(a)):
            universe.add((h, frozenset(a[i] for i in range(len(a))
                                       if bits & (1 << i))))
    assert len(universe) == 48
    assert {support_step(s) for s in universe} == universe
    orbits = []
    used = set()
    for start in sorted(universe, key=lambda s: (len(s[1]), s[0], sorted(s[1]))):
        if start in used:
            continue
        cur = start
        path = []
        while cur not in used:
            used.add(cur)
            path.append(cur)
            cur = support_step(cur)
        assert cur == start
        action = {x: x for x in start[1]}
        for h, _ in path:
            action = {x: column_step(h, y) for x, y in action.items()}
        assert set(action.values()) == set(start[1])
        unseen = set(action)
        lengths = []
        while unseen:
            x = next(iter(unseen))
            y = x
            t = 0
            while y in unseen:
                unseen.remove(y)
                y = action[y]
                t += 1
            assert y == x
            lengths.append(t)
        q = lcm(*lengths)
        k = len(start[1])
        p = len(path)
        orbits.append((k, p, q, p*q, start))
    assert len(used) == 48
    assert len(orbits) == 13
    expected = [
        (1, 2, 1), (1, 3, 1), (1, 8, 1),
        (2, 1, 2), (2, 4, 1), (2, 4, 2), (2, 8, 1),
        (3, 1, 3), (3, 3, 2), (3, 8, 3),
        (4, 2, 3), (4, 3, 2), (5, 1, 6),
    ]
    assert sorted((k, p, q) for k, p, q, _, _ in orbits) == expected
    assert sum(p for _, p, _, _, _ in orbits) == 48
    return orbits


def onto(n, k):
    return sum((-1)**(k-j)*comb(k, j)*j**n for j in range(k+1))


def predicted(n):
    return {
        2: 2**(n-1),
        3: 3**(n-1) - 2**n + 2,
        4: 2**n - 2,
        6: (5**n - 7*3**n + 11*2**n - 6)//6,
        8: 3*2**(n-1) - 2,
        24: 3**(n-1) - 2**n + 1,
    }


def from_support(n, orbits):
    answer = Counter()
    for k, _, q, length, _ in orbits:
        assert onto(n, k) % q == 0
        answer[length] += onto(n, k)//q
    return {length: answer[length] for length in (2,3,4,6,8,24)}


def direct_census(n):
    # Independent calculation using all actual ideals and the literal
    # minimal-complement definition of rowmotion, cross-checked against
    # the reverse-rank toggle sweep.
    m = n+2
    vfull = (1 << m)-1
    edges = [(i, 2+j) for i in (0,1) for j in range(n)]
    masks = [(1 << u) | (1 << v) for u,v in edges]
    all_states = set()
    for vertices in range(1 << m):
        eligible = sum(1 << i for i, endpoints in enumerate(masks)
                       if endpoints & vertices == endpoints)
        edges_in = eligible
        while True:
            all_states.add((vertices, edges_in))
            if edges_in == 0:
                break
            edges_in = (edges_in-1) & eligible
    assert len(all_states) == 2**n + 2*3**n + 5**n

    successors = {}
    for vertices, present in all_states:
        eligible = sum(1 << i for i, endpoints in enumerate(masks)
                       if endpoints & vertices == endpoints)
        new_edges = eligible ^ present
        via_complement = vfull ^ vertices
        for i, endpoints in enumerate(masks):
            if new_edges & (1 << i):
                via_complement |= endpoints
        successor = (via_complement, new_edges)

        # Literal toggles in rank order: edges first, vertices second.
        tv, te = vertices, present
        for i, endpoints in enumerate(masks):
            if te & (1 << i):
                te ^= 1 << i
            elif tv & endpoints == endpoints:
                te |= 1 << i
        for v in range(m):
            incident_present = any(te & (1 << i) and
                                   (endpoints & (1 << v))
                                   for i, endpoints in enumerate(masks))
            if tv & (1 << v):
                if not incident_present:
                    tv ^= 1 << v
            else:
                tv |= 1 << v
        assert (tv, te) == successor
        assert successor in all_states
        successors[(vertices, present)] = successor

    assert len(set(successors.values())) == len(all_states)
    histogram = Counter()
    pending = set(all_states)
    while pending:
        start = next(iter(pending))
        x = start
        cycle = []
        while x in pending:
            pending.remove(x)
            cycle.append(x)
            x = successors[x]
        assert x == start
        histogram[len(cycle)] += 1
    return histogram


def main():
    orbits = support_orbits()
    for n in range(2, 20):
        formula = predicted(n)
        assert formula == from_support(n, orbits)
        assert sum(k*v for k,v in formula.items()) == 2**n+2*3**n+5**n
    for n in range(2, 7):
        assert predicted(n) == {k: direct_census(n)[k]
                                 for k in (2,3,4,6,8,24)}
    assert {length for _,_,_,length,_ in orbits} == {2,3,4,6,8,24}
    assert lcm(*(length for _,_,_,length,_ in orbits)) == 24
    print('VERIFY_OK: 48 support states; 13 support orbits; order 24; '
          'formulas through n=19; independently enumerated n=2..6')

if __name__ == '__main__':
    main()
