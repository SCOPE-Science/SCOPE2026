# Scientific review

## Correctness — PASS

The result concerns the literal positive Gauss–Legendre approximation to the process-noise integral in Bosch–Hennig–Tronarp (arXiv:2305.14978, Section 3.2), applied to the paper's noiseless EKL update and deterministic initial covariance (Appendix B). The impulse response \(v(s)\) satisfies \(Hv(s)=1\). Conditioning therefore turns the process-noise approximation into the exact weighted variance of \((1-e^{-as})/a\). This proves the one-node zero, strict two-node positivity, analytic covariance formula, and the fixed-node stiff asymptotic. A direct one-step forced-ODE calculation proves strictly positive mean error with zero covariance. The repeated-mesh statement is a rank-one Gaussian-conditioning induction. The included script checks 2,886 finite cases; finite tests are not treated as infinite proofs.

## Originality — PASS (best-knowledge comparison)

The source paper's Section 3.2 specifies \(m=q\) Gauss–Legendre nodes and Appendix B proves identities for the **exact covariance**. Neither its relevant full-text statements nor appendices were found to contain the conditioned weighted-variance law, the exact collapse for \(q=m=1\), the forced-ODE false-zero-uncertainty example, or the exponentially deficient stiff limit for every fixed Gauss node count. Schmidt–Hennig–Nick–Tronarp (arXiv:2306.07774) discuss general overconfidence from deliberate low-rank filtering, which does not give these method-specific formulas; Tronarp et al. (arXiv:1810.03440) give the general filtering model. Related published mathematical findings about Langevin covariance, sensor OU modes and general filtering do not imply this specific claim. Exact and alias searches did not locate a covering theorem. There remains a risk of a published equivalent in numerical covariance quadrature or low-rank Kalman theory; a failed search is not proof of world-first novelty.

## Mathematical value — PASS

The result identifies a design-critical mechanism, not merely a rank count: a publicly described process-noise approximation can eliminate **all** reported mesh uncertainty on an ODE with a rigorously nonzero error. The analysis supplies the sharp minimum node count for nonzero one-step variance, its exact formula for two nodes, and a second failure regime—exponentially wrong fixed-order uncertainty in stiff dynamics despite positive variance. These are directly relevant to covariance quadrature and uncertainty-aware stiff integration. The finding does not claim a full convergence or calibration theorem and does not assess altered implementations.

## Closest sources and residual scope

Primary: Bosch–Hennig–Tronarp, arXiv:2305.14978 (Sections 2.3, 3.2–3.4, Appendix B). Related: Schmidt–Hennig–Nick–Tronarp, arXiv:2306.07774 (Sections 2–5); Tronarp–Kersting–Särkkä–Hennig, arXiv:1810.03440. The proof assumes positive \(h,a,\kappa\), initially exact state, noiseless EKL observation, and the mathematically specified quadrature covariance. Independent publication-priority checking and practical implementation testing remain outstanding.

Self-review: passed. Independent audit: not yet performed.
