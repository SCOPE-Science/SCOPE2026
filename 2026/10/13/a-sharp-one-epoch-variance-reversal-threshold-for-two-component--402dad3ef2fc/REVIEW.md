# Self-review

## Correctness — PASS
The deterministic component maps \(T_i(x)=(1-\eta\lambda_i)x-\eta c s_i\) give exactly four possible final iterates. Their two different sampling weights lead to the stated identity by an explicit polynomial subtraction, without approximation. In the equal-curvature case, both sampling schemes share the same propagated initial point, and the two noise variances differ by exactly \(2\eta^2c^2(\eta L-1)\). The sharp uniform cutoff follows from the sum of the two curvatures, with an equal-curvature witness. The rational checker replayed directly from the packaged `verify.py` also examines varying starting points. Limits: only two updates in one dimension; experiments do not prove universal identities.

## Originality — PASS, with residual risk
Focused searches for two-component scalar quadratic shuffling, variance reversal, large steps, and with/without replacement located relevant but mathematically different results. Liu (2026) compares worst-case averaged-iterate rate bounds and studies a different two-component construction in its appendix. De Sa (2020) establishes other counterexamples, including noiseless multi-dimensional long-run phenomena. Domingo-Enrich (2022) studies mainly stationary variance under a stochastic-noise model, not a complete exact one-epoch parameter frontier. These results give vital context but no inspected theorem directly implies the exact formula or its sharp all-initialization threshold. An unindexed, elementary equivalent calculation could remain undiscovered; no exhaustiveness or human originality certification is claimed.

## Value — PASS
The frontier separates an algorithm-independent per-component stability range from the much smaller range in which RR is guaranteed not to underperform iid sampling **instancewise after one epoch** within a natural minimal noise-bearing quadratic class. The reversal persists for every starting point when curvatures agree, so it is not an isolated exact-initialization artifact. It also clarifies why rate-bound superiority must not be read as exact single-instance superiority. No convergence-rate improvement, dominance of all data distributions, or long-run conclusion is claimed.

## Sources and risks
Original rate paper: https://arxiv.org/abs/2606.32005 ; extended version: https://optimization-online.org/wp-content/uploads/2026/09/Random-Reshuffling-for-Smooth-Convex-Optimization.pdf . Related negative example: https://proceedings.neurips.cc/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf . Related stationary-noise analysis: https://arxiv.org/abs/2206.00632 . Principal residual risk is earlier equivalent finite-horizon computations not indexed by these search phrases. Independent audit is not yet performed.

Self-review: passed. Independent audit: not yet performed.
