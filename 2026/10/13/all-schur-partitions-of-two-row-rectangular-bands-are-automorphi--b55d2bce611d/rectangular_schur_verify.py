"""Finite verification of a classification of Schur partitions of 2-by-m rectangular bands.

No external packages; run: python3 rectangular_schur_verify.py
The proof covers all m; this verifier checks the indicated finite cases only.
"""
from collections import defaultdict
from math import comb


def partitions(n):
    blocks = []
    def rec(k):
        if k == n:
            yield tuple(tuple(B) for B in blocks)
            return
        for B in blocks:
            B.append(k)
            yield from rec(k + 1)
            B.pop()
        blocks.append([k])
        yield from rec(k + 1)
        blocks.pop()
    yield from rec(0)


def labels(P, m):
    color = [-1] * (2*m)
    for a, B in enumerate(P):
        for u in B:
            color[u] = a
    return color


def schur_by_products(P, m):
    """Test exact coefficients of (sum A)(sum B) for all primitive sets A,B."""
    for A in P:
        for B in P:
            counts = [0] * (2*m)
            for u in A:
                for v in B:
                    counts[(u // m)*m + (v % m)] += 1
            for C in P:
                if len({counts[x] for x in C}) != 1:
                    return False
    return True


def form(P, m):
    """Recognize either a common-column row split or balanced color pairs."""
    colors = labels(P, m)
    row_counts = [(sum(x < m for x in B), sum(x >= m for x in B)) for B in P]
    if all(a == b for a, b in row_counts):
        sig = [tuple(sorted((colors[j], colors[m+j]))) for j in range(m)]
        if all(len({sig[x % m] for x in B}) == 1 for B in P):
            return 'balanced'
        return None
    if all(all(x < m for x in B) or all(x >= m for x in B) for B in P):
        if all((colors[j] == colors[k]) == (colors[m+j] == colors[m+k])
               for j in range(m) for k in range(m)):
            return 'separated'
    return None


def cycles_for_pair(P, m, typ):
    """Return explicit automorphism generators (row_flip, column_permutation)."""
    colors = labels(P, m)
    colgens = []
    ident = tuple(range(m))
    def trans(j, k):
        arr = list(ident)
        arr[j], arr[k] = arr[k], arr[j]
        colgens.append((False, tuple(arr)))
    if typ == 'separated':
        groups = defaultdict(list)
        for j in range(m):
            groups[colors[j]].append(j)
        for group in groups.values():
            for j in group[1:]:
                trans(group[0], j)
    elif typ == 'balanced':
        groups = defaultdict(list)
        for j in range(m):
            groups[tuple(sorted((colors[j], colors[m+j])))].append(j)
        flip = list(ident)
        for sig, J in groups.items():
            if sig[0] == sig[1]:
                for j in J[1:]:
                    trans(J[0], j)
            else:
                lo = sorted(j for j in J if colors[j] == sig[0])
                hi = sorted(j for j in J if colors[j] == sig[1])
                assert len(lo) == len(hi)
                for part in (lo, hi):
                    for j in part[1:]:
                        trans(part[0], j)
                for j, k in zip(lo, hi):
                    flip[j], flip[k] = flip[k], flip[j]
        colgens.append((True, tuple(flip)))
    return colgens


def generated_orbits(P, m, typ):
    gens = cycles_for_pair(P, m, typ)
    left = set(range(2*m))
    orbits = set()
    while left:
        seed = min(left)
        orbit = {seed}
        queue = [seed]
        while queue:
            u = queue.pop()
            for row_flip, colperm in gens:
                nxt = ((u//m) ^ row_flip)*m + colperm[u % m]
                if nxt not in orbit:
                    orbit.add(nxt)
                    queue.append(nxt)
        left -= orbit
        orbits.add(frozenset(orbit))
    return orbits


def bell(n):
    return sum(1 for _ in partitions(n))


def balanced_count(n):
    total = 0
    for P in partitions(n):
        term = 1
        for B in P:
            k = len(B)
            if k % 2 == 0:
                term *= 1 + comb(k, k//2)//2
        total += term
    return total


def verify():
    for m in range(1, 5):
        observed = {'separated': 0, 'balanced': 0}
        for P in partitions(2*m):
            direct = schur_by_products(P, m)
            t = form(P, m)
            assert direct == (t is not None), (m, P, direct, t)
            if t:
                observed[t] += 1
                assert generated_orbits(P, m, t) == {frozenset(B) for B in P}, (m, P, t)
        expected = {'separated': bell(m), 'balanced': balanced_count(m)}
        assert observed == expected, (m, observed, expected)
        print('m=%d: %d row-separated + %d balanced = %d Schur partitions; all automorphic' %
              (m, observed['separated'], observed['balanced'], sum(observed.values())))
    assert bell(5) == 52 and balanced_count(5) == 132
    print('m=5: formula = 52 + 132 = 184 (not exhaustively enumerated)')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
