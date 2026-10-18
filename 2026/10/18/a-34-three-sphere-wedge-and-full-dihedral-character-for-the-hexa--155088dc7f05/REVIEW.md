# Scientific review: hexagonal-antiprism two-independence complex

## Correctness — PASS

The object is exactly the 12-vertex cyclic-distance-one-or-two graph and the induced-component-size-at-most-two complex. Every nonempty subset (4095 possibilities) is covered by the local degree-at-most-one criterion. The supplied 243-pair matching covers 486 of the 521 nonempty faces. Every matched inclusion and all 1800 Hasse covers are checked; a complete topological order excludes a closed gradient path. The remaining 0/3-dimensional critical cells prove the integral wedge of 34 three-spheres by discrete Morse theory, not merely a homology calculation. A distinct three-vertex-path forbidden-triple face enumeration and mod-two boundary reduction separately confirm third Betti number 34. The exact signed Lefschetz computation on all 24 group elements gives the stated character and invariant dimensions. The automorphism group is proved to be dihedral by the graph-intrinsic common-neighbor distinction between cycle and length-two edges.

## Originality — PASS, with residual risk

The closest primary sources give a general theory of higher-independence complexes, a tree-family theorem, and complete-multipartite three-path-free classifications. None states or implies an exact classification for the hexagonal antiprism, which is neither a tree, chordal, nor complete multipartite. The equivalent name 'three-path-free complex' was included in the search. Accessible prior mathematical records for cycle-square triangle-free complexes, cycle-power cut complexes, antiprism matching complexes, and hexagonal-prism cut complexes are distinct constructions; none determines the present forbidden-induced-path complex or its dihedral character. This is an evidence-based novelty comparison, not proof of global uniqueness; inaccessible and unindexed overlapping mathematics remains a risk.

## Mathematical value — PASS

The hexagonal antiprism is a canonical vertex-transitive planar polyhedral graph (the square of a 12-cycle), and its two-independence complex is a natural nonchordal test case for new higher-independence theory. Despite having simplices through dimension five, its exact integral homotopy type is a wedge of 34 spheres in dimension three; the complete dihedral character exhibits four global rational homology invariants and a nontrivial half-turn splitting. These precise invariants are not implied by the known tree and complete-multipartite classes and provide a nontrivial benchmark for a natural infinite cyclic-square family. No general family theorem or shellability conclusion is claimed.

## Closest literature and limits

R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150 (first posted 2026-05-24); P. Deshpande, S. Goyal and R. Sawant, *On a Complete Characterization of Path-Free Complexes Associated with Complete Multipartite Graphs*, arXiv:2607.05358; P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775. The exact result is limited to the labeled 12-vertex graph, and no wider antiprism homotopy pattern is established. Verification scripts depend only on Python's standard library. The scientific result has not undergone independent assessment.

Self-review: passed. Independent audit: not yet performed.
