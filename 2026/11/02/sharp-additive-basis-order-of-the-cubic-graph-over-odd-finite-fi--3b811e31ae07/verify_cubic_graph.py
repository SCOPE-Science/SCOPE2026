"""Independent finite-field checks for the cubic-graph additive-cover theorem.

Uses only Python's standard library. All sums are computed from scratch.
"""
from itertools import product


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def field(p, degree=1, nonsquare=None):
    assert is_prime(p) and p % 2 == 1
    if degree == 1:
        return list(range(p)), lambda a, b: (a + b) % p, lambda a, b: (a * b) % p
    assert degree == 2 and nonsquare is not None
    assert pow(nonsquare, (p - 1) // 2, p) == p - 1
    # a + p*b represents a + b*u, with u*u = nonsquare.
    def add(a, b):
        return ((a % p + b % p) % p) + p * ((a // p + b // p) % p)
    def mul(a, b):
        x, y = a % p, a // p
        z, w = b % p, b // p
        return ((x*z + nonsquare*y*w) % p) + p*((x*w + y*z) % p)
    return list(range(p*p)), add, mul


def check(p, degree=1, nonsquare=None):
    elems, add, mul = field(p, degree, nonsquare)
    q = len(elems)
    points = [(x, mul(mul(x, x), x)) for x in elems]
    pairs = {(add(x, y), add(x3, y3)) for (x, x3) in points for (y, y3) in points}
    triples = {(add(s, x), add(w, x3)) for (s, w) in pairs for (x, x3) in points}
    allpts = set(product(elems, repeat=2))
    if p == 3:
        assert triples == set(points)
        assert len(triples) == q
    elif q == 5:
        missed = {(s, mul(3, mul(mul(s, s), s))) for s in elems if s}
        assert allpts - triples == missed and len(missed) == 4
    elif q == 7:
        assert allpts - triples == {(0, 2), (0, 5)}
    else:
        assert q >= 11 and triples == allpts
    if p >= 5:
        assert pairs != allpts
        if q in (5, 7):
            fourth = {(add(s, x), add(w, x3)) for (s, w) in triples for (x, x3) in points}
            assert fourth == allpts
    print(f"CASE_OK p={p} degree={degree} q={q} two={len(pairs)} three={len(triples)} missing={q*q-len(triples)}")


if __name__ == '__main__':
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        check(p)
    for p, a in ((3, 2), (5, 2), (7, 3), (11, 10)):
        check(p, 2, a)
    print('VERIFY_OK 12 fields, exact sumsets and sharp boundary cases')
