"""Exact rational Riccati/Sturm gap certificate for the disordered dimer Jacobi box.

Box J: n=10, d_i in [-1/10,1/10], odd off-diagonals e in [7/5,8/5],
even off-diagonals e in [2/5,3/5]. Test points lam = +/-3/5.

Method: Riccati ratios r_k = p_k/p_{k-1} with r_1 = lam - d_1 and
  r_k = (lam - d_k) - e_{k-1}^2 / r_{k-1}.
At lam=+3/5 we exhibit sign-invariant boxes Ro (odd, >0) x Re (even, <0)
closed under the interval step maps over the WHOLE continuum box J.
Nonvanishing of every enclosed ratio implies no p_k hits 0 at lam=+/-3/5
for any T in J, and the fixed sign pattern gives Sturm agreement count
exactly 5 at both endpoints, hence 5 eigenvalues below -3/5 and 5 above
+3/5: (-3/5,3/5) is eigenvalue-free uniformly on J.

Interval rule used throughout: for L in [Llo,Lhi], S in [Slo,Shi],
t in [tlo,thi] (t strictly signed), the enclosure of L - S*t is
  [Llo - maxProd, Lhi - minProd],
where [minProd,maxProd] is the four-corner product
  [min(Slo*tlo,Slo*thi,Shi*tlo,Shi*thi), max(...)]).

Also: textbook baselines (Gershgorin / Brauer / T^2-Gershgorin) as exact
rationals.

Run: python3 sturm_gap_certificate.py  (stdlib only)
"""
from fractions import Fraction as Q

D = (Q(-1, 10), Q(1, 10))
ES = (Q(7, 5), Q(8, 5))
EW = (Q(2, 5), Q(3, 5))
ES2 = (ES[0] * ES[0], ES[1] * ES[1])   # [49/25, 64/25]
EW2 = (EW[0] * EW[0], EW[1] * EW[1])   # [4/25, 9/25]
LAM_P = Q(3, 5)
LAM_M = Q(-3, 5)


def prod_interval(S, t):
    """Four-corner product enclosure of S*t (exact, no sign assumption)."""
    ps = (S[0] * t[0], S[0] * t[1], S[1] * t[0], S[1] * t[1])
    return (min(ps), max(ps))


def step_images(lam, Ro, Re):
    """Return (E1, O1): image of Ro under even step (strong bond), image of Re
    under odd step (weak bond), as exact Fraction intervals.
    Step map: r -> (lam - d) - S/r with S the bond-square interval and
    1/r ranging over the reciprocal interval t = [1/b, 1/a] (Ro, Re are
    strictly signed, so this is exact monotone). The subtraction uses the
    four-corner rule L - S*t = [Llo-maxProd, Lhi-minProd]."""
    lamd = (lam - D[1], lam - D[0])
    a, b = Ro
    assert (a > 0 and b > 0) or (a < 0 and b < 0), Ro
    t = (Q(1) / b, Q(1) / a)
    minP, maxP = prod_interval(ES2, t)
    E1 = (lamd[0] - maxP, lamd[1] - minP)
    c, e = Re
    assert (c > 0 and e > 0) or (c < 0 and e < 0), Re
    u = (Q(1) / e, Q(1) / c)
    minQ, maxQ = prod_interval(EW2, u)
    O1 = (lamd[0] - maxQ, lamd[1] - minQ)
    return E1, O1


def check_closed(lam, Ro, Re):
    r1 = (lam - D[1], lam - D[0])
    E1, O1 = step_images(lam, Ro, Re)
    ok_r1 = (r1[0] >= Ro[0] and r1[1] <= Ro[1])
    ok_e = (E1[0] >= Re[0] and E1[1] <= Re[1])
    ok_o = (O1[0] >= Ro[0] and O1[1] <= Ro[1])
    return ok_r1 and ok_e and ok_o, {"r1": r1, "E1": E1, "O1": O1}


