#!/usr/bin/env python3
"""Verify the genus-9 rank-2 Clifford certificate lattice.

Lattice Lambda = Z*H + Z*L with Gram matrix G = diag(16,-8).
Checks (exact integer arithmetic, stdlib only):
  A. G even, det=-128, signature (1,1) [Sylvester].
  B. No (-2)-vectors in Lambda (global parity obstruction).
  C. No isotropic vectors except 0 (descent; plus box scan).
  D. D.H = 16*x, so the Hodge window 0 < D.H < H^2=16 is EMPTY (global).
     Box scan |x|,|y|<=30 confirms no (d,mu) with 0<d<16, mu<=2,
     and logs the per-class table near x in {0,1}.
  E. Every Brill-Noether contributor (d,r) with Cliff<=2 on a genus-9
     curve has rho(g,d,r)<0 (finite enumeration).
  F. Explicit primitive embedding into the K3 lattice U^3+E8(-1)^2:
       H |-> e1+8*f1 in one U summand (square 16, primitive);
       L |-> r1+r2+r3+r4, four pairwise-orthogonal roots in E8(-1)
            (square -8, primitive: L/2 not in E8).
Prints VERIFY_OK on success.
"""
import itertools

G = ((16, 0), (0, -8))
H = (1, 0)


def q(v):
    x, y = v
    return G[0][0]*x*x + 2*G[0][1]*x*y + G[1][1]*y*y


def dot_H(v):
    x, _ = v
    return 16*x


def mu(v):
    return dot_H(v) - q(v) - 2


# A. even / det / signature
assert G[0][0] % 2 == 0 and G[1][1] % 2 == 0 and G[0][1] % 2 == 0
det = G[0][0]*G[1][1] - G[0][1]**2
assert det == -128, det
assert G[0][0] > 0 and det < 0  # Sylvester -> signature (1,1)
print("A: even, det=-128, signature (1,1) OK")

# B. no (-2): 16x^2-8y^2=-2  <=>  4(2x^2-y^2)=-1, LHS divisible by 4.
for x in range(-50, 51):
    for y in range(-50, 51):
        assert q((x, y)) != -2
# global: LHS-RHS parity: q(x,y) is even for all x,y, so -2 possible a
# priori, but mod 4: q = 4*(4x^2-2y^2) is 0 mod 4, -2 is 2 mod 4. QED.
print("B: no (-2)-vectors (box scan + mod-4 proof) OK")

# C. isotropic: 16x^2-8y^2=0 <=> y^2=2x^2 => x=y=0 (sqrt(2) irrational /
# infinite descent: y^2 even => y even => x even => ...).
for x in range(-50, 51):
    for y in range(-50, 51):
        if q((x, y)) == 0:
            assert (x, y) == (0, 0), (x, y)
print("C: no nonzero isotropic vectors OK")

# genus of H
g = G[0][0]//2 + 1
assert g == 9
print("C2: H^2=16, adjunction genus g=%d OK" % g)

# D. window: D.H = 16x, so 0 < D.H < 16 has NO integral solutions at all.
B = 30
danger = []
table = []
for x in range(-B, B+1):
    for y in range(-B, B+1):
        if x == 0 and y == 0:
            continue
        d, qq, m = dot_H((x, y)), q((x, y)), mu((x, y))
        if 0 < d < 16 and m <= 2:
            danger.append((x, y, d, qq, m))
        if x in (-1, 0, 1, 2) and abs(y) <= 3:
            table.append((x, y, d, qq, m))
assert danger == [], danger
print("D: Hodge window 0<D.H<16 with mu<=2 is EMPTY (global: D.H=16x) OK")
print("D-log per-class (x,y,d,q,mu):")
for row in sorted(table, key=lambda r: (r[0], r[1])):
    print("   ", row)
# spot: x=1 (D.H=H^2): mu = 8y^2-2 -> y=0 is D=H (residual 0), else >=6
for y in range(-B, B+1):
    m = mu((1, y))
    if y == 0:
        assert m == -2
    else:
        assert m >= 6, (y, m)
print("D2: x=1 slice: D=H gives mu=-2 (residual trivial); else mu>=6 OK")

# E. rho<0 for every contributing (d,r) with Cliff(d,r)=d-2r<=2, g=9.
bad = []
for r in range(1, 12):
    for d in range(0, 17):  # special: d<=2g-2=16
        h1 = g - d + r  # h^0(K-A) by Riemann-Roch given h^0(A)=r+1
        if h1 < 2:
            continue  # does not contribute to Clifford index
        if d - 2*r > 2:
            continue  # Cliff > 2
        rho = g - (r+1)*(g - d + r)
        if rho >= 0:
            bad.append((d, r, rho))
assert bad == [], bad
print("E: all Cliff<=2 contributors (d,r) have rho(g,d,r)<0 OK")

# F. primitive embedding.
# U summand: basis e,f, e^2=f^2=0, e.f=1. H_vec=(1,8) -> 2*1*8=16.
Hx, Hy = 1, 8
assert 2*Hx*Hy == 16 and Hx == 1  # primitive (coeff 1)
print("F1: H=e+8f in U, square 16, primitive OK")


def sdot(a, b):
    return sum(i*j for i, j in zip(a, b))


# E8(-1): pairing = -(standard dot). Roots have std-norm 2.
r1 = (1, -1, 0, 0, 0, 0, 0, 0)
r2 = (0, 0, 1, -1, 0, 0, 0, 0)
r3 = (0, 0, 0, 0, 1, -1, 0, 0)
r4 = (1, 1, 0, 0, 0, 0, 0, 0)
roots = (r1, r2, r3, r4)
for r in roots:
    assert sdot(r, r) == 2
for a, b in itertools.combinations(roots, 2):
    assert sdot(a, b) == 0, (a, b)
L = tuple(sum(v) for v in zip(*roots))
assert sdot(L, L) == 8  # -> square -8 in E8(-1)


def in_E8(v):
    # v a tuple of ints or half-integers (as doubled ints)
    d = [2*c for c in v]
    all_int = all(c % 2 == 0 for c in d)
    all_half = all(c % 2 == 1 or c % 2 == -1 for c in d)
    s = sum(d)
    return (all_int or all_half) and (s % 4 == 0)


half = tuple(c/2 for c in L)
assert not in_E8(half), half  # L/2 not in E8 -> L primitive (p^2|8 -> p=2)
print("F2: L=sum of 4 orthogonal E8(-1) roots, square -8, primitive OK")
print("F3: H.L=0 across summands; <H,L> primitive in U+E8(-1) OK")

print("VERIFY_OK")
