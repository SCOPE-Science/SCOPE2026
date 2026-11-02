# Scientific review

## Correctness — PASS

The source-defined normalized Gaussian weights and unbiased local covariance denominator reduce algebraically to the two explicit covariance expressions in `RESULT.md`. All denominators are positive on the stated open interval. The resulting relaxed hyperbolic-tangent map has relaxation factor strictly between zero and one. Strict concavity and monotonicity give every fixed point and basin, while Taylor expansion and telescoping inverse squares give the exact critical limit. The branch asymptotics follow from the inverse hyperbolic tangent. The independent full-weight formula was compared numerically with the reduction on a parameter grid, and the extracted verifier completes 2,095 checks; these are supplementary to the proof, not infinite certificates.

## Originality — PASS (qualified)

The primary PEKI text arXiv:2610.31907v1 defines the target method, proves cross-cluster suppression and linear-case contraction, and acknowledges spurious clusters in a separate experiment, but does not state this exact nonlinear three-particle finite-ridge phase diagram or its critical time scale. The important prior arXiv:2402.00027v3 supplies a weighted-ensemble ODE; the stationary hyperbolic-tangent equation is compatible with that more general covariance framework and is not claimed as an independently new scalar fixed-point theorem. The exact discrete-time PEKI map, global attraction proof, nonzero observation-residual branch, and critical iterate asymptotics were not located in inspected primary texts or indexed comparison results. General nonlinear EKI analyses could imply an equivalent specialization and remain a priority risk; independent historical audit is outstanding.

## Mathematical value — PASS

The classification gives a sharp boundary \(\kappa=a\) where a supposedly mode-resolving localized inverse solver changes from one to three possible stationary middle-particle states, with all such states still data-inconsistent. It quantifies the residual floor and critical slowdown at an exactly reproducible, minimal multimodal benchmark. This is useful for testing radius-selection and convergence diagnostics: observing three separated groups of particles is not alone evidence that every group solves the observation equation. Its narrow ensemble assumptions and fixed deterministic ridge are explicitly declared and preclude claims about general finite-horizon stochastic performance.

## Related science and remaining limitations

Yang–Wu 2026 (arXiv:2610.31907v1) gives the original update and motivating multicluster behavior. Wacker 2024/2025 (arXiv:2402.00027v3) is the closest conceptual antecedent for local weighted covariance and explicitly differs by considering a continuous-time ODE without the same positive-ridge discrete gain. Tong–Morzfeld (arXiv:2201.10821) studies localization and convergence in another setting. The scalar hyperbolic-tangent bifurcation is classical; novelty is claimed only for its exact appearance and consequences in this PEKI specialization. Only accessible records and inspected sources inform priority; absolute historical uniqueness is not established.

Self-review: passed. Independent audit: not yet performed.
