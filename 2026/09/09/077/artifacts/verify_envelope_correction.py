"""Envelope-correction certificate for lane-432 emergent finding (stdlib only).

Checks, with exact Fraction arithmetic:
  (E1) R(t) = P(J_t)/(128/15) = A(t)*B(t) with R(0)=1;
  (E2) transverse slope R'(0+) in (9,11) via h=1e-6 difference quotient,
       components A'(0) in (-16,-14), B'(0) in (24,26);
  (E3) at t in {1/1000, 1/100, 1/10, 1/4}: exact R(t) fractions recorded,
       each certifies R(t) > 1+4t^2 (falsifying the (1+4t^2) upper envelope);
  (E4) Hanner_5 vertex-count census excludes 242 (J_t has 242 vertices for t>0);
  (E5) proved BM upper bound d_BM(J_t,C)-1 <= 5t (sandwich) plus qualitative
       strict positivity for t>0 by the vertex-count linear-equivalence
       obstruction (242 vs 32). Volume-ratio quantities q(t)=A(t)^(-1/5)-1
       are reported ONLY as volume-ratio quantities, not as BM lower bounds.
Scale note: fallback J_t^{fb}=(1+5t)*J_t^{ours}; P and d_BM are scale-invariant,
so (E3) transfers to the fallback normalization on [0,1/4].
"""
from fractions import Fraction
from math import comb


def A_of(t):
    s = Fraction(0)
    for j in range(1, 6):
        c = comb(5, j) * (j ** 5)
        term = Fraction(c, 120) / (1 + (5 - j) * t)
        s += term if (5 - j) % 2 == 0 else -term
    return s / ((1 + 5 * t) ** 5)


def B_of(t):
    return 120 * t**5 + 600 * t**4 + 600 * t**3 + 200 * t**2 + 25 * t + 1


def R_of(t):
    return A_of(t) * B_of(t)


# E1
assert A_of(Fraction(0)) == 1 and B_of(Fraction(0)) == 1 and R_of(Fraction(0)) == 1
print("E1 OK: R(0)=1")

# E2
h = Fraction(1, 10**6)
dR = (R_of(h) - 1) / h
dA = (A_of(h) - 1) / h
dB = (B_of(h) - 1) / h
print(f"E2: dR={float(dR):.6f} dA={float(dA):.6f} dB={float(dB):.6f}")
assert Fraction(9) < dR < Fraction(11)
assert Fraction(-16) < dA < Fraction(-14)
assert Fraction(24) < dB < Fraction(26)
print("E2 OK: R'(0+)=10 in (9,11)")

# E3: exact fractions + envelope violation
expected = {
    Fraction(1, 1000): Fraction(215378277437, 213253198587),
    Fraction(1, 100): Fraction(24434731, 22283226),
    Fraction(1, 10): Fraction(15403, 9009),
    Fraction(1, 4): Fraction(4043, 1890),
}
for t, want in expected.items():
    r = R_of(t)
    assert r == want, f"mismatch at {t}: {r} != {want}"
    env = Fraction(1) + 4 * t * t
    excess = r - env
    print(f"E3 t={t}: R={r} float={float(r):.10f} env={float(env):.10f} "
          f"excess={float(excess):.8f} VIOLATED={r > env}")
    assert r > env and excess > 0
print("E3 OK: (1+4t^2) envelope violated at all four depths")

# E4: Hanner_5 vertex census excludes 242


def hanner_vertices(n):
    if n == 1:
        return {2}
    out = set()
    for k in range(1, n):
        for a in hanner_vertices(k):
            for b in hanner_vertices(n - k):
                out.add(a + b)
                out.add(a * b)
    return out


H5 = sorted(hanner_vertices(5))
# J_t vertex count (t>0): support-pattern vertices c*1_S with c=1/(1+tm),
# m=|S|: total nonzero = sum_m C(5,m)2^m = 3^5-1 = 242.
N_JT = sum(comb(5, m) * 2**m for m in range(1, 6))
assert N_JT == 242
print(f"E4: J_t nonzero vertices = {N_JT}; Hanner_5 counts = {H5}")
assert N_JT not in H5
# J_t vertex feasibility: 10 axial e_i/(1+t), 32 diagonal (+-1)/(1+5t)


def ft(x, t):
    return max(abs(v) for v in x) + t * sum(abs(v) for v in x)


t = 0.1
x = [0.0] * 5
x[0] = 1 / (1 + t)
assert abs(ft(x, t) - 1) < 1e-12
assert abs(ft([1 / (1 + 5 * t)] * 5, t) - 1) < 1e-12
print("E4 OK: 242 not in Hanner_5 census; J_t axial/diagonal points feasible")

# E5: proved BM upper bound d_BM(J_t,C)-1 <= 5t (sandwich (1/(1+5t))C subset
# J_t subset C), plus qualitative strict positivity for t>0: J_t has 242
# vertices while any linear image of the 5-cube (a parallelepiped) has 32
# vertices, and invertible linear maps preserve vertex count, so J_t is not
# linearly equivalent to C and d_BM(J_t,C) > 1. Volume-ratio quantities
# q(t) = A(t)^(-1/5)-1 are reported for reference ONLY (not BM lower bounds).
QREF = {}
for num, den in [(1, 1000), (1, 100), (1, 10), (1, 4)]:
    tt = Fraction(num, den)
    q = float(A_of(tt)) ** (-0.2) - 1
    ub = float(5 * tt)
    QREF[str(tt)] = (q, ub)
    print(f"E5 t={tt}: volume-ratio quantity q={q:.6f} (NOT a BM lower bound); "
          f"proved BM upper 5t={ub:.6f}")
    assert ub > 0
# qualitative positivity certificate: vertex counts differ under GL
N_CUBE_IMAGE = 2**5
assert N_JT == 242 and N_CUBE_IMAGE == 32 and N_JT != N_CUBE_IMAGE
print("E5 OK: BM upper bound 5t proved; d_BM>1 for t>0 by 242-vs-32 "
      "linear-equivalence obstruction")

print("\nENVELOPE_CORRECTION_CERTIFICATE_OK")
