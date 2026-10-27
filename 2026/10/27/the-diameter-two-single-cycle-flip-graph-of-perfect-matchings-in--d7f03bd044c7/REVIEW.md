# Scientific review: single-cycle matching flips on Fisher-expanded prisms

## Correctness — PASS

The all-order proof starts with the explicit Fisher bijection between perfect matchings and even base subgraphs. The local triangle matching rule is unique in both degree-zero and degree-two cases. Every pairwise matching symmetric difference decomposes into the lifts of exactly the simple-cycle components of the base even-subgraph difference. A direct binary encoding \((a,x)\) of all even subgraphs of \(C_n\square K_2\) gives the complete adjacency criterion: opposite \(a\)-classes are fully joined; within one class, adjacency holds exactly when \(x+y\) is a nonempty proper circular interval. It yields the graph join, degree and distance distribution for **every** integer \(n\ge3\). Independent finite programs confirm the Cayley interpretation for \(3\le n\le9\) and check actual expanded-graph perfect matchings and all pairwise cycle flips for \(3\le n\le7\). Those computations are corroboration and are not used as proof of the universal statement.

## Originality — PASS (qualified)

Ciucu–Liu–Yang (2012, DOI 10.2206/kyushujm.66.291, Proposition 5 and Theorem 1) already provides the Fisher matching correspondence and universal count. Grimmett–Li (2012/2013, arXiv:1208.5019) studies the same triangle construction for self-avoiding walks. Bošković (2026, arXiv:2607.16101) addresses flip connectivity of decorated graphs and upper bounds on permitted cycle lengths. The specific complete prism-family reconfiguration graph, exact degree, and uniform **two moves irrespective of order** are not stated by these inspected results and do not follow from their numerical matching enumeration or cycle-length bound alone. Searches also considered cycle-space XOR of simple cycles and planar dual bonds. Equivalent formulations in unindexed material remain a priority risk.

## Mathematical value — PASS

For an infinite family of nonbipartite cubic expansions with exponentially many perfect matchings, the theorem determines not just connectivity but the **entire exchange adjacency graph**. The surprising diameter-two conclusion is sharp for every order, despite the number of states growing exponentially. The two-layer circular-interval Cayley description explains why every state can be reached in at most two *single*-cycle flips and yields a closed local-mobility degree formula. This is not merely a restatement of the old perfect-matching count. It makes no assertion about mixing time or short-cycle-only flips.

## Closest literature and limitations

The most relevant antecedent is the exact Fisher even-subgraph bijection in Ciucu–Liu–Yang. The strongest nearby dynamics treatment inspected is Bošković's 2026 paper; its general flip-connectivity/cycle-length estimates do not classify the present state graph. Full priority against unindexed equivalent results is not established. This review checks the written proof and independent program outputs but does not constitute outside expert or independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
