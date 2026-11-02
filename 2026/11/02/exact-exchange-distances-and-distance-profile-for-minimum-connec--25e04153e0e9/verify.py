#!/usr/bin/env python3
"""Standalone check of crown-graph connected domination and minimum-set exchanges.
Usage: python3 verify.py
Requires only the Python standard library.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def crown_cds(n, bitmask):
    """Directly test the original domination and induced-connectivity definitions."""
    if not bitmask:
        return False
    vertices = [i for i in range(2*n) if bitmask & (1 << i)]
    def adjacent(i, j):
        if (i < n) == (j < n):
            return False
        return (i % n) != (j % n)
    for i in range(2*n):
        if not (bitmask & (1 << i)) and not any(adjacent(i, j) for j in vertices):
            return False
    reached = {vertices[0]}
    queue = deque([vertices[0]])
    while queue:
        i = queue.popleft()
        for j in vertices:
            if j not in reached and adjacent(i, j):
                reached.add(j)
                queue.append(j)
    return len(reached) == len(vertices)


def check(n):
    bits = (1 << n) - 1
    all_cds = set()
    observed_card = Counter()
    for mask in range(1, 1 << (2*n)):
        A = {i for i in range(n) if mask & (1 << i)}
        B = {i for i in range(n) if mask & (1 << (n+i))}
        structural = len(A) >= 2 and len(B) >= 2 and not (len(A) == len(B) == 2 and A == B)
        actual = crown_cds(n, mask)
        assert actual == structural, (n, mask, A, B, actual)
        if actual:
            all_cds.add(mask)
            observed_card[mask.bit_count()] += 1
    # Full polynomial = ((1+z)^n-1-nz)^2 - C(n,2)z^4.
    expected_card = Counter()
    for a in range(2, n+1):
        for b in range(2, n+1):
            expected_card[a+b] += comb(n, a)*comb(n, b)
    expected_card[4] -= comb(n, 2)
    assert observed_card == expected_card, (n, observed_card, expected_card)

    minimal = {mask for mask in all_cds if all((mask ^ (1 << i)) not in all_cds
                    for i in range(2*n) if mask & (1 << i))}
    pairs = list(combinations(range(n), 2))
    labels = []
    to_mask = {}
    for A in pairs:
        for B in pairs:
            if A == B:
                continue
            mask = sum(1 << i for i in A) + sum(1 << (n+i) for i in B)
            assert mask in minimal
            labels.append((A, B))
            to_mask[(A,B)] = mask
    assert len(minimal) == len(labels) == comb(n,2)*(comb(n,2)-1)
    assert len(minimal) == n*(n-1)*(n-2)*(n+1)//4
    assert all(mask.bit_count() == 4 for mask in minimal)

    index = {v:i for i,v in enumerate(labels)}
    adj = [[] for _ in labels]
    for i, (A,B) in enumerate(labels):
        src = to_mask[(A,B)]
        for j, (C,D) in enumerate(labels):
            if i == j:
                continue
            dst = to_mask[(C,D)]
            jump = (src ^ dst).bit_count() == 2
            johnson = ((B==D and len(set(A)&set(C))==1) or
                       (A==C and len(set(B)&set(D))==1))
            assert jump == johnson, (n,(A,B),(C,D))
            if jump:
                adj[i].append(j)
                # Every crown edge changes bipartition, hence slides cannot
                # preserve the two-per-side minimum-CDS occupancy.
    v = comb(n, 2)
    k = 2*(n-2)
    q = comb(n-2, 2)
    assert k+q+1 == v
    deg = Counter()
    for i,(A,B) in enumerate(labels):
        observed = len(adj[i])
        expected = 2*k - (2 if len(set(A)&set(B)) == 1 else 0)
        assert observed == expected
        deg[observed] += 1
    assert deg[2*k-2] == v*k
    if q:
        assert deg[2*k] == v*q
    assert sum(len(x) for x in adj)//2 == v*k*(v-2)

    distance_profile = Counter()
    for i,(A,B) in enumerate(labels):
        found = {i:0}
        queue = deque([i])
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if b not in found:
                    found[b] = found[a]+1
                    queue.append(b)
        assert len(found) == len(labels)
        for j,(C,D) in enumerate(labels):
            dA = 2-len(set(A)&set(C))
            dB = 2-len(set(B)&set(D))
            exception = int(A==D and B==C and len(set(A)&set(B))==1)
            predicted = dA+dB+exception
            assert found[j] == predicted, (n, (A,B), (C,D), found[j], predicted)
            distance_profile[found[j]] += 1
    # Complete ordered-pair distance polynomial.
    expected = {
        0:v*(v-1),
        1:2*v*(v-2)*k,
        2:v*(v-2)*(k*k+2*q),
        3:2*v*(v-2)*k*q+v*k,
        4:v*(v-2)*q*q+v*q,
    }
    assert all(distance_profile[d] == expected[d] for d in range(5))
    assert sum(distance_profile.values()) == len(labels)**2
    assert max(distance_profile) == (3 if n==3 else 4)
    print('n=%d; cds=%d; min=%d; exchange_edges=%d; distance_profile=%s' % (
        n, len(all_cds), len(minimal), sum(map(len,adj))//2,
        tuple(distance_profile[d] for d in range(5))))


if __name__ == '__main__':
    for n in range(3,8):
        check(n)
    print('VERIFY_OK')
