# Review of the spectral-decay allocation theorem

## Correctness

**PASS.** Diagonalization of the exact ideal preconditioner leaves a centered Gaussian quadratic-form estimator with variance \(2S(k)/N\). A termwise shifted-tail inequality under the adjacent log-spectral ratio gives the global upper bound \(\mathcal V_1/\mathcal V_N\leq Nq^{2c(N-1)}\). The elementary inequality \(N\leq2^{N-1}\) gives sufficiency. Finite geometric matrices at the two-probe budget show necessity of the ratio threshold. Consecutive-risk ratios determine the complete infinite-geometric optimizer, including ties. The integral test and compactness of minimizing rank fractions justify the polynomial-spectrum limit and constant. The standalone program tests exact finite identities and supporting numerical examples; none is substituted for an infinite proof.

## Originality

**PASS, conditional on the inspected literature.** The 2026 Cortinovis–Toni paper explicitly provides the underlying variance identity and a general *pairwise* test for allocation, so neither identity is claimed new. Its inspected full arXiv manuscript does not state the present uniform sharp spectral-ratio threshold for *all* budgets and allocations, its finite-dimensional necessity witness, or the geometric/power-law exact optimization classification. The 2023 XTrace study instead concerns exchangeable estimators, and the 2016 Saibaba–Alexanderian–Ipsen study concerns randomized subspace approximation. An accessible earlier mathematical finding about Gaussian Nyström log-determinant error for two-block spectra concerns high-contrast moments, not optimal allocation under adjacent spectral-decay envelopes. Search absence is not proof of novelty; a sharper unindexed or uninspected allocation theorem remains a bibliographic risk.

## Value

**PASS.** The recent research asks when one Gaussian probe is a defensible allocation instead of spreading a fixed budget over many probes. The sharp dimension-free decay threshold supplies a direct sufficient rule with a matching obstruction, and the geometric-versus-polynomial contrast identifies two quantitatively different resource-allocation regimes. Unlike a mere numerical benchmark, the criterion holds for an entire spectrum class and all integer budgets in its clearly stated ideal model. It is not a guarantee for randomly computed preconditioners or finite-precision Lanczos.

## Closest literature and residual limits

The main contextual source is Cortinovis and Toni, arXiv:2601.05778v1 (especially Section 2, equations (8)–(11)). Comparison was also made to Epperly–Tropp–Webber, arXiv:2301.07825, and Saibaba–Alexanderian–Ipsen, arXiv:1605.04893. The mathematical gap is a uniform *optimization* result, not a new trace-variance identity. A cost-unit model for exact eigenpairs and exact quadratic forms abstracts away algorithm implementation expense. Independent scholarly comparison remains desirable before any publication claim.

Self-review: passed. Independent audit: not yet performed.
