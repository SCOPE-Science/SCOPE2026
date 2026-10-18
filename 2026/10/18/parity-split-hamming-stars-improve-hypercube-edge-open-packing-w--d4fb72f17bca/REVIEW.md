# Scientific review

## Correctness (PASS)

The infinite claim follows from the explicit binary Hamming parity-check matrix with one copy of every nonzero column. Its code has exactly \(2^{h-k}\) words and pairwise minimum distance at least three; radius-one balls are disjoint and exhaust \(2^h\) vertices. A weight-three codeword guarantees equal even and odd halves, and equal parity improves mutual center distance to at least four. The corresponding full neighborhood stars are induced-disjoint within fibers. Opposite parity in adjacent fibers means their occupied vertex supports are disjoint, ruling out every cross-fiber edge. Counting fibers, centers, and spoke edges gives the stated lower bound for every admitted integer dimension.

The exact claim for \(Q_5\) has a finite exhaustive certificate. Cube-edge compatibility is defined directly using binary adjacency. The bitset clique branch-and-bound pruning is justified by greedy proper vertex colorings, because a clique uses at most one vertex from each color class. The anchored maximum is twelve; a distinct increasing-index enumerator counts exactly twelve anchored maximizers. Cube edge-transitivity and double counting give eighty global maximizers. An independent explicit eighty-member family gives the matching constructive classification. The search source and recorded outputs are supplied; this is an exact computational proof for \(Q_5\), not an inference from a few samples.

## Originality (PASS, with priority risk)

The exact closest full-text source is Brešar–Dravec–Hedžet–Samadi, arXiv:2406.04020v2, Section 5.1. Its Table 1 explicitly records \(\rho_e^{\mathrm{o}}(Q_5)\ge10\), and it derives only \(\rho_e^{\mathrm{o}}(Q_9)\ge153\) from its present methods. Its Theorem 5.10 gives equality in power-of-two dimensions, but does not imply either the exact five-cube classification or the new nine-cube construction. Proposition 5.9 and Corollary 5.8 connect distance packings and EOP lower bounds, but do not supply the parity-lift across arbitrary spare coordinates. The complete accessible 2026 paper by Das–Santra, arXiv:2610.02275v1, treats edge-open-packing algorithms in other graph classes; it neither states nor entails this construction or exact census. The known equivalence to induced star forests was explicitly searched, not treated as a novelty argument. Relevant mathematical-record searches also returned no overlapping claim. Searches cannot guarantee publication priority; additional obscure or unindexed results may exist.

## Value (PASS)

The five-cube was an explicit unresolved lower-bound entry in a published study: the exact value twelve, exact eighty optimal subsets, and single-orbit structural classification close this natural concrete instance. The parity-split Hamming construction provides an entire infinite family of feasible induced-star forests, explaining an interaction between error-correcting perfect codes and Cartesian graph products. At nine dimensions its constructive lower bound improves the published value \(153\) to \(224\), a nontrivial step toward the known general upper bound \(256\). Both the exact finite gap closure and the infinite method give reusable mathematical information, rather than an arbitrary parameter slice.

## Literature and remaining limits

- B. Brešar et al., *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v2, especially Section 5.1, Table 1 and Theorem 5.10.
- G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs*, arXiv:2610.02275v1 (first posted 2026-10-01), complete accessible mathematical text.

The five-cube upper bound depends on a fully disclosed exact search; it is not claimed to follow solely from the infinite Hamming construction. Higher-dimensional bounds may not be optimal; bibliographic coverage may be incomplete. Independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
