# Review of Mixed fault-tolerant metric bases of crown graphs

## Correctness
PASS. For same-side crown vertices \(a_i,a_j\), the complete distinguisher set is \(P_i\cup P_j\); mixed fault tolerance therefore forces at least two selected vertices across every two deleted-matching pairs and gives the lower bound \(n\). Equality forces exactly one selected endpoint in every \(P_i\). Explicit one-hole-transversal coordinate formulas make the vertex and edge codes separately injective and reduce every possible vertex-edge collision to an incident pair; those collisions occur exactly when one bipartition contributes one or two selected landmarks. Applying the one-hole lemma after every landmark deletion gives precisely the pure transversals or the transversals with at least four selected vertices on each side. Exhaustive checks for \(4\le n\le9\) agree.

## Originality
PASS. The foundational mixed-metric paper was inspected in searchable full text: it treats cycles, complete bipartite graphs, trees, and grids and contains no crown treatment. The 2022 paper introducing the mixed fault-tolerant notion was inspected at its definition, existence theorem, girth construction, conclusion, and searchable family terminology; it gives no crown specialization. Targeted semantic and exact-phrase searches under crown graph, \(K_{n,n}\) minus a perfect matching, bipartite double cover, mixed fault tolerance, and MFTM terminology located no equivalent theorem. The closest crown results concern different metric or domination variants and do not imply two-landmark mixed resolution after every deletion.

## Value
PASS. The result gives an exact minimum, every minimum configuration, and a closed basis count for a canonical highly symmetric family under a robustness requirement. The threshold at \(n=8\) is structural: minimum size remains \(n\), but mixed-orientation bases become possible exactly when four redundant landmarks can remain on both sides after any one failure. This materially sharpens the general existence/construction theory.

Self-review: passed. Independent audit: not yet performed.
