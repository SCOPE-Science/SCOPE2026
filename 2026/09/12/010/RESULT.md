# Refutation of the uniform 15% cyclotomic smoothing-width improvement at dimension 1024

## Context

Every dual Fourier distinguishing argument in lattice cryptography pays a
smoothing-width cost via Banaszczyk-type Gaussian tail bounds. Generic
constants are known to be loose for structured lattices, so a sharper
explicit tail lemma for the workhorse power-of-two cyclotomic family at
dimension N=1024 with negligible tail 2^{-128} would tighten all
fixed-parameter Module-LWE thresholds at once. The admitted target asked
whether every dual of a power-of-two cyclotomic ideal lattice of dimension
1024 satisfies rho_{1/s}(L^* \\ {0}) <= 2^{-128} at width s >= 0.85 s_B(N),
i.e. a uniform 15% saving over the generic Banaszczyk baseline s_B(N).

## Definitions

Use the Micciancio-Regev convention rho_t(x)=exp(-pi ||x||^2/t^2), so
rho_{1/s}(y)=exp(-pi s^2 ||y||^2): larger smoothing width s gives smaller
tail mass. For an integer lattice with shortest vector 1 the generic
textbook baseline (Micciancio-Regev/Banaszczyk smoothing lemma, Lemma 3.3
form) is s_B(N)^2=L/pi with L=ln(2N(1+2^{128})) and N=1024, at smoothing
error eps=2^{-128}. Let R=Z[x]/(x^{1024}+1) be the ring of integers of the
power-of-two cyclotomic field Q(zeta_{2048}).

## Result

The claimed uniform 15% improvement is FALSE. The dual L^*=Z^{1024} of the
unit ideal lattice has Gaussian tail mass at least 2^{-90}, strictly
exceeding 2^{-128}, at the claimed width s'=0.85 s_B(1024). The violation
is at least 38 bits (factor at least 2^{38} ~ 2.7e11). In fact no constant
factor c<1 can work uniformly on this member: beating the target would
require c^2 L >= 139 ln 2, i.e. c^2 >= 1-O(2^{-128}), so the generic union
bound is essentially tight here and c^2=0.7225 fails with enormous margin.

## Proof / evidence

Under the coefficient embedding, R is exactly Z^{1024} as a Euclidean
lattice: the unit ideal lattice (1), a valid power-of-two cyclotomic ideal
lattice. Since Z^{1024} with the standard inner product is self-dual, its
lattice dual is L^*=Z^{1024}, hence a member of the target family. Z^{1024}
has exactly 2N=2048 shortest nonzero vectors (+-e_i, norm 1). Dropping all
other shells gives tail >= 2048 exp(-pi (s')^2). Since
(s')^2=(85/100)^2 s_B^2=(289/400)(L/pi), pi cancels exactly:
pi (s')^2=(289/400) L and tail >= 2048 exp(-(289/400)L). Now
L=ln(2048(1+2^{128}))=139 ln 2+d with 0<d=ln(1+2^{-128})<2^{-128}. It
suffices to show (289/400)L <= 101 ln 2, for then tail >= 2048 e^{-101 ln 2}
=2^{11} 2^{-101}=2^{-90} >> 2^{-128}. Rigorous interval certificate with
exact rational arithmetic and wide enclosures
0.6931471805 <= ln 2 <= 0.6931471806: L_HI=139*0.6931471806+2^{-128}
~96.34745810, (289/400)L_HI ~69.6110 <= 101*0.6931471805 ~70.0079. Hence
pi(s')^2 <= 101 ln 2 rigorously and the tail is at least 2^{-90}. Floating
cross-check: s_B~5.5379, s'~4.7072, first shell ~1.2e-27 ~4.1e11 times
2^{-128}. The certificate script uses Python stdlib exact Fraction
arithmetic and prints VERIFY_OK.

## Limitations

The refutation uses the coefficient-embedding unit ideal (Z^{1024},
self-dual). Under the canonical embedding the unit ideal is a unitarily
scaled copy with an identical scale-invariant tail ratio, so the
counterexample is robust to embedding normalization. The result rules out
only the uniform 15% improvement over the whole dual family (indeed any
uniform c<1 on this member); it does not preclude smaller improvements for
restricted subfamilies excluding the integer lattice.

## Reproducibility

Run `python3 output/artifacts/verify_counterexample.py` (Python 3 stdlib
only). Expected output ends with `VERIFY_OK`.

## References

- D. Micciancio, O. Regev, Worst-Case to Average-Case Reductions Based on
  Gaussian Measures, SIAM J. Comput. 37(1):267-302.
- W. Banaszczyk, New Bounds in Some Transference Theorems in the Geometry
  of Numbers, Math. Ann. 296:625-635; Inequalities for convex bodies and
  polar reciprocal lattices.
- C. Peikert et al., On the Lattice Smoothing Parameter Problem.
- H. Guo et al., New bounds of the smoothing parameter for lattices,
  PLOS One 20(7):e0328688 (2025).
- Z. Zheng et al., Cyclic Lattices, Ideal Lattices and Bounds for the
  Smoothing Parameter (arXiv:2112.13185).
