# Scientific review: odd biclique covers of cycle bouquets

## Correctness — PASS

The proof establishes the claimed formula for all finite one-vertex unions of \(t\ge1\) cycles with lengths at least three. The path-adjacency rank calculation gives \(\operatorname{rank}_{\mathbf F_2}A(G)=2s\), and the Eulerian even-core obstruction rules out a perfect cover exactly when the number of odd petals is odd. A direct two-biclique identity for a pair of triangles, a one-biclique square identity, and a two-vertex edge expansion produce an explicit cover meeting the lower bound. The mathematical argument is independent of exhaustive testing. Replaying the included verifier confirms 1,484 explicit covers and ranks and ten small exact minima. Risk: finite checks cannot detect every conceivable mistake in the infinite proof; the algebraic and parity lemmas have therefore been proved explicitly.

## Originality — PASS

The closest primary research is Buchanan et al., *Odd Covers of Graphs*, arXiv:2202.09822, and Buchanan et al., *On odd covers of cliques and disjoint unions*, arXiv:2408.08598. The latter full article, especially §§1–3, was inspected for the butterfly example, the even-core obstruction (Corollary 5), and disjoint-union cycles (Theorem 8). The former article establishes the general rank method and individual-cycle background. Those statements do not provide the odd-cover number of heterogeneous bouquets or an all-length pairing-and-expansion construction. Published-result similarity searches over friendship, windmill, cycle bouquet, coalescence, one-vertex union, rank-bound and odd-biclique-cover aliases returned no same-invariant covering claim; retrieved graph-bouquet studies addressed different invariants. Risk: a mathematically equivalent result may exist in unindexed or more recent material. This review reports the actual comparisons and does not claim universal novelty certification.

## Value — PASS

This determines a natural exact graph invariant throughout a connected family obtained by the first nontrivial operation beyond disjoint cycles: identification of one vertex. The formula distinguishes parity of the *number* of odd petals from the published disjoint-union rule, reveals precisely when an Eulerian nonbipartite bouquet has a perfect odd cover, and supplies a reusable local expansion realizing optimal covers for arbitrarily long heterogeneous petals. It is a structural result, not an arbitrary finite calculation.

## Literature and scope

References: arXiv:2202.09822 (rank bound and foundational odd covers); arXiv:2408.08598, §§1–3 (butterfly, even-core obstruction, disjoint-union cycle formula). The general cactus case and enumeration of minimum covers are not settled here. Independence of review has not been established.

Self-review: passed. Independent audit: not yet performed.
