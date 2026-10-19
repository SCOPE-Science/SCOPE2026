# Scientific review

## Correctness — PASS

The stated theorem is deliberately about a *symbolic Markov coding*. The primary source's exact cells and covering relations imply the displayed four closed first-return routes via vertex \(M_2\). Removing this vertex leaves a directed acyclic graph, so there are no other directed cycles; renewal decomposition gives the determinant and symbolic zeta. The Perron equation follows from the same graph, and the maximum-entropy return law follows from the normalized Perron weights. The Taylor steps use \(m=n+2\), not an unscaled index; the source's exact parameter equation verifies \(r_n-1=4\pi^2m^{-3}+O(m^{-5})\) and the determinants as claimed. Exact symbolic finite-matrix checks and high-precision scaling tests agree, but the proof does not rely on them.

## Originality — PASS with residual uncertainty

Glendinning–Wong (MIMS EPrint 2010.100, full text, pp. 12–15) already establish the full-dimensional polygon, its Markov graph and its parameter equations. No novelty is assigned to those. This result quantifies the four-return structure, its entropy/zeta, and the simultaneous \(m^{-1}\), \(m^{-3}\), \(m^2\) singular scales; the inspected 2010/2011 full text gives no equivalent formulas. Glendinning's 2014 full manuscript examines invariant measures and equivalent expanding metrics, rather than this specific countable sequence's rare-return symbolic law. Other Markov renewal and symbolic zeta theorems are general mechanisms, not this family-specific computation. Residual risk: an unindexed later calculation or a thesis may have independently stated the same formulas; these sources cannot be exhaustively excluded by searches.

## Value — PASS

The source constructs countably many transitive **two-dimensional** attractors with both branch determinants larger than one in modulus for large indices, but does not quantify how their natural itineraries degenerate as the number of polygonal cells grows. The exact return law and entropy give a computable complexity benchmark; the determinant asymptotics show a nontrivial triple-scale contrast between symbolic information generation and geometric area expansion. The return-time distribution supplies an invariant interpretation of the entropy decay, not merely a matrix eigenvalue. The claim does not rely on an unproved identification between itinerary entropy and actual planar topological entropy.

## Closest literature and limitations

The source's equation (29) is strong antecedent coverage for the graph, and its equation (30) is the antecedent for the left determinant, while the new assertion is the joint explicit asymptotic and renewal law. The later invariant-measure paper is related but does not calculate this quantity. No statement is made about physical periodic-orbit counts, planar topological entropy, or an explicit minimal valid index.

Self-review: passed. Independent audit: not yet performed.
