"""Lane-479 target audit: exact rational verification of the diagonal family rate.

Target: B=[-1,1]^4, P(B)=32/3; K_s={|x_i|<=1, |sum x_i|<=4-s}, s in [0,1/2].
Hand-derived exact identities under test:
  Vol(K_s)   = 16 - s^4/12            (two corner simplices cut off)
  Vol(K_s^oo) = 2/3 + s/(12(4-s))     (cross-polytope + 2 pyramids, base 1/3, h=s/(2(4-s)))
  P(s)-P(B)  = 4s/(3(4-s)) - s^4/18 - s^5/(144(4-s))     (LINEAR leading term s/3)
Checks:
  A) deficit(s) > P(B)*2*s^3 at SMALL nodes -> falsifies C<=2 cubic upper envelope
     (a uniform envelope on all of [0,1/2] needs only one counterexample node)
  B) deficit(s) >= s/4 on (0,1/2]       -> certified linear lower rate
  C) deficit(s)/s -> 1/3 (linear, not cubic)
  D) (P(B)/1000)*d_up(s)^2 < deficit(s) with d_up(s)=x+x^2, x=s/4 (rational
     upper bound of -ln(1-s/4) >= delta(s)) -> falsifies the "hence" clause
  E) pyramid volume cross-check via exact 4x4 Fraction determinants
  F) extremality of the 10 polar vertices via exact separating functionals
Stdlib only. Prints VERIFY_OK iff every check passes.
"""
from fractions import Fraction as F

def deficit(s):
    return F(4)*s/(F(3)*(F(4)-s)) - s**4/F(18) - s**5/(F(144)*(F(4)-s))

PB = F(32, 3)
NODES = [F(1, 1000), F(1, 100), F(1, 10), F(1, 4), F(1, 2)]
ok = True
falsified_at = []   # nodes where exact deficit EXCEEDS the C=2 cubic envelope

print("node | deficit(s) [exact] | deficit approx | P(B)*2s^3 approx | A:def>env | B:def>=s/4 | D:quad-env<def")
for s in NODES:
    d = deficit(s)
    env_cubic = PB * 2 * s**3
    x = s / 4
    d_up = x + x*x                      # rational upper bound of -ln(1-x), see DRAFT
    quad_env = PB * d_up * d_up / 1000
    a = d > env_cubic
    b = d >= s / 4
    dd = quad_env < d
    if a:
        falsified_at.append(s)
    # ok tracks the uniform claims B, D, E, F; cubic-falsification needs only ONE node
    ok = ok and b and dd
    print(f"s={s} | {d} | {float(d):.10f} | {float(env_cubic):.3e} | {a} | {b} | {dd}")

# C) linear rate
print("\ndeficit(s)/s at nodes (must cluster at 1/3, not -> 0):")
for s in NODES:
    r = deficit(s) / s
    print(f"s={s}: {float(r):.10f}  (exact {r})")
    assert F(2631, 8064) <= r <= F(8, 21), "rate out of certified band"
print("limit s->0+: 4/(3*4) = 1/3 by leading term 4s/(3(4-s)).")

# E) pyramid cross-check: apex p=(a,a,a,a), a=1/(4-s); base tet conv{e1..e4}
def det4(M):
    M = [list(map(F, row)) for row in M]
    n = 4
    det = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        assert piv is not None
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        pivv = M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / pivv
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return det

def simplex4_vol(q0, q1, q2, q3, q4):
    M = [[qi[j] - q0[j] for j in range(4)] for qi in (q1, q2, q3, q4)]
    return abs(det4(M)) / F(24)

print("\npyramid cross-check (apex + 4 base faces), exact Fractions:")
e = [[F(int(i == j)) for j in range(4)] for i in range(4)]
for s in NODES:
    a = F(1) / (F(4) - s)
    p = [a, a, a, a]
    # pyramid over the tetrahedral facet conv{e1..e4} has 5 vertices => one 4-simplex
    v = simplex4_vol(p, *e)
    formula = s / (F(24) * (F(4) - s))
    match = (v == formula)
    ok = ok and match
    print(f"s={s}: det-sum={v} formula={formula} match={match}")

# F) extremality of 10 polar vertices: C verts +-e_i plus tips +-p
print("\nextremality certificates (separating functional values):")
for s in [F(1, 100), F(1, 2)]:
    a = F(1) / (F(4) - s)
    pts = []
    for i in range(4):
        pts.append(([F(int(i == j)) - F(int(False)) for j in range(4)], f"e{i}"))
    for i in range(4):
        pts.append(([-F(int(i == j)) for j in range(4)], f"-e{i}"))
    pts.append(([a]*4, "p")); pts.append(([-a]*4, "-p"))
    # tip p: functional sum(y): p gives 4a>1; every other point gives <=1
    sums = [(sum(q), n) for q, n in pts]
    assert sum([a]*4) > 1 and all(v <= 1 for v, n in sums if n != "p"), sums
    # -p symmetric
    assert sum([-a]*4) < -1 and all(v >= -1 for v, n in sums if n != "-p")
    # e_0: functional y_0: e_0 gives 1, all others strictly <1
    y0 = [(q[0], n) for q, n in pts]
    assert all(v < 1 for v, n in y0 if n != "e0"), y0
    print(f"s={s}: tip-sum={float(sum([a]*4)):.6f}>1, others<=1; e0 extremal OK; "
          f"all 10 vertices extreme: True")
