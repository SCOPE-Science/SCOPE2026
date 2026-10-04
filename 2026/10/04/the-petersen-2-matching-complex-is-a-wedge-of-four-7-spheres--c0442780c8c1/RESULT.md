# The Petersen 2-matching complex is a wedge of four 7-spheres
## Finding
For the Petersen graph \(P\), the \(2\)-matching complex \(M_2(P)\) is homotopy equivalent to a wedge of four \(7\)-spheres: \(M_2(P)\simeq\bigvee^{4}S^{7}\).

## Assumptions and scope
Let \(P\) be the Petersen graph on vertices \(0,1,\ldots,9\) with edge set
\[
\{01,12,23,34,04,05,16,27,38,49,57,68,79,58,69\}.
\]
The \(2\)-matching complex \(M_2(P)\) has these fifteen graph edges as its vertices, and a set of graph edges is a face exactly when every vertex of the induced subgraph has degree at most \(2\). This is the bounded-degree / higher-matching convention used in the cited literature.

## Proof
Order the fifteen vertices of \(M_2(P)\) by the displayed edge order. Starting from the nonempty face poset, repeatedly perform element matching (toggle matching) on each complex vertex in that order, removing each matched pair before moving to the next vertex. Repeated element matching is acyclic by the standard patchwork argument for discrete Morse matchings.

Exhaustive enumeration gives the face vector
\[
(f_0,f_1,\ldots,f_9)=(15,105,445,1245,2358,2985,2400,1095,215,6).
\]
The repeated-toggle matching contains \(5432\) pairs. Exactly five faces remain unmatched: one \(0\)-simplex and four \(7\)-simplices. The four critical \(7\)-simplices, written as graph-edge sets, are
\[
\begin{aligned}
&\{12,04,16,27,49,68,79,58\},\\
&\{23,04,05,27,38,68,79,69\},\\
&\{12,34,16,38,49,57,58,69\},\\
&\{23,04,05,27,49,68,58,69\}.
\end{aligned}
\]
Thus discrete Morse theory gives a CW complex with one \(0\)-cell and four \(7\)-cells and no cells in dimensions \(1,\ldots,6\). Since there are no lower positive-dimensional cells to support nontrivial attaching maps, this CW complex is the wedge \(\bigvee^4 S^7\).

## Verification
The accompanying verifier reconstructs the Petersen graph and all faces of \(M_2(P)\), checks the face vector, rebuilds the repeated-toggle matching, checks every pair is a codimension-one face relation, orients all \(63780\) Hasse edges with matched edges reversed, and verifies acyclicity by a complete topological sort of the directed Hasse graph. It also independently computes mod-\(2\) simplicial homology and obtains reduced Betti number \(4\) in degree \(7\) and \(0\) in every other degree.

The Euler characteristic is
\[
15-105+445-1245+2358-2985+2400-1095+215-6=-3,
\]
which agrees with \(\chi(\bigvee^4S^7)=-3\).

## Relationship to prior work
Vega introduced and studied \(2\)-matching complexes using discrete Morse theory and repeated element matchings, with explicit families including wheel and caterpillar graphs. Singh studied higher matching complexes and emphasized that exact homotopy types are known for only a few graph classes, proving wedge-of-spheres results for selected complete and complete-bipartite cases. The searches used for this result found no statement giving the homotopy type of the Petersen graph's \(2\)-matching complex; in particular, the Petersen graph does not belong to the complete, complete-bipartite, tree, wheel, or cycle families covered by those results.

## Limitations
This is a single-graph homotopy computation. It does not assert a formula for all cubic graphs, generalized Petersen graphs, or all higher matching complexes. The originality check is a targeted comparison against the named primary literature, web searches under standard aliases, and the available result database; absence from those searches is evidence but not a proof of absolute novelty.

## References
1. Julianne Vega, “2-Matching Complexes,” arXiv:1909.10406, first posted 2019-09-23.
2. Anurag Singh, “Higher matching complexes of complete graphs and complete bipartite graphs,” arXiv:2006.13632, first posted 2020-06-24.
