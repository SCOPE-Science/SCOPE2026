# Self-review

**Correctness — PASS.** The Jury stability test, stationary covariance identity, strict endpoint reduction, and two single-mode derivative signs prove the exact, unique median selector for all \(0<a\le b<4\). The positive-noise and boundary cases are addressed. The factor-two negative-momentum advantage follows from an exact expression, not a regression or finite experiment. Standalone checks compare direct discrete Lyapunov covariance and scalar global optimization against the formulas. These tests do not replace the general proof.

**Originality — PASS with residual risk.** Flammarion–Bach (2015) supplies archival stochastic second-order background. Mohammadi–Razaviyayn–Jovanović (2019) already derive modal stationary variance for heavy-ball; their 2022 Theorem 5 and Lemma 4 give general two-step noise amplification and an adjustable-step endpoint-equalizing family. The known variance formula, stability test, and endpoint equalization are excluded from novelty. The assessed addition is the complete unique fixed-step signed-momentum minimax decision, its two nonequalizing regimes, and a sharp twofold sign-restriction loss. An unindexed specialization or derivation implicit in wider design literature remains possible; the search cannot prove universal uniqueness.

**Value — PASS.** A natural robust stochastic control problem is solved for all positive curvature intervals and all nonzero fixed stepsizes in the stable range. Its three allocation regimes and sharp asymptotic gap give quantitative tuning guidance absent from a bare covariance formula. It neither asserts optimal trace variance for a fixed finite Hessian nor rate optimality.

**Sources and limitations.** arXiv:1504.01577 (2015), arXiv:1905.11011 (2019), arXiv:2209.11920 (2022). The user of this result must distinguish an unknown spectral interval from a known full eigenspectrum and fixed stepsize from jointly optimized parameters. Independent validation is pending.

Self-review: passed. Independent audit: not yet performed.
