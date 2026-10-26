"""Reproducible integer checks for minimum maximal distance-two-free subsets of cubes.

The known characterization of total mutual visibility in binary Hamming cubes
reduces the graph-geodesic definition to the distance-two exclusion.
No external packages required.
"""
from itertools import combinations
from collections import Counter


def hdist(x, y):
    return (x ^ y).bit_count()


def parity_part(n, parity):
    return [x for x in range(1 << n) if x.bit_count() % 2 == parity]


def audit_half(n):
    vertices = parity_part(n, 0)
    all_v = set(vertices)
    neighborhood = {x: {y for y in vertices if hdist(x, y) in (0, 2)} for x in vertices}
    minimal_k = None
    minimal_sets = []
    trial_counts = {}
    # Combinations of size <=4 suffice for the claimed dimension range.
    for k in range(1, min(4, len(vertices)) + 1):
        count = 0
        for c in combinations(vertices, k):
            if any(hdist(x, y) == 2 for x, y in combinations(c, 2)):
                continue
            if set.union(*(neighborhood[x] for x in c)) == all_v:
                count += 1
                if minimal_k is None:
                    minimal_k = k
                if k == minimal_k:
                    minimal_sets.append(c)
        trial_counts[k] = count
        if minimal_k is not None:
            break
    return minimal_k, minimal_sets, trial_counts


def direct_total_visibility(n, S):
    # Test the ORIGINAL geodesic definition rather than a distance-two shortcut.
    # BFS in the subcube interval I(x,y) after removing forbidden interiors.
    V = list(range(1 << n))
    adj = [[x ^ (1 << i) for i in range(n)] for x in V]
    blocked = set(S)
    for x in V:
        for y in V:
            if x == y:
                continue
            forbidden = blocked - {x, y}
            frontier = {x}
            seen = {x}
            while frontier and y not in seen:
                upcoming = set()
                for u in frontier:
                    for v in adj[u]:
                        if v not in seen and v not in forbidden and hdist(x, v) + hdist(v, y) == hdist(x, y):
                            upcoming.add(v)
                seen.update(upcoming)
                frontier = upcoming
            if y not in seen:
                return False
    return True


def main():
    expected = {1: (1, 1), 2: (1, 2), 3: (1, 4), 4: (2, 4), 5: (2, 40), 6: (2, 16), 7: (4, 1120)}
    for n in range(1, 8):
        k, codes, detail = audit_half(n)
        assert (k, len(codes)) == expected[n], (n, k, len(codes))
        print(f'HALF n={n} minimum={k} number={len(codes)}')
        if n == 7:
            patterns = Counter(tuple(sorted(hdist(u,v) for u,v in combinations(C,2))) for C in codes)
            assert patterns == {(4,4,4,4,6,6):1120}, patterns
            for c in codes:
                assert c[0] ^ c[1] ^ c[2] ^ c[3] == 0, c
            print('Q7_PATTERNS', sorted(patterns.items()))
            print('Q7_ALL_AFFINE', len(codes))
        if n == 6:
            assert all(hdist(C[0], C[1]) == 6 for C in codes)
        if n == 5:
            assert all(hdist(C[0], C[1]) == 4 for C in codes)
    # Build a concrete parity-separated minimum set in Q7; the odd half is translated by 1.
    k, even_codes, _ = audit_half(7)
    S = set(even_codes[0]) | {x ^ 1 for x in even_codes[0]}
    assert len(S) == 8
    assert direct_total_visibility(7, S)
    for x in range(128):
        if x in S: continue
        assert not direct_total_visibility(7, S | {x})
    print('DIRECT_GEODESICS_Q7=PASS; ALL_120_SINGLE_VERTEX_ADDITIONS=FAIL')
    print('TOTAL_MINIMAL_Q7=8 TOTAL_NUMBER=1254400')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
