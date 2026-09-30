# Independent Audit — 2026-09-30

**Record:** `2026/09/20/polyak-objective-monotonicity-frontier--169a05cdc789`  
**Title:** Sharp one-step objective frontier for scaled Polyak steps on SPD quadratics  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `664cfd92c51c5e7317cd240d486264e8e15fd1e8`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The exact one-step factor follows by direct expansion: with S_j=e^T A^j e and alpha=(gamma/2)S_1/S_2, the objective ratio is 1-gamma+(gamma^2/4)S_1S_3/S_2^2. Weighting eigenvalues by p_i=lambda_i e_i^2/S_1 turns the moment ratio into E[Lambda^2]/E[Lambda]^2. The endpoint quadratic inequality lambda^2<=(mu+L)lambda-mu L and scalar maximization at E Lambda=2mu L/(mu+L) give (kappa+1)^2/(4kappa), attained on the two-point spectrum. All monotonicity thresholds and the minimax gamma follow algebraically and the kappa=20 example checks.
- **Originality — PASS:** The spectral moment bound is a classical Kantorovich-type inequality and is not itself novel. The located Polyak-step literature treats convergence rates, distance contraction, exact-line-search comparisons, and broader worst-case behavior, but the audited statements do not give this exact all-state SPD one-step objective envelope together with the sharp thresholds 7+4sqrt(3) and 3+2sqrt(2). The contribution is therefore a sharp application/frontier rather than a new moment inequality.
- **Scientific value — PASS:** The result cleanly separates Fejér/distance improvement from objective monotonicity and gives exact parameter/condition-number boundaries, plus a minimax scaling with the classical steepest-descent factor. That is a useful diagnostic for target-value Polyak steps on quadratics.

## Independent findings
- Equality is achieved already in dimension two with spectrum {mu,L} and endpoint weights L/(mu+L), mu/(mu+L).
- For gamma=1, Q<=1 is equivalent to kappa<=7+4sqrt(3); for gamma=2 it is equivalent to kappa<=3+2sqrt(2).
- Minimizing Q_gamma over gamma gives gamma*=8kappa/(kappa+1)^2 and factor ((kappa-1)/(kappa+1))^2.
- At kappa=20 and gamma=1, the stated equality example gives objective factor 1.378125 while Euclidean distance decreases.

## Independent checks
- Re-derived the S_1,S_2,S_3 expansion and moment reduction.
- Solved the scalar moment extremum and equality conditions independently.
- Checked the threshold algebra and minimax derivative by hand and numerically.
- Compared against current accessible statements of Huang–Qi, Orabona–D’Orazio, and He et al.

## Literature evidence
- https://arxiv.org/abs/2407.04914 — Huang and Qi (2024), analytic worst-case study of exact line search and Polyak steps, emphasizing distance/convergence behavior rather than this exact one-step objective frontier.
- https://arxiv.org/abs/2505.20219 — Orabona and D’Orazio (2025/2026), broader Polyak-stepsize perspective and negative results; no matching sharp SPD objective thresholds located in the accessible statements.
- https://arxiv.org/abs/2512.06231 — He et al. (2025/2026), tight convergence analysis and universal function classes; no matching all-state one-step quadratic objective envelope located.
- https://doi.org/10.1007/s11590-016-1087-4 — de Klerk, Glineur and Taylor (2017), classical sharp exact-line-search factor used only as a comparison.

## Limitations
- Exact arithmetic, unconstrained Euclidean SPD quadratics, and exact knowledge of f_* only.
- This is a one-step worst-case theorem; it does not characterize long-run trajectories or nonquadratic behavior.
- Historical-equivalence risk remains because the underlying moment inequality is classical and older target-value literature is broad.

The assigned source tree remained unchanged from the source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `664cfd92c51c5e7317cd240d486264e8e15fd1e8` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
