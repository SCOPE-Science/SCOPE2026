# Self-review

## Correctness — PASS

The claim is over the integers for all \(r\ge1\), including the degenerate case \(r=1\). The argument explicitly classifies every clique as lying in a cyclic window or a distinguished equilateral triangle, collapses the window subcomplex to the original circle, computes the integral relative boundary as the surjective all-ones map, and tracks signs of both generators of the dihedral group. The only imported topological lemma is Adamaszek's documented cyclic-power collapse under a verified girth bound. A rank-only calculation or a mod-two finite experiment would not establish the integral representation; here the actual connecting homomorphism and its group action do. Two standalone independent computations replay finite cases and complement the proof. No claim is made about scales other than one-third.

## Originality — PASS, with residual risks

The most directly overlapping source is Adamaszek (arXiv:1104.0433, Corollary 6.7): it proves the nonequivariant sphere count, not the dihedral lattice. The strongest potential implication is Adamaszek–Adams–Frick–Peterson–Previte-Johnson (arXiv:1410.4336): Proposition 7.2 computes a similar lattice for circular-arc nerve complexes, while Theorem 8.5 furnishes a nonequivariant map from a corresponding clique complex. That map is not equivariant for the relevant polygon rotations: reduction from \(3r\) vertices modulo \(2r\) does not commute with the cyclic wraparound. Therefore those two statements do not alone identify the induced action of \(D_{3r}\) on the clique complex. Their Example 8.3 does explicitly prefigure the \(r=3\) attachment argument. The present result does not claim its wedge calculation as new, and the exact integral dihedral action is established directly for all \(r\). Searches of published mathematical records and recoverable earlier results found no covering claim. Equivalent unindexed literature or implicit unpublished arguments remain a bibliographic risk.

## Value — PASS

The first singular radius is a natural threshold in finite circle Rips topology, and its wedge multiplicity alone cannot determine how reflections or rotations act on homology. The integral answer identifies a nontrivial family of symmetry lattices, determines both reflection classes when \(r\) is even, and gives a direct rational acyclicity result for the full symmetry quotient. The result is an intrinsic equivariant refinement of a known family rather than an arbitrary slice of numerical data. No higher critical scales or integral quotient classification are claimed.

## Limits

Correctness relies on the stated radius convention and on finite simplicial homology with integer coefficients. Independent external validation and absolute literature priority have not been established.

Self-review: passed. Independent audit: not yet performed.
