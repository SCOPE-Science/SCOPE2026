# Scientific review: largest uniform spacing and Greenwood statistic

## Correctness — PASS
For every integer \(n\ge2\), the finite Dirichlet-simplex inclusion-exclusion argument gives the displayed mixed moment. Its beta integrals and alternating-binomial identities were reconstructed, the marginal second moments and variance formulas checked, and strict positivity follows from \((H_n-1)^2+H_n^{(2)}-1>0\). The asymptotic rate follows from harmonic asymptotics. The standalone exact-rational checker independently confirms the moment identity for \(2\le n\le80\) and direct simplex integration for \(n=2,3\). Finite checks supplement, rather than replace, the proof.

## Originality — PASS, with residual priority risk
The full available articles by Shtembari and Caldwell (arXiv:2008.02048), Singh and Misra (arXiv:2110.10737), and Eller and Shtembari (arXiv:2111.02252) treat ordered-spacing marginal/sum distributions or tests but not the precise mixed moment and sharp correlation formula. Database searches across uniform spacings, the Dirichlet simplex, Greenwood statistics, and equivalent exponential normalizations did not return the same theorem. A related published exponential-range/sample-variance covariance concerns unnormalized, different variables and does not itself imply the result. The 2021 Greenwood stochastic-dominance paper was not inspectable in full, so hidden prior coverage cannot be excluded; failed searches are not novelty proofs.

## Value — PASS
The largest-gap statistic responds to a single long empty interval, while Greenwood's sum responds to total spacing concentration; both are standard goodness-of-fit diagnostics. Their exact finite-sample dependence matters when combining or comparing such diagnostics under the same null. The theorem supplies the otherwise missing mixed moment, strict sign at all finite sample sizes, and an unexpectedly slow but vanishing asymptotic correlation, rather than an arbitrary finite numerical invariant.

## Scientific limitations
No claim is made for general Dirichlet shapes, irregular sampling, complete joint distributions, asymptotic independence, or statistical optimality of a combined test. Older literature may contain the exact formula or a more general identity. Separate independent mathematical and priority review is outstanding.

Self-review: passed. Independent audit: not yet performed.
