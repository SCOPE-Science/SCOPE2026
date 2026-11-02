# Scientific review

## Correctness: PASS

The exact Ornstein–Uhlenbeck endpoint is a stochastic convolution with deterministic kernel \(g(s)=e^{-\lambda(h-s)}\). The Brownian increment and the bridge sine coefficients are orthogonal Wiener integrals against a complete cosine basis. Itô isometry therefore gives the exact squared-error sum, not a truncated numerical estimate. The coefficient integral is evaluated directly. The optimal fixed-budget subset is the largest-weight set by orthogonality, with parity monotonicity reducing the two-mode case to frequencies \(2\) and \(3\). Their comparison is a single strictly monotone exponential equation, proving uniqueness and both boundary cases. Dominated convergence and the odd-integer zeta sum prove the small-damping 84.11% asymptotic. An independently integrated cosine-coefficient checker, a direct series-tail comparison and rank checks passed 127 supplementary tests. This verification does not replace the proof, and no numeric sample is used as an infinite-index certificate.

## Originality: PASS, subject to priority uncertainty

The closest recent source is Binkowski–Christian–Götschel–Minion, arXiv:2610.23693v1 (public October 16, 2026), which motivates smooth Brownian-bridge approximations of SDEs and experiments with retained spectral modes. Its inspected material does not give an arbitrary-subset fixed-budget Ornstein–Uhlenbeck endpoint optimization or the sharp switch between frequencies \(\{1,3\}\) and \(\{1,2\}\). Koskela–Relton, arXiv:2004.05687, Theorems 3 and 6, have an exact mean-square truncation decomposition, but use the *unconditioned Brownian-motion* half-integer-frequency series with consecutive truncation. Their result supplies a related projection principle but neither the same endpoint-preserving bridge coordinates nor the transition equation. Foster–Lyons–Oberhauser, arXiv:1904.06998, derive optimal polynomial Brownian approximations for different weighted path and iterated-integral objectives. Foster–Habermann, DOI 10.1017/S096354832200030X, explicitly study the standard sine bridge expansion but optimize Lévy-area approximations, not the scalar OU endpoint. No matching claim was found in the indexed mathematical-record queries or prior accessible research claims. Absence of a match is not a novelty proof. Specialized unindexed historical coverage remains possible; independent priority audit is not complete.

## Mathematical value: PASS

For SDE solvers that replace Brownian bridges by finite smooth Fourier expansions and evaluate deterministic random ODEs, choosing how to spend a small Gaussian coefficient budget is a natural numerical-design problem. The exact first nontrivial case exhibits a genuine frequency bypass, a unique damping-dependent change of the optimal support, and an 84.11% asymptotic improvement in the residual strong endpoint mean-square error at unchanged mode count. The parity mechanism explains why a path-optimal initial segment can be endpoint-suboptimal. The result is a sharp fixed-basis benchmark, not a proposal to replace exact Gaussian OU transition simulation or a claimed universal optimality theorem.

## Closest literature and limitations

The four primary sources, the exact kernel projection and the explicit mismatch in their optimization objectives are documented in `RESULT.md`, `AUDIT.json` and `VERIFICATION.md`. The random ODE is solved exactly, and nonlinear SDEs, fully discretized spectral-deferred-correction schemes, all-time path error and arbitrary Gaussian linear-function observations are excluded. Potential earlier specialized Fourier endpoint analyses remain the main originality risk.

Self-review: passed. Independent audit: not yet performed.
