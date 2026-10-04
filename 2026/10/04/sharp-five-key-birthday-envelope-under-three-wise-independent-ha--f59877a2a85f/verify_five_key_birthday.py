#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations
from collections import Counter, defaultdict

TYPES = {
    (1,1,1,1,1): (0,0),
    (2,1,1,1): (1,0),
    (2,2,1): (2,0),
    (3,1,1): (3,1),
    (3,2): (4,1),
    (4,1): (6,4),
    (5,): (10,10),
}

def typ(y):
    return tuple(sorted(Counter(y).values(), reverse=True))

def moments(masses):
    s = sum(masses.values(), Fraction(0))
    t2 = sum(Fraction(TYPES[k][0]) * p for k,p in masses.items())
    t3 = sum(Fraction(TYPES[k][1]) * p for k,p in masses.items())
    return s,t2,t3

def upper(q):
    return {
        (1,1,1,1,1): Fraction(q*q - 5*q + 10, q*q),
        (2,2,1): Fraction(5*(q-4), q*q),
        (3,2): Fraction(10, q*q),
    }

def lower(q):
    if q >= 9:
        return {
            (1,1,1,1,1): Fraction((q-1)*(q-9), q*q),
            (2,1,1,1): Fraction(10*(q-1), q*q),
            (5,): Fraction(1, q*q),
        }
    return {
        (2,1,1,1): Fraction(2*(q-1)*(q-4), q*q),
        (2,2,1): Fraction((q-1)*(9-q), q*q),
        (5,): Fraction(1, q*q),
    }

def mix(A,B,t):
    out = defaultdict(Fraction)
    for k,p in A.items():
        out[k] += (1-t)*p
    for k,p in B.items():
        out[k] += t*p
    return {k:p for k,p in out.items() if p}

def check_symbolic():
    cert_checks = 0
    for k,(t2,t3) in TYPES.items():
        I = Fraction(0 if k == (1,1,1,1,1) else 1)
        assert Fraction(t2,2) - t3 <= I
        assert I <= t2 - Fraction(9,10)*t3
        cert_checks += 2

    formula_checks = 0
    for q in range(5, 2001):
        for masses in (upper(q), lower(q)):
            assert all(p >= 0 for p in masses.values())
            s,t2,t3 = moments(masses)
            assert s == 1
            assert t2 == Fraction(10,q)
            assert t3 == Fraction(10,q*q)
            formula_checks += 1

        u = upper(q).get((1,1,1,1,1), Fraction(0))
        l = lower(q).get((1,1,1,1,1), Fraction(0))
        assert u == Fraction(q*q-5*q+10, q*q)
        assert l == max(Fraction(0), Fraction((q-1)*(q-9), q*q))
    return cert_checks, formula_checks

def explicit_joint(q, masses):
    counts = Counter()
    for y in product(range(q), repeat=5):
        counts[typ(y)] += 1
    assert all(k in counts for k in masses)

    triple = {
        inds: defaultdict(Fraction)
        for inds in combinations(range(5),3)
    }
    total = Fraction(0)
    all_distinct = Fraction(0)

    for y in product(range(q), repeat=5):
        k = typ(y)
        if k not in masses:
            continue
        p = masses[k] / counts[k]
        total += p
        if k == (1,1,1,1,1):
            all_distinct += p
        for inds in triple:
            out = tuple(y[i] for i in inds)
            triple[inds][out] += p

    assert total == 1
    target = Fraction(1, q**3)
    marg_checks = 0
    for inds in triple:
        assert len(triple[inds]) == q**3
        for out in product(range(q), repeat=3):
            assert triple[inds][out] == target
            marg_checks += 1
    return all_distinct, marg_checks

def run():
    cert_checks, formula_checks = check_symbolic()
    explicit_cases = 0
    marginal_checks = 0

    for q in range(5, 10):
        U = upper(q)
        L = lower(q)
        M = mix(L, U, Fraction(1,2))
        for tag, masses in (("lower",L),("upper",U),("mid",M)):
            pA, checks = explicit_joint(q, masses)
            if tag == "upper":
                assert pA == Fraction(q*q-5*q+10, q*q)
            elif tag == "lower":
                assert pA == max(Fraction(0), Fraction((q-1)*(q-9), q*q))
            else:
                expected = (
                    Fraction(q*q-5*q+10, q*q)
                    + max(Fraction(0), Fraction((q-1)*(q-9), q*q))
                ) / 2
                assert pA == expected
            explicit_cases += 1
            marginal_checks += checks

    print(
        "VERIFY_OK "
        f"certificate_checks={cert_checks} "
        f"formula_checks={formula_checks} "
        f"explicit_joint_cases={explicit_cases} "
        f"triple_marginal_checks={marginal_checks}"
    )

if __name__ == "__main__":
    run()
