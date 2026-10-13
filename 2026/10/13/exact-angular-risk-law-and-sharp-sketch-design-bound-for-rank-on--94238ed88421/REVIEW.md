# Review: Exact angular risk law and sharp sketch-design bound for rank-one Nyström

## Correctness — PASS
The exact rank-one residual factorization in `RESULT.md` fixes the Frobenius/trace/operator normalization. The Gaussian direction has the real arcsine law, and its integral gives the stated complete error distribution, exact first/second moments, and moment thresholds. At the critical half-order the logarithmic coefficient is \(1/\pi\); for larger orders the rescaled beta integral gives the full constant. Jensen's inequality yields the extremal isotropic directional law with the correct equality condition, except at the explicitly excluded degenerate contrast \(\kappa=1\). The standalone rational and quadrature checks passed. Proofs are analytic rather than extrapolations from finite tests.

## Originality — PASS (residual literature risk)
Persson--Boullé--Kressner (arXiv:2404.00960) analyze Gaussian Nyström approximation in broader dimensions but their expectation bounds require positive oversampling and target rank at least two. Tropp--Yurtsever--Udell--Cevher (arXiv:1706.05736) provide the deterministic projection mechanism but require strictly more sketch columns than the approximation rank for the main relative guarantees. Carson--Daužickaitė (arXiv:2205.13355) study finite-precision single-pass Nyström rather than exact angular distributions. Searches for equivalent Schur-complement, beta, Gaussian, sign-sketch, and exact two-eigenvalue formulations did not uncover prior coverage of the **combined one-column distribution, all-moment asymptotics and isotropic equality law**. A specialized unindexed derivation remains possible; uniqueness of provenance is not claimed.

## Value — PASS
One Nyström probe is the least expensive nonzero-rank setting and is a meaningful edge case excluded by oversampling theorems. The precise \(\kappa^{3/2}\) mean-square deterioration and the sharp half-moment cutoff explain rare-direction risk not visible from typical finite trials. The complete isotropic directional equality theorem supplies a mathematically motivated sketch-distribution benchmark and shows why an eigenbasis-aligned sign sketch has bounded relative squared-error risk. The result has concrete dimensional and orientation limitations; it is not a general claim about Rademacher superiority under arbitrary rotations.

## Sources and boundaries
The three primary sources are listed in `RESULT.md`. Their relevant full-text constructions, theorem hypotheses, and proofs were compared directly. The remaining uncertainty is unindexed specialized literature; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