def main():
    # ---- positive test point lam = +3/5 ----
    Ro_p = (Q(1, 2), Q(11, 10))     # odd ratios: strictly positive
    Re_p = (Q(-5), Q(-1))           # even ratios: strictly negative
    okp, tabp = check_closed(LAM_P, Ro_p, Re_p)
    assert tabp["E1"] == (Q(-231, 50), Q(-119, 110)), tabp["E1"]
    assert tabp["O1"] == (Q(133, 250), Q(53, 50)), tabp["O1"]
    # ---- negative test point lam = -3/5 (mirror) ----
    Ro_m = (Q(-11, 10), Q(-1, 2))
    Re_m = (Q(1), Q(5))
    okm, tabm = check_closed(LAM_M, Ro_m, Re_m)
    assert tabm["E1"] == (Q(119, 110), Q(231, 50)), tabm["E1"]
    assert tabm["O1"] == (Q(-53, 50), Q(-133, 250)), tabm["O1"]

    print("lam=+3/5: Ro=", Ro_p, " Re=", Re_p)
    for k, v in tabp.items():
        print(f"  {k}: [{v[0]}, {v[1]}] = [{float(v[0]):.6f}, {float(v[1]):.6f}]")
    print("  CLOSED:", okp)
    print("lam=-3/5: Ro=", Ro_m, " Re=", Re_m)
    for k, v in tabm.items():
        print(f"  {k}: [{v[0]}, {v[1]}] = [{float(v[0]):.6f}, {float(v[1]):.6f}]")
    print("  CLOSED:", okm)

    # Sign pattern: at +3/5, odd ratios>0, even<0 -> p signs: +,+,-,-,...
    signs_p = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1]
    agr_p = sum(1 for k in range(1, 11) if signs_p[k] * signs_p[k - 1] > 0)
    # at -3/5: r_odd<0, r_even>0.
    s = [1]
    rsign = [-1, 1]  # odd, even repeating; r1..r10 = -,+,-,+,...,-,+
    for k in range(1, 11):
        s.append(s[-1] * rsign[(k - 1) % 2])
    agr_m = sum(1 for k in range(1, 11) if s[k] * s[k - 1] > 0)
    print("signs(+3/5):", signs_p, "agreements:", agr_p)
    print("signs(-3/5):", s, "agreements:", agr_m)
    assert okp and okm and agr_p == 5 and agr_m == 5
    print("CERTIFICATE OK: Sturm counts 5/5 -> (-3/5,3/5) eigenvalue-free on all of J.")

    # ---- textbook baselines (exact rationals) ----
    print("\n--- baselines ---")
    # (a) Gershgorin: every disc contains [-3/5,3/5].
    print("Gershgorin: interior discs have R_i>=[9/5], edge rows R_i>=[7/5], "
          "centers in [-1/10,1/10]; each disc contains [-3/5,3/5]; "
          "union connected, no gap.")
    # (b) Brauer: single oval (1,3) covers [-3/5,3/5].
    z = Q(3, 5)
    dm = Q(1, 10)
    lhs = (z + dm) ** 2  # worst case |z-d1||z-d3| <= (|z|+1/10)^2
    rhs = Q(7, 5) * (Q(9, 5))  # min R_1*R_3 = 7/5 * 9/5
    assert lhs <= rhs
    print(f"Brauer oval(1,3): worst LHS ({z}+1/10)^2={lhs}={float(lhs):.4f} <= "
          f"min R1*R3={rhs}={float(rhs):.4f}; whole [-3/5,3/5] in one oval.")
    # (c) T^2-Gershgorin by joint optimisation: exact row minima of C-R.
    t2_edge = t2_baseline()
    print(f"  uniform T^2-Gershgorin lower edge over J = {t2_edge} = 0.13: "
          f"certifies spec(T^2) >= 13/100, i.e. at best the gap "
          f"(-sqrt(13)/10, sqrt(13)/10) ~ (-0.3606, 0.3606).")
    print("  The Sturm 0.6 certificate is >=66% sharper (0.6/0.3606 > 1.66) "
          "and adds exact 5/5 eigenvalue counts.")


