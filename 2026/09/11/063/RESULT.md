# Adjoint H2 ledger for the model filiform Lie algebra m2(9)

## Context and motivation

Filiform Lie algebras are the nilpotent Lie algebras of maximal nilpotency
class. In dimension 9 the Vergne picture is anchored by two naturally graded
models, m0(9) and m2(9). For deformation theory the governing invariant is
cohomology with coefficients in the adjoint module: H^2(g,g) parametrizes
infinitesimal deformations and its vanishing is cohomological rigidity.
Existing published tables for low-dimensional filiforms (notably Burde's
affine tables through dimension 11) use trivial coefficients H^2(g,K), a
strictly smaller linear system that does not determine deformations.
Results on infinite-dimensional N-graded maximal-class algebras m0, m2, L1
(Fialowski-Millionshchikov, Millionschikov, Fialowski-Wagemann) concern a
different limit object with a grading-restricted and completed complex.
Dense-open non-rigidity theorems in dimensions 9-11 prove existence of
deformations without computing any exact adjoint H2 integer for a named
model. No prior source publishes the finite-dimensional adjoint
cocycle-modulo-coboundary ledger for m2(9).

## Definitions

Let m2(9) be the 9-dimensional Lie algebra over Q (hence over C) with basis
x1,...,x9 and nonzero brackets, plus skew-symmetry,

- [x1,xi] = x(i+1) for 2 <= i <= 8,
- [x2,xj] = x(j+2) for 3 <= j <= 7.

Let C^k = Hom(Lambda^k g, g) be the Chevalley-Eilenberg cochain spaces with
adjoint coefficients. Then dim C^1 = 81, dim C^2 = 324, dim C^3 = 756.
Differentials (standard conventions):

- d1(f)(x,y) = [f(x),y] + [x,f(y)] - f([x,y]),
- d2(phi)(x,y,z) = [x,phi(y,z)] + [y,phi(z,x)] + [z,phi(x,y)]
  - phi([x,y],z) - phi([y,z],x) - phi([z,x],y).

Cocycles Z^2 = ker d2, coboundaries B^2 = im d1, H^2 = Z^2/B^2.
Notation e_t(xa,xb) is the alternating bilinear map sending (xa,xb) to xt.
Weights deg(xi) = i make d1, d2 homogeneous; all computations are exact
rational, per weight block.

## Result

For m2(9) with the brackets above, over Q (hence over C):

- rank(d1 : C^1 -> C^2) = 66,
- rank(d2 : C^2 -> C^3) = 241,
- dim H^2(m2(9), m2(9)) = 324 - 241 - 66 = 17.

Seventeen explicit adapted-basis 2-cocycles span the quotient:

1. phi1 = e8(x1,x3)
2. phi2 = e8(x1,x4)
3. phi3 = e6(x1,x3) + e8(x1,x5)
4. phi4 = -e7(x1,x4) + e9(x3,x4)
5. phi5 = -e5(x1,x3) - e6(x1,x4) - e7(x1,x5) + e8(x3,x4) + e9(x3,x5)
6. phi6 = -e4(x1,x3) - 2e5(x1,x4) - e6(x1,x5) - e7(x1,x6) + e7(x3,x4) + e8(x3,x5) + e9(x3,x6)
7. phi7 = e3(x1,x3) + e4(x2,x3)
8. phi8 = -e2(x1,x2) + 3e3(x1,x3) + 2e4(x1,x4) + 2e5(x1,x5) + e6(x1,x6) + e7(x1,x7)
9. phi9 = e3(x1,x4) + e3(x2,x3) + e4(x2,x4)
10. phi10 = -e1(x1,x2) + 3e3(x1,x4) - 3e3(x2,x3) + 2e4(x1,x5) + 2e5(x1,x6) + e6(x1,x7) + e7(x1,x8)
11. phi11 = -e3(x2,x3) + e4(x1,x5) + e6(x1,x7) + e8(x1,x9)
12. phi12 = e3(x1,x5) + e3(x2,x4) + e4(x2,x5)
13. phi13 = -(1/2)e1(x1,x3) - e2(x2,x3) - (3/2)e3(x2,x4) - (3/2)e4(x3,x4) - e5(x1,x7) - e5(x3,x5) - (1/2)e6(x1,x8) - (1/2)e6(x3,x6) - e7(x1,x9) + (1/2)e8(x3,x8) + e9(x3,x9)
14. phi14 = e3(x1,x6) + e3(x2,x5) + e4(x2,x6)
15. phi15 = e3(x1,x7) + e3(x2,x6) + e4(x2,x7)
16. phi16 = e3(x1,x8) + e3(x2,x7) + e4(x2,x8)
17. phi17 = e3(x1,x9) + e3(x2,x8) + e4(x2,x9)

