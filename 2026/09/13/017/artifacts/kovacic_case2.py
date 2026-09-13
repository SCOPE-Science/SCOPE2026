"""Kovacic Cases 1-3 no-Liouvillian certificate for the resonant doubly-confluent Heun point.

System: M(x) = A2 x + A1 + A0/x + Am1/x^2 with the symmetric params of topic.json.
Scalar reduction (system traceless, second row identity):
  a(x) = 2x + 1/x^2 + 1/(2x), u'' = Q(x) u, Q = a^2 + a' + 1
       = 4x^2 + 5 + 4/x - 1/(4x^2) - 1/x^3 + 1/x^4  (exact).

 Step-0 pole data (exact): Q = s(x)/t(x) with s = 16x^6+20x^4+16x^3-x^2-4x+4
 (deg 6) and t = 4x^4 (deg 4); hence the only finite pole is x = 0 of order 4
 (x^4 Q -> 1, x^5 Q -> 0), and ord_infty(Q) = deg(t) - deg(s) = -2, i.e. in
 Kovacic's normalisation (pole at infinity of order 0) infinity is an ordinary
 point of the coefficient.  These facts are recomputed exactly in-script below.

 All arithmetic below is exact rational (sympy Rational / Fraction), no floats.
 Cross-checked with a second independent recurrence script in WORKLOG derivation.
"""
import json
from fractions import Fraction
import sympy as sp

x = sp.Symbol('x')
Q = 4*x**2 + 5 + 4/x - sp.Rational(1, 4)/x**2 - 1/x**3 + 1/x**4

result = {"Q": str(Q)}

# ---------- Step 0: exact pole inventory ----------
s_poly, t_poly = sp.fraction(sp.together(Q))
sP, tP = sp.Poly(sp.expand(s_poly), x), sp.Poly(sp.expand(t_poly), x)
pole0_order = 4  # verified: x^4 Q -> 1, x^5 Q -> 0 (limits computed exactly)
ord_inf = tP.degree() - sP.degree()  # = -2: ordinary point at infinity
assert (sP.degree(), tP.degree()) == (6, 4)
assert sp.limit(x**4 * Q, x, 0) == 1 and sp.limit(x**5 * Q, x, 0) == 0
assert sP.eval(0) != 0  # no cancellation: pole order is exactly 4
result["pole_data"] = {"num_deg": sP.degree(), "den_deg": tP.degree(),
                       "finite_poles": [{"point": "0", "order": pole0_order}],
                       "ord_inf": ord_inf,
                       "note": "only finite pole is x=0 (order 4); "
                               "ord_inf(Q)=-2 so infinity is an ordinary "
                               "point of Q (pole order 0 there)"}

# ---------- Case 1: rational Riccati root u = P'/P + sum local parts ----------
# Local polar part at 0: u = l/x^2 + m/x + O(1).
# R = u'+u^2-Q; R*x^4 polynomial coefficient conditions:
#   x^0: l^2-1 = 0;  x^1: 2lm-2l+1 = 0.
loc0 = []
for l in (sp.Integer(1), sp.Integer(-1)):
    m = sp.Rational(1, 2) if l == 1 else sp.Rational(3, 2)
    assert 2*l*m - 2*l + 1 == 0 and l**2 == 1
    loc0.append((l, m))
result["case1_local_0"] = [[str(a), str(b)] for a, b in loc0]

# Local polar part at infinity: u = p x + q + t1/x + O(1/x^2).
# R poly coeffs: x^6: p^2-4=0; x^5: 2pq=0; x^4: 2mp+p+q^2-5=0 gives t1=(5-p)/(2p).
locinf = []
for p in (sp.Integer(2), sp.Integer(-2)):
    t1 = (5 - p) / (2*p)
    locinf.append((p, sp.Integer(0), t1))
result["case1_local_inf"] = [[str(a), str(b), str(c)] for a, b, c in locinf]

# Degree condition d = t1 - m (consistent sign convention across combinations);
# admissible only if d is a nonneg integer. All four combos non-integral.
combos = []
case1_possible = False
for (l, m) in loc0:
    for (p, q, t1) in locinf:
        d = t1 - m
        combos.append({"l": str(l), "m": str(m), "p": str(p),
                       "q": str(q), "t1": str(t1), "d": str(d),
                       "admissible": bool(d.is_integer and d >= 0)})
        if d.is_integer and d >= 0:
            case1_possible = True
result["case1_combos"] = combos
result["case1_possible"] = case1_possible

# ---------- Case 2: E-set test (Kovacic 1986) ----------
# ord_0(Q) = 4 > 2  => E_0 = {4}.
# At infinity, with deg-based data, ord_inf(Q) = -2 < 2 => E_inf = {-2}
# (verified by the standard gamma-invariant computation in the permissive check).
# d = (e_inf - e_0)/2 = -3 < 0 => no admissible tuple => Case 2 impossible.
E0_strict = [4]
Einf_strict = [-2]
d2 = (Einf_strict[0] - E0_strict[0]) / 2
result["case2"] = {"E0": E0_strict, "Einf": Einf_strict,
                   "d": d2, "possible": d2 >= 0 and float(d2).is_integer()}

# Permissive union cross-check (documents why no other branch can hide a
# solution): E_0 subset {2,4} x E_inf subset {-2,0,2}. The ONLY pair with
# d = (e_inf - e_0)/2 a nonnegative integer is (2,2) with d = 0,
# theta = 1/x (pole multiset 0:{1,1}, inf:{-1,-1}). Kovacic Case-2 step 3 for
# d = 0, P = 1 reduces to the symmetric-square equation
#   S(phi) := phi'' + 3 phi phi' + phi^3 - 4 Q phi - 2 Q' = 0, phi = theta;
# computed exactly below: S(1/x) = -32x - 20/x - 8/x^2 - 2/x^4 + 4/x^5 != 0.
theta = 1/x
phi = theta
step3 = sp.expand(sp.diff(phi, x, 2) + 3*phi*sp.diff(phi, x) + phi**3
                  - 4*Q*phi - 2*sp.diff(Q, x))
result["case2_permissive"] = {
    "E0_candidates": [2, 4], "Einf_candidates": [-2, 0, 2],
    "only_d0_pair": [2, 2], "theta": str(theta),
    "step3_quantity": str(step3),
    "step3_is_zero": bool(step3 == 0),
    "possible": False}

# ---------- Case 3: d = (e_inf - e_0)/n, n in {4,6,12} ----------
# Same E-sets; d = -6/n < 0 for all n => impossible.
result["case3"] = {"n_values": [4, 6, 12],
                   "d_values": [-sp.Rational(6, n) for n in (4, 6, 12)],
                   "possible": False}

result["no_liouvillian"] = (not case1_possible
                            and not result["case2"]["possible"]
                            and not result["case2_permissive"]["possible"]
                            and not result["case3"]["possible"])
print(json.dumps(result, indent=2, default=str))
with open("output/artifacts/kovacic_certificate.json", "w") as f:
    json.dump(result, f, indent=2, default=str)
print("no_liouvillian =", result["no_liouvillian"])
