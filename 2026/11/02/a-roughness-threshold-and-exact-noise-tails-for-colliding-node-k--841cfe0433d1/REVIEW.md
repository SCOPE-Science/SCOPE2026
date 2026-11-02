# Scientific review

## Correctness — PASS

All quantities, expectations, kernel mean, original-versus-nugget weights and independent observations are explicitly defined in `RESULT.md`. Exact diagonalization proves the weight formulas, and uniform collision expansions of the continuously differentiable kernel mean produce a reciprocal-power noise coefficient. The Gaussian tail integral establishes both one-sided limits with the stated \(\Gamma\)-constant; layer-cake integration establishes the endpoint moment divergence. A local rescaling of the positive collision-distance integral proves the \(\alpha=3/2\) logarithmic transition and the all-\(\alpha\) beta-integral coefficients. Conditional noise variance establishes the exact threshold for finite second moments. Direct numerical integration reproduced the critical and supercritical constants; 109 deterministic script checks passed. The numerical checks corroborate but do not prove the quantified claims.

## Originality — PASS, with residual priority risk

The motivating 2023 Nyström/kernel-quadrature study treats broader random sampling and convex subspace constructions; the 2018 weight-magnitude paper gives separation-sensitive general bounds. Neither of the inspected relevant sections gives the sharp iid two-node, noise-induced, **all-roughness** \(\alpha=3/2\) threshold, its logarithmic ridge coefficient, or the full tail-power family. A prior isolated \(\alpha=2\) Gaussian result already contains the Cauchy tail and square-root nugget coefficient: those statements are **explicitly not claimed new** and cannot imply a nontrivial phase boundary at \(\alpha=3/2\). The new theorem is the full regularity-dependent classification and its critical law. Search did not prove absolute novelty, and earlier specialized probabilistic-kernel numerical analysis may overlap.

## Value — PASS

Kernel quadrature weight magnitudes control robustness under noisy evaluations, and iid nodes can collide without being deliberately selected. A complete quantitative phase diagram shows exactly when ordinary data noise makes mean-squared quadrature error infinite and when adding a nugget incurs logarithmic versus power-law amplification. This gives a meaningful, reproducible regularity-dependent stability benchmark rather than a generic two-by-two formula or arbitrary numerical instance. The critical exponent and endpoint law do not follow from the previously available single Gaussian point.

## Closest literature and scientific limits

Closest sources are Hayakawa–Oberhauser–Lyons, arXiv:2301.09517; Karvonen–Kanagawa–Särkkä, arXiv:1812.08509; and Briol et al., arXiv:1706.03369. The proof is exact only for two independent uniform points, exact kernel means and Gaussian errors. It does not establish optimal regularization, general-node asymptotics or universal publication priority. A complete independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
