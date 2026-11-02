# Scientific review

## Correctness — PASS

The proof reconstructs unique interpolation-quadrature weights from the three moment equations and derives the strictly positive denominator from the positive circular gaps. The three bad-gap events are disjoint, so their probabilities add. The almost-sure endpoint singularities arise only at three two-coordinate collision corners, where the paired weights have opposite leading terms proportional to the reciprocal gap. The corner is two-dimensional; integrability is exactly for moments of order less than two. The logarithmic second-moment coefficient follows by integrating the reciprocal squared gap and then \(\tan^2(\pi z/3)\); the subleading terms remain uniformly integrable. The packaged symbolic/numeric verifier passed 251 checks, independently of the analytic general proof.

## Originality — PASS, qualified

The most closely related inspected scientific treatment is Yu–Townsend, arXiv:2202.04722, Section 4 and Appendix B. It analyzes deterministic envelopes and sufficiently large-rule negative weights, not the exact independent-jitter probability for three nodes or its squared-weight moment barrier. The earlier Austin–Trefethen arXiv:1612.04018 establishes smooth-integrand convergence on increasingly fine perturbed periodic grids, not the stated random finite-grid law. Karvonen–Kanagawa–Särkkä (2019) addresses a distinct kernel-based Bayesian quadrature model. Closely related polynomial three-node random-quadrature laws involve a different interpolation space and a different perturbation distribution, and neither imply these sign events or their logarithmic coefficient. The unresolved risk is older or specialized small-grid trigonometric sampling literature; one source main text was not readable beyond its abstract and appendix. Search failure alone is not treated as priority certification.

## Value — PASS

The published large-grid trigonometric quadrature literature makes the finite-node sign and noise behavior a motivated question. The result supplies a complete sharp smallest-grid classification with two distinct natural thresholds, including a universal exact coefficient governing the onset of infinite expected noise variance. No generalization beyond three uniform-jittered nodes is claimed.

## Limitations and comparison boundary

The random jitters must be independent and uniform; the rule is exact for the three trigonometric basis functions, and the moment criterion concerns the exact weights. The proof gives no larger-grid, arbitrary-distribution, or finite-precision guarantee. The scientific record has not been independently audited. An accessible full-text read of the first public 2016 main journal paper was not available, although its abstract and attached detailed supplementary proof were inspected.

Self-review: passed. Independent audit: not yet performed.
