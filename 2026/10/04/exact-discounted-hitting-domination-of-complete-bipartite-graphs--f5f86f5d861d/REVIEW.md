# Same-model review

## Correctness
PASS. For a source profile with \(a\) selected vertices in the \(m\)-part and \(b\) in the \(n\)-part, automorphism symmetry reduces the equilibrium to two variables. Solving the resulting two-by-two system gives the stated support formulas. When \(0<\tau<\lambda\), each threshold inequality is linear in \(b\) after cross-multiplication by a strictly positive determinant, which yields the two exact ceiling bounds and hence \(b_a\). The cases \(\tau=\lambda\) and \(\tau>\lambda\) follow from the sharp one-step support bound. Exact-rational verification independently confirms the formula over \(1280\) profile cases and \(28\) direct subset-level cases.

## Originality
PASS. The initiating paper defines the parameter and its full text treats spiders, stars, and complete graphs, but not non-star complete bipartite graphs. Searches for “discounted hitting domination complete bipartite”, “discounted hitting domination biclique”, the \(K_{m,n}\) notation, and equivalent group-hitting formulations did not locate a statement implying this theorem. The 2024 group-hitting-probability paper evaluates prescribed target groups and top-\(k\) queries relative to a source node; the 2014 random-walk-domination paper optimizes fixed-budget finite-horizon aggregate objectives. Neither covers minimum-cardinality uniform-floor placement on \(K_{m,n}\).

## Value
PASS. Complete bipartite graphs are the first dense two-class family beyond the already treated complete graphs and stars. The theorem converts an exponential source-set problem into an exact one-dimensional integer optimization and isolates a sharp boundary at \(\tau=\lambda\). The \(K_{10,10}\) example shows a qualitative phenomenon absent from the star benchmark: every optimum must split sources across both sides.

## Closest literature and limitations
The closest source is arXiv:2609.31535v1. Section 6 gives stars and Section 7 gives complete graphs, while no complete-bipartite result appears in the inspected full text. The formula here is exact but remains a finite minimum over \(a\) when \(0<\tau<\lambda\), and no extension to three or more multipartite classes is claimed.

Same-model review: passed. Independent audit: not yet performed.
