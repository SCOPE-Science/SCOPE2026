# Nonexistence of a four-atom degree-5 cubature for 2D fractional Brownian motion at H = 3/8

## Context

Cubature on path space compresses the law of a stochastic process into finitely
many deterministic paths with weights so that expectations of functionals are
matched up to a given degree. For Brownian motion this goes back to Lyons and
Victoir; for fractional Brownian motion (fBm) cubature theory exists for
H > 1/2 (Boutaib/Passeggeri), while sharp minimal-support boundaries in the
rough regime H < 1/2 were open. The admitted target asks whether the law of
the 2D fractional Brownian rough path at H = 3/8 can be compressed to four
deterministic paths matching all expected-signature moments through degree 5.
Degree 5 is the first level with genuine non-Gaussian area corrections, and
support size 4 is the first non-rank-trivial minimality threshold.

## Definitions

Let B = (B^1, B^2) be standard 2D fBm with Hurst index H = 3/8 on [0,1] (two
independent 1D fBms), lifted to a geometric rough path with Stratonovich
signature S(B) = (1, S_1, S_2, ...). A degree-m cubature with n atoms is a set
of continuous bounded-variation paths omega_1,...,omega_n : [0,1] -> R^2 and
weights lambda_j > 0 with sum 1 such that sum_j lambda_j S_k(omega_j) =
E[S_k(B)] for k = 0,...,m. Write x = omega(1) - omega(0) for the endpoint
increment, S_k(omega) in (R^2)^{otimes k} for level k, and sym for
symmetrization sym(T) = (1/k!) sum_{sigma} sigma . T. Let Z ~ N(0, I_2) and
P_{<=d}(R^2) denote real polynomials of total degree at most d.

## Result

Theorem. There do not exist n <= 4 continuous bounded-variation paths and
positive weights summing to one matching the expected Stratonovich signature
levels 0 through 5 of standard 2D fBm at H = 3/8 on [0,1].
Stronger form proved: for every H > 1/4, no formula with n <= 5 atoms matches
levels 0 through 4. Hence at least 6 atoms are necessary for any degree-4
(and a fortiori degree-5) cubature uniformly over the geometric rough-path
regime.

## Proof / Evidence

Lemma 1 (shuffle symmetric part): for every continuous BV path,
sym(S_k(omega)) = x^{otimes k}/k!. Proof by dissecting the cube [0,1]^k into
permuted simplices up to null diagonals; the integral over the cube is the
product of increments while each simplex gives a permuted iterated integral.

Since H = 3/8 > 1/4, fBm lifts to a geometric p-rough path and its
Stratonovich signature is the rough-path limit of piecewise-linear signatures
(Coutin-Qian; Friz-Wik). Each approximant satisfies the fixed finite shuffle
identities, which pass to the limit, so sym(S_k(B)) = B_1^{otimes k}/k! a.s.
with B_1 = B(1). Taking expectations gives sym(E[S_k(B)]) = E[B_1^{otimes k}]/k!.
For standard fBm, B_1 ~ N(0, I_2) since Var = 1^{2H} = 1, independent of H.

If a cubature existed, applying sym gives
sum_j lambda_j x_j^{otimes k} = E[Z^{otimes k}] for k <= 5, i.e. exact
quadrature sum_j lambda_j q(x_j) = E[q(Z)] for all q in P_{<=5}(R^2), in
particular through degree 4. But dim P_{<=2}(R^2) = 6 with basis
{1,x,y,x^2,xy,y^2}, so for n <= 5 the evaluation map to R^n has rank at most
5 and a nonzero p in P_{<=2} vanishes at all atoms. Then q = p^2 of degree
<= 4 gives 0 = sum lambda_j q(x_j) = E[p(Z)^2], contradicting Lemma 2 that
E[p(Z)^2] > 0 for every nonzero real polynomial (a nonzero polynomial cannot
vanish on an open set and the Gaussian density is everywhere positive). This
rules out n <= 5 at degree 4, hence n <= 4 at degree 5.

Computational certificate: output/artifacts/verify_obstruction.py replays
Part A (shuffle identity at k = 2,3 to ~1e-16) and Part B (exact sympy
vanishing quadrics with E[p^2] in {2, 5498/2209, 8/3}, all > 0): VERIFY_OK.
The Gaussian moment Gram matrix on the six monomials is positive-definite
(determinant 4), independently rechecked.

## Limitations

The obstruction uses only symmetric signature parts (levels 0-4) and the
endpoint law B_1 ~ N(0, I_2); it does not use H-specific iterated-integral
values. It gives the lower bound of at least 6 atoms for degree-4 cubature
but does not determine the minimal atom count for degree 5, nor construct any
upper-bound cubature formula.

## Reproducibility

Run `python3 output/artifacts/verify_obstruction.py` (requires numpy, sympy;
stdlib otherwise). Expected output: Part A maxerr ~1e-16 VERIFY_OK and Part B
exact E[p(Z)^2] values above VERIFY_OK. The analytic proof covers all
configurations of <= 5 points; the script certifies the mechanism on three
instance atom sets.

## References

- T. Lyons, N. Victoir, Cubature on Wiener space, Proc. R. Soc. A 460 (2004).
- R. Passeggeri, Some results on the Signature and Cubature of the Fractional
  Brownian motion for H > 1/2, arXiv:1609.07352.
- C. Litterer, Lower Bounds for the Support of Cubature Measures on Wiener
  Space and Optimal Degree-Five Constructions, Springer (2026),
  doi:10.1007/978-3-032-03914-9_5.
- E. Ferrucci, T. Herschell, C. Litterer, T. Lyons, High-degree cubature on
  Wiener space through unshuffle expansions, arXiv:2411.13707.
- H. M. Moeller, Lower bounds for the number of nodes in cubature formulae
  (1979), doi:10.1007/978-3-0348-6288-2_17.
