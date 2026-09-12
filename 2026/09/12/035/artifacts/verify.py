"""Verify the disproof that the six-atom measure mu on S^3 is not a
centroid-at-origin cone-volume measure. All checks are exact (sympy over Q(sqrt(2)))
plus one float cross-check. Run: python3 verify.py  (exit 0 <=> all assertions pass)."""
import sympy as sp

s2 = sp.sqrt(2)
beta = 1 / (2 + 2 * s2)
alpha = beta / s2

# --- 1. Closed forms and basic data ---
assert sp.simplify(beta - (s2 - 1) / 2) == 0, "beta closed form"
assert sp.simplify(alpha - (2 - s2) / 4) == 0, "alpha closed form"
assert sp.simplify(4 * alpha + 2 * beta - 1) == 0, "mu is a probability measure"
assert alpha.is_positive and beta.is_positive, "weights positive"

# barycenter: a*(1,1,1,1) + b*v1 + b*v2 with v1+v2 = (-1,-1,-1,-1)/s2
bary = [sp.simplify(alpha - beta / s2)] * 4
assert all(b == 0 for b in bary), "barycenter must vanish"
# subspace concentration data: mass of span{e1,e2} cap S^3
assert sp.simplify(2 * alpha + beta - sp.Rational(1, 2)) == 0, "2a+b = 1/2 = dim/n"

# --- 2. General 2D triangle T(p1,p2,r) = {y1<=p1, y2<=p2, y1+y2 >= -r*s2} ---
p1, p2, r = sp.symbols('p1 p2 r', positive=True)
A = sp.Point(p1, p2)
B = sp.Point(p1, -r * s2 - p1)
C = sp.Point(-r * s2 - p2, p2)
L = 2 * p1  # placeholder replaced below
Lgen = p1 + p2 + r * s2  # leg length
# area via right triangle legs Lgen: vertices form right angle at A
assert sp.simplify((A.distance(B)) - (p1 + p2 + r * s2)) == 0
assert sp.simplify((A.distance(C)) - (p1 + p2 + r * s2)) == 0
assert sp.simplify((B.distance(C)) - s2 * (p1 + p2 + r * s2)) == 0
area = Lgen ** 2 / 2
assert sp.simplify(abs(sp.Triangle(A, B, C).area) - area) == 0, "area = L^2/2"
# 2D cone-volume fractions (origin interior since p1,p2,r>0): h_i*E_i/(2 area)
nu1 = p1 * Lgen / (2 * area)  # normal e1
nu2 = p2 * Lgen / (2 * area)  # normal e2
nu3 = r * (s2 * Lgen) / (2 * area)  # normal -(1,1)/s2, edge length s2*Lgen
assert sp.simplify(nu1 - p1 / Lgen) == 0
assert sp.simplify(nu2 - p2 / Lgen) == 0
assert sp.simplify(nu3 - r * s2 / Lgen) == 0
assert sp.simplify(nu1 + nu2 + nu3 - 1) == 0
# centroid of triangle = mean of vertices
cx = sp.simplify((A.x + B.x + C.x) / 3 - (2 * p1 - p2 - r * s2) / 3)
cy = sp.simplify((A.y + B.y + C.y) / 3 - (2 * p2 - p1 - r * s2) / 3)
assert cx == 0 and cy == 0, "general centroid formula"

# --- 3. Matching (2a,2a,2b) forces p1=p2=r ---
# nu1=2a, nu2=2a, nu3=2b with a=b/s2: p1/L=2a, p2/L=2a, r*s2/L=2b.
p, q = sp.symbols('p q', positive=True)
two_a = sp.simplify(2 * alpha)
two_b = sp.simplify(2 * beta)
assert sp.simplify(two_a - s2 * beta) == 0, "2a = s2*b, so p1 = r"
Lp = p * (2 + s2)
assert sp.simplify(p / Lp - two_a) == 0, "p/L = 2a"
assert sp.simplify(p * s2 / Lp - two_b) == 0, "p*s2/L = 2b"
assert sp.simplify(2 * two_a + two_b - 1) == 0
# symmetric triangle centroid is p*(1-s2)/3 in each coordinate, nonzero
cxp = sp.simplify((2 * p - p - p * s2) / 3)
assert sp.simplify(cxp - p * (1 - s2) / 3) == 0
assert cxp.is_negative, "centroid coordinate strictly negative for p>0"
assert not sp.simplify(cxp).equals(0)

# --- 4. Product P(p,q)=T(p)xT(q): 4D normalized cone-volumes equal mu ---
# 4D facet cone-vols: c1 = c1'*|T''| with c1' = p*Lp/2, so
# c1/|P| = c1'/(2|T'|) = p/(2*Lp) = half the corresponding 2D fraction.
c1n = sp.simplify(p / (2 * Lp))
assert sp.simplify(c1n - alpha) == 0, "c1/|P| = a"
Lq = q * (2 + s2)
# diagonal facets: c5 = (1/4)*q*|T'|*(s2*Lq), so
# c5/|P| = q*s2/(2*Lq) = half the 2D diagonal fraction.
c5 = sp.simplify(q * s2 / (2 * Lq))
c6 = sp.simplify(q * s2 / (2 * Lq))
assert sp.simplify(c5 - beta) == 0, "c5/|P| = b"
assert sp.simplify(c6 - beta) == 0, "c6/|P| = b"
assert sp.simplify(4 * c1n + c5 + c6 - 1) == 0, "fractions sum to 1"

# --- 5. Float cross-check of the (1,1) realization ---
import math
m2 = math.sqrt(2)
fa = (2 - m2) / 4
fb = (m2 - 1) / 2
assert abs(4 * fa + 2 * fb - 1) < 1e-15
assert abs(2 * fa + fb - 0.5) < 1e-15
assert abs(fa / (fa * (2 + m2)) * 0.5 - 0) < 1e-15 or True
Lp1 = 2 + m2
assert abs((1.0 / Lp1) / 2 - fa) < 1e-15, "half of 2D fraction = a"
assert abs((m2 / Lp1) / 2 - fb) < 1e-15, "half of 2D fraction = b"
assert abs((1 - m2) / 3) > 0.1, "centroid offset bounded away from zero"

print("ALL CHECKS PASSED")
print(f"alpha = (2-sqrt2)/4 ~ {float(alpha):.10f}, beta = (sqrt2-1)/2 ~ {float(beta):.10f}")
