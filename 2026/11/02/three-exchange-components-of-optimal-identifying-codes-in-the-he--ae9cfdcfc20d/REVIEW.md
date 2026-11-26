# Independent mathematical audit

## correctness

PASS

The cyclic triples and nonzero binary vectors with orthogonal incidence give the same Fano plane. A set identifies exactly when it hits every closed neighborhood and every pairwise symmetric difference of closed neighborhoods. The independent hitting-set replay at /workspace/branches/01391297-e8b9-4d0c-969e-0b47611a0409/replay_hitting_set.py exhausted all 9908 subsets of sizes 0 through 7, verified none below 7, and found 268 at size 7. The multiplicities by selected-point count are 1,21,0,112,112,0,21,1. With one exchange the two gaps isolate the three blocks by point count; for the outer blocks the 21 codes next to the all-one-part universal vertex are indexed by incident flags, and two are joined exactly when they share a point or a line. This gives the two K1 joins of L(H), each with 63 edges. The replay used the full pairwise symmetric-difference criterion (cardinality 2 for one exchange, 4 for exactly two), not a heuristic neighbor search. It found (22,22,224) components, 658 edges, degree counts 56 at degree 4, 210 at 5 and two at 21, and eccentricity 6 throughout the middle component (532 edges). The at-most-two union has one component, 4438 edges and eccentricity multiplicities 224 at 3, 42 at 4 and two at 5. The two missing point-count levels force any path from 0 to 7 to traverse all six available levels, giving a mathematical lower bound of five moves independently of all-source BFS. Exactly-two-only has sizes 1,1,266, in agreement with the direct isolation argument for the pure-part codes. The argument covers unrestricted endpoint-valid replacements at radius one only.

## originality

PASS

The supported distinct contribution is the detailed unrestricted exchange structure and sharp at-most-two versus exactly-two behavior, not the definition of identification, the Johnson embedding, or priority for the 268 census or three-component count in isolation. The nearest same-object record explicitly reports overlap for the census and the three one-jump components including the 224-state component, but its theorem is the adjacency-constrained slide forest, and its jump remark does not supply the detailed metrics or two-exchange results. That remark alone does not identify a separate exact source or establish precedence over the frozen record.

## value

PASS

The Heawood graph is the canonical smallest projective-plane incidence graph. Its minimum-code states give a concrete, nontrivial benchmark for how allowing larger moves changes reachability: one-exchange fragmentation survives even in a symmetric graph, allowing at most two replaces it by diameter-five connectivity, and requiring exactly two again strands two states. The explicit join components and middle eccentricity provide structural information about this benchmark beyond a recomputed optimum or state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
