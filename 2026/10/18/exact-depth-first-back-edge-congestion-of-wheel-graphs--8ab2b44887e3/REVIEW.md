# Scientific review: depth-first congestion of wheel graphs

## Correctness
PASS. The lower bound isolates the two DFS-tree edges incident with the hub when internal. A DFS prefix before hub discovery must be a contiguous rim path, and its complement is connected; therefore every remaining rim vertex lies in the unique first child subtree of the hub. The corresponding cuts contain respectively \(a+2\) and \(n-a+2\) edges, giving the bottleneck \(\max\{a+1,n-a+1\}\). Root/leaf hub cases are handled separately for \(n\ge4\). A balanced Hamiltonian DFS path reaches the lower bound without enveloping arcs. The wheel has classical spanning-tree congestion three and treewidth three by the given elementary proofs. A standalone program independently checks the full arc definition for all 2,380 ordered DFS traversals through nine rim vertices, including branching trees, and the construction through 500 rim vertices. Finite tests do not replace the infinite proof.

## Originality
PASS on examined sources, with residual risk. The June 2026 initiating paper gives definitions, \(\operatorname{DTC}\le\operatorname{KLX}\), low-value characterizations, and a degree-based bound, but no wheel exact evaluation. The published complete/bipartite and balanced multipartite KLX evaluations have disjoint nontrivial graph domains; only the excluded four-vertex wheel is already covered by the complete-graph result. The ordinary spanning-tree-congestion problem allows the hub star and has value three, whereas the new DFS value grows linearly. Named and alias searches did not identify a covering wheel result. Unindexed prior calculations or a theorem stated using DFS-normal-tree congestion remain possible.

## Value
PASS. The exact solution treats the canonical planar, three-connected apex-cycle family, and the crossing-only equality proves that enveloping arcs are unnecessary in an optimum even though branching DFS trees exist. The unbounded ratio between depth-first and unconstrained tree congestion on a fixed-treewidth family quantifies a natural constraint in the newly introduced traversal model. This is stronger than merely deriving growth from the known hub-degree bound, and supplies exact benchmarks for DFS congestion algorithms.

## Limits and closest literature
The scope is precisely \(K_1\vee C_n\), \(n\ge4\), and does not classify other apex graphs. Source comparisons: Bourotte–Ducloz–Orponen–Seki (arXiv:2606.24675v1); published complete and complete-bipartite evaluation (record b27f97da8029); published balanced complete multipartite evaluation (record d7d7a1fe0f08). Independent bibliographic validation remains desirable.

Self-review: passed. Independent audit: not yet performed.
