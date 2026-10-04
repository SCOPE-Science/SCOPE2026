#!/usr/bin/env python3
from itertools import product

def f(localN, Bs, A):
    return any((D & ~A) == 0 and all(D & B for B in Bs) for D in localN)

# Exhaustive reconstruction over every possible local neighbourhood family
# for carriers of size at most four.
for n in range(1, 5):
    teams = list(range(1 << n))
    for fam_mask in range(1 << len(teams)):
        localN = {D for D in teams if (fam_mask >> D) & 1}
        for D in teams:
            if D == 0:
                recovered = f(localN, (), 0)
            else:
                elems = [i for i in range(n) if (D >> i) & 1]
                Bs = tuple(1 << i for i in elems)
                recovered = f(localN, Bs, D)
            assert recovered == (D in localN), (n, fam_mask, D)

# Exhaustively check equality below the sharp cutoff.
for n in range(1, 5):
    full = (1 << n) - 1
    minus = set(range(1 << n)) - {full}
    plus = set(range(1 << n))

    for k in range(n):
        choices = list(range(1 << n))
        for A in choices:
            for Bs in product(choices, repeat=k):
                assert f(minus, Bs, A) == f(plus, Bs, A), (n, k, A, Bs)

    singleton_Bs = tuple(1 << i for i in range(n))
    assert not f(minus, singleton_Bs, full)
    assert f(plus, singleton_Bs, full)

print("VERIFY_OK")
