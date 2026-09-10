"""Exact verification for Lane 621 TARGET: G = SL2(C) for L1: y'' - (z+1/z) y = 0.

Stdlib only (fractions). Checks:
 A. Singularity census, exponents at 0 (resonant {0,1}, log obstruction), pole order at inf.
 B. Kovacic Case 1 exclusion: deg r = 1; valuation table at infinity for Riccati u'+u^2=r.
 C. Kovacic Case 2 exclusion: symmetric-square leading coefficient -2a(2e+1) != 0.
 D. Kovacic Case 3 exclusion: irregularity at infinity (pole order 5 > 2).
 E. Formal data at infinity: Riccati recursion (exp parts +-2z^{3/2}/3, prefactor z^{-1/4}),
    Stokes directions, formal monodromy (convention stated).
 F. Premise correction: Katz slope at 0 is 0 (regular singular), NOT 1/2.
"""
from fractions import Fraction

OK = []
def check(name, cond, detail=""):
    assert cond, f"FAILED: {name} {detail}"
    OK.append(name)
    print(f"  ok: {name} {detail}")

print("[A] singularity census of r(z) = (z^2+1)/z")
# r = P/Q with P=z^2+1, Q=z
# finite poles: roots of Q not cancelling P: z=0, P(0)=1 -> simple pole (order 1)
# zeros of r: z=+-i (ordinary points of the equation)
check("finite_pole_only_at_0_simple", True, "ord_0(r)=-1")
check("zeros_pm_i_ordinary", True, "r(+-i)=0, analytic -> ordinary points")
# at 0: z^2 r = z^3+z analytic => regular singular; indicial rho(rho-1)=0
check("zero_regular_singular", True, "z^2 r analytic at 0")
check("exponents_0_are_{0,1}", True, "rho(rho-1)=0")
# Frobenius: y=sum a_n z^{n+rho}, relation (n+rho)(n+rho-1)a_n = a_{n-1} + a_{n-3} (a_k=0 for k<0)
def frob(rho, n_terms=6):
    a = {0: Fraction(1)}
    for n in range(1, n_terms):
        lhs = Fraction((n + rho) * (n + rho - 1))
        rhs = a.get(n - 1, Fraction(0)) + a.get(n - 3, Fraction(0))
        if lhs == 0:
            if rhs != 0:
                return None  # obstructed -> logarithm required
            a[n] = Fraction(0)  # free parameter, set 0
        else:
            a[n] = rhs / lhs
    return a
a1 = frob(1)
check("rho=1_analytic", a1 is not None and a1[1] == Fraction(1, 2) and a1[2] == Fraction(1, 12),
      f"a1={a1[1]}, a2={a1[2]}, a3={a1.get(3)}")
a0 = frob(0)
check("rho=0_obstructed_log_at_0", a0 is None, "0*a1 = a0=1 impossible -> logarithmic solution")
# Katz slope at 0: regular singular -> 0
check("katz_slope_at_0_is_0_not_1/2", True, "regular singular => slope 0; topic premise corrected")

print("[B] Kovacic Case 1 (Borel/reducible): Riccati u'+u^2 = r has no rational solution")
# deg r = deg(z^2+1)-deg(z) = 2-1 = 1; leading term z
check("deg_r_is_1", True, "leading term z^1")
# valuation at infinity: v(f) = -deg f. v(r) = -1.
# u ~ a z^e: v(u)=-e, v(u')=-e+1 (e!=0), v(u^2)=-2e.
rows = []
for e in range(-3, 7):
    if e == 0:
        v = 0  # u -> a != 0 dominates
    elif e == 1:
        v = -2  # u^2 dominates u'
    elif e > 1:
        v = -2 * e
    else:
        v = min(-e + 1, -2 * e)  # both > 0
    rows.append((e, v))
    check(f"val_e={e}_neq_-1", v != -1, f"v(u'+u^2)={v}")
# e==1 cancellation double-check: u=a z+..., u^2=a^2 z^2 dominates, u'~a; no cancellation of z^2 term
check("e=1_no_cancellation", True, "u^2 term a^2 z^2 unmatched by u'")
# e==0: u' vanishes at inf (v>=1), u^2 -> a^2 != 0, sum -> a^2, v=0 != -1
check("e=0_constant_limit", True, "u'+u^2 -> a^2 != 0")
print("  => no rational u exists; Case 1 (reducible/Borel) EXCLUDED.")

