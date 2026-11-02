# Scientific review: Sharp quadratic least-squares stability on complete metric graphs

## Correctness — PASS
An orthogonal nodal/bubble decomposition gives the inverse mass matrix explicitly. Exactly two reproducing-kernel quadratic types occur at a vertex. Their negative regions and absolute integrals yield the exact \(N_n\). Symbolic differentiation establishes its strict monotonicity, and an explicit shape-function inequality gives the full \(L^\infty\) norm for every \(n\ge6\), with no interior norming point. The positivity defect follows from the fact that constants are reproduced. The independent original-basis checker constructs exact Gram matrices and verifies 83 kernels without relying on the symbolic nodal decomposition. It supports, rather than replaces, the infinite-family argument.

## Originality — PASS (qualified)
The closest prior mathematical comparison, quadratic-star endpoint sensitivity, concerns pendant edges and does not imply the full dense complete-graph norm. General and complete-multipartite **linear** spline results have a different approximation space. Kayumov's 2004 interval spline discussion covers a different topology; Arioli–Benzi's metric-graph finite-element mass matrices treat piecewise-linear elements; the higher-order stability estimates of Diening–Storn–Tscherpel do not give sharp complete-graph constants. Published mathematical-record searches for the exact constants, Gram matrix, and corresponding kernel found no dominating result. The 2006 Boman manuscript was available only at abstract level, so publication priority is qualified rather than asserted beyond doubt.

## Value — PASS
Sharp amplification governs the maximum possible pointwise error after least-squares reconstruction. The complete graph tests whether increasing connectivity controls amplification when every edge has its own quadratic bubble and no vertex is pendant. The exact norm rises with degree and approaches a nontrivial algebraic constant; the \(5/2\) threshold identifies when vertex bounds control all edge interiors, and the theorem proves the sharp full operator norm on an infinite family, rather than only an evaluation estimate. This is a natural high-connectivity stability classification, not a reparameterized elementary example.

## Scope and risks
Full operator norms for the smaller complete graphs of orders three, four and five are not established. Input sign extremizers are essentially bounded and need not be continuous. The calculation assumes unit arclength edges, uniform densities, and value-only vertex matching. Older unindexed work and the unavailable full Boman manuscript remain literature-priority risks. No independent scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.