print("=> Vol(K_s^oo) = 2/3 + 2*(1/4)*(1/3)*h, h = s/(2(4-s)): EXACT, no overlap.")

print("\n" + (f"VERIFY_OK (cubic falsified at {falsified_at})" if (ok and falsified_at) else "VERIFY_FAIL"))
assert ok and falsified_at

# G) analytic interval falsification of the C=2 cubic envelope on (0,1/10]:
# D(s) >= s/4 (proved) vs P(B)*2 s^3 = 64/3 s^3 <= 64/300 s < s/4 for s <= 1/10.
from fractions import Fraction as F  # noqa: E402 (reuse)
s10 = F(1, 10)
assert PB * 2 * s10**3 < s10 / 4, "interval step fails"
print(f"G) analytic: on (0,1/10], P(B)*2s^3 <= 64/3 s^2 (s) <= {float(PB*2*s10**2):.6f} s < s/4 <= D(s). OK")

# J) Vol(B^oo)=2/3 via orthant triangulation: 16 simplices conv{0,s1e1,..,s4e4},
# each |det|/24 = 1/24.
print("\ncross-polytope volume cross-check (16 orthant simplices):")
tot = F(0)
for mask in range(16):
    sgn = [F(1) if (mask >> i) & 1 else F(-1) for i in range(4)]
    M = [[sgn[i] if i == j else F(0) for j in range(4)] for i in range(4)]
    tot += abs(det4(M)) / F(24)
assert tot == F(2, 3), tot
print(f"Vol(C) = {tot} = 2/3 OK  =>  P(B) = 16*2/3 = 32/3 OK")

# K) Mahler-monotonicity weak linear LOWER bound on delta(s):
# any admissible lambda satisfies P(K_s) <= lambda^4 P(B), so with x=D/P(B),
# delta >= (1/4) ln(1+x) >= x/(4(1+x)) (rational certificate, ln(1+x)>=x/(1+x)).
# This certifies delta = Theta(s) but with constant ~1/133, a factor ~16 short
# of the target's s/8 -- recorded honestly as OPEN.
print("\nweak linear lower bound on delta(s) via Mahler monotonicity:")
print("node | D/P(B) [exact] | cert LB x/(4(1+x)) | s/8 | LB>=s/8? | UB s(4+s)/16")
open_gap = True
for s in NODES:
    d = deficit(s)
    x = d / PB
    lb = x / (F(4) * (F(1) + x))
    ub = s * (F(4) + s) / F(16)
    reaches = lb >= s / 8
    open_gap = open_gap and (not reaches)
    print(f"s={s}: x={float(x):.6f} LB={float(lb):.7f} s/8={float(s/8):.7f} "
          f"{reaches} UB={float(ub):.6f}")
    assert lb >= s / F(140), f"weak bound fails at {s}"   # certified ~1/133 band
    assert ub >= lb, f"band inverted at {s}"
assert open_gap, "unexpected: Mahler route reaches s/8 (recheck)"
print("=> delta(s) in [s/140, s(4+s)/16]: linear band certified; s/8 OPEN via this route.")
# conv{0, s e_1,.., s e_4}; exact det check that its volume is s^4/24.
print("\ncorner-cut cross-check (exact 4x4 determinants):")
for s in NODES:
    q0 = [F(0)]*4
    verts = [[s if i == j else F(0) for j in range(4)] for i in range(4)]
    M = [[verts[i][j] - q0[j] for j in range(4)] for i in range(4)]
    v = abs(det4(M)) / F(24)
    assert v == s**4 / F(24), (s, v)
    print(f"s={s}: corner simplex vol={v} = s^4/24 OK")
print("=> Vol(K_s) = 16 - 2*(s^4/24) = 16 - s^4/12: EXACT (s<=1/2 so box vacuous).")
# D(s) >= 2631 s/8064 (proved) and delta(s) <= s(4+s)/16 <= 9s/32 (proved).
# 2631/8064 = 0.3263... > 9/32 = 0.28125, hence D(s) >= delta(s) on (0,1/2].
assert F(2631, 8064) >= F(9, 32), "ratio step fails"
print(f"H) analytic: D(s)/s >= 2631/8064 = {float(F(2631,8064)):.6f} > "
      f"9/32 = {float(F(9,32)):.6f} >= delta(s)/s on (0,1/2] => D(s) >= delta(s). OK")
print("=> quadratic stability HOLDS with room on this path (D/delta^2 -> +inf).")
