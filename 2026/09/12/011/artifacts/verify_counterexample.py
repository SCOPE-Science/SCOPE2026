#!/usr/bin/env python3
"""Rigorous counterexample to the 8% binomial-vs-Gaussian Fourier envelope.

TARGET: phi_B, phi_G = char. functions of Kyber eta=2 centered binomial and
variance-matched rounded Gaussian mod q=3329; claim |phi_B/phi_G - 1| <= 0.08
uniformly over scaled dual frequencies in [0, T768].

DISPROOF WITNESS: t = 768. True values (float, non-rigorous cross-check):
  phi_B(768) = cos^4(768*pi/3329) ~ 0.31414
  phi_G(768) ~ 0.34919  (rounded Gaussian, variance matched Var = 1)
  ratio - 1 ~ -0.1004, violating the 8% envelope.

RIGOROUS STRATEGY (all exact Fraction arithmetic + analytic remainders):
  s1 = 0.955, s2 = 0.96 (Fractions 191/200, 24/25).
  1. V(s1) < 1 < V(s2)  => any variance-matched s* lies in (s1, s2),
     using monotonicity of V (layer-cake + normal-tail monotonicity, proved
     analytically in DRAFT.md; the code certifies the endpoint inequalities).
  2. B^U: rigorous upper bound on phi_B(768) = cos^4(768*pi/3329).
  3. G^L: rigorous lower bound on phi_{G,s}(768) uniform over s in [s1,s2].
  4. Exact check 100*B^U < 92*G^L  =>  phi_B/phi_G < 0.92  =>  |ratio-1| > 0.08.

Primitives proved from scratch: pi via Machin + Leibniz, sqrt via verified
rational squaring, exp lower bounds via positive Taylor sums, normal CDF via
integrated Taylor series with Leibniz remainder, cos via Taylor + Lipschitz,
Gaussian tails via Mills ratio. No floats in the verified path (floats are
used ONLY for initial guesses that are then verified, and in the labeled
cross-check section at the end).
"""
from fractions import Fraction
import math

# ---------------------------------------------------------------- pi bounds
def arctan_leibniz(z, N):
    """Two-sided bound on arctan(z), 0 < z <= 1, via N-term Leibniz sum."""
    t = z  # t_0
    S = Fraction(0)
    terms = []
    for n in range(N + 2):
        if n > 0:
            # t_n = (-1)^n z^{2n+1}/(2n+1); recurrence from t_{n-1}
            t = terms[-1] * (-z * z) * (2 * n - 1) / (2 * n + 1)
        terms.append(t)
        if n <= N:
            S += t
    # exact decreasing check on magnitudes
    for n in range(N + 1):
        assert abs(terms[n + 1]) < abs(terms[n]), "Leibniz decrease fails"
    rem = abs(terms[N + 1])
    if N % 2 == 0:
        return S - rem, S
    else:
        return S, S + rem

A_lo, A_hi = arctan_leibniz(Fraction(1, 5), 12)
B_lo, B_hi = arctan_leibniz(Fraction(1, 239), 4)
PI_LO = 16 * A_lo - 4 * B_hi
PI_HI = 16 * A_hi - 4 * B_lo
assert PI_LO < PI_HI
assert Fraction(31415926535, 10**10) < PI_LO and PI_HI < Fraction(31415926536, 10**10)

# ---------------------------------------------------------------- sqrt bounds
def sqrt_hi(X):
    c = Fraction(math.sqrt(float(X))) + Fraction(1, 10**12) * (1 + abs(Fraction(math.sqrt(float(X)))))
    while c * c < X:
        c += Fraction(1, 10**12)
    return c

def sqrt_lo(X):
    c = Fraction(math.sqrt(float(X))) - Fraction(1, 10**12) * (1 + abs(Fraction(math.sqrt(float(X)))))
    while c * c > X:
        c -= Fraction(1, 10**12)
    assert c > 0
    return c

C_LO = 1 / sqrt_hi(2 * PI_HI)   # 1/sqrt(2*pi) lower
C_HI = 1 / sqrt_lo(2 * PI_LO)   # 1/sqrt(2*pi) upper
assert C_LO < C_HI and C_LO > Fraction(39, 100) and C_HI < Fraction(41, 100)

# ---------------------------------------------------------------- normal CDF
_phi_cache = {}

