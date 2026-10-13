# Review of the Gaussian-sketched two-column QR pivot theorem

## Correctness — PASS

The proof identifies the signed eigenvalues of the two-dimensional Gaussian covariance quadratic form and then combines independent sketch rows into independent chi-square random variables with exactly \(d\) degrees of freedom. Their normalized ratio has the beta distribution, including the parallel-column boundary. The Gram eigenvalue formula establishes strict conditioning monotonicity against the strict risk monotonicity. Endpoint Laplace analysis and Stirling supply the precise asymptotic coefficient. The enclosed verifier replays exact fractions and additional simulations, which are not substitutes for this analytic proof.

## Originality — PASS, with risks

The closest defining source is CQRRPT (arXiv:2311.08316), whose Gaussian sketched QR stage is exactly the object considered. Earlier randomized QRCP papers (arXiv:1509.06820 and arXiv:1804.05138) use the same Gaussian sketch primitive, derive marginal length or probability bounds, and analyze pivot selection, but the inspected full-text sections do not derive this *joint correlated two-column* equality law or the inverse trend with conditioning. This is a statement/implication comparison, not a title comparison. Specialized unindexed probability or QR literature could contain equivalent results. Prior generic Gaussian and beta identities are credited, not described as novel.

## Value — PASS

The theorem supplies an exact first-pivot risk and a sharp sketch-size asymptotic for a natural randomized numerical linear algebra operation, and it exhibits a strict mismatch between spectral condition number and wrong-column probability. It has direct parameter and example interpretation without pretending to characterize full QR reliability. The result is limited to a two-column initial pivot in exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
