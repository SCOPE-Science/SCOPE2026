# Self-review

## Correctness — PASS

The three equiangular unit rows satisfy \(U^\mathsf T U=3I/2\) and have an all-ones left nullvector, so every fixed right-hand side has the same scalar residual \(\delta\) after least-squares centering. The affine row-action maps have cross terms that cancel after either IID sampling or uniform permutation averaging. Exact six-permutation matrix moments yield \(c_R\), \(d_R\); the IID one-step moment yields \(c_I\), \(d_I\). The positive change of variables \(t=\eta/(2-\eta)\) verifies sign uniqueness of the one-epoch quartic and positivity of the stationary denominator. The stationary threshold is the sole positive root of a strictly increasing cubic, and the epoch-count ordering follows from a monotone ratio of geometric factors. The rational \(\eta=6/5\) witness is checked directly. The embedded script recomputes exact symbolic moments and finite enumerations; it is not a substitute for the analytic proof. The scope excludes independent rowwise perturbations resampled at each visit.

## Originality — PASS, with residual risk

Gan–Wu (arXiv:2608.22259) studies noisy randomized row methods with IID sampling and general upper bounds, not the exact reshuffling-vs-IID error-ordering transitions. Han–Xie (arXiv:2410.01140) gives RRK convergence under consistency and hence has no nonzero affine fixed-residual forcing. Recht–Ré (arXiv:1202.4184) analyzes noncommutative sampling and noisy stochastic gradient variants, but its displayed comparison uses independent row noises, not the fixed all-ones inconsistency residual here. Ferreira–Acebrón–Monteiro (2024 survey) describes fresh shuffles without a closed exact noisy two-threshold classification, and Epperly–Goldshlager–Webber (arXiv:2411.19877) changes the estimator to tail averaging. A preprint on power-spectral analysis of shuffled stochastic gradients (arXiv:2206.00632) was located but its full text could not be read in this inspection, leaving an explicit residual possibility of a reparameterized antecedent. The original contribution claimed is the paired sharp threshold classification and finite-to-stationary reversal for this entire fixed-right-hand-side frame, not the general finite-population matrix-product formula.

## Value — PASS

The frame is a natural smallest noncommuting overdetermined row system, with exact least-squares residual mode and normal-matrix condition number one. Distinct roots of the noise-injection and stationary equations show that comparing a single pass and comparing limiting error floors are genuinely different optimization decisions; in between them the relative ranking reverses in time, without poor conditioning or nonuniform row selection. The conclusion is narrowly scoped but fully classifies this baseline and identifies a concrete boundary for transferring sampling claims between noisy and homogeneous methods.

## Limitations and literature risk

The threshold and first-to-later-epoch reversal are not universal outside this model. Literature searches cannot prove historical uniqueness; older matrix-product or shuffled-gradient calculations might contain an equivalent reparameterization. Verification does not constitute independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