def T_series(x):
    """Bound T(x)=sum (-1)^n x^{2n+1}/(2^n n! (2n+1)) for x>=0 (Fraction)."""
    assert x >= 0
    if x == 0:
        return Fraction(0), Fraction(0)
    tol = Fraction(1, 10**12)
    t = x
    S = t
    n = 0
    while True:
        # ratio r_n for step n -> n+1: x^2 (2n+1)/((2n+2)(2n+3))
        r = x * x * (2 * n + 1) / ((2 * n + 2) * (2 * n + 3))
        t = -t * x * x * (2 * n + 1) / ((2 * n + 2) * (2 * n + 3))
        n += 1
        S += t
        # g(k)=(2k+1)/((2k+2)(2k+3)) is decreasing (proved in DRAFT), so once
        # r<1 all later ratios are <1 and Leibniz applies from here.
        if r < 1 and abs(t) <= tol:
            # confirm next ratio also < 1 (monotone decrease => all future <1)
            r2 = x * x * (2 * n + 1) / ((2 * n + 2) * (2 * n + 3))
            assert r2 < 1 and r2 < r
            return S - abs(t), S + abs(t)
        assert n < 2000, "series did not converge"

def Phi(x):
    """Two-sided bound on standard normal CDF at Fraction x."""
    if x in _phi_cache:
        return _phi_cache[x]
    if x == 0:
        r = (Fraction(1, 2), Fraction(1, 2))
    elif x > 0:
        T_lo, T_hi = T_series(x)
        r = (Fraction(1, 2) + C_LO * T_lo, Fraction(1, 2) + C_HI * T_hi)
    else:
        lo, hi = Phi(-x)
        r = (1 - hi, 1 - lo)
    assert r[0] <= r[1]
    _phi_cache[x] = r
    return r

# ---------------------------------------------------------------- cos bounds
def cos_interval(r):
    """Two-sided bound on cos(r*pi) for Fraction r >= 0."""
    assert r >= 0
    m = int(math.floor(float(r) / 2 + 0.5))
    d = r - 2 * m
    assert abs(d) <= 1
    if d >= 0:
        z_lo, z_hi = d * PI_LO, d * PI_HI
    else:
        z_lo, z_hi = d * PI_HI, d * PI_LO
    zc = (z_lo + z_hi) / 2
    delta = (z_hi - z_lo) / 2
    zmax = abs(zc) + delta
    tol = Fraction(1, 10**12)
    u = Fraction(1)
    S = u
    N = 0
    while True:
        u = -u * zc * zc / ((2 * N + 1) * (2 * N + 2))
        N += 1
        S += u
        # remainder of alternating cos series at zmax
        if zmax * zmax / ((2 * N + 1) * (2 * N + 2)) < 1:
            p, q = zmax.numerator, zmax.denominator
            pw = 2 * N + 2
            eps = Fraction(p**pw, q**pw) / math.factorial(pw)
            if eps <= tol:
                return S - eps - delta, S + eps + delta
        assert N < 2000

# ---------------------------------------------------------------- exp lower
def exp_lo(v):
    """Lower bound on exp(v) for Fraction v>0 via positive Taylor sum."""
    assert v > 0
    S = Fraction(0)
    t = Fraction(1)
    for n in range(60):
        S += t
        t = t * v / (n + 1)
    return S

def phi_dens_hi(y):
    """Upper bound on standard normal density at Fraction y."""
    assert y > 0
    return C_HI / exp_lo(y * y / 2)

def mill_hi(y):
    """Upper bound on 1-Phi(y), y>0, via Mills ratio phi(y)/y."""
    assert y > 0
    lo, _ = Phi(y)
    direct = 1 - lo
    mills = phi_dens_hi(y) / y
    return min(direct, mills)

# ---------------------------------------------------------------- model setup
Q = 3329
T = 768
S1 = Fraction(191, 200)   # 0.955
S2 = Fraction(24, 25)     # 0.96
K = 6

def quot_interval(a, s_lo, s_hi):
    """[min, max] of a/s over s in [s_lo, s_hi], a Fraction."""
    v1 = a / s_lo
    v2 = a / s_hi
    return (min(v1, v2), max(v1, v2))

