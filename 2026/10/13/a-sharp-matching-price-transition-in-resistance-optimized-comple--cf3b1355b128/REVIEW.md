# Scientific review: priced perfect-matching resistance optimization

## Correctness — PASS
The objective and budget are explicitly specified for every even \(N\ge4\) and every \(t>0\). Strict convexity of the Laplacian inverse-trace and injectivity of the edge-to-Laplacian map prove uniqueness of the **unrestricted** optimum; orbit transitivity then justifies two conductance classes. Exact antisymmetric and pair-constant eigenspaces yield the complete spectrum. The derivative of the resulting scalar objective gives the exact threshold, including equality and the entire \(t\ge2\) regime. Explicit substitutions prove the optimum, deletion benefit, and finite-size limits. The standard-library checker computes 66 rational examples by independent matrix inverse and spectrum routes, including exact boundary cases. Finite checks support but do not replace the proof.

## Originality — PASS with residual uncertainty
Ghosh, Boyd, and Saberi, *SIAM Review* **50** (2008), doi:10.1137/050645452, established the broad convex optimization problem and the equal-price complete graph. Their inspected primary full text does not specify the two-price perfect-matching allocation or threshold. Bapat, Karimi, and Liu, arXiv:1611.09457, provide fixed-weight complete multipartite Kirchhoff formulas, including the deleted-matching cocktail-party endpoint, but no optimized reinstated matching class. Gervacio's 2012/2016 fixed-unit-resistance multipartite paper is also relevant endpoint literature; only its abstract was accessible in the checked route. The proposed contribution is the explicit all-price optimum and finite-size transition, not general convexity, fixed-unit endpoint calculations, or a full class of arbitrary costs. A differently named historical specialization remains possible.

## Value — PASS
A priced disjoint matching is a motivated sparse class of paired links within a dense network. The theorem gives exact globally optimal rates and the price at which purchasing any matched link ceases to be worthwhile, uniformly across all even graph orders. The \(N^{-1}\)-width transition near unit price and squared resistance-benefit scaling identify a meaningful sensitivity regime that neither a single fixed-price calculation nor a numerical optimization certificate conveys.

## Scientific limitations
No results are asserted for other cost classes, odd graph order, nonlinear budget rules, or other graph objectives. The independent audit channel has not been exercised. A negative literature search is not a mathematical proof of novelty.

Self-review: passed. Independent audit: not yet performed.
