# Scientific review

## Correctness — PASS

The full-residual-span embedding makes the sketch injective on the relevant subspace. Exact sketched minimization forces the new sketched residual orthogonal to the old-to-new change. The induced true metric has eigenvalues in the reciprocal squared-distortion interval, and a complete two-eigenvalue minimax computes the precise envelope. An explicit two-dimensional family attains it for every positive measured improvement; the zero-improvement and zero-sketch-optimum endpoints are treated separately. The exact rational witness and standalone verification script agree with the analytical identities. Experiments do not replace proof.

## Originality — PASS, residual risk stated

The closest direct theorem, Sabaté Landman–Nakatsukasa, arXiv:2510.11237v1, Proposition 1, requires relative sketched improvement at least \(2\varepsilon/(1-\varepsilon)\) for monotonicity. The present optimal threshold \(4\varepsilon^2/(1-\varepsilon^2)\), quantitative envelope, and exact counterexamples are not implied by that sufficient condition. Its Proposition 2 instead concerns minimizing the true quadratic. Epperly–Webber (arXiv:2605.19096v2) treats distributional final error, Nakatsukasa–Tropp (arXiv:2111.00113v2) gives quasi-optimality, and Pilanci–Wainwright (JMLR 2016) gives statistical and iterative-sketch bounds; none of their examined results supplies the measured-decrease frontier. Published mathematical-finding searches did not reveal a dominating formulation, but an older unindexed spectral-equivalence lemma remains possible. This assessment is not an independence or exhaustive novelty certificate.

## Value — PASS

The source identifies the existing sufficient acceptance condition as often too stringent and discusses restarts or sketch refinement. The exact quadratic-in-distortion criterion addresses that concrete mathematical and algorithmic gap, substantially enlarging the acceptance region for small distortion and describing worst-case failure with sharp counterexamples. Unlike a mere normalization check or table recomputation, it establishes a complete optimal decision frontier for an observed sketched minimizer. Conditional use for tangent majorants follows only under explicit majorization assumptions.

## Limits and closest literature

The claim is exact arithmetic, deterministic conditional on an embedding, with fixed affine space and exact sketched minimization; probabilistic and nonlinear convergence consequences require extra hypotheses. Closest direct literature: arXiv:2510.11237v1, Proposition 1; related residual analyses: arXiv:2605.19096v2, arXiv:2111.00113v2 and Pilanci–Wainwright (JMLR 2016).

Self-review: passed. Independent audit: not yet performed.