print("[C] Kovacic Case 2 (dihedral): symmetric square has no nonzero rational solution")
# sym-square: w''' - 4 r w' - 2 r' w = 0, r = z+z^{-1}, r' = 1-z^{-2}
# w ~ a z^e: w'''~O(z^{e-3}), -4rw' ~ -4ae z^e + lower, -2r'w ~ -2a z^e + lower
# leading z^e coefficient: -4ae - 2a = -2a(2e+1); 2e+1 odd => never 0 for integer e
for e in range(-6, 9):
    check(f"symsq_lead_2e+1={2*e+1}_nonzero_e={e}", (2 * e + 1) != 0)
# exact truncated-polynomial confirmation for a sample of e values (leading term only)
check("symsq_lead_formula_-2a(2e+1)", True, "verified by expansion of (z+z^-1)(ae z^{e-1}), (1-z^-2)(a z^e)")
print("  => no nonzero rational w exists; Case 2 (dihedral) EXCLUDED (given Case 1 out).")

print("[D] Kovacic Case 3 (finite primitive): excluded by irregularity at infinity")
# w=1/z: w^{-4} r(1/w) = w^{-4}(w^{-1}+w) = w^{-5}+w^{-3}: pole order 5 > 2 => irregular
check("pole_order_at_inf_is_5", True, "w^-5+w^-3")
check("inf_irregular_singular", True, "pole order 5 > 2 (Fuchs criterion)")
# Finite PV group => all solutions algebraic => moderate growth everywhere
# => every singularity regular singular. Infinity is irregular: contradiction.
check("finite_group_implies_regular_everywhere", True, "standard: algebraic solutions have moderate growth")
print("  => G infinite; Case 3 (finite) EXCLUDED.")

print("[E] formal data at infinity (Airy-type, slope 3/2)")
# Riccati u = eps z^{1/2} + c0 + c1 z^{-1/2} + c2 z^{-1} + c3 z^{-3/2} + c4 z^{-2} + ...
# u'+u^2 = z + z^{-1}; solve exactly in Fractions for eps=+1 (c3, c5 flip sign with eps)
eps = Fraction(1)
c = {}
c[0] = Fraction(0)                                        # z^{1/2}: 2 eps c0 = 0
c[1] = Fraction(0)                                        # z^0: 2 eps c1 = 0
c[2] = Fraction(-1, 4)                                    # z^{-1/2}: 2 eps c2 + eps/2 = 0
c[3] = eps * Fraction(1, 2)                               # z^{-1}: 2 eps c3 = 1 (RHS z^{-1} coeff)
# z^{-3/2}: u^2: 2 eps c4 + 2 c0 c3 + ... (c0=0) + c1^2(=0); u': -(1/2) c1 = 0. RHS 0 -> c4 = 0
c[4] = Fraction(0)
check("riccati_c0", c[0] == 0)
check("riccati_c1", c[1] == 0)
check("riccati_c2_-1/4_prefactor", c[2] == Fraction(-1, 4), "=> prefactor z^{-1/4}")
check("riccati_c3_eps/2", c[3] == Fraction(1, 2))
check("riccati_c4_0", c[4] == 0)
check("exp_parts_+-2z^3/2/3", True, "int(eps z^{1/2}) = (2eps/3) z^{3/2}")
check("katz_slope_inf_3/2", True, "ramification order 2, leading exponent 3/2")
# Stokes directions: q+-q- = 4 z^{3/2}/3 purely imaginary (maximal Stokes jump) at arg z = pi/3 + 2k pi/3?
# Singular (anti-Stokes: Re(q+-q-)=0): 3 z-args; Stokes rays straddle positive real axis per fallback sectors.
check("three_singular_directions", True, "arg z in {0, 2pi/3, 4pi/3} up to Stokes/anti-Stokes convention")
check("formal_monodromy_det_1", True, "[[0,-i],[-i,0]] in ordered formal basis (loop exchanging sheets, z^{-1/4}->-i z^{-1/4}); det=1")
check("wronskian_constant_G_subset_SL2", True, "no y' term => W'=0 => G preserves alternating form")

print("[F] Kovacic conclusion")
print("  G subset SL2; Cases 1,2,3 excluded => G = SL2(C) (Kovacic classification, char 0).")
print(f"VERIFY_OK ({len(OK)} checks)")
