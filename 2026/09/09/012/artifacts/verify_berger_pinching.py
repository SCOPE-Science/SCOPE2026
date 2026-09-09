"""Stdlib-only verifier for the Berger/pinching/systolic theorem (lane-284).

Replays with exact rational arithmetic (fractions.Fraction):
 1. Cartan/Milnor connection computation vs closed-form coordinate sectionals
    at several rational triples (exact equality).
 2. Geodesic-circle fact: Gamma_{ii,k} = 0 (principal circles are geodesics).
 3. Berger branch identities K12 = 4-3s, K23 = K31 = s (s = tau^2), exact.
 4. Sharp thresholds by exact integer arithmetic on s: s=4/3 (K=0),
    s=4/7 and s=16/13 (pinching ratio exactly 4).
 5. Certified triaxial positivity box [0.92,1.08]^2 (exact Fraction margins).
 6. Non-positivity witnesses: tau=2 -> K12=-8; (1/4,1/4,1) -> K12=-704.
 7. Systolic chain: min^3 <= abc and the sharp constant derivation.
"""
from fractions import Fraction as F

def conn_curv(a, b, c):
    c1 = 2 * a / (b * c)
    c2 = 2 * b / (c * a)
    c3 = 2 * c / (a * b)

    def br(i, j):
        if i == j:
            return {}
        s = 1
        if (i, j) in [(2, 1), (3, 2), (1, 3)]:
            s = -1
        if set([i, j]) == {1, 2}:
            return {3: s * c3}
        if set([i, j]) == {2, 3}:
            return {1: s * c1}
        return {2: s * c2}

    G = {}
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                G[(i, j, k)] = (br(i, j).get(k, 0) - br(j, k).get(i, 0)
                                + br(k, i).get(j, 0)) / F(2)

    def R(i, j, k, l):
        t1 = sum(G[(j, k, m)] * G[(i, m, l)] for m in (1, 2, 3))
        t2 = sum(G[(i, k, m)] * G[(j, m, l)] for m in (1, 2, 3))
        t3 = sum(br(i, j).get(m, 0) * G[(m, k, l)] for m in (1, 2, 3))
        return t1 - t2 - t3
    return G, R

def closed_form(a, b, c):
    u, v, w = a * a, b * b, c * c
    d = u * v * w
    K12 = ((u - v) ** 2 + 2 * w * (u + v) - 3 * w * w) / d
    K23 = ((v - w) ** 2 + 2 * u * (v + w) - 3 * u * u) / d
    K31 = ((w - u) ** 2 + 2 * v * (w + u) - 3 * v * v) / d
    return K12, K23, K31

# 1+2. Cartan vs closed form (exact) + geodesic-circle fact.
triples = [(F(1), F(1), F(1, 2)), (F(1), F(1), F(1)),
           (F(2), F(1), F(3)), (F(7, 10), F(7, 5), F(1)),
           (F(1, 4), F(1, 4), F(1)), (F(23, 20), F(27, 25), F(1))]
for (a, b, c) in triples:
    G, R = conn_curv(a, b, c)
    K12k, K23k, K31k = R(1, 2, 2, 1), R(2, 3, 3, 2), R(3, 1, 1, 3)
    K12, K23, K31 = closed_form(a, b, c)
    assert (K12k, K23k, K31k) == (K12, K23, K31), (a, b, c)
    for i in (1, 2, 3):
        for k in (1, 2, 3):
            assert G[(i, i, k)] == 0, (a, b, c, i, k)
print("CARTAN_VS_CLOSED_FORM_EXACT_OK", len(triples), "triples")
print("PRINCIPAL_CIRCLES_GEODESIC_OK (Gamma_ii,k = 0)")

# 3. Berger identities at rational tau (exact).
for t in [F(1, 4), F(1, 2), F(3, 4), F(1), F(6, 5), F(3, 2), F(2)]:
    K12, K23, K31 = closed_form(F(1), F(1), t)
    s = t * t
    assert K12 == 4 - 3 * s and K23 == s and K31 == s, t
print("BERGER_IDENTITIES_EXACT_OK")

# 4. Sharp thresholds (exact arithmetic on s = tau^2).
assert 4 - 3 * F(4, 3) == 0                                   # K=0 at s=4/3
assert (F(4) - 3 * F(4, 7)) / F(4, 7) == 4                    # ratio 4 at s=4/7
assert F(16, 13) / (F(4) - 3 * F(16, 13)) == 4                # ratio 4 at s=16/13
assert F(4) - 3 * F(16, 13) == F(4, 13) and F(4) - 3 * F(4, 7) == F(16, 7)
# interior/exterior rational samples (evidence for the window (4/7, 16/13))
for s in [F(3, 5), F(4, 5), F(1), F(8, 7), F(6, 5)]:
    Klo, Khi = (s, 4 - 3 * s) if s <= 1 else (4 - 3 * s, s)
    assert Khi / Klo < 4, s
