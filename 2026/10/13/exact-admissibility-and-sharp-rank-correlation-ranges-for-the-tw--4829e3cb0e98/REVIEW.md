# Review of the exact two-mode Legendre-copula admissibility theorem

## Correctness — PASS

The continuous polynomial has the required copula margins identically. Its nonnegativity reduces to the explicit infimum of \((1+bP_2(s)P_2(t))/(st)\). The ratio reduction through \(w=st\) and \(R=s/t+t/s\) correctly handles both signs of \(b\), both endpoint axes, and the exceptional \(b=2\) infimum. The rank correlations are independently derived from the defining integrals, and their stationary-point optimizations are global on the compact admissible region. The standard-library verifier reproduces six exact two-parameter interpolation nodes and 33,371 deterministic probes. This is a human-checkable analytic proof, not an inference from finite experiments.

## Originality — PASS with residual bibliographic risk

The defining formula and original coefficient sufficient condition appear in Longla, arXiv:2308.11074v1, equation (25). The revised preprint and 2024 journal article give the same sufficient domain, not the exact non-polyhedral one. Longla–Hamadou's 2025 statistical analysis of this exact density expands the coefficient region only to a linear subregion still requiring \(|\lambda_1|\le1/3\), whereas the exact region proved here reaches \(1/\sqrt3\). The 2025 multivariate extension uses a sufficient sum-of-absolute-coefficients bound; a 2026 paper concerns non-diagonal cross-mode kernels. Searches for exact nonlinear positivity boundaries, sharp Spearman/Kendall limits, FGM aliases and published result records did not surface an equivalent or dominating result. The known generic positivity criterion alone is not the evaluated optimal region. Earlier algebraically equivalent parameterizations remain a possible priority risk; no independent bibliographic audit has taken place.

The direct Kendall integral in the proof is \(\frac{2\lambda_1}{3}(1+\lambda_2/5)\); equation (26) printed in the 2023/2024 source displays a different factor. The present computation uses the polynomial definition directly, not the displayed formula. The six exact interpolation checks reproduce the direct integral without importing that expression.

## Value — PASS

The admissible set is the natural unresolved parameter domain of a named, applied dependence model: a necessary-and-sufficient classification is needed to distinguish genuine copulas from choices rejected merely by conservative sufficient tests. The curved boundary gives new valid coefficients and exact dependence ranges, including a strictly larger attainable Spearman magnitude than the FGM threshold. The exact Kendall extremum and its distinct optimizer reveal a structural difference between dependence measures. This supplies a usable full two-parameter classification rather than a routine isolated parameter evaluation. It does not address additional modes, statistical estimators, or general copula classes.

Self-review: passed. Independent audit: not yet performed.