Each satisfies d2(phi) = 0 and their classes are linearly independent modulo
B^2, hence form a basis of H^2. In particular phi1(x1,x3) = x8 is closed but
not a coboundary, so dim H^2 >= 1 and m2(9) is not cohomologically rigid.

## Proof and evidence

The structure constants are sparse in the Vergne-adapted basis, so d1
(324x81) and d2 (756x324) are explicit small integer matrices (entries in
{-1,0,1}). The verifier rebuilds them from the brackets, checks Jacobi and
weight-homogeneity, and checks d2*d1 = 0 exactly by sparse multiplication.
Exact rational (Fraction) rank per N-homogeneous weight block gives
rank(d1) = 66 and rank(d2) = 241 = 171 + 70, hence dim H2 = 17. Per-block
nullspace extraction confirms each listed representative is closed and that
the 17 raise rank(B^2) from 66 to 83, i.e. they are quotient-independent and
span the 17-dimensional quotient. Mod-p probes at 32003 and 1000003 agree
(66/241). The audit independently rebuilt both matrices from the brackets in
a separate script and reproduced Jacobi, d2*d1 = 0, ranks 66/241, closedness
of all 17 cocycles, the +17 quotient increment, and the phi1 certificate.

Non-coboundary certificate for phi1: let y in C^2* be
y(psi) = -psi_8(x1,x3) - psi_9(x1,x4) + psi_9(x2,x3), i.e. -e^253 - e^290 +
e^296 in global C^2 coordinates. Then y^T d1 = 0 (all 81 entries vanish
exactly) while y^T phi1 = -1. In the weight -4 block with rows
e7(x1,x2), e8(x1,x3), e9(x1,x4), e9(x2,x3),
d1|block = [[-1,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1],[0,0,1,0,-1]] and
y|block = (0,-1,-1,1) is a left null vector pairing -1 with phi1. Hence
d1 f = phi1 is inconsistent and [phi1] != 0 in H^2.

Per-weight ledger (wt | dimC1 | dimC2 | dimC3 | rk d1 | rk d2 | H2):
-6: 3,1,0,1,0,0; -5: 4,2,0,2,0,0; -4: 5,4,0,3,0,1; -3: 6,6,1,4,1,1;
-2: 7,9,2,5,2,2; -1: 8,12,4,7,4,1; 0: 9,16,7,8,7,1; 1: 8,20,11,8,10,2;
2: 7,24,16,7,14,3; 3: 6,26,23,6,18,2; 4: 5,28,30,5,22,1;
5: 4,28,38,4,23,1; 6: 3,28,45,3,24,1; 7: 2,26,52,2,23,1;
8: 1,24,57,1,23,0; weights 9-16: C2 dims 20/16/12/9/6/4/2/1, rk d2 = 70,
H2 = 0. Totals: rk d1 = 66, rk d2 = 241, H2 = 17.

## Limitations

Certified over Q (hence over C) for the stated Vergne-adapted basis and
bracket convention. The integer dim H^2 = 17 and the ranks are
isomorphism-invariant facts; individual cocycle representatives are
basis-dependent. No claim is made about versal-space structure, Massey
products, or adjacent models (m0(9), dimension 10).

## Reproducibility

`output/artifacts/verify.py` (Python stdlib only: Fraction) rebuilds the
structure constants, both matrices, checks Jacobi, weight-homogeneity,
d2*d1 = 0, exact per-weight ranks, closedness plus quotient-independence of
the 17 representatives, and the phi1 left-null certificate; it prints
VERIFY_OK. Re-running `python3 output/artifacts/verify.py` reproduces
rank(d1)=66, rank(d2)=241, dimH2=17.

## References

- D. Burde, Affine cohomology classes for filiform Lie algebras (H^2(g,K), trivial coefficients, dim <= 11).
- A. Fialowski, D. Millionshchikov, Cohomology of graded Lie algebras of maximal class (math/0412325; trivial coefficients, infinite-dimensional graded m0/m2).
- D. Millionshchikov, Adjoint cohomology of graded Lie algebras of maximal class (arXiv:0709.2468; infinite-dimensional graded m0, m2).
- A. Fialowski, F. Wagemann, Cohomology and deformations of the infinite-dimensional filiform Lie algebra m2 (J. Algebra 319 (2008); HAL hal-00168473).
- D. Burde, F. Wagemann, Sympathetic Lie algebras and adjoint cohomology for Lie algebras (arXiv:1908.05963; J. Algebra 2023; general theory, semidirect-product examples).
- L. Cagliero, P. Tirao, The cohomology of filiform Lie algebras of maximal rank (2014; neighboring family).
