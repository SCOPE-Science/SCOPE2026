#!/usr/bin/env python3
"""Standalone finite checks of the geometric plateau and occupation formulas.

No finite test is used as a proof of any infinite-time statement.
"""
from fractions import Fraction
from math import isqrt, log

Z = (Fraction(2, 9), Fraction(4, 9), Fraction(8, 9))

def tent(x):
    return 2 * min(x, 1 - x)

def prop_end(q, m):
    return (q**m - 1) // (q - 1)

def sqrt_ends(m):
    t = [0, 1]
    for _ in range(1, m):
        t.append(4 * t[-1] ** 2 + 1)
    return t

def empirical_end(ends, k):
    total = ends[k + 1]
    masses = [0, 0, 0]
    for m in range(k + 1):
        masses[m % 3] += ends[m + 1] - ends[m]
    return tuple(Fraction(v, total) for v in masses)

def polygon_vertex(q, r, p=3):
    mass = []
    for j in range(p):
        d = (r - j) % p
        mass.append(Fraction((q - 1) * q ** (p - 1 - d), q ** p - 1))
    return tuple(mass)

def max_error(v, w):
    return max(abs(a - b) for a, b in zip(v, w))

assert [tent(Z[i]) for i in range(3)] == [Z[(i + 1) % 3] for i in range(3)]
for q in (2, 3, 4, 5):
    K = 7
    ends = [prop_end(q, m) for m in range(K + 1)]
    assert ends[0] == 0 and ends[1] == 1
    M = ends[-1]
    x = [Z[0]]
    for n in range(M - 1):
        x.append(tent(x[n // q]))
    for m in range(K):
        assert all(x[n] == Z[m % 3] for n in range(ends[m], ends[m + 1]))
    ends2 = [prop_end(q, m) for m in range(27)]
    for k in (20, 22, 25):
        v = empirical_end(ends2, k)
        target = polygon_vertex(q, k % 3)
        assert max_error(v, target) < Fraction(1, 100000)

ends = sqrt_ends(6)
M = ends[4]
x = [Z[0]]
for n in range(M - 1):
    x.append(tent(x[isqrt(n) // 2]))
for m in range(4):
    assert all(x[n] == Z[m % 3] for n in range(ends[m], ends[m + 1]))
ends2 = sqrt_ends(9)
for k in range(5, 8):
    v = empirical_end(ends2, k)
    pure = [Fraction(0)] * 3
    pure[k % 3] = Fraction(1)
    assert max_error(v, pure) < Fraction(1, 10000)

# Verify geometric discounted-weight identities and affine independence.
for q in (2, 3, 4, 7):
    for r in range(3):
        v = polygon_vertex(q, r)
        nxt = polygon_vertex(q, (r + 1) % 3)
        point = [Fraction(0)] * 3
        point[(r + 1) % 3] = Fraction(1)
        assert all(nxt[j] == v[j] / q + Fraction(q - 1, q) * point[j] for j in range(3))
        assert sum(v) == 1

# Stage-weight calculation uses continuous antiderivatives only; the proof
# separately bounds discrete harmonic/quasi-harmonic summation errors.
q = 4
logs = [0.0] + [log((q**m-1)/(q-1)) for m in range(1, 110)]
harmonic_stage = [logs[m+1]-logs[m] for m in range(1, 100)]
masses = [0.0] * 3
for m, weight in enumerate(harmonic_stage, start=1):
    masses[m % 3] += weight
norm = sum(masses)
assert max(abs(m / norm - 1 / 3) for m in masses) < 0.011

# log T for T(next)=4*T*T+1, avoiding enormous integers at high level.
logT = [0.0, 0.0, log(5)]
for m in range(2, 180):
    v = logT[-1]
    from math import log1p, exp
    logT.append(2*v + log(4) + log1p(exp(-2*v)/4))
stage_double_log = [(log(logT[m+1])-log(logT[m])) for m in range(2, 160)]
masses = [0.0] * 3
for m, weight in enumerate(stage_double_log, start=2):
    masses[m % 3] += weight
norm = sum(masses)
assert max(abs(v/norm - 1/3) for v in masses) < 0.009

# First 3-cycle: periodic tent orbit 2/9 -> 4/9 -> 8/9 -> 2/9.
assert polygon_vertex(4, 0) == (Fraction(16,21), Fraction(1,21), Fraction(4,21))
assert polygon_vertex(2, 0) == (Fraction(4,7), Fraction(1,7), Fraction(2,7))
print('VERIFY_OK plateau_identity=4_proportional_bases_and_square_root; polygon_vertices=4_bases; time_clock_tests=2')

# Subcritical exponent 1/2: the physical proportional clock has effective
# geometric growth q^(1-gamma).  These are exact integral-stage masses,
# separate from the proof's discrete-sum comparison bounds.
from math import sqrt
b = 4
starts = [prop_end(b, m) for m in range(45)]
weighted = [2 * (sqrt(starts[m+1]) - sqrt(starts[m])) for m in range(1, 42)]
masses = [0.0] * 3
for m, weight in enumerate(weighted, start=1):
    masses[m % 3] += weight
norm = sum(masses)
target = polygon_vertex(2, 41 % 3)
assert max(abs(m/norm-float(target[i])) for i,m in enumerate(masses)) < 0.00001

# Square-root logarithmic sampling w(n)=1/[n sqrt(log n)] also grows by
# asymptotic factor sqrt(2) per plateau.
logT=[0.0,0.0,log(5)]
for m in range(2, 145):
    v=logT[-1]
    from math import log1p,exp
    logT.append(2*v+log(4)+log1p(exp(-2*v)/4))
weighted=[2*(sqrt(logT[m+1])-sqrt(logT[m])) for m in range(2,125)]
masses=[0.0]*3
for m,weight in enumerate(weighted,start=2):
    masses[m%3]+=weight
norm=sum(masses)
target=tuple((sqrt(2)-1)*sqrt(2)**(2-((124%3-j)%3))/(sqrt(2)**3-1) for j in range(3))
assert max(abs(m/norm-target[i]) for i,m in enumerate(masses)) < 0.000001
print('VERIFY_OK fractional_exponents=proportional_and_square_root')
