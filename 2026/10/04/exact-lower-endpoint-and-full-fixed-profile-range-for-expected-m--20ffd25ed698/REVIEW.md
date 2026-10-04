# Review

## Correctness

PASS. The maximum probabilities are
\[
w_i=P_i^n-P_{i-1}^n,
\]
so the normalized maximum gap is the weighted covariance between the support
and the increasing score \(w_i/p_i\). Every centered increasing support is an
exact positive combination of centered threshold vectors. On each threshold
ray, the covariance-to-norm ratio is exactly
\[
\frac{P_j-P_j^n}{\sqrt{P_j(1-P_j)}}.
\]
The triangle inequality therefore gives the lower bound. Strictness for at
least three distinct atoms and sharpness by a two-level collapse are both
proved from the same decomposition. Connectedness of positive gap ratios
fills the interval up to the projection upper endpoint.

## Originality

PASS, with an explicit residual access risk. The accessible 1998
López-Blázquez material is the closest source and clearly formulates the
discrete **upper** expected-maximum optimization under moment constraints.
The full article was not available for inspection, so no whole-document
noncoverage claim is made.

A complete full-text treatment of expected-maxima sequences was inspected.
It develops characterization and discrete-uniform approximation machinery,
but not a profile-fixed lower support extremum. The later finite-population
without-replacement paper has different sampling and weighting constraints.

Targeted statement-level searches for a lower standardized maximum with
prescribed atom masses, two-level cut extremizers, and complete fixed-profile
ranges did not locate a stronger or equivalent result.

## Value

PASS. Upper bounds for expected maxima are classical, but fixing the discrete
mass profile creates a complementary geometric question: how close can the
sample maximum remain to the parent mean after variance normalization? The
answer is a finite, explicit cut functional, with a complete closure
classification and full attainable interval. It distinguishes support
geometry from mass geometry and is directly computable for any prescribed
discrete law profile.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK identity_checks=48000 decomposition_checks=16000 lower_checks=16000 upper_checks=16000 upper_equality_checks=16000 two_point_checks=152 boundary_checks=12000`.
