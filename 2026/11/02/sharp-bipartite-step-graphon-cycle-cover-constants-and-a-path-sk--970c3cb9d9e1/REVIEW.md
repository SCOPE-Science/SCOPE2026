# Review of the sharp bipartite step-graphon cycle-cover constant

## Correctness — PASS

The precise event is a spanning undirected \(2\)-regular subgraph of a fixed, finite, loopless, connected bipartite step-graphon sampled graph. The theorem also covers the standard symmetric-directed cycle-cover convention. For either event, the class-count edge-cone criterion is necessary. For occupancy vectors in the cone with all classes linearly large, the complete-blow-up cycle-cover theorem and a fixed-skeleton bounded-degree embedding lemma give sufficiency with exponentially small failure: with each supported edge probability bounded below, Chernoff and a finite union bound verify the required cross-pair densities and degrees. The relevant density threshold is taken strictly below the smallest supported probability. The probability therefore differs from exact multinomial cone membership by at most an exponentially small amount.

Bipartite edge vectors impose equal vertex counts on the two sides, ruling out odd orders. The probability of equal counts at even order is asymptotic to \(\sqrt{2/(\pi n)}\). Conditional on equality, the two multinomials are independent; their joint Gaussian fluctuation has the stated covariance and lives in the balance subspace. The finite active-facet system converges in probability to the Gaussian tangent cone, with no Gaussian mass on nontrivial facet boundaries. Its angle is strictly positive. These arguments prove the general constant.

For \(P_{2r}\) with equal block masses, the edge-flow equations are a single forced recursion: alternate edge variables are partial sums of differences of two independent multinomials, while the remaining edge variables are linearly large with high probability. The limit is an exchangeable continuous Gaussian bridge with \(r\) cyclic rotations. Almost surely exactly one rotation is a nonnegative excursion, giving the exact angle \(1/r\). The checker replays 4,382 finite assertions; it is supplemental and is not used as a proof of the asymptotic statements.

## Originality — PASS, subject to historical priority

Gao–Hu–Chen (arXiv:2604.05138v1, Theorem 1(3), Section 2.3) prove only an \(O(n^{-1/2})\) upper bound in this in-cone bipartite case. They do not derive an equality with the leading coefficient. Gao–Chen (arXiv:2502.14853, Theorem 2) determine Gaussian cone probabilities for the nonbipartite, full-rank residual case, not the codimension-one lattice-balanced bipartite case. Jiang–Chen (arXiv:2603.27424v3, Theorem 1 and Sections 4–5) characterize complete blow-up cycle covers, rather than a random-graph leading coefficient. Chen (arXiv:2510.02074, Theorem 2) treats zero-one properties for independently sampled directed edges, not this sharp symmetric undirected coefficient. Literature and semantic-record checks using graphon H-property, two-factor, edge cone, local central limit, Gaussian tangent angle, and path-ballot reformulations found no direct coverage. Earlier general multinomial cone local limit and conditioned-bridge literature might contain an equivalent abstract theorem; definitive universal novelty is not claimed. The accepted new scope is the explicit bipartite coefficient and the sharp path family \(1/r\), not the known embedding or general Gaussian/cone tools.

## Mathematical value — PASS

The previously established root-order upper bound leaves the actual success probability undetermined. A sharp constant distinguishes block skeletons having the same decay exponent and same population-level bipartite balance. In the natural connected-path family, the conditional Gaussian angle is explicitly \(1/r\) for every number of paired blocks, independently of fixed supported edge probabilities. It provides a computable statistical signature of boundary geometry and an exact leading rare-event probability, including when the population vector lies on multiple edge-cone facets.

## Limitations and verification status

The theorem has fixed numbers of positive-mass blocks, fixed positive supported edge probabilities, and a connected loopless bipartite skeleton. It does not address odd-cycle skeletons, zero block masses, growing block counts or edge probabilities decaying with sample size. The conclusion is a leading asymptotic, not a second-order expansion. No independent mathematical audit or comprehensive historical priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
