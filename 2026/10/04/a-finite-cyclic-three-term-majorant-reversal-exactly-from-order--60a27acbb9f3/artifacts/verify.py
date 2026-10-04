#!/usr/bin/env python3
"""Directed-interval checks for the finite-cyclic three-term majorant theorem."""
import mpmath as mp
from mpmath import iv

if mp.__version__ != "1.3.0":
    raise RuntimeError(f"expected mpmath 1.3.0, found {mp.__version__}")
mp.mp.dps = 80
iv.dps = 50


def delta_interval(L):
    s = iv.mpf([0, 0])
    twopi = 2 * iv.pi
    for j in range(L):
        t = twopi * j / L
        c1 = iv.cos(t)
        c2 = iv.cos(2 * t)
        c3 = iv.cos(3 * t)
        gp = 3 + 2*c1 + 2*c2 + 2*c3
        gm = 3 + 2*c1 - 2*c2 - 2*c3
        # For this pair both squared magnitudes stay positive on the circle.
        hp = gp * iv.sqrt(gp)
        hm = gm * iv.sqrt(gm)
        s += hm - hp
    return s / L


def lo(x):
    return mp.mpf(x._mpi_[0])


def hi(x):
    return mp.mpf(x._mpi_[1])

# Exact low-order formulas, compared numerically only as a replay check.
exact_low = {
    1: -26,
    2: -13,
    3: -8 - 2*mp.sqrt(3),
    4: (5*mp.sqrt(5) - 14)/2,
}
for L, target in exact_low.items():
    v = delta_interval(L)
    assert lo(v) < 0 and hi(v) < 0
    assert lo(v) - mp.mpf('1e-40') <= target <= hi(v) + mp.mpf('1e-40')

M = 10000
vM = delta_interval(M)
expected_lo = mp.mpf('0.115540979579483608345382687211526474116269209806')
expected_hi = mp.mpf('0.115540979579483608345382687211526474116269209820')
assert lo(vM) > expected_lo - mp.mpf('1e-48')
assert hi(vM) < expected_hi + mp.mpf('1e-48')

C = 372 * iv.pi**2
I_lower = lo(vM) - hi(C) / (M*M)
assert I_lower > mp.mpf('0.1155042646511115')

min_lower = None
min_L = None
for L in range(5, 200):
    v = delta_interval(L)
    lower = lo(v)
    assert lower > 0
    if min_lower is None or lower < min_lower:
        min_lower = lower
        min_L = L
assert min_L == 10
assert min_lower > mp.mpf('0.1055728090000841')

tail_lower = I_lower - hi(C)/(200*200)
assert tail_lower > mp.mpf('0.0237169437209805')
assert min(min_lower, tail_lower) > mp.mpf('0.0237')

print(f"delta_10000=[{lo(vM)}, {hi(vM)}]")
print(f"I_lower={I_lower}")
print(f"finite_min_L={min_L} finite_min_lower={min_lower}")
print(f"tail_lower_from_L_200={tail_lower}")
print("VERIFY_OK")
