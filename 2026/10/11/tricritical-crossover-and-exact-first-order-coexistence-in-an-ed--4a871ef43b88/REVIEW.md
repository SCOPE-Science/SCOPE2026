# Review of the edge-weighted forbidden-transition theorem

## Correctness — PASS

The Perron matrix admits the exhibited positive eigenvector and eigenvalue; differentiation gives the exactly monotone correlation. The derivative of the response ratio reduces globally to one scalar expression, whose derivative has a single sign crossing for \(k>3\) and no crossing for \(k\le3\). This supplies the missing global control: the nonzero solution is retained only after its exact stationary free-energy advantage becomes positive. The coexistence equation decreases then increases, so it has exactly one positive root. Uniform Taylor expansions near the cubic--quintic cancellation give the constants \(5/216\), \(5/288\), \(5/6\), \(5/4\), and \(\sqrt{5/12}\). Both limiting branches were checked algebraically. The bundled finite checker verified 89 symbolic, high-precision, and Markov-stationarity assertions. Numerical checks alone do not prove uniqueness, infinitude of branches, or asymptotic limits; those follow from the derivative and Taylor arguments in RESULT.md.

## Originality — PASS, with residual risk

Tang, Yang, and Li (arXiv:2609.25915v1, Sections 6.4--6.5, 7.6, 8) prove the unweighted \(k=3\) quartic-root transition and supply the general Legendre apparatus; they describe the joint cubic--quintic crossover as a further direction. The complete weighted family, unique first-order coexistence, and exact model-specific spinodal and jump constants are not consequences of the fixed-weight statement. Buzzi, Kloeckner, and Leplaideur (DOI:10.5802/ahl.192) already develop general metastable nonlinear pressure; Ostilli and Mukhamedov (arXiv:1205.6777) analyze a related Potts model, but use full adjacency and different order parameters. The residual risk is an older or unindexed equivalent spin-one hard-core mean-field computation.

## Mathematical value — PASS

The unweighted correspondence has an exceptional fourth-root transition. The theorem answers the natural stability question for the single edge weighting that preserves spin reversal and primitivity: it separates continuous and discontinuous behavior, exactly locates global coexistence, quantifies metastability, and derives a two-sided crossover at the coalescing transition. These are natural, sharp dynamical/thermodynamic invariants, not arbitrary numerical refinements. The theorem makes no claim about arbitrary graph perturbations or dynamical metastable escape.

## Closest literature and limits

The strongest sources are the original finite-state nonlinear-correspondence calculation (arXiv:2609.25915v1), the established nonlinear-pressure/metastability framework (DOI:10.5802/ahl.192), and transfer-matrix first-order transitions in a different Potts interaction (arXiv:1205.6777). Exact application-specific priority remains uncertain until an independent review. The finite checker is corroborative and not exhaustive.

Same-model review: passed. Independent audit: not yet performed.
