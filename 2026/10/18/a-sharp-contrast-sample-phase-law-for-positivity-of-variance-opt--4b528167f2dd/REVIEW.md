# Self-review

## Correctness — PASS

The claim is limited to an explicitly specified real orthonormal-column design, positive diagonal parameter matrix, and independent fair Bernoulli sketches. Reconstructing the two orthogonal projector components gives the exact eigenvalues of the raw and corrected sketches. Independence yields two binomial counts and all stated probabilities; the extreme count gives both strict all-realizations positivity frontiers. Directly computing the two Frobenius variances and comparing the variance-ratio ridge with the extremal eigenvalue gives the sharp ridge crossover. Standard binomial central-limit and large-deviation theorems supply the stated asymptotics. The independently executable exact-arithmetic checker reproduced the spectra and finite-state probability identities. It has no role as an infinite proof.

## Originality — PASS, with a material access limitation

The 2025 Polydorides–Noori–Vandierendonck–Woods source (DOI 10.1109/SSP64130.2025.11073388), examined in its accessible accepted manuscript, **already states that control-variate correction can cause singularity or ill-conditioning**, and supplies the exact entrywise optimal control-weight formula. Both facts are prior art, not new contributions. The claim assessed here is the exact four-row positive-definiteness threshold, all-sketch binomial law, contrast-versus-repetition normal transition, and exact fusion/ridge calibration obstruction. Neither the inspected equations and discussion of that predecessor nor accessible source summaries supply those quantitative statements. Generic covariance positive-definiteness repair results do not imply the specific Bernoulli selection law.

The June 2026 continuation was publicly indexed, but its complete primary text could not be inspected; only its abstract and a detailed secondary mathematical account were accessible. Therefore its unseen results or appendices, and unindexed related literature, remain genuine overlap risks. Searches of accessible mathematical records did not identify a dominating implication. This is a best-knowledge comparison, not a uniqueness certificate.

## Value — PASS

The question is intrinsic to randomized finite-element reduced-matrix assembly: an estimator optimized separately for entrywise variance need not remain in the positive-definite cone required for stable inversion or certain inverse-loss formulations. The theorem quantifies the risk despite strict variance reduction, gives a natural condition-number threshold and a square-root sample-count scale, and derives an exact failure boundary for a natural fused inverse matrix. These are actionable structural diagnostics beyond the general qualitative warning of prior work.

## Scientific limitations and residual risk

The model uses exactly two spectral directions, four equal-leverage rows, diagonal coefficients in two groups, and population-optimal control weights. Empirically estimated weights, truncation of weak correlations, positivity-preserving line search, coefficient-specific leverage sampling, and other fusion objectives are outside scope. The 2026 motivating preprint's full text remains uninspected. The proof is analytical, but independent validation was not performed.

Self-review: passed. Independent audit: not yet performed.