for s in [F(1, 2), F(13, 10), F(5, 4)]:
    if 4 - 3 * s > 0:
        Klo, Khi = (s, 4 - 3 * s) if s <= 1 else (4 - 3 * s, s)
        assert Khi / Klo > 4, s
print("THRESHOLDS_SHARP_OK s*=4/3; pinch endpoints s=4/7, 16/13 ratio=4")

# 5. Certified triaxial boxes with c=1 (exact Fractions).
# 5a. Positivity box [0.92,1.08]^2 (numerator certificates).
lo, hi = F(92, 100), F(108, 100)
ulo, uhi = lo * lo, hi * hi          # u,v range
n12 = 2 * (ulo + ulo) - 3            # (u-v)^2 >= 0 dropped
assert n12 == F(241, 625) and n12 > 0, n12          # 0.3856
inner = 2 * ulo + 2 - 3 * uhi        # 2v+2-3u lower bound
assert inner == F(121, 625) and inner > 0, inner    # 0.1936
n23 = ulo * inner
assert n23 == F(64009, 390625) and n23 > F(16, 100), n23  # ~0.1639
print("BOX_CERT_OK [0.92,1.08]^2 N12>=%s N23,N31>=%s" % (n12, n23))

# 5b. Pinching box [0.98,1.02]^2 via direct numerator/denominator bounds (c=1).
# K12 = ((u-v)^2+2(u+v)-3)/(uv): lower bound drops (u-v)^2 >= 0 and takes
# uv <= puhi^2; upper bound uses |u-v| <= puhi-pulo and uv >= pulo^2.
# K23 = (v-1)^2/(uv) + (2v+2-3u)/u: lower bound drops the square (>= 0);
# upper bound adds max(v-1)^2/(pulo^2). (K31 is symmetric in u,v, same bounds.)
plo, phi = F(49, 50), F(51, 50)
pulo, puhi = plo * plo, phi * phi
assert (pulo, puhi) == (F(2401, 2500), F(2601, 2500))
K12lo = (4 * pulo - 3) / (puhi * puhi)
K12hi = (4 * puhi - 3 + (puhi - pulo) ** 2) / (pulo * pulo)
assert (K12lo, K12hi) == (F(5260000, 6765201), F(7300000, 5764801))
mlo = 2 * pulo + 2 - 3 * puhi
mhi = 2 * puhi + 2 - 3 * pulo
assert (mlo, mhi) == (F(1999, 2500), F(2999, 2500))
dmax = max(puhi - 1, 1 - pulo)          # max|v-1| over the box
assert dmax == F(101, 2500)
K23lo = mlo / puhi
K23hi = mhi / pulo + dmax * dmax / (pulo * pulo)
assert (K23lo, K23hi) == (F(1999, 2601), F(7210800, 5764801))
Kmin, Kmax = min(K12lo, K23lo), max(K12hi, K23hi)
assert Kmin == F(1999, 2601) and Kmax == F(7300000, 5764801)
assert Kmin > 0 and Kmax / Kmin < 2, (Kmin, Kmax)
print("PINCH_BOX_OK [0.98,1.02]^2 K in [%s,%s] ratio<%s<2"
      % (Kmin, Kmax, Kmax / Kmin))

# 6. Witnesses.
assert closed_form(F(1), F(1), F(2))[0] == -8
assert closed_form(F(1, 4), F(1, 4), F(1))[0] == -704
print("WITNESSES_OK tau=2:K12=-8; (1/4,1/4,1):K12=-704")

# 7. Systolic algebra: min^3 <= abc; constant 4*pi^2*min^2/(2*pi^2*abc)^{2/3}
#    <= 2^{4/3} pi^{2/3} with equality iff a=b=c (exact combinatorial part).
import math
for (a, b, c) in [(F(1), F(1), F(1)), (F(1, 2), F(1), F(3, 2)),
                  (F(23, 25), F(27, 25), F(1)), (F(2), F(2), F(1))]:
    assert min(a, b, c) ** 3 <= a * b * c
    assert (min(a, b, c) ** 3 == a * b * c) == (a == b == c)
C = 2 ** (F(4, 3)) * math.pi ** (F(2, 3))
assert abs(float(C) - 4 * math.pi**2 / (2 * math.pi**2) ** (2/3)) < 1e-12
print("SYSTOLIC_ALGEBRA_OK C=2^{4/3} pi^{2/3} ~ %.10f" % float(C))
print("ALL_OK")
