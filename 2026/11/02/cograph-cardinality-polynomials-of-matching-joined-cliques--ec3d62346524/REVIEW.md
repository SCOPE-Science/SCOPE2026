# Scientific review

## Correctness

**PASS.** In two cliques joined by a matching, every induced four-vertex path uses a joining edge as its unique cross-clique middle edge. This gives a necessary-and-sufficient structural criterion for induced cographs. Counting its three exhaustive classes gives the first polynomial; testing each class for vertex-addition maximality gives the second. The proof handles every integer parameter with \(3\le t\le\min(a,b)\), including the endpoint \(t=3\), when the bridge-free maximal coefficient can vanish. A graph-level checker tested all \(320832\) vertex subsets across \(57\) graph instances, including direct induced-path and inclusion-maximality tests. These tests corroborate rather than replace the unrestricted proof.

## Originality

**PASS, with provisional publication priority.** Brosse et al., *Efficient enumeration of maximal split subgraphs and induced sub-cographs and related classes* (arXiv:2007.01031, Section 4), establish a polynomial-delay general-purpose algorithm for listing maximal induced cographs. Their construction and theorem do not give the closed coefficient formulas or the classification by two-clique matching patterns. Cao's *Enumerating Maximal Induced Subgraphs* (arXiv:2004.09885, introduction and theorem inventory) covers broader enumeration algorithms but not these graph-family counts. Dąbrowski, Lozin and Stacho explicitly identify the broad graph class as co-bipartite matching graphs, and prove partition algorithms, not induced cograph coefficient identities. Published descriptions of the two-row rook graph identify its matched subfamily, without counting its maximal induced cographs. Relevant indexed claims on cograph extremal graphs, matching-deleted bipartite graphs and rook-graph cluster subgraphs concern different properties; their statements neither imply the two formulas nor determine the cardinality gaps. The possibility of a differently indexed prior formula remains a residual risk.

## Mathematical value

**PASS.** Minimal vertex deletions to a hereditary graph class are a natural enumeration problem. The theorem solves the complete labelled cardinality census of induced cographs and inclusion-maximal induced cographs throughout a three-parameter, canonical co-bipartite matching family, rather than just its maximum or minimum size. Boundary corrections when one clique has no unmatched vertices quantify a genuine structural transition. The symmetric complete-prism specialization yields arbitrarily long gaps between attainable sizes even in connected vertex-transitive graphs, as well as asymptotic concentration of maximal cographs at one size.

## Limits

The result concerns vertex-induced cographs, not edge-deletion versions. The maximal-set formula requires at least three matching edges. It does not cover arbitrary cross-clique graphs. Computational evidence is finite, and publication priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
