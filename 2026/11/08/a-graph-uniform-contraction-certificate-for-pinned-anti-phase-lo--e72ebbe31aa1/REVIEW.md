# Self-review: pinned logistic checkerboard theorem

## Correctness (C): PASS

The exact swapping equations are solved in both directions, not inferred from a numerical orbit. The admissible parameter interval is derived from \(\varepsilon>0\) and \(\mu\le4\). The full linearized two-step map is block triangular on the whole graph state space. Double stochasticity of the bipartite adjacency block makes the spectral radius exactly \(v^2\), while a direct four-step block product gives the exact induced norm \(v^3(v+2)\). Symbolic differentiation proves monotonicity of \(v\); the endpoint radical is strictly below \(1/2\). A dimension-free second-derivative estimate for the fourth iterate justifies the common quantitative basin radius \(1/174080\). The cube invariance, endpoint inclusivity, and all graph quantifiers have been checked. A standalone checker reproduces exact algebra and finite examples.

The check is not an independent proof audit. Its finite graph tests are not used to infer the theorem for arbitrary graph size.

## Originality (O): PASS within inspected evidence

The closest primary recent source is Dixit, Chauhan and Shrimali, arXiv:2609.00983 (2026-09-01). Its full available article was inspected at the model, simulation, and conclusion sections: its nonzero-coupling numerical phase-ordering results and fixed \(\varepsilon=0.4\) are distinguished from this exact pinned curve with \(\varepsilon\le0.18\). The 1991 Amritkar–Gade–Gangal–Nandakumaran full text was inspected across its four pages: it already establishes two-color periodic-wave existence/stability analyses in one-dimensional rings, including a parameter window for a two-color period-two wave at \(\mu=4\). Those results are not claimed as new. The present graph-independent **all-regular-bipartite** Floquet spectrum, sharp four-step maximum norm and explicit uniform basin radius are additional structural assertions not found in that inspected paper.

The Xie–Hu 1997 two-dimensional periodic-pattern study was available through its abstract only, which reports analytic patterns and small-system stability boundaries. This is a substantive residual priority risk, as are other older coupled-map classification papers. Searches by the exact parameter, critical logistic point, bipartite graph, traveling checkerboard, and equivalent spectrum did not locate a statement implying the full theorem. Absence of search hits alone was not treated as proof of novelty. Independent historical-priority examination remains warranted.

## Mathematical value (V): PASS

This is a natural exact contrast to numerical phase ordering in high-dimensional logistic lattices: a nontrivial anti-phase two-cycle can be established analytically with strict full-state attraction, uniform over graph topology and dimension. Fixing the logistic critical point eliminates one part of the one-step Jacobian; the resulting all-graph singular-value law and universal four-step contraction certificate are structurally motivated by the nonlinear criticality and coupling architecture, rather than an arbitrarily chosen numerical slice. The explicit \(\ell_\infty\) basin radius enables uniform perturbation estimates even for growing networks. It is an existence-and-robustness theorem, not a general explanation of the source's transition at different coupling.

## Scope and remaining risks

No global basin classification, necessity for arbitrary checkerboard cycles, extension to irregular graphs, or transition threshold at fixed coupling is asserted. The result is local in the full state space and confined to a critical-point-pinned parameter curve. Older two-dimensional results could contain closely related special cases. The numerical and symbolic checker provides reproducibility, not independent validation.

Self-review: passed. Independent audit: not yet performed.
