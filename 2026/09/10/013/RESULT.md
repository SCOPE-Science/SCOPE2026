# Exterior-stacked Mahler stability cell in R^4: certified 1%-gap above 32/3

## Context

The symmetric Mahler conjecture (reverse Blaschke–Santalo) asserts that for
every origin-symmetric convex body K in R^n,
P(K) = vol(K)·vol(K°) ≥ 4^n/n!,
with equality for the cube and cross-polytope (and Hanner polytopes).
It is resolved for n ≤ 3 (Iriyeh–Shibata) and open in R^4, the first open
symmetric dimension. Quantitative stability around the conjectured minimum
32/3 in R^4 needs exact data on genuinely new bodies outside the
cube/cross-polytope/Hanner and unconditional classes.

## Definitions

Let e_1,…,e_4 be the standard basis of R^4, z = (1,1,1,1), and for
s ∈ [3/8, 5/8]:

R_s = conv{±e_1, ±e_2, ±e_3, ±e_4, ±s·z}.

Write C = conv{±e_i} for the 4-cross-polytope (vol(C) = 2^4/4! = 2/3),
P(s) = vol(R_s)·vol(R_s°), D(s) = P(s) − 32/3 (Mahler deficit).
Conjectured R^4 minimum: 32/3. Decision threshold: (32/3)·1.01 = 808/75 ≈ 10.7733.

## Result

inf_{s ∈ [3/8,5/8]} P(s) ≥ 11 = (32/3)·(33/32),

with equality (minimum P = 11) at s = 1/2. In particular no
s* ∈ [3/8,5/8] has P(s*) ≤ (32/3)·1.01; the deficit satisfies
D(s) ≥ 1/3 throughout the scope.

Exact endpoint values: P(3/8) = 8126/729 ≈ 11.147,
P(1/2) = 11, P(5/8) = 21728/1875 ≈ 11.588.
Margin over threshold: 11 − 808/75 = 17/75.
The (Gap) alternative of the admitted cell holds; no witness exists.

## Proof / evidence

Vertices and polar. Since s ≤ 5/8 < 1, each ±e_i is uniquely maximized by
±x_i, hence a vertex. Since 4s ≥ 3/2 > 1, ±s·z is uniquely maximized by
±Σx_i, hence a genuine vertex: R_s is a 10-vertex body over the whole scope.
The polar of a hull of points is the intersection of slabs, exactly:

R_s° = {y : |y_i| ≤ 1 ∀i, |Σy_i| ≤ 1/s},

the cube [−1,1]^4 cut by one diagonal slab.

Primal volume. Each cross-polytope facet is a regular tetrahedron of edge √2
with 3-volume 1/3; a 4-pyramid has vol = h·base/4. The apex p = sz lies beyond
F_+ = conv{e_i} (Σp_i = 4s > 1). For a facet with sign pattern σ ∈ {±1}^4,
plane Σσ_i x_i = 1, visibility is σ·p = sΣσ_i > 1. With Σσ_i = 4−2k
(k = number of −1's) and t = 1/s ∈ [8/5, 8/3], value 4 always qualifies,
2 qualifies iff t < 2 (s > 1/2), and 0,−2,−4 never do. By the visible-facet
pyramid lemma, doubling over both apices:

V(s) := vol(R_s) = (4s+7)/12 for s ≤ 1/2; s+1/4 for s ≥ 1/2,

continuous with V(1/2) = 3/4. Heights are (4s−1)/2 and (2s−1)/2.

Dual volume. Put t = 1/s. By symmetry,
V*(s) := vol(R_s°) = 16 − 2C(t), C(t) = vol{y ∈ [−1,1]^4 : Σy_i > t}.
With w = (y+1)/2, a = (t+4)/2, C(t) = 16F(a),
F(a) = vol{w ∈ [0,1]^4 : Σw_i > a}.
Piece A (t ≥ 2, s ≤ 1/2): F(a) = (4−a)^4/24, so V*(s) = 16 − (4−t)^4/12.
Piece B (t ≤ 2, s ≥ 1/2): F(a) = 1 − [a^4 − 4(a−1)^4 + 6(a−2)^4]/24
(two-level inclusion–exclusion), so V*(s) = t(3t^3 − 16t^2 + 128)/12.

Gap certificate. Piece A (t ∈ [2,8/3]): P ≥ 11 ⟺
H(u) := 7u^5 − 32u^4 + 240u − 192 ≥ 0 on u = 4−t ∈ [4/3,2].
H''(u) = 140u^3 − 384u^2 = 28u^2(5u − 96/7) < 0 there, so H strictly
concave; H(2) = 0, H(4/3) = 13696/243 > 0; chord bound gives H ≥ 0.
Piece B (t ∈ [8/5,2]): P = (t+4)(3t^3−16t^2+128)/48 ≥ 11 ⟺
S(t) := 3t^4 − 4t^3 − 64t^2 + 128t − 16 ≥ 0.
S''(t) = 36t^2 − 24t − 128 is increasing for t ≥ 1/3 with S''(2) = −32 < 0,
so S strictly concave; S(2) = 0, S(8/5) = 17648/625 > 0; chord bound
gives S ≥ 0. Hence P(s) ≥ 11 on [3/8,5/8], equality only at s = 1/2.

Certificate replayed exactly in stdlib Fractions
(artifacts/verify_gap.py): endpoint fractions, concavity signs, margin
17/75, and a 2001-point scan. Monte-Carlo rejection checks agree to ~1%
(sanity only).

## Limitations

The explicit Steiner symmetrization w.r.t. {x_1 = x_2} fixes R_s
(equality case) rather than strictly decreasing volume; the deficit line
D(s) ≥ 1/3 follows from the exact product bound, not from a quantitative
stability modulus. Monte-Carlo checks are non-rigorous sanity only.
No claim beyond s ∈ [3/8,5/8] or about the global R^4 Mahler minimum.

## Reproducibility

Run `python3 artifacts/verify_gap.py` (stdlib only) — expects VERIFY_OK.
All endpoint fractions, second-derivative signs, threshold margin, and the
float scan replay from committed rational inputs.

## References

- H. Iriyeh, M. Shibata, Symmetric Mahler's conjecture for the volume
  product in the three dimensional case, Duke Math. J. 169 (2020).
  https://arxiv.org/abs/1706.01749
- J. Kim, Minimal volume product near Hanner polytopes.
  https://arxiv.org/abs/1212.2544
- J. Kim, A. Zvavitch, Stability of the reverse Blaschke-Santalo
  inequality for unconditional convex bodies.
  https://arxiv.org/abs/1302.5719
- G. Kuperberg, From the Mahler conjecture to Gauss linking integrals,
  Geom. Funct. Anal. 18 (2008). https://arxiv.org/abs/math/0610904
