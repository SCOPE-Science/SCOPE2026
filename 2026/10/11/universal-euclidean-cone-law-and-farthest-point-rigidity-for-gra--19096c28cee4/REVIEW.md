# Scientific review: universal Euclidean cone law

## Correctness — PASS

The signed-endpoint representation is exact for unweighted graphical zonotopes. The cone norm expansion subtracts precisely \(4\big(k(m-k)+\sum_{i\in S}d_i\big)\); the cut sum is bounded below by minus the crossing-edge count, itself at most \(k(m-k)\). Uniform spoke signs attain the upper bound for every original norm-maximizer. The two equality defects must vanish separately, proving the complete-cut criterion. For bipartite graphs, the local degree bound is sharp exactly for componentwise source/sink orientations, and a complete cut with any internal edge would make a triangle. The resulting contact counts include isolated vertices correctly. The proof covers all finite graphs in the stated domain and does not infer infinitary correctness from finite enumeration.

The packaged exact-integer checker enumerates 1,104 graphs, 431 bipartite, and all their signed endpoint choices. This is corroboration rather than a proof for arbitrary graph size.

## Originality — PASS, with residual risk

Padrol–Pilaud–Poullot (arXiv:2111.12422, Sections 1–2) derive deformation-cone structure; Chapoton–Pilaud (arXiv:2201.06896, Sections 1.4, 2.3, 2.4, Proposition 98 and tables) establish graph joins as zonotope shuffles and combinatorial vertex/facet information. These are pertinent **background identities**, not a result about the Euclidean norm maxima of the shuffle. The latter theorem therefore does not follow by simply matching a title or operation name. The apparently close “diameter of lattice zonotopes” paper (arXiv:1905.04750, introduction) expressly concerns the graph of the polytope, not ambient Euclidean distance.

A related complete-multipartite Euclidean circumradius formula already implies examples where the base graph is complete bipartite, as well as complete-graph examples. Those are acknowledged as covered *special cases*, not separately presented as discoveries. The general all-graph identity, the complete-cut characterization, and the four-contact rigidity for connected bipartite non-complete-bipartite bases go beyond that special-case coverage. Semantic search and direct primary-text checks did not find the full combination. This is evidence for originality, not proof of absolute priority; support-function/graph-orientation literature could contain the same lemma under a different name.

## Value — PASS

Coning is a canonical graph operation and is exactly a shuffle with a point in the zonotope literature. The theorem controls a non-affine Euclidean extremal invariant by a universal squared increment independent of the base graph, not merely a numerical result for a chosen small graph. Its equality-cut rigidity classifies all extremal contact points; the bipartite corollary shows a sharp distinction between complete bipartite and every other connected bipartite base. It supplies usable exact metric data for infinite families (including all fans over long paths) without computing their acyclic-orientation vertices individually. These are structural metric results rather than a change of symbols or a tiny numeric improvement.

## Closest literature and limitations

Sources: arXiv:2111.12422 (graphical zonotopes and deformations); arXiv:2201.06896 (join/shuffle operation and enumerations); arXiv:1905.04750 (distinct graph diameter invariant). Exact first-public dates, code domain and residual earlier-equivalence risk are documented with the finding. Only simple unweighted graphs and ordinary Euclidean distance are claimed. The same-model examination is not independent validation.

Same-model review: passed. Independent audit: not yet performed.