def mass_bounds(k, s_lo, s_hi):
    """Two-sided bound on P(round(Z_s)=k) uniform over s in [s_lo,s_hi]."""
    u2_lo, u2_hi = quot_interval(Fraction(k) + Fraction(1, 2), s_lo, s_hi)
    u1_lo, u1_hi = quot_interval(Fraction(k) - Fraction(1, 2), s_lo, s_hi)
    F2_lo, F2_hi = Phi(u2_lo)[0], Phi(u2_hi)[1]
    F1_lo, F1_hi = Phi(u1_lo)[0], Phi(u1_hi)[1]
    return F2_lo - F1_hi, F2_hi - F1_lo

def tail_prob_hi(s):
    """Upper bound on P(|R_s| > K) via Mills ratio at edge (K+.5)/s."""
    y = (Fraction(K) + Fraction(1, 2)) / s
    return 2 * mill_hi(y)

def tail_var_hi(s):
    """Upper bound on E[R_s^2 1_{|R_s|>K}]."""
    c = Fraction(K) + Fraction(1, 2)
    y = c / s
    EZ2 = 2 * (s * s * mill_hi(y) + s * c * phi_dens_hi(y))
    P = 2 * mill_hi(y)
    return EZ2 * (1 + Fraction(1, 1) / c) + P / 4

# ---- (1) variance bracket
V1_hi = sum(Fraction(k * k) * mass_bounds(k, S1, S1)[1] for k in range(-K, K + 1)) + tail_var_hi(S1)
V2_lo = sum(Fraction(k * k) * mass_bounds(k, S2, S2)[0] for k in range(-K, K + 1))
print("V(0.955) upper =", float(V1_hi))
print("V(0.960) lower =", float(V2_lo))
assert V1_hi < 1, "need V(s1)<1"
assert V2_lo > 1, "need V(s2)>1"

# ---- (2) binomial side upper bound
X_LO = Fraction(T) * PI_LO / Q
X_HI = Fraction(T) * PI_HI / Q
assert 0 < X_LO < X_HI < 1
# cos decreasing on [0,1]: cos(x) <= cos(X_LO); Leibniz even-sum upper bound
u = Fraction(1)
S = u
xc = X_LO
for n in range(1, 11):
    u = -u * xc * xc / ((2 * n - 1) * (2 * n))
    S += u
# S is S_10 (even) => upper bound up to next-term remainder; add it
rem10 = abs(u * xc * xc / (21 * 22))
cos_hi = S + rem10
assert cos_hi > 0
B_U = cos_hi ** 4
print("phi_B(768) upper =", float(B_U))

# ---- (3) Gaussian side uniform lower bound
G_L = Fraction(0)
for k in range(-K, K + 1):
    p_lo, p_hi = mass_bounds(k, S1, S2)
    c_lo, c_hi = cos_interval(Fraction(1536 * abs(k), Q))
    corners = (p_lo * c_lo, p_lo * c_hi, p_hi * c_lo, p_hi * c_hi)
    G_L += min(corners)
G_L -= tail_prob_hi(S2)
print("phi_G(768) uniform lower =", float(G_L))
assert G_L > 0

# ---- (4) envelope violation
print("100*B^U =", float(100 * B_U), "  92*G^L =", float(92 * G_L))
assert 100 * B_U < 92 * G_L, "envelope not violated"
print("CERTIFIED: phi_B/phi_G <", float(B_U / G_L), "<= 0.92 at t=768")
print("=> |phi_B/phi_G - 1| >", 1 - float(B_U / G_L), "> 0.08. TARGET REFUTED.")

# ------------------------------------------------- non-rigorous cross-check
print("\n--- float cross-check (not part of proof) ---")
import math as _m
s_star = 0.9574271350290928
def _Phi(x):
    return 0.5 * (1 + _m.erf(x / _m.sqrt(2)))
ps = [(_Phi((k + .5) / s_star) - _Phi((k - .5) / s_star)) for k in range(-40, 41)]
print("var:", sum(k * k * p for k, p in zip(range(-40, 41), ps)))
b = _m.cos(_m.pi * 768 / 3329) ** 4
g = sum(p * _m.cos(2 * _m.pi * 768 * k / 3329) for k, p in zip(range(-40, 41), ps))
print("phi_B:", b, "phi_G:", g, "ratio-1:", b / g - 1)
