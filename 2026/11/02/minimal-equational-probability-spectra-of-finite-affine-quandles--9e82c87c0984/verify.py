"""Finite checks for probability spectra of affine quandles.

Runs with CPython 3 and the standard library.  Small-field checks do not
replace the general algebraic proof.
"""
from itertools import product
from math import factorial


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def zero(n):
    return tuple((0,) * n for _ in range(n))


def add(A, B, p):
    return tuple(tuple((x + y) % p for x, y in zip(r, s))
                 for r, s in zip(A, B))


def sub(A, B, p):
    return tuple(tuple((x - y) % p for x, y in zip(r, s))
                 for r, s in zip(A, B))


def mult(A, B, p):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) % p
                       for j in range(n)) for i in range(n))


def rank(rows, p):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    n, m = len(a), len(a[0])
    pivots = 0
    for j in range(m):
        k = next((i for i in range(pivots, n) if a[i][j] % p), None)
        if k is None:
            continue
        a[pivots], a[k] = a[k], a[pivots]
        inv = pow(a[pivots][j], -1, p)
        a[pivots] = [(v * inv) % p for v in a[pivots]]
        for i in range(n):
            if i != pivots:
                f = a[i][j]
                a[i] = [(v - f * w) % p for v, w in zip(a[i], a[pivots])]
        pivots += 1
        if pivots == n:
            break
    return pivots


def ring(A, p):
    n = len(A)
    powers = [eye(n)]
    for _ in range(1, n):
        powers.append(mult(powers[-1], A, p))
    out = set()
    for cc in product(range(p), repeat=n):
        B = zero(n)
        for c, P in zip(cc, powers):
            for _ in range(c):
                B = add(B, P, p)
        out.add(B)
    return out


def coefficients(A, p, arity):
    # Here A is the coefficient 1-T of the first argument, while T=I-A.
    n = len(A)
    I = eye(n)
    Z = zero(n)
    U = sub(I, A, p)
    start = set()
    for i in range(arity):
        start.add(tuple(I if i == j else Z for j in range(arity)))
    seen = set(start)
    # Closure of term coefficient tuples under the *only* basic operation.
    while True:
        old = list(seen)
        new = set()
        for x in old:
            for y in old:
                z = tuple(add(mult(A, a, p), mult(U, b, p), p)
                          for a, b in zip(x, y))
                if z not in seen:
                    new.add(z)
        if not new:
            return seen
        seen.update(new)


def spectrum(A, p, arity):
    n = len(A)
    clone = coefficients(A, p, arity)
    out = set()
    for x in clone:
        for y in clone:
            D = [sub(a, b, p) for a, b in zip(x, y)]
            block = [sum((list(B[i]) for B in D), []) for i in range(n)]
            out.add(rank(block, p))
    return len(clone), tuple(sorted(out))


def gl_order(s, q):
    v = 1
    for i in range(s):
        v *= q ** s - q ** i
    return v


def mobius(n):
    k = 0
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return 0
        if n % d == 0:
            k += 1
            n //= d
        else:
            d += 1
    if n > 1:
        k += 1
    return (-1) ** k


def irreducible_count(p, d):
    return sum(mobius(e) * p ** (d // e)
               for e in range(1, d + 1) if d % e == 0) // d


def n_types(p, m):
    return 1 + sum(irreducible_count(p, d) - (2 if d == 1 else 0)
                   for d in range(1, m + 1) if m % d == 0)


def labeled_tables(p, m):
    n = p ** m
    ans = 1
    for d in range(1, m + 1):
        if m % d:
            continue
        count = irreducible_count(p, d) - (2 if d == 1 else 0)
        ans += count * (factorial(n) // (n * gl_order(m // d, p ** d)))
    return ans


def main():
    tests = [
        ('F2 quadratic irreducible', 2, ((0, 1), (1, 1)), 2, (0, 2)),
        ('F2 two identical irreducible blocks', 2,
         ((0, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 1)), 3, (0, 4)),
        ('F3 scalar -1', 3, ((2, 0), (0, 2)), 3, (0, 2)),
        ('F3 nonlatin nonprojection', 3, ((0, 0), (0, 2)), 3, (0, 1, 2)),
        ('F3 nonsemisimple latin', 3, ((2, 1), (0, 2)), 3, (0, 1, 2)),
        ('F5 split semisimple latin', 5, ((2, 0), (0, 3)), 2, (0, 1, 2)),
        ('F2 projection', 2, ((0, 0), (0, 0)), 3, (0, 2)),
    ]
    for name, p, A, arity, expected in tests:
        A = tuple(tuple(r) for r in A)
        n = len(A)
        R = ring(A, p)
        b = coefficients(A, p, 2)
        present = {u[0] for u in b}
        latin = rank(A, p) == n and rank(sub(eye(n), A, p), p) == n
        if latin:
            assert present == R, (name, 'binary term coefficient gap', len(present), len(R))
        c, ranks = spectrum(A, p, arity)
        assert ranks == expected, (name, ranks, expected)
        print(f'{name}: |R|={len(R)}, Latin={latin}, arity={arity}, terms={c}, equation ranks={ranks}')
    for p, m, expected_types, expected_labeled in [(2, 1, 1, 1), (2, 2, 2, 3),
                                                    (3, 1, 2, 2), (3, 2, 5, 15961)]:
        assert n_types(p, m) == expected_types
        assert labeled_tables(p, m) == expected_labeled
        print(f'order={p**m}: types={expected_types}, labeled={expected_labeled}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