def t2_baseline():
    """Joint row-wise minimisation of (T^2 center - radius) over J.

    Row i (1-based): C_i = d_i^2 + e_L^2 + e_R^2 (absent bonds omitted);
    R_i = e_L*|d_{i-1}+d_i| + e_R*|d_i+d_{i+1}|
          + (e_{i-2}*e_{i-1} if i>=3) + (e_i*e_{i+1} if i<=8).
    Diagonals: for fixed bonds the d-part is smooth on each sign-case
    region with no stationary point in the box (along t=|d_i| the diagonal
    parabola t^2-S*t has vertex S/2 with S = adjacent-bond sum >= 4/5, so
    S/2 >= 2/5 > 1/10 -- asserted per row below; neighbour equations need
    e=0), so the minimum sits at aligned +-1/10 corners: d_i^2 = 1/100,
    |sums| = 1/5. Neighbour-only bonds appear solely as -e*e_nb (e>0),
    hence are set to hi. Each adjacent bond minimises e^2 - K*e (convex),
    K = 1/5 + (outer neighbour hi if a product sits on that side, else 0);
    the vertex K/2 lies outside the bond box in every case (asserted), so
    the minimum is at an endpoint: hi for weak bonds, lo for strong bonds.
    """
    from fractions import Fraction as F
    Slo, Shi, Wlo, Whi = F(7, 5), F(8, 5), F(2, 5), F(3, 5)

    def bond(j):
        """(lo, hi) of bond e_j (1-based); odd j strong, even j weak."""
        return (Slo, Shi) if j % 2 == 1 else (Wlo, Whi)

    # sign-case enumeration: max |d_i+d_j| over [-1/10,1/10]^2
    corners = [F(-1, 10), F(1, 10)]
    assert max(abs(x + y) for x in corners for y in corners) == F(1, 5)

    def min_bond_term(lo, hi, K, name):
        """min of e^2-K*e over [lo,hi]; vertex asserted outside the box,
        then cross-checked against both endpoints."""
        v = K / 2
        cands = (lo * lo - K * lo, hi * hi - K * hi)
        if hi <= F(3, 5):  # weak bond: minimum at hi
            assert v >= hi, (name, v, hi)
            assert cands[1] <= cands[0], (name, cands)
            return cands[1], f"{name}=hi"
        else:  # strong bond: minimum at lo
            assert v <= lo, (name, v, lo)
            assert cands[0] <= cands[1], (name, cands)
            return cands[0], f"{name}=lo"

    # per row: adjacent bonds, and outer-neighbour hi where a product sits
    # on that bond's outer side (left bond: e_{i-2}*e_{i-1} iff i>=3;
    # right bond: e_i*e_{i+1} iff i<=8)
    rows = {
        1: {"adj": [1], "prod_hi": {1: Whi}},
        2: {"adj": [1, 2], "prod_hi": {2: Shi}},
        3: {"adj": [2, 3], "prod_hi": {2: Shi, 3: Whi}},
        4: {"adj": [3, 4], "prod_hi": {3: Whi, 4: Shi}},
        5: {"adj": [4, 5], "prod_hi": {4: Shi, 5: Whi}},
        6: {"adj": [5, 6], "prod_hi": {5: Whi, 6: Shi}},
        7: {"adj": [6, 7], "prod_hi": {6: Shi, 7: Whi}},
        8: {"adj": [7, 8], "prod_hi": {7: Whi, 8: Shi}},
        9: {"adj": [8, 9], "prod_hi": {8: Shi}},
        10: {"adj": [9], "prod_hi": {9: Whi}},
    }
    expected = {1: F(17, 20), 10: F(17, 20),
                2: F(97, 100), 9: F(97, 100),
                3: F(13, 100), 4: F(13, 100), 5: F(13, 100),
                6: F(13, 100), 7: F(13, 100), 8: F(13, 100)}
    edge = None
    for i in range(1, 11):
        spec = rows[i]
        # diagonal vertex check: S/2 > 1/10 for every bond sign case
        S_lo = sum(bond(j)[0] for j in spec["adj"])
        assert S_lo / 2 > F(1, 10), (i, S_lo)
        f = F(1, 100)  # aligned +-1/10 diagonals: d_i^2 = 1/100
        desc = []
        for j in spec["adj"]:
            lo, hi = bond(j)
            K = F(1, 5) + spec["prod_hi"].get(j, F(0))
            val, where = min_bond_term(lo, hi, K, f"e{j}")
            f += val
            desc.append(f"e{j}{where[-3:]}")
        assert f == expected[i], (i, f, expected[i])
        edge = f if edge is None else min(edge, f)
        print(f"  T^2 row {i}: min(C-R) = {f} = {float(f):.4f} "
              f"({', '.join(desc)}, aligned +-1/10 diagonals)")
    assert edge == F(13, 100), edge
    return edge


if __name__ == "__main__":
    main()
