# Uniform non-compressedness and uniform Weak Lefschetz Property for the bigraded sextic family G_{a,b}

## Context

Artinian Gorenstein algebras of codimension 4 and socle degree 6 form the
Gondim-excluded cell (N,d) = (3,6): Gondim's higher-Hessian WLP-failure
theorem covers all (N,d) with N >= 3, d >= 3 except (3,3), (3,4), (3,6),
(4,4), and Abdallah–Schenck leave the weak Lefschetz property (WLP) at
c = 4, r = 6 open (failures known at r = 5 by Ikeda and r >= 7 by Gondim).
The admitted target asked whether the bigraded sextic subfamily G_{a,b}
below carries a compressed-Hilbert WLP-failing locus. The answer is a
complete uniform negative: the whole plane misses the compressed stratum
and every member satisfies WLP with the same Lefschetz element.

## Definitions

Let k = QQ. Let S = k[X,Y,U,V] and R = k[x,y,u,v] acting by differentiation
(x = d/dX, y = d/dY, u = d/dU, v = d/dV). For (a,b) in k^2 set

    G_{a,b} = X^2 U^4 + X Y U^2 V^2 + Y^2 V^4 + a U^5 V + b U V^5,

a homogeneous sextic, and B_{a,b} = R/Ann(G_{a,b}) its apolar Artinian
Gorenstein algebra of socle degree 6. Write h_e(a,b) = dim_k (B_{a,b})_e
(catalecticant rank) and L0 = x+y+u+v. Monomial bases of R_e are the
lexicographically sorted exponent tuples (R_2 has 10, R_3 has 20 elements).
WLP means some linear form has maximal-rank multiplication maps in every
degree; here the witness is uniformly L0.

## Result

For EVERY (a,b) in QQ^2 (indeed every real (a,b)):

(a) The Hilbert function is constantly (1,4,10,14,10,4,1) (total
    dimension 44). No member lies in the compressed stratum
    (1,4,10,20,10,4,1).

(b) Ann_3(a,b) is exactly the fixed 6-dimensional monomial span of
    {x^3, x^2y, xy^2, y^3, y^2u, x^2v}; hence h_3 = 14 identically.

(c) The map xL0 : (B_{a,b})_2 -> (B_{a,b})_3 has rank 10 (maximal),
    certified by a constant 10x10 quotient minor equal to 1. Together with
    constant full-rank minors in degrees 0 and 1 and Gorenstein duality in
    degrees 3, 4, 5, L0 is a Lefschetz element for every B_{a,b}: every
    member HAS WLP with the uniform witness L0. The subfamily contains no
    WLP-failing locus.

(d) At G0 (a=b=0): the Jordan type of xL0 is the generic
    conjugate-of-h partition [7,5,5,5,3,3,3,3,3,3,1,1,1,1] (also verified
    at (1,2)); Ann_1 = Ann_2 = 0 so mu_3 = 6 minimal cubic generators;
    mu_4 = 8 new quartic generators (dim Ann_4 = 25, rank of R_1*Ann_3 in
    R_4 is 17).

(e) Minor-census guardrail: among the C(14,10) = 1001 maximal minors of the
    quotient-projected 14x10 matrix Q, 318 are nonzero and 683 vanish
    (Q-rows 0..9 give determinant 0). A single vanishing maximal minor
    therefore cannot certify rank deficiency; the nonvanishing minor (= 1)
    is what decides the rank.

Consequence: the target's "general compressed Hilbert" and "rank <= 9 at
L0 / nonempty failing locus" assertions are false at every (a,b), and the
exact fallback conjunction for G0 at a=b=1 (H = (1,4,10,20,10,4,1) with
rank 9) is likewise false: at (1,1), H = (1,4,10,14,10,4,1) with middle
rank 10.

## Proof / evidence

Write C_e(a,b) for the degree-e catalecticant matrix (rows = R_e monomials,
cols = S_{6-e} monomials). All identities below are exact over QQ (integer
/ rational arithmetic, no Groebner bases) and replay via
`output/artifacts/verify_all.py` (VERIFY_OK, 14/14 PASS).

Lemma 1 (six forced cubics). The six operators x^3, x^2y, xy^2, y^3, y^2u,
x^2v annihilate every monomial of G_{a,b}. The five F-monomials have
(X,Y)-bidegrees (2,0),(1,1),(0,2),(0,0),(0,0); the first four operators
require total (X,Y)-order 3 > 2. For y^2u: it kills X^2U^4 (no Y),
XYU^2V^2 (Y-exponent 1 < 2), Y^2V^4 (yields 2V^4, then d/dU kills it), and
both tail terms (no Y). For x^2v: every term except X^2U^4 has X-exponent
< 2; X^2U^4 gives 2U^4, then d/dV kills it. All 30 operator/monomial pairs
verified exactly. Hence six rows of C_3(a,b) (positions 8,9,15,16,18,19)
are identically zero, so rank C_3(a,b) <= 14 and compressed h_3 = 20 is
impossible.

