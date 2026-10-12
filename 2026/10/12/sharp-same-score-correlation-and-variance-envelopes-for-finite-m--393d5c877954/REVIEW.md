# Scientific review

## Correctness — PASS

The scope assumes a nonnegative density with real bounded mean-zero orthonormal basis elements, so the displayed transition is a genuine uniform-stationary Markov kernel. Explicitly computing its nilpotent action yields the exact lag covariance as a quadratic form for every centered unit-variance score; conjugation by alternating signs proves the lag matrices have symmetric spectral endpoints. The eigenvectors are themselves legitimate score functions, establishing attainment rather than a loose inequality. Exact finite-sample variances lead to the path-product matrix \(H_N\), and operator-norm convergence gives the long-run matrix \(H\). The trigonometric example meets copula positivity and yields an exact symbolic counterexample to the previously asserted correlation ceiling. The embedded reproducibility code passed 718 checks, including independent quadrature; the universal conclusion rests on the proof, not experiments.

## Originality — PASS, with qualifications

The principal 2026 article explicitly derives scalar lag covariances and the variance of a fixed score, but its asserted sharp upper bound for a common score is strictly false for connected coefficients. The present result instead obtains sharp extrema *over all scores*, for each lag and each sampling horizon, and displays the exact failure using the article's own copula family. The 2025 one-dependent predecessor has no adjacent path interference. The homogeneous path-product matrix belongs to the classical Kac–Murdock–Szegő literature, which is acknowledged rather than reclaimed; the identification with a score-uniform finite-memory copula variance envelope and the contradictory modal example are the claimed contribution. Searches did not disclose an identical specialized correction. Residual risk: other unindexed corrections, or broader operator results specializing immediately to this model, could preempt the claim.

## Value — PASS

This is a complete natural extremal classification of actual autocorrelation and effective sample-mean variability in an explicitly proposed statistical family. The gap is substantive: for \(m=2\) the claimed \(1/8\) ceiling is beaten by the realizable \(\sqrt2/8\), while for longer homogeneous paths the optimal ceiling approaches twice the previously claimed one in relative terms. The covariance and variance intervals have attained endpoints and identify scores that attain best- and worst-case precision; the fixed-score formulas alone do not give these robust inference envelopes. This is more than a sign or normalization check: it replaces an incorrect sharp parameter bound with a full finite-dimensional optimization theorem.

## Remaining limitations

Only one-chain finite-range copulas with square-integrable real scores are covered. Source scalar identities and classical matrix diagonalization are not presented as inventions. No claim of global literature exhaustiveness, independent review or certification is made.

Self-review: passed. Independent audit: not yet performed.
