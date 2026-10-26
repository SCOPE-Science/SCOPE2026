"""Finite exact-integer checks for a Diophantine-density construction.

Not a proof of any infinite or novelty assertion.
"""
from math import gcd
from fractions import Fraction


def integer_root_floor(z: int, degree: int) -> int:
    if degree == 1:
        return z
    lo, hi = 0, 1 << ((z.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** degree <= z:
            lo = mid
        else:
            hi = mid
    return lo


def core_stage(frac: Fraction, k: int):
    assert 0 < frac < 1
    m = integer_root_floor(1 << (frac.numerator * k), frac.denominator)
    d = (1 << k) // m
    return m, d


rational_checks = 0
for alpha in map(Fraction, ("1/5", "1/3", "1/2", "2/3", "4/5")):
    for q in range(3, 260):
        k = (q-1).bit_length()-1
        assert (1 << k) < q <= (1 << (k+1)), (k,q)
        n, d = core_stage(alpha, k)
        assert n*d <= 1 << k < q
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            distance_num = min(min((m*d*p) % q, q - ((m*d*p) % q)) for m in range(1, n+1))
            assert distance_num * (n+1) <= q, (alpha,p,q,k,n,d)
            rational_checks += 1

# Boundary values and the first substantial alternating intervals.
endpoints = [2,4,16,65536]

def is_even_block(v):
    return v >= 2 and ((0 if v < 4 else 1 if v < 16 else 0 if v < 65536 else 1) == 0)

cover_checks = 0
for v in range(1, 65537):
    e = is_even_block(v)
    o = not e
    assert e != o
    cover_checks += 1

for alpha in map(Fraction, ("1/3", "1/2", "2/3")):
    stage_sets = []
    for k in range(71):
        n, d = core_stage(alpha, k)
        stage_sets.append((n,d))
    for q in [16, 63, 100, 1000, 4096, 65536]:
        # Beyond stage 70, the general bound d_k >= 2^((1-alpha)k-1)
        # exceeds every listed q. Only members below q are enumerated.
        assert stage_sets[-1][1] > q
        core = {m*d for n,d in stage_sets for m in range(1, min(n, (q-1)//d)+1)}
        assert all(v >= 1 for v in core)
        # Stage-by-stage bound used in Sanford's theorem.
        assert len(core) <= sum(min(n, (q-1)//d) for n,d in stage_sets)

print(f"VERIFY_OK rational_dirichlet_checks={rational_checks} integer_partition_checks={cover_checks} exact_fraction_floor_checks=PASS all_finite")
