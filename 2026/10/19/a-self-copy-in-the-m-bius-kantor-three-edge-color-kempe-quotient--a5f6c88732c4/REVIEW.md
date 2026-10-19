# Scientific review: Möbius–Kantor edge-color Kempe quotient

## Correctness
PASS. `verify.py` exhaustively constructs all 33 perfect matchings, all 20 unlabeled three-factorizations, and all 120 labeled three-edge-colorings. Independent direct edge-color backtracking agrees with matching-based enumeration. Two distinct quotient-adjacency tests agree; an explicit state-to-vertex bijection verifies both edges and nonedges of the full sixteen-state Möbius–Kantor component. All-source shortest-path checks establish the named-state metrics. The scope is a single finite graph, and the code does not establish a result for an infinite family.

## Originality
PASS, with uncertainty. The prior class-count census by Goedgebeur and Östergård covers the existence of two Kempe equivalence classes in this small graph; that count is prior art, not the new result. The inspected Belcastro–Haas structural papers and relevant source tables do not give the explicit quotient graph type \(K_{1,3}\sqcup M\), the identity of the sixteen-state component with the original graph, or the labeled component metrics. Searches also compared terminology for named edge-colorings, unlabeled one-factorizations, and connected alternating-cycle moves. A related prior matching-flip problem is not the same state space or operation. Unindexed equivalent work remains possible; a failed search is not uniqueness proof.

## Value
PASS. The self-copy component is a non-obvious structural phenomenon of a natural optimal-coloring reconfiguration problem, supplemented by a distinct star component and exact named-state distances. General class counts cannot supply this geometry.

## Closest literature and limitations
Belcastro and Haas, arXiv:1209.1730 and *Australasian J. Combin.* 69 (2017), develop the underlying equivalence graphs. Goedgebeur and Östergård, arXiv:2105.01363, determine class counts in small cubic graphs. McDonald, Mohar and Scheide, arXiv:1005.2248, establish a related four-edge-color connectedness theorem, not this three-color quotient metric. This is an exact finite result without a claimed canonical isomorphism. Unindexed prior exact calculations might overlap. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
