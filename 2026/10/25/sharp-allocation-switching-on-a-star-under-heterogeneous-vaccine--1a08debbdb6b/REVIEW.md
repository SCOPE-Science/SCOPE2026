# Review of the spectral vaccination allocation theorem

## Correctness — PASS
The geographic linear infection operator is symmetric, irreducible and Metzler. Its positive principal eigenvector and symmetric eigenvalue second-variation formula prove strict convexity on the exact resource-budget simplex; vertex permutation then enforces uniform doses across leaves. Compressing to a two-dimensional center/leaf block produces a strictly convex scalar function whose unique unconstrained stationary point is computed with its sign intact and clipped to the physical budget interval. Endpoint derivatives and the affine formula cover the complete stated parameter space. The standalone `verify.py` passed 20,706 assertions, including full-matrix eigenvalue calculations and exact-rational special cases. Computations corroborate rather than establish the universal theorem.

## Originality — PASS (provisional priority assessment)
Bustamante-Castañeda et al. (arXiv:1906.07449) give the source geographic Laplacian epidemic model and fixed-node isolation. Badaoui et al. (Axioms 13 (2024), 769) study vaccination and spectral perturbations on networks including stars. Preciado et al. (arXiv:1303.3984) give related general SIS spectral control methods. Their inspected statements do not provide the unique unequal-effectiveness fixed-dose star optimizer, sharp both-direction switch thresholds, or affine mixed-allocation value. Semantic searches of research records and earlier accessible claims did not show the exact same classification; search incompleteness and possible stronger spectral optimization results remain residual priority risks.

## Value — PASS
The exact classifications decide whether finite supplies should be concentrated or shared across location classes in a minimal natural geographic contact network under a clearly specified early-growth objective. They delimit physical resource feasibility and provide analytical benchmarks for spectral epidemic control beyond perturbation or numerical scanning. The exact linear high-budget branch and uniqueness are substantive structural information.

## Limitations
Only early linearized growth is optimized, not outbreak size, intervention cost at arbitrary nonlinear budgets, or societal utility. The model requires symmetric homogeneous migration on a star, identical baseline susceptibles, positive homogeneous local infection and recovery rates, linear dose effectiveness and the conservative budget constraint. Broader spectral control literature may subsume the solution; no independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
