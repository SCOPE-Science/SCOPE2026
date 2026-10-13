# Scientific review

## Correctness — PASS

The channel is specified as exactly one contiguous length-two deletion, with all five possible starting positions and duplicate outputs collapsed. The upper bound is a direct pigeonhole transversal: among input positions \(2,4,6\) two bits agree, so one of three disjoint pair deletions gives a receiver word whose second and fourth symbols agree. That eight-word receiver family intersects every source shadow. Every size-eight equality case must contribute one receiver to each transversal bucket; complete enumeration of the eight explicit buckets produces just two codes, with partial-node counts \(1,5,13,28,17,8,11,2,2\). The two codebooks are explicitly exhibited, their shadow disjointness and perfect coverage checked, and their linearity verified. Two independently structured executable programs produce the same optimum and exact number of equality cases. This is a finite theorem, not an inference from an incomplete finite search.

## Originality — PASS, subject to residual historical risk

The full accessible text of Schoeny et al., arXiv:1602.06820v2, defines the same contiguous-deletion channel, establishes equivalence with burst insertion, and derives a non-asymptotic general upper bound. At the present parameter their Theorem 4 permits nine words, and their constructions do not present a labeled equality census. Cheng et al. (2014) explicitly study three or more adjacent deletions. Searches for aliases, perfect burst-deletion packings, exact size tables, the precise parameter, and published research records identified no stronger or equivalent size-six classification. The OEIS entry A057591 concerns **unrestricted** two-deletion correction and cannot imply this different channel's eight-word classification. Earlier original Levenshtein (1967) work was not available in full; an unpublished or unindexed older enumeration remains possible, and database silence is not a novelty proof.

## Value — PASS

This resolves the complete equality layer at the first length with three disjoint two-bit deletion windows, a natural finite test case for burst synchronization. The result exhibits a sharp, transparent transversal improving the general bound from nine to eight; moreover, every optimum must be one of two three-dimensional linear codes, and both are perfect output partitions. The forced linearity and rigidity of an a priori unrestricted nonlinear packing are substantively stronger than a routine construction or an arbitrary checksum slice. The scope is exact length six only, and it is not a theorem for arbitrary or at-most-two deletions.

Self-review: passed. Independent audit: not yet performed.
