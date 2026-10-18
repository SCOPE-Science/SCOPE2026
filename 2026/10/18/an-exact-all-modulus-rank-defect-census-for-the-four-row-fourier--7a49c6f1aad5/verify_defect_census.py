"""Exact cyclotomic verification of a four-row Fourier defect census.

Requires Python >= 3.9, standard library only. No numerical tolerances.
Run: python verify_defect_census.py
"""
from itertools import combinations
from math import comb


def divide_monic(a, b):
    a = a[:]
    q = [0] * (max(0, len(a) - len(b)) + 1)
    while len(a) >= len(b):
        t, k = a[-1], len(a) - len(b)
        q[k] = t
        for j, bj in enumerate(b):
            a[j + k] -= t * bj
        while a and a[-1] == 0:
            a.pop()
    if a:
        raise AssertionError('nonexact cyclotomic division')
    return q


def cyclotomic(n, cache={}):
    if n not in cache:
        f = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                f = divide_monic(f, cyclotomic(d))
        cache[n] = f
    return cache[n]


def power_vectors(n):
    phi = cyclotomic(n)
    m = len(phi) - 1
    out = [(1,) + (0,) * (m - 1)]
    for _ in range(1, n):
        previous = out[-1]
        c = previous[-1]
        out.append(tuple(([0] + list(previous[:-1]))[i] - c * phi[i]
                         for i in range(m)))
    return out


def class_types(indices, n):
    S = set(indices)
    kind2 = False
    if n % 2 == 0:
        for a in indices:
            if (a + n // 2) % n in S:
                others = [b for b in indices if b != a and b != (a + n // 2) % n]
                if len(others) == 2 and (sum(others) - 2 * a) % n == 0:
                    kind2 = True
    kind3 = False
    if n % 3 == 0:
        third = n // 3
        for a in indices:
            if (a + third) % n in S and (a + 2 * third) % n in S:
                kind3 = True
    kind30 = False
    if n % 30 == 0:
        step = n // 30
        bases = ((0, 12, 13, 19), (0, 6, 7, 19))
        for anchor in indices:
            for pattern in bases:
                for b in pattern:
                    shift = (anchor - step * b) % n
                    if S == {(shift + step * v) % n for v in pattern}:
                        kind30 = True
    return kind2, kind3, kind30


def predicted(n):
    return ((n * (n - 2) // 4 - (n // 4 if n % 4 == 0 else 0)) if n % 2 == 0 else 0) + (n * (n - 3) // 3 if n % 3 == 0 else 0) - (n if n % 6 == 0 else 0) + (2 * n if n % 30 == 0 else 0)


def verify(n):
    phi = cyclotomic(n)
    vec = power_vectors(n)
    m = len(phi) - 1
    singular = 0
    types = [0, 0, 0]
    overlap = 0
    for a, b, c, d in combinations(range(n), 4):
        roots = (vec[(a + b) % n], vec[(a + c) % n], vec[(a + d) % n],
                 vec[(b + c) % n], vec[(b + d) % n], vec[(c + d) % n])
        zero = all(sum(v[k] for v in roots) == 0 for k in range(m))
        is2, is3, is30 = class_types((a, b, c, d), n)
        assert zero == (is2 or is3 or is30), (n, (a, b, c, d), zero, is2, is3, is30)
        if zero:
            singular += 1
            types[0] += int(is2)
            types[1] += int(is3)
            types[2] += int(is30)
            overlap += int(is2 and is3)
            assert not (is30 and (is2 or is3))
    assert singular == predicted(n)
    assert singular == sum(types) - overlap
    return n, comb(n, 4), singular, tuple(types), overlap


def primitive_certificate():
    from itertools import permutations
    S = (5, 25, 6, 12, 18, 24)
    matchings = set()
    for v in permutations(S):
        if (v[0] + v[1]) % 30 == (v[2] + v[3]) % 30 == (v[4] + v[5]) % 30:
            matchings.add(tuple(sorted(tuple(sorted(v[j:j+2])) for j in (0, 2, 4))))
    assert matchings == {((5, 25), (6, 24), (12, 18))}
    seeds = ((0, 12, 13, 19), (0, 6, 7, 19))
    for seed in seeds:
        products = sorted((a + b) % 30 for a, b in combinations(seed, 2))
        assert any(products == sorted((v + shift) % 30 for v in S) for shift in range(30))
        assert not any({(v + shift) % 30 for v in seed} == set(seed) for shift in range(1, 30))
    assert not any({(v + shift) % 30 for v in seeds[0]} == set(seeds[1]) for shift in range(30))
    print('primitive six-term pair matching unique; two distinct free translation orbits: PASS')




def symbolic_determinant_certificate():
    """Compare formal polynomials over Z in four commuting variables."""
    from itertools import permutations
    zero = (0, 0, 0, 0)
    def add(a, b):
        out = a.copy()
        for e, coeff in b.items():
            out[e] = out.get(e, 0) + coeff
            if not out[e]:
                del out[e]
        return out
    def mult(a, b):
        out = {}
        for ex, cx in a.items():
            for ey, cy in b.items():
                v = tuple(x + y for x, y in zip(ex, ey))
                out[v] = out.get(v, 0) + cx * cy
        return {x: y for x, y in out.items() if y}
    def mono(k, deg=1):
        return {tuple(deg if i == k else 0 for i in range(4)): 1}
    det = {}
    for perm in permutations(range(4)):
        inv = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        ex = [0, 0, 0, 0]
        for row, power in enumerate((0, 1, 3, 4)):
            ex[perm[row]] += power
        mon = {tuple(ex): (-1) ** inv}
        det = add(det, mon)
    vand = {zero: 1}
    for i, j in combinations(range(4), 2):
        vand = mult(vand, add(mono(j), {k: -v for k, v in mono(i).items()}))
    e2 = {}
    for i, j in combinations(range(4), 2):
        e2 = add(e2, mult(mono(i), mono(j)))
    assert det == mult(vand, e2), 'generalized Vandermonde identity false'
    print('formal determinant identity Vandermonde times e_2: PASS')

def main():
    symbolic_determinant_certificate()
    primitive_certificate()
    for n in (5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 27, 30, 36, 40, 42, 45, 50, 60):
        n, total, D, bykind, overlap = verify(n)
        print(f'N={n:3} all minors={total:7} rank-three={D:5} type-counts={bykind} 2-and-3-overlap={overlap} PASS')
    print('exact cyclotomic arithmetic and structural classification: all tests PASS')


if __name__ == '__main__':
    main()
