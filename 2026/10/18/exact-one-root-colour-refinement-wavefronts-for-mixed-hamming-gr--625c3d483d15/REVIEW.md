# Review of rooted refinement on mixed Hamming graphs

## Correctness

PASS. The graph-theoretic steps are exact: root-neighbour cliques determine coordinate sizes, shortest-path first-neighbour sets determine vertices, and the group action yields the orbit profiles. The wavefront induction works because every vertex has the same degree and a weight-\(t\) vertex has exactly \(t\) predecessor neighbours. For the next-round recovery step, the multiset of profile-deleted predecessors determines \((k_q)\) through \(\sum_q k_q(\mathbf{k}-\mathbf e_q)=(t-1)\mathbf{k}\). The exceptional weight-one base case is separated by the \(q-2\) within-shell neighbours. This also proves sharpness for both equal-factor and heterogeneous cases. Two fully executable standard-library verifiers independently reproduce exact partitions and depth across 3,014 factor tuples at the quotient level, including 18 graph-level instances. The finite calculations corroborate but do not establish the general result.

## Originality

PASS, with residual risk. The inspected graph-isomorphism and refinement paper establishes general refinability notions, not the explicit iterated refinement partition of a rooted mixed Hamming product; the Hamming-recognition paper establishes coordinate factorization but not colour dynamics. The known two-dimensional rook-graph and binary-cube boundaries overlap parts of the statement, but do not imply the exact result for arbitrary heterogeneous dimension \(d\ge3\). No matching stronger theorem was found in the targeted literature and research-record comparisons. The possibility of an unlocated specialized theorem remains and prevents a claim of certified publication priority.

## Value

PASS. The result gives a dimension-uniform exact answer, including *every intermediate partition*, exact class sizes, and a sharp depth dichotomy for a well-defined family of non-distance-regular Hamming products. Its explanation of the one-round delay between detecting distance and reconstructing heterogeneous support gives mathematical structure beyond a stand-alone computational table or a two-factor special case. It can serve as an explicit model for counting refinement on graphs with several coordinate alphabet sizes.

## Limits and comparison

The conclusions concern a single marked vertex, Cartesian factors that are complete, and orbit-refinement inside one graph; they do not establish isomorphism identification against arbitrary graphs. Imrich–Klavžar's Hamming recognition algorithm and Arvind–Köbler–Rattan–Verbitsky's general colour-refinement theory are the closest inspected primary foundations. The classical Cartesian automorphism theorem supplies group structure but not round-by-round counting signatures. An independent science audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
