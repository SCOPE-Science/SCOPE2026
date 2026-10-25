# Scientific review: clique-prism higher-cut symmetry

## Correctness (C): PASS
The claim is precisely scoped to the ordinary cut complexes \(\Delta_k(K_n\square K_2)\) with \(n\ge k\ge4\). Any complementary vertex set is a face of the Alexander dual exactly when it occupies fewer than \(k\) columns, or lies entirely in one layer. The dual therefore equals the union of the occupied-column truncation \(B\) and the two layer simplices. Each layer skeleton embeds into \(B\) by an equivariant homotopy equivalence: its retraction is contiguous to the identity. The relative long exact sequence computes a single homology group and its natural \(S_n\)-module, and the layer involution exchanges its two relative summands while acting trivially on the shared lower homology. The sign twist \((-1)^n\) in equivariant Alexander duality changes its eigenvalue from \(-1\) to \((-1)^{n+1}\). The standard exterior-power identity then gives the hook representation.

The standalone program independently checks graph-induced disconnected sets, signed simplicial traces and exact mod-two ranks for small parameters; see `VERIFICATION.md` for precise counts and limits. The infinite-parameter theorem rests on the supplied proof, not on numerical extrapolation.

## Originality (O): PASS, with bounded search risk
The primary paper *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, Theorem 7.19 and Section 7.3, explicitly proves the **nonequivariant** wedge-of-spheres homotopy classification for the identical objects and parameters; this is treated as prior knowledge, not a new result. Its table separately lists equivariant results for multipartite graphs and cycles, but no prism symmetry representation. Its prism proof gives an element matching that is not shown to be equivariant under the full natural symmetry group.

The close public mathematical finding *Integral and equivariant homology of three-cut complexes of rook graphs* proves a different, cut-size-three statement for \(K_m\square K_n\) with \(m,n\ge3\); it neither includes a factor \(K_2\) nor any \(k\ge4\). The published *Complete coordinate-symmetry homology of Hamming-graph total two-cut complexes* treats cut size two, not higher ordinary cuts. The original paper's complete-multipartite formula concerns a different graph product. A later paper *Topology of Cut Complexes II* concerns disjoint graph unions and path-based families; only its public abstract/metadata were inspected, so an unexpectedly related detail remains a lower-confidence possibility. Query terms included clique prism, ordinary cut, hook Specht representation, Alexander dual skeleton, and layer exchange.

No mathematically equivalent or stronger published statement was identified after comparing objects, parameters, and implications. This is not proof of priority. Exact comparisons, searched source titles and remaining risks appear in `AUDIT.json`.

## Mathematical value (V): PASS
This determines **all degrees and the entire irreducible rational representation** of the full natural automorphism group across an infinite two-parameter family. Previous sphere ranks alone cannot distinguish a trivial sum of lines from an irreducible hook, nor the parity-dependent action of the global layer swap. The simple character-generating formula yields every symmetry trace and rules out invariant classes. The problem is motivated by the primary paper's explicit homotopy classification and its separate study of equivariant topology for other graph families; it is not an arbitrary finite slice or a recomputation of a known Betti table.

## Scope and residual limits
Only rational homology actions are classified; no integral-lattice action or equivariant homotopy splitting is asserted. Standard combinatorial Alexander duality is used with its full vertex-permutation orientation twist. Small finite tests do not certify the theorem beyond their ranges. Unindexed or differently formulated equivalent published work may remain.

Self-review: passed. Independent audit: not yet performed.