Lemma 2 (constant Hilbert function). Symbolic Gram determinants, each
verified as a polynomial identity:

    det(C_1 C_1^T) = 25(a^2+25b^2+20)(25a^2+b^2+20),
    det(C_2 C_2^T) = 303038464(100a^2+37)(100b^2+37),
    det(C_4^T C_4) = 46812394747330560000(180a^2+29)(180b^2+29),
    det(C_5^T C_5) = 34447360000(180a^2+180b^2+29)^2.

Every factor is a sum of squares plus a positive constant, hence nonzero
for every real (hence every rational) (a,b). Thus h_1 = 4, h_2 = 10,
h_4 = 10, h_5 = 4 identically; h_0 = h_6 = 1 (the C_6 entry at D = x^2u^4
is 2!4! = 48 for all (a,b) since D kills the other four F-terms).

Lemma 3 (h_3 = 14, Ann_3 fixed). The 14x14 minor of C_3(a,b) on rows =
columns = (0,1,2,3,4,5,6,7,10,11,12,13,14,17) is the constant 86369107968
!= 0 (symbolic determinant). With the Lemma 1 upper bound, rank C_3 = 14
for all (a,b); h_3 = 14, dim Ann_3 = 6, and Ann_3 is exactly the fixed span.

Lemma 4 (uniform middle full rank). Quotient (B)_3 by the fixed Ann_3 by
dropping coordinates J = (8,9,15,16,18,19). The projected multiplication
matrix Q is a constant integer matrix (L0 has constant coefficients); its
10x10 minor on Q-rows (0,1,2,4,5,7,8,9,11,13) with all 10 domain columns
equals 1 and rank Q = 10. Hence rank(xL0 : A_2 -> A_3) = 10 = min(h_2,h_3)
for every (a,b). Domain A_2 = R_2 since Ann_2 = 0, and Ann_3 is a
coordinate subspace, so Q exactly represents the quotient map.

WLP everywhere. Degree 1: the 10x4 matrix of xL0 : R_1 -> R_2 has 4x4 minor
1 on rows (v^2, uv, yv, xv); degree 0 is trivial. Gorenstein duality
(socle degree 6) transfers full rank to degrees 3, 4, 5. All six maps have
maximal rank, so L0 is a uniform Lefschetz element.

Part (d): quotient-basis Jordan computation at G0 gives kernel dimensions
[14,24,34,38,42,43,44] and partition
[7,5,5,5,3,3,3,3,3,3,1,1,1,1], the conjugate of (1,4,10,14,10,4,1);
identical at (1,2). Ann_1 = Ann_2 = 0 gives mu_3 = 6; the 24 products
R_1*Ann_3 span 17 dimensions in R_4 while dim Ann_4 = 25, so mu_4 = 8. The
318/683 census is a direct exact enumeration of all 1001 maximal minors of
Q (independently re-enumerated during audit).

## Limitations

- Proves nothing about the full compressed stratum (1,4,10,20,10,4,1)
  beyond this subfamily; the Gondim-excluded (3,6) cell remains open in
  general.
- Betti data are the head (mu_3, mu_4) = (6,8) only, not a full minimal
  resolution.
- Jordan type computed at G0 and (1,2) only; uniformity over the plane is
  not claimed.
- Certified over QQ (hence all rational, indeed all real, pairs (a,b));
  positive characteristic and arbitrary characteristic-0 extension fields
  are not addressed.

## Reproducibility

Run `python3 output/artifacts/verify_all.py` (stdlib + sympy only; exact
QQ/integer arithmetic) — expect VERIFY_OK (14/14 PASS). Supporting scripts
in `output/artifacts/`: audit_target.py (engine: catalecticants, Hilbert,
Lefschetz rank), handcheck.py (prints the det-1 Q10 matrix), jordan.py
(Jordan partition), betti_head.py (mu_3, mu_4). Independent audit
recomputed the Hilbert function with study-only Fraction arithmetic at
(0,0),(1,1),(1,2),(3,-1),(7,11),(2,3) — all (1,4,10,14,10,4,1) — and
re-enumerated the 1001 maximal minors (318 nonzero / 683 vanishing).

## References

- R. Gondim, On higher Hessians and the Lefschetz properties,
  https://arxiv.org/abs/1506.06387 (Thm 3.8 excludes (3,6)).
- N. Abdallah, H. Schenck, Free resolutions and Lefschetz properties of
  some Artin Gorenstein rings of codimension four,
  https://arxiv.org/abs/2208.01536 (c = 4, r = 6 WLP open).
- R. Gondim, G. Zappala, Lefschetz properties for Artinian Gorenstein
  algebras presented by quadrics, https://arxiv.org/abs/1601.04454.
- R. M. Miro-Roig, J. Perez-Diez, Perazzo hypersurfaces and the weak
  Lefschetz property, https://arxiv.org/abs/2402.09188.
