"""Exhaustive reproducibility checks for the Kneser-pair higher independence theorem.
Only the finite test instances are verified computationally; the all-order
classification follows from the separate symbolic Morse-matching proof.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb
import sys


def verify_universal_block():
    """Check all 37 members of the order-independent six-bit upper filter."""
    q = {mask for mask in range(64)
         if any(mask & (3 << 2 * i) == (3 << 2 * i) for i in range(3))}
    assert len(q) == 37
    live = set(q)
    pairs = {}
    for pivot in (0, 2, 4):
        bit = 1 << pivot
        lowers = {mask for mask in live if not mask & bit and mask | bit in live}
        for lower in lowers:
            pairs[lower] = lower | bit
        live -= lowers | {lower | bit for lower in lowers}
    assert len(pairs) == 18 and live == {0b101011}
    directions = {f: [] for f in q}
    indegree = {f: 0 for f in q}
    for upper in q:
        for bit in (1 << j for j in range(6) if upper & (1 << j)):
            lower = upper ^ bit
            if lower not in q:
                continue
            src, dst = (lower, upper) if pairs.get(lower) == upper else (upper, lower)
            directions[src].append(dst)
            indegree[dst] += 1
    pending = deque(f for f in q if indegree[f] == 0)
    count = 0
    while pending:
        src = pending.popleft()
        count += 1
        for dst in directions[src]:
            indegree[dst] -= 1
            if not indegree[dst]:
                pending.append(dst)
    assert count == 37
    print('universal_6_bit_block faces=37 matched_pairs=18 critical_3=1 acyclic=PASS', flush=True)


def verify(n):
    edges = list(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    degree = len(edges)
    disj = [sum(1 << j for j, f in enumerate(edges) if not set(e).intersection(f)) for e in edges]
    faces = []

    def enumerate_faces(pos, mask, used):
        faces.append(mask)
        for j in range(pos, degree):
            meets = mask & disj[j]
            if meets.bit_count() > 1 or (meets & used):
                continue
            enumerate_faces(j + 1, mask | (1 << j), used | meets | ((1 << j) if meets else 0))

    enumerate_faces(0, 0, 0)
    allfaces = set(faces)
    assert len(allfaces) == len(faces)
    pairs = {}
    matched = set()
    fibers = {}
    blocks = {}
    four_universe = set(range(1, n))
    for mask in faces:
        h = [edges[j] for j in range(degree) if mask & (1 << j) and 0 not in edges[j]]
        opposite = [(a, b) for a, b in combinations(h, 2) if not set(a).intersection(b)]
        if not opposite:
            key = tuple(h)
            fibers.setdefault(key, []).append(mask)
        else:
            a, b = opposite[0]
            U = frozenset(a + b)
            assert len(U) == 4 and U.issubset(four_universe)
            assert all(set(edges[j]).issubset(U) for j in range(degree) if mask & (1 << j))
            blocks.setdefault(U, []).append(mask)

    def match(lower, upper):
        assert lower in allfaces and upper in allfaces
        assert lower not in matched and upper not in matched
        assert upper.bit_count() == lower.bit_count() + 1
        assert lower & upper == lower
        pairs[lower] = upper
        matched.add(lower)
        matched.add(upper)

    for key, masks in fibers.items():
        if not key:
            pivot = 1
        else:
            common = set(key[0])
            for edge in key[1:]:
                common.intersection_update(edge)
            if common:
                pivot = min(common)
            else:
                assert len(key) == 3
                pivot = min(v for edge in key for v in edge)
        bit = 1 << edge_index[(0, pivot)]
        masksset = set(masks)
        for mask in masks:
            if not mask & bit:
                assert mask | bit in masksset, (n, 'star fiber failure', key, mask)
                match(mask, mask | bit)

    block_critical = []
    for U, masks in blocks.items():
        a, b, c, d = sorted(U)
        local = set(masks)
        for e in ((a, b), (a, c), (a, d)):
            bit = 1 << edge_index[e]
            candidates = [mask for mask in local if not mask & bit and mask | bit in local]
            for lower in candidates:
                match(lower, lower | bit)
                local.remove(lower)
                local.remove(lower | bit)
        assert len(local) == 1, (n, 'critical block size', U, local)
        crit = next(iter(local))
        expected = ((a, b), (c, d), (b, d), (b, c))
        assert crit == sum(1 << edge_index[e] for e in expected), (n, U, crit, expected)
        block_critical.append(crit)

    critical = allfaces - matched
    assert set(block_critical) == critical
    assert len(critical) == comb(n - 1, 4)
    assert all(mask.bit_count() == 4 for mask in critical)
    assert 0 in matched

    # Directed matching-poset Hasse diagram; augmented empty face included.
    adj = {mask: [] for mask in faces}
    indegree = {mask: 0 for mask in faces}
    incidences = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            lower = upper ^ bit
            assert lower in allfaces
            if pairs.get(lower) == upper:
                src, target = lower, upper
            else:
                src, target = upper, lower
            adj[src].append(target)
            indegree[target] += 1
            incidences += 1
            bits ^= bit
    zero = deque(mask for mask, count in indegree.items() if not count)
    seen = 0
    while zero:
        mask = zero.popleft()
        seen += 1
        for target in adj[mask]:
            indegree[target] -= 1
            if not indegree[target]:
                zero.append(target)
    assert seen == len(faces), (n, 'directed cycle', seen, len(faces))
    euler = sum((-1) ** (mask.bit_count() - 1) for mask in faces if mask)
    assert euler == 1 - comb(n - 1, 4), (n, euler)
    print('n=%d faces=%d matched_pairs=%d critical_3=%d cover_relations=%d acyclic=PASS'
          % (n, len(faces), len(pairs), len(critical), incidences), flush=True)


if __name__ == '__main__':
    verify_universal_block()
    for n in (int(x) for x in sys.argv[1:]) if len(sys.argv) > 1 else range(5, 10):
        verify(n)
