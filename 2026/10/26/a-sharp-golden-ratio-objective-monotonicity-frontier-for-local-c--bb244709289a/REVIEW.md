# Self-review

## Correctness — PASS

The analyzed step is the square-root LCD3 metric-projection update in the primary source, not the standard Polyak update. The curvature assumptions are satisfied because \(C\preceq I\preceq C+(1-\kappa^{-1})I\). In the eigenbasis of \(B=C^{-1}\), direct expansion gives the objective ratio \(1-2\alpha m_1+\alpha^2m_2\). The pointwise chord bound \(\lambda^2\le(\kappa+1)\lambda-\kappa\) yields an attainable upper envelope; maximizing the one-dimensional rational function gives the unique interior optimizer \(\varphi^{-1}\) and the claimed phase transition. A two-eigendirection witness attains the sharp bound for every \(\kappa\). The scalar algebra and numerical witnesses were separately cross-checked with the package's verifier. This proves the universal one-step statement; finite tests do not prove any infinite-time claim, and none is made.

## Originality — PASS (best-knowledge comparison)

Primary full-text inspection included the original LCD3 definition, its derivation, and the quadratic appendix in arXiv:2405.16574v1, and the corresponding sections and Appendix D.2 in the final 2025 proceedings version. The originals give a one-step Newton identity only when the curvature matrix equals the Hessian; they explicitly leave general LCD3 convergence untreated. That theorem does **not** cover anisotropic strict curvature lower bounds or the exact worst-direction function \(M(\kappa)\). Preconditioned stochastic Polyak [3] and published exact bounds for *scaled Polyak* iterations use a different update; neither supplies the nonlinear LCD3 square-root envelope. Searches included the original algorithm name and metric/ellipsoid aliases, spectral thresholds, and the golden-ratio value. No directly covering result was identified; searching cannot prove uniqueness. Remaining risk: an older ellipsoid-projection or normalized metric descent result equivalent to this one-step law.

## Value — PASS

The original LCD3 paper lacks a general convergence theorem; a sharp criterion for whether *one step increases the very objective being minimized* is a motivated boundary and not an arbitrary coordinate slice. The theorem is dimension-independent, quantifies exact worst amplification, supplies extremizers and a sharp universal threshold, and isolates a real algorithmic difference from LCD2's Euclidean metric. The object is deliberately simple so the observed energy increase cannot be blamed on a poorly conditioned objective: the objective Hessian is the identity. One-step overshoot is not mistaken for global divergence.

## Limits and independent status

Only the specified normalized constant-curvature, exact-arithmetic, isotropic quadratic setting is classified. Residual novelty risks require independent scrutiny, and universal convergence or nonconvergence is not claimed.

Self-review: passed. Independent audit: not yet performed.
