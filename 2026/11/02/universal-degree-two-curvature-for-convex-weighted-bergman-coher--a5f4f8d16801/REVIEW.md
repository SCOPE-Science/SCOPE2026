# Mathematical assessment

## Correctness

The second-variation normalization uses the probability-normalized Bergman norm \((\beta-1)\int|f|^2(1-|z|^2)^\beta d\mu\), and the coherent density always belongs to \([0,1]\). The coefficient is computed by differentiating the normalized path, using analytic Fourier orthogonality, then representing \(G\) by its convex hinge decomposition. The exact integration-by-parts identity for the hinge coefficients proves the strict mode ordering for all real \(\beta>1\); monotone/dominated convergence gives the endpoint. A standalone exact-rational checker passed 704 identities and Taylor comparisons. The analytic proof, not the finite checks, supports the infinite-dimensional theorem.

## Originality

The relevant antecedent is Kulikov's 2022 maximization theorem (arXiv:2203.12349), which proves global optimality of normalized reproducing kernels and Möbius invariance but does not supply their complete Hessian spectrum. Frank–Nicola–Tilli (2023, arXiv:2307.14089) establishes quantitative generalized Wehrl stability in Gaussian Fock space; it does not imply the stated disk mode gaps by a change of variables. Melentijević (2025, arXiv:2508.01939) studies nonlinear weighted Bergman stability without determining the complete ordered curvature spectrum for every convex observable. Gómez–Kalaj–Melentijević–Ramos (2024, arXiv:2411.16010) concerns set concentration stability rather than the displayed functional Hessian. Priority searches and statement comparisons found no dominating theorem. This remains best-knowledge originality, not an independence certification.

## Value

Known coherent-state optimality does not quantify how the deficit grows in different holomorphic directions. This result simultaneously diagonalizes the entire infinite Hessian for every convex observable in the class, identifies the symmetry kernel, and proves the universal sharp degree-two transverse mode with a computable coefficient. That exact spectral hierarchy gives a principled local stability benchmark rather than an arbitrary finite special case.

## Scientific limits

The result establishes infinitesimal curvature for normalized pure states on weighted analytic disks. It does not establish a globally sharp nonlinear stability constant or a mixed-state or higher-dimensional analogue. An independently conducted audit and exhaustive historic-priority search remain outstanding.

Self-review: passed. Independent audit: not yet performed.
