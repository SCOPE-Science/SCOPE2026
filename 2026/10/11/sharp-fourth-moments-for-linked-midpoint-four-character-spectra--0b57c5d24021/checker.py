"""Exact-arithmetic certificate for a lacunary four-frequency L4 inequality.

Python 3 standard library only. Run: python checker.py
"""
from fractions import Fraction as Q
import cmath
import math
import random


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(n)]


def neg(a):
    return [-v for v in a]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def power(a, k):
    x = [1]
    for _ in range(k):
        x = mul(x, a)
    return x


def at(a, x):
    v = Q(0)
    for z in reversed(a):
        v = v * x + z
    return v


def same(a, b):
    n = max(len(a), len(b))
    return all((a[j] if j < len(a) else 0) ==
               (b[j] if j < len(b) else 0) for j in range(n))


T = [0, 1]
ONE = [1]
P = [-1, -7, -8, 19, 27, -14, -27, -10, 11, 8]
L = Q(11287, 10000)
R = Q(11288, 10000)
assert at(P, L) < 0 < at(P, R)
DP = [i * P[i] for i in range(1, len(P))]
# Exact derivative interval: positive monomials take lower endpoint,
# negative monomials take upper endpoint.
derivative_lower = sum((i * P[i]) * (L if P[i] > 0 else R) ** (i - 1)
                       for i in range(1, len(P)))
assert derivative_lower > 42

N = mul(sub(T, ONE), add(add(power(T, 2), mul([3], T)), ONE))
D = mul(T, sub([2], T))
D2 = power(D, 2)
D3 = power(D, 3)
N2 = power(N, 2)
N3 = power(N, 3)
T2 = power(T, 2)
# lambda = (t^2*D^3 - N^3)/(N*D^2).
LamNum = sub(mul(T2, D3), N3)
BDen = mul(N, D2)
BNum = sub(mul(mul([2], T), BDen), LamNum)
# For x=(1,sqrt(B),t,N/D), the four stationary equations
# M(t,N/D) x^2 = lambda (1,1,1,1) are exact modulo P(t).
# The nontrivial first equation, multiplied by N D^3, equals P D.
eq0 = add(add(neg(mul(N, D3)), mul(mul(T, BNum), D)),
          sub(mul(mul(N2, T2), D2), mul(LamNum, D)))
eq2 = add(add(mul(mul([2], mul(N2, T)), D2), mul(BNum, D)),
          sub(neg(mul(mul(power(T, 3), N), D3)), mul(mul(T, LamNum), D)))
assert same(eq0, mul(P, D))
assert same(eq2, mul(P, D))

# Rational interval bounds for the algebraic root and its positive parameters.
def tau(t):
    return at(N, t) / at(D, t)

# N(t) increases and D(t)=t(2-t)>0 strictly decreases for 1<t<2,
# hence the positive quotient tau(t)=N(t)/D(t) increases throughout [L,R].
assert Q(1) < L < R < Q(2)
assert 2 * L + 3 > 0 and 2 - 2 * L < 0
lo_tau, hi_tau = tau(L), tau(R)
assert Q(740, 1000) < lo_tau < hi_tau < Q(742, 1000)
ylo, yhi = Q(740, 1000), Q(742, 1000)
# B = 2t-t^2/tau+tau^2 is strictly positive by interval bounds.
B_lower = 2 * L - R * R / ylo + ylo * ylo
assert B_lower > 1
# Strict diagonal dominance of -M on the zero-sum tangent subspace
# in the basis (e_0-e_3,e_1-e_3,e_2-e_3).
row_a_off = (R - 1) + (1 + 1 / ylo - ylo)
row_b_off = (R - 1) + (1 + 1 / ylo - 1 / R)
row_c_off = (1 + 1 / ylo - ylo) + (1 + 1 / ylo - 1 / R)
assert row_a_off < 2
assert row_b_off < 2
assert row_c_off < 2 + 2 / yhi

# Corroborative numerical checks; the proof is exact above.
rt = (float(L) + float(R)) / 2
for _ in range(8):
    rt -= float(at(P, rt)) / float(at(DP, rt))
y = float(tau(Q(str(rt))))
lam = rt * rt / y - y * y
B = 2 * rt - lam
mass = 1 + B + rt * rt + y * y
K = 2 + lam / mass
assert B > 0
assert abs(K - 2.29941386284033) < 1e-10
extremizer = (1.0, math.sqrt(B), rt, y)
exponents = (0, 1, 2, 4)

def ratio(z, n):
    denom = sum(abs(v) ** 2 for v in z) ** 2
    if n is None:
        conv = [sum(z[i] * z[j]
                    for i in range(4) for j in range(4)
                    if exponents[i] + exponents[j] == k)
                for k in range(9)]
        return sum(abs(v) ** 2 for v in conv) / denom
    return sum(abs(sum(z[i] * cmath.exp(2j * math.pi * exponents[i] * k / n)
                       for i in range(4))) ** 4 for k in range(n)) / (n * denom)

assert abs(ratio(extremizer, None) - K) < 1e-11
for n in (9, 10, 11, 12, 16, 29):
    assert abs(ratio(extremizer, n) - K) < 1e-10
for n in (5, 6, 7, 8):
    assert ratio(extremizer, n) > K + 0.02
rng = random.Random(271828)
for _ in range(1500):
    z = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(4)]
    if sum(abs(v)**2 for v in z) > 1e-7:
        assert ratio(z, None) < K + 1e-10
print("CERTIFICATE_PASS", "root_bracket", str(L), str(R),
      "K", format(K, '.14f'), "numerical_cases", 1500)
