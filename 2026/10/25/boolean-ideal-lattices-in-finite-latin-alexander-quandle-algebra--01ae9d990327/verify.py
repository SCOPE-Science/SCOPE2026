"""Exact checks for the Fourier-coordinate ideal decomposition of Latin Alexander quandle algebras.

Run: python verify.py
Uses only the Python standard library.
"""
from itertools import combinations, product
from math import gcd
from random import Random


def root_of_order(n, q):
    assert (q - 1) % n == 0
    assert all(q % d for d in range(2, int(q ** .5) + 1))
    for w in range(2, q):
        if pow(w, n, q) == 1 and all(pow(w, n // p, q) != 1 for p in prime_divisors(n)):
            return w
    raise AssertionError((n, q))


def prime_divisors(n):
    return [p for p in range(2, n + 1) if n % p == 0 and all(p % d for d in range(2, int(p ** .5) + 1))]


def orbit_partition(n, t):
    remaining = set(range(n))
    out = []
    while remaining:
        start = min(remaining)
        todo, orb = [start], set()
        while todo:
            x = todo.pop()
            if x in orb:
                continue
            orb.add(x)
            todo.extend([t * x % n, (1 - t) * x % n])
        assert orb <= remaining
        remaining -= orb
        out.append(frozenset(orb))
    return out


def fw(a, w, n, q):
    return [sum(a[x] * pow(w, j * x, q) for x in range(n)) % q for j in range(n)]


def coefficient_product(a, b, n, t, q):
    c = [0] * n
    for x, vx in enumerate(a):
        for y, vy in enumerate(b):
            c[(t * x + (1 - t) * y) % n] = (c[(t * x + (1 - t) * y) % n] + vx * vy) % q
    return c


def rank_mod(rows, q):
    a = [[x % q for x in row] for row in rows]
    if not a:
        return 0
    n = len(a[0]); r = 0
    for c in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, q)
        a[r] = [(x * inv) % q for x in a[r]]
        for i in range(r + 1, len(a)):
            mult = a[i][c]
            a[i] = [(a[i][j] - mult * a[r][j]) % q for j in range(n)]
        r += 1
        if r == len(a):
            break
    return r


def all_rref(n, q):
    for d in range(n + 1):
        for pivots in combinations(range(n), d):
            positions = [(i, j) for i in range(d) for j in range(pivots[i] + 1, n) if j not in pivots]
            for values in product(range(q), repeat=len(positions)):
                rows = [[0] * n for _ in range(d)]
                for i, j in enumerate(pivots):
                    rows[i][j] = 1
                for (i, j), v in zip(positions, values):
                    rows[i][j] = v
                yield rows


def check_all_ideals_f7_r3():
    n, q, t = 3, 7, -1
    ideals, count = [], 0
    for B in all_rref(n, q):
        count += 1
        dim = len(B)
        good = True
        for b in B:
            for j in range(n):
                e = [int(k == j) for k in range(n)]
                left = [b[t*k % n] * e[((1 - t) * k) % n] % q for k in range(n)]
                right = [e[t*k % n] * b[((1 - t) * k) % n] % q for k in range(n)]
                if rank_mod(B + [left], q) > dim or rank_mod(B + [right], q) > dim:
                    good = False
                    break
            if not good:
                break
        if good:
            ideals.append(B)
    assert count == 116, count
    assert len(ideals) == 4, len(ideals)
    assert sorted(map(len, ideals)) == [0, 1, 2, 3]
    return count, len(ideals)


def check_case(n, q, t, seed):
    assert gcd(t, n) == gcd(1 - t, n) == 1
    w = root_of_order(n, q)
    orbits = orbit_partition(n, t)
    r = len(orbits)
    covered = set.union(*map(set, orbits))
    assert covered == set(range(n))
    for O in orbits:
        for k in O:
            assert t * k % n in O and (1 - t) * k % n in O
        # Every nonzero coordinate generates the entire orbit as an ideal.
        for a in O:
            reached, pending = {a}, [a]
            while pending:
                j = pending.pop()
                for nxt in (t * j % n, (1 - t) * j % n):
                    if nxt not in reached:
                        reached.add(nxt); pending.append(nxt)
            assert reached == set(O)
    rng = Random(seed)
    for _ in range(120):
        a = [rng.randrange(q) for _ in range(n)]
        b = [rng.randrange(q) for _ in range(n)]
        f, g = fw(a, w, n, q), fw(b, w, n, q)
        h = fw(coefficient_product(a, b, n, t, q), w, n, q)
        assert h == [f[(t * j) % n] * g[((1 - t) * j) % n] % q for j in range(n)]
    return r, sorted(map(len, orbits))


def check_vector_space_f3_squared():
    n, q = 3, 7
    w = root_of_order(n, q)
    pts = [(a, b) for a in range(3) for b in range(3)]
    chars = pts[:]
    orbits = []
    unused = set(chars)
    while unused:
        v = min(unused)
        orb = frozenset([v, ((-v[0]) % 3, (-v[1]) % 3)])
        assert orb <= unused
        unused -= orb
        orbits.append(orb)
    assert sorted(map(len, orbits)) == [1, 2, 2, 2, 2]
    rng = Random(2026)
    for _ in range(100):
        a = {x:rng.randrange(q) for x in pts}
        b = {x:rng.randrange(q) for x in pts}
        product_ab = {x:0 for x in pts}
        for x in pts:
            for y in pts:
                z = ((-x[0] + 2*y[0]) % 3, (-x[1] + 2*y[1]) % 3)
                product_ab[z] = (product_ab[z] + a[x]*b[y]) % q
        def fhat(vec, c):
            return sum(vec[x] * pow(w, c[0]*x[0] + c[1]*x[1], q) for x in pts) % q
        for c in chars:
            neg = ((-c[0]) % 3, (-c[1]) % 3)
            assert fhat(product_ab, c) == fhat(a, neg)*fhat(b, neg)%q
    print('F3^2 over F7: 5 simple ideals, dimensions [1,2,2,2,2], 32 ideals; 100 exact product checks')


def main():
    for n, q in [(3, 7), (5, 11), (7, 29), (9, 19), (11, 23), (15, 31), (17, 103), (31, 311)]:
        # 11 | 22; 23 is prime. 31 | 310; 311 is prime.
        r, dims = check_case(n, q, -1, seed=n+q)
        print('Cyclic n=%d over F_%d: %d simple ideals, dimensions %s, two-sided ideal count %d' % (n, q, r, dims, 2**r))
    r, dims = check_case(31, 311, 3, seed=333)
    print('Alexander Z31 scalar 3: %d simple ideals, dimensions %s' % (r, dims))
    check_vector_space_f3_squared()
    tested, found = check_all_ideals_f7_r3()
    print('R3/F7: exhaustive enumeration of %d subspaces gives %d two-sided ideals' % (tested, found))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
