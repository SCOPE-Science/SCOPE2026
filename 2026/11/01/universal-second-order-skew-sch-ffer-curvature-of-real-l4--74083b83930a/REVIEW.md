# Scientific review: universal quadratic skew-Schäffer curvature

## Correctness
The proof works for every real \(L_4\) space containing two disjoint unit functions. The exact quartic-square identity (2) provides the global first-order deficit, and its three moment consequences force the second-variation coefficient \(5/4\) near every first-order optimizer. The full third derivative of the squared \(L_4\) norm is uniformly controlled away from zero; every relevant segment remains uniformly bounded away from zero. The lower bound for the arithmetic mean, including its squared norm-difference correction, is explicit. The upper construction has equal output norms for every parameter and works for every power mean. The resulting coefficient for the radius is \(9/16\), with a uniform cubic remainder. `verify.py` supplies 12,828 finite checks; the proof does not rely on extrapolation from them.

## Originality
The closest source is Xu–Liu, *Skew Schäffer Type Constants* (arXiv:2610.03050v1, 2026-10-02). It proves the matched-exponent \(L_p\) formula, particularly the outer quartic mean for real \(L_4\), but not a matching lower bound for the arithmetic mean. A previous published result on infinitesimal skew radii (identifier 88548343e0a2, full available statement and proof inspected) covers common first derivatives for finite outer exponents but no second-order term and no maximum-mean endpoint curvature. Another previous result (identifier 7a18ef79086d, full statement and proof inspected) computes a **supremal** arithmetic-mean invariant, not the infimal one. Search comparisons targeted the exact \(9/16\) coefficient, all-exponent second variation, duality asymmetry, and the quartic-square identity. No source inspected covers the new common second-order coefficient across all outer exponents. Residual risk: an older unindexed or differently formulated two-point inequality might imply the result.

## Mathematical value
This is a complete local curvature determination for the entire natural power-mean family on a classical non-Hilbert space. It advances beyond a known first-order slope and beyond the exact matched-exponent case. The crucial structure is an exact positive quartic defect that controls the second variation of *all* asymptotically minimizing pairs; the arithmetic-mean estimate then proves uniformity even at the endpoint where the ordinary mean is least favorable. The quantified separation between the leading and cubic terms may support stability and extrapolation of other skew radii.

## Limitations
The analysis does not determine the full positive-parameter profile, assert an optimal third-order coefficient, or establish a complex-space analogue. Absolute publication priority is not certified. Numerical checks are supplementary and no independent mathematical audit has been completed.

Self-review: passed. Independent audit: not yet performed.
