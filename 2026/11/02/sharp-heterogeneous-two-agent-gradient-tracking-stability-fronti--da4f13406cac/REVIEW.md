# Self-review

**Correctness — PASS.** The source-derived three-dimensional reduced matrix yields the displayed cubic characteristic polynomial. The proof applies every strict cubic Schur–Jury inequality: the \(-1\) polynomial evaluation gives the first threshold, a globally positive residual Jury expression proves sufficiency before that threshold, and the sign of \(-P(-1)\) plus the constant term rules out every larger stepsize. The argument covers all real \(0<s<1\), \(0\le\eta<1\), and positive steps; the 13,860 exact-rational and spectral checks are corroboration, not infinite proof.

**Originality — PASS under inspected literature, with priority risk.** Wang et al. (2026, arXiv:2608.03548v1, Sections II–IV, VII) introduce the exact reduced DGT dynamics but supply certificates for general heterogeneous networks, while asserting tightness for complete networks or homogeneous curvatures. This statement classifies the previously uncovered joint case of nonzero curvature spread and an incomplete two-node network, including a global no-restabilization conclusion. The closest retrieved homogeneous graph-specific spectral optimization covers \(\eta=0\), not \(\eta>0\). Standard Schur–Jury is acknowledged. An older equivalent two-agent spectral calculation is not ruled out by database searches alone.

**Mathematical value — PASS.** The exact dimensionless stability ceiling answers the natural sharp calibration question for the smallest network where topology and heterogeneous local Hessians interact. It quantifies the step restriction caused by curvature dispersion, locates the first flip eigenvalue, and excludes isolated larger stable windows. This informs constant-step DGT design rather than being a mere parameter substitution or arbitrary finite example.

**Limitations.** The result concerns Schur stability of a linear reduced iteration, not the optimal convergence rate and not time-varying, directed, or larger networks. The numerical tests do not establish a theorem beyond the analytic derivation. The motivating paper's general certificate remains applicable in broader settings.

Self-review: passed. Independent audit: not yet performed.
