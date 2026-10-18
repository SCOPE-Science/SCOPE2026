# Scientific review

**Correctness — PASS.** The canonical partial polar factor preserves the initial singular-vector-pair span. For nonvanishing modes, post-step singular values obey the exact contraction \(s^+=|qs-\tau|\) with factor \(q<1\); the countable resonant preimage set is excluded when asserting full rank. The signed recurrence distinguishes post-step sign preservation from pre-step sign reversal above \(\eta a=1\). Exact proximal shrinkage reaches zero in finitely many steps. Fractional and dense-SVD checks replay the formulas, but the proof supports all dimensions.

**Originality — PASS with limitations.** The motivating 2026 source states the polar post-step rule and a one-step update-order bound. Its inspected full text and appendices do not supply the asymptotic rank-flat attractor classification or unbounded long-horizon ratio. The analogous SLORR pre-step rule, classical singular-value thresholding, general constant-step subgradient instability, exact-line-search matrix-polar descent, and a smoothed Polar-Express scalar update were compared at the level of hypotheses and dynamical implications. These results do not imply the exact simultaneous post/pre/prox theorem as stated. The inaccessible full SLORR text and unindexed work on nonsmooth spectral dynamics leave bibliographic uncertainty.

**Value — PASS.** Low-rank induction and update ordering are explicit central motivations for spectral weight decay. The theorem gives a complete sharp limiting benchmark: the same nonzero regularized quadratic has a rank-flat attractor under the ideal post-step rule, a singular order transition, and a diverging pre/post long-run separation, while true proximal shrinkage terminates. The exact limiting residual objective and the countable exceptional set quantify the phenomenon rather than only furnishing a small counterexample.

**Restrictions:** Canonical exact partial polar, isotropic centered quadratics, deterministic nonadaptive constant steps, exact arithmetic, generic initial singular spectrum where required. The claimed pre/post ratio concerns asymptotic magnitudes of separately evolved trajectories, not a direct difference lower bound, and does not contradict one-step order sensitivity estimates.

Self-review: passed. Independent audit: not yet performed.

