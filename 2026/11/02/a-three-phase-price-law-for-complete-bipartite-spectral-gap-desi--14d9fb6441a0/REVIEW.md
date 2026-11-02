# Mathematical review: three-phase bipartite spectral-gap design

## Correctness — PASS

For all integers \(m\ge p\ge3\), both strict price classes and all boundary ratios are handled by the exact eigenvalue factorization and the unit-gap feasible-region reduction. The important implication from the quadratic condition \(f(a,b)\ge0\) to \(\lambda_-\ge1\) explicitly includes the root-sum test; the derived lower envelope is convex and its unique stationary point gives the third price regime. Independent whole-matrix tests and symbolic identities are reproducible with `verify.py` (1,716 passing assertions, 26 successful numerical optimizations). Experiments are supplementary, not infinite proofs.

## Originality — PASS on inspected evidence, qualified

The closest full-text source is Sun–Boyd–Xiao–Diaconis (2006), establishing the general weighted-budget semidefinite optimization but not the two-price complete-bipartite formula. Boyd–Diaconis–Parrilo–Xiao (2007/2009), Section 5.4.2, treats complete bipartite walks under discrete-time SLEM with uniform transition-orbit parameters, and does not imply the continuous-time heterogeneous-price optimum. Shakeri et al. (2015) analyze one-to-one coupling between fixed connected layers. Closely related previous two-hub formulas concern \(\(K_{2,m}\)\), not the \(p\ge3\) statement, whose ordinary-hub eigenspace yields a different feasibility boundary and threshold. published-finding corpus searches for pricing, spectral-gap design and bipartite optimization returned no matching theorem. Residual risk: specialist work under algebraic connectivity, optimal weight design or semidefinite spectral allocation could state an equivalent formula not located in the accessible evidence.

## Mathematical value — PASS

The exact unrestricted optimum is explicit for infinitely many bipartite dimensions and all positive price ratios. The formula identifies two distinct allocation regimes and a genuine active-eigenspace transition; the high-price boundary scales like \(\(m^4/(p-1)^2\)\) at fixed \(p\), so the price range in which a leaf-degree constraint remains binding can be unexpectedly large. This gives a usable exact benchmark for weighted network design rather than simply another SDP formulation or a tiny finite example.

## Limits

The symmetric solution need not describe every possible asymmetric optimizer. Prices are fixed by two hub classes; arbitrary edge prices and normalized objectives are outside scope. Historical full-text coverage is not exhaustive; independent mathematical audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
