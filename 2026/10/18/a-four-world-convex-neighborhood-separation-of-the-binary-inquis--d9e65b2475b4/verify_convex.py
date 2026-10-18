#!/usr/bin/env python3
"""Finite semantic cross-check for a four-world convex-neighborhood separation.

No external dependencies. Run: python3 verify_convex.py.
All models and finite truth predicates are constructed independently of paper notation.
"""
W = range(4)                 # 0=a, 1=a', 2=b, 3=c
TYPES = (0, 0, 1, 2)        # (p,q)=(0,0),(0,0),(1,0),(0,1)
U = (1 << 0)
T = (1 << 0) | (1 << 2)
V = (1 << 1) | (1 << 2) | (1 << 3)
LEFT = frozenset((U, V))
RIGHT = frozenset((U, T, V))
P = (1 << 2)
Q = (1 << 3)


def subsets(mask):
    return [s for s in range(1 << len(W)) if s & ~mask == 0]


def convex(fam):
    for x in fam:
        for y in fam:
            if x & ~y == 0:
                for s in subsets(y):
                    if s and x & ~s == 0 and s not in fam:
                        return False
    return True


def signature(s):
    out = 0
    for w in W:
        if s & (1 << w):
            out |= 1 << TYPES[w]
    return out


def downsets():
    universe = range(1 << 3)
    out = []
    for d in range(1 << (1 << 3)):
        if not (d & 1):
            continue
        if all(not (d & (1 << t)) or all(d & (1 << s) for s in range(8) if s & ~t == 0) for t in universe):
            out.append(frozenset(t for t in universe if d & (1 << t)))
    return out


def modal(fam, support, existential):
    if existential:
        return any(support(s) for s in fam)
    return all(support(s) for s in fam)


def supp_atom(s, mask):
    return s & ~mask == 0


def supp_imp(s, a, b):
    return all(not a(t) or b(t) for t in subsets(s))


def down_support(d):
    return lambda s: signature(s) in d


def main():
    assert LEFT != RIGHT
    assert convex(LEFT) and convex(RIGHT)
    assert all(0 < s < 16 for s in LEFT | RIGHT)
    assert (signature(U), signature(T), signature(V)) == (1, 3, 7)

    ds = downsets()
    assert len(ds) == 19, len(ds)
    tests = 0
    for d in ds:
        fn = down_support(d)
        for existential in (False, True):
            assert modal(LEFT, fn, existential) == modal(RIGHT, fn, existential)
            tests += 1
        # The consequent/antecedent is an arbitrary downward-closed predicate;
        # the two endpoints alone determine the quantification.
        assert modal(LEFT, fn, True) == fn(U)
        assert modal(LEFT, fn, False) == fn(V)

    # Verify support operators, not just their end results.
    for d in ds:
        for e in ds:
            f, g = down_support(d), down_support(e)
            for s in range(16):
                if all((signature(t) in d) <= (signature(t) in e) for t in subsets(s)) != supp_imp(s, f, g):
                    raise AssertionError('implication semantics')
                tests += 1

    not_q = lambda s: supp_imp(s, lambda t: supp_atom(t, Q), lambda t: t == 0)
    not_p = lambda s: supp_imp(s, lambda t: supp_atom(t, P), lambda t: t == 0)
    phi = not_q
    psi = lambda s: not_p(s) and not_q(s)
    # Formulas are ¬q and ¬p∧¬q, both truth conditional here.
    for s in range(16):
        assert phi(s) == (not (s & Q))
        assert psi(s) == (not (s & (P | Q)))
    conditional = lambda fam: all(not phi(s) or psi(s) for s in fam)
    assert conditional(LEFT) is True
    assert conditional(RIGHT) is False
    assert (phi(U), psi(U), phi(T), psi(T), phi(V), psi(V)) == (True, True, True, False, False, False)
    print('VERIFY_OK convexity=2 models; support-types=3; downsets=19; unary_tests=38; implication_tests=5776; conditional=True/False')


if __name__ == '__main__':
    main()
