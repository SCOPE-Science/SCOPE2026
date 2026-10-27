# Scientific review

## Correctness — PASS

The claim specifies all integer orders \(n\ge3\), \(m\ge2\), the symmetric stochastic admissible class, and exactly two natural edge orbits. Convexity of SLEM and automorphism averaging justify unrestricted global optimality. The product spectrum is reconstructed exactly, yielding the three affine gap inequalities; two explicit universal upper bounds coincide with the gap of one feasible chain. Equality in whichever bound is active forces both invariant edge weights, so invariant uniqueness is proved but unrestricted uniqueness is not asserted. The parity threshold comes from an exact cosine equivalence; the heuristic-gap asymptotics use the full signed spectrum. An independently constructed LP and dense-matrix spectral replay agree with the formulas on their tested finite ranges. These finite checks are not substituted for the all-orders proof.

## Originality — PASS, with residual uncertainty

Boyd–Diaconis–Parrilo–Xiao's 2007 preprint and 2009 paper develop the general symmetry reduction and product eigenvalue machinery but explicitly solve edge-transitive products, not the generic two-orbit cycle-by-clique product with separate cycle and fiber weights. The 2010 cyclic multipartite source has only cross-layer connections and does not contain the within-layer cliques needed here. Jafarizadeh's later clique lifts connect neighboring fibers completely rather than by a perfect matching. Olesker-Taylor–Zanetti discuss the two-matched-clique bottleneck but give geometric/order estimates rather than the exact \(n\ge3\) two-sided SLEM. A 2026 weighted product paper optimizes algebraic connectivity under a different linear weight budget; its spectral formulas alone do not imply the sharp stochastic SLEM transition. Published-record and mathematical-result queries, together with the recoverable comparison history, did not show the present complete parameter classification. Standard components and previously known special graph cases are not independently claimed as new. Residual risk: less-indexed specialized cylinder/product analyses could already give an equivalent theorem.

## Value — PASS

The analytic theorem resolves a natural infinite-family two-edge-orbit network design problem, including the exact switching boundary between spectral balancing and stochastic row saturation, and the complete role of cycle parity. This boundary distinguishes the entire range \(2\le m\le7\) from \(m\ge8\) for odd cycles of length at least five, not merely a single numerical instance. The unoptimized uniform-edge rule can be periodic for even prisms and has an asymptotic spectral gap a factor \((m+1)/2\) smaller at fixed \(m\ge3\). Thus the exact formulas expose a substantive design difference rather than a relabeling of the Cartesian-product spectrum.

## Scientific limitations

Only symmetric, uniform-stationary discrete-time stochastic matrices are optimized. The result does not assert unrestricted optimizer uniqueness or a total-variation mixing-time optimum. Algebraic identity and numerical stress tests do not certify novelty; remaining literature coverage is a risk. An independent external mathematical audit is not available.

Self-review: passed. Independent audit: not yet performed.
