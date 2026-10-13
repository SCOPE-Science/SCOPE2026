# Self-review

## Correctness — PASS

The assertion concerns exactly a scalar equal-leverage Bernoulli Galerkin sketch and a deterministic correction coefficient. Unbiasedness and strict convexity of the variance quadratic follow from independent Bernoulli moments. Every zero-one mask is genuinely accessible for any finite number of averaged sketches, so a finite affine-vertex minimization is necessary and sufficient, rather than a sampled approximation. Sorting the coefficients gives the complete samplewise positivity interval including the zero and negative boundaries. The variance-optimal support minimum is a one-sided mean deviation. The fixed-cardinality upper bound is attained by endpoint-valued coefficients, and its continuous optimization over the low fraction yields the sharp contrast ratio. Rational squared contrasts attain equality; irrational endpoints are approached by finite populations. The packaged exact-rational verifier succeeds. There is no claim of an infinite proof from finite code.

## Originality — PASS, with specific residual uncertainty

The accessible full 2025 primary paper contains precisely the Bernoulli/control-variate Gram construction, variance weights, and a qualitative concern that correction can make positive-definite sketches singular or ill-conditioned. It suggests scaling a correction, not the exact support-wise coefficient boundary, coefficient-contrast positivity envelope, or finite-averaging impossibility in this scalar class. The 2026 source abstract discusses probabilistic bounds and inverse fusion, not an identifiable support-wise scalar threshold; the full 2026 text was not accessible. Keyword, equivalent-formulation, parameter, and stronger-coverage searches yielded other variance, Bernoulli, and matrix sketching bounds without the combined sharp claim. The elementary ingredients and the general positivity concern are not original. Residual risks: an equivalent result may lie within the inaccessible 2026 full text or older bounded-mean-deviation / positivity-preserving variance-reduction literature; a fresh independent full-text check is warranted. This is not an independence or exhaustive-novelty certificate.

## Value — PASS

The motivating numerical task requires a positive Galerkin Gram matrix to remain invertible. The classification provides the exact damping interval for control-variate corrections and a sharp coefficient-contrast sampling-fraction frontier for a variance-optimal scalar benchmark. It clarifies a practical design distinction that ordinary variance and high-probability invertibility bounds do not settle: repetition suppresses risk probability but never eliminates support-wise loss of positivity. The explicit four-row example shows a negative corrected Gram estimate despite a positive exact Gram. The result is a precise structural guarantee and limitation for the smallest nontrivial sketching setting, not a universal high-dimensional performance claim.

## Literature comparisons and limitations

The 2025 Polydorides et al. paper was read in full, especially its construction and Section III.A, equations (13)–(18), and its discussion of scaling positivity corrections. The 2026 Polydorides et al. arXiv submission was identified and its abstract inspected, but full-text retrieval was unsuccessful. Related randomized sketch and bounded Bernoulli sampling searches did not identify a covering theorem; search failure is not proof of novelty. Oracle weights require the full coefficient mean, and this classification neither proves implementability of an oracle nor gives finite-precision, high-rank, or high-probability guarantees.

Self-review: passed. Independent audit: not yet performed.
