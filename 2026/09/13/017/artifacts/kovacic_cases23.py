"""Kovacic Cases 2 and 3: complete E-set tables for Q (exact rational arithmetic).

Reference: J. J. Kovacic, "An algorithm for solving second order linear
homogeneous differential equations", Journal of Symbolic Computation 2
(1986) 3-43, DOI 10.1016/S0747-7171(86)80010-4.  Bibliographic record
verified via OpenAlex work W2067358142 (title / journal / year / DOI match).
The E-set definitions and degree formulae below are that paper's algorithm
(Case 2 with n = 2; Case 3 with n in {4, 6, 12}); only the branches actually
triggered by this Q are invoked, so the hand-run is self-verifying.

Equation: y'' = Q y with Q = 4x^2 + 5 + 4/x - 1/(4x^2) - 1/x^3 + 1/x^4.
Only the pole orders of Q enter the tables; they are recomputed exactly here.
"""
import json
import sympy as sp

x = sp.Symbol("x")
Q = 4*x**2 + 5 + 4/x - sp.Rational(1, 4)/x**2 - 1/x**3 + 1/x**4

out = {"Q": str(Q),
       "reference": {
           "author": "J. J. Kovacic",
           "title": "An algorithm for solving second order linear "
                    "homogeneous differential equations",
           "journal": "Journal of Symbolic Computation 2 (1986) 3-43",
           "doi": "10.1016/S0747-7171(86)80010-4",
           "record_check": "OpenAlex W2067358142: title/journal/year/DOI match"}}

# ---------------- Step 0: exact pole inventory ----------------
s_poly, t_poly = sp.fraction(sp.together(Q))
sP, tP = sp.Poly(sp.expand(s_poly), x), sp.Poly(sp.expand(t_poly), x)
assert (sP.degree(), tP.degree()) == (6, 4), (sP.degree(), tP.degree())
assert sp.limit(x**4 * Q, x, 0) == 1 and sp.limit(x**5 * Q, x, 0) == 0
assert sP.eval(0) != 0  # numerator does not vanish at 0: pole order exactly 4
ord0 = 4                      # finite pole: x = 0, order 4
ordinf = tP.degree() - sP.degree()   # deg(den) - deg(num) = -2
assert ordinf == -2
out["pole_data"] = {
    "num_deg": sP.degree(), "den_deg": tP.degree(),
    "num_at_0": str(sP.eval(0)),
    "finite_poles": [{"point": "0", "order": ord0}],
    "ord_inf_deg_diff": ordinf,
    "pole_order_at_inf": 0,
    "note": ("Only finite pole is x=0 (order 4, since x^4*Q->1, x^5*Q->0 "
             "and num(0)=4<>0). At infinity o(inf) = deg(den)-deg(num) = -2, "
             "i.e. an ordinary point of Q (pole order 0 there).")}

# ---------------- Necessary-condition gates (Kovacic p.3) ----------------
# Case 1: every pole even order or order 1; o(inf) even or > 2.
# Case 2: some pole of odd order > 2 or of order 2.
# Case 3: every pole order <= 2 and o(inf) >= 2.
orders = {"0": ord0, "inf": 0}  # pole orders (0 at inf = ordinary point)
gates = {
    "case1": all((v % 2 == 0) or (v == 1) for v in orders.values()) and (
        (ordinf % 2 == 0) or (ordinf > 2)),
    "case2": any((v == 2) or (v > 2 and v % 2 == 1) for v in orders.values()),
    "case3": all(v <= 2 for v in orders.values()) and (ordinf >= 2)}
out["necessary_conditions"] = {
    "case1_gate_pass": gates["case1"],
    "case1_note": "pole order 4 (even), o(inf)=-2 (even): full Case-1 test "
                  "required; run exactly in kovacic_case2.py, fails on d.",
    "case2_gate_pass": gates["case2"],
    "case2_note": "pole orders are {0: 4, inf: 0}: no pole of order 2 or of "
                  "odd order > 2, so Case 2 is already impossible.",
    "case3_gate_pass": gates["case3"],
    "case3_note": "pole of order 4 > 2 (and o(inf)=-2 < 2), so Case 3 is "
                  "already impossible."}

# ---------------- E-sets (rules invoked) ----------------
# Finite pole of order v > 2: E = {v}.  At infinity with o(inf) < 2: E = {o(inf)}.
# Order-1 / order-2 branches are vacuous for this Q (no such poles).
E0 = [ord0]        # {4}
Einf = [ordinf]    # {-2}
out["E_sets"] = {
    "E_0": E0, "E_0_rule": "finite pole of order 4 > 2 -> {4}",
    "E_inf": Einf, "E_inf_rule": "o(inf) = -2 < 2 -> {-2}",
    "vacuous_branches": "order-1 and order-2 E-set branches do not occur "
                        "(no such poles of Q)"}

# ---------------- Case 2 table (n = 2): d = (e_inf - e_0)/2 ----------------
rows2 = []
for e0 in E0:
    for einf in Einf:
        d = sp.Rational(einf - e0, 2)
        ok = bool(d.is_integer and d >= 0)
        rows2.append({"e_0": e0, "e_inf": einf, "d": str(d), "admissible": ok})
case2_possible = any(r["admissible"] for r in rows2)
out["case2_table"] = {"n": 2, "formula": "d = (e_inf - e_0)/2",
                      "rows": rows2, "possible": case2_possible}

# ---------------- Case 3 tables: d = (n/12)(e_inf - e_0), n = 4, 6, 12 ------
rows3 = {}
case3_possible = False
for n in (4, 6, 12):
    rows = []
    for e0 in E0:
        for einf in Einf:
            d = sp.Rational(n, 12) * (einf - e0)
            ok = bool(d.is_integer and d >= 0)
            rows.append({"e_0": e0, "e_inf": einf, "d": str(d),
                         "admissible": ok})
            if ok:
                case3_possible = True
    rows3[str(n)] = {"n": n, "formula": "d = (n/12)(e_inf - e_0)",
                     "rows": rows,
                     "possible": any(r["admissible"] for r in rows)}
out["case3_tables"] = rows3
out["case3_possible"] = case3_possible

out["verdict"] = {
    "case2_possible": case2_possible,
    "case3_possible": case3_possible,
    "no_liouvillian_cases23": (not case2_possible) and (not case3_possible),
    "meaning": ("With Case 1 already ruled out exactly "
                "(kovacic_certificate.json), no Liouvillian solution exists; "
                "Kovacic Case 4 holds, so the Galois group is SL(2,C).")}

print(json.dumps(out, indent=2))
with open("output/artifacts/kovacic_cases23.json", "w") as f:
    json.dump(out, f, indent=2)
