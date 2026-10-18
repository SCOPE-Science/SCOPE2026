# Planar colour-refinement twins of every nontrivial rectangular grid

## Finding

Let \(G_{m,n}=P_m\mathbin\square P_n\) denote the simple undirected Cartesian grid, with \(2\le m\le n\). For every \((m,n)\ne(2,2)\) there is an explicit graph \(H_{m,n}\), on the same vertex set, satisfying all of the following:

1. \(H_{m,n}\) is **connected and planar**.
2. \(G_{m,n}\) and \(H_{m,n}\) have identical vertex colours in **every round** of ordinary colour refinement, under the natural identification of their vertex sets. They therefore satisfy exactly the same \(C^2\) sentences (two-variable first-order logic with counting).
3. The number \(c_4\) of unoriented, unrooted, simple four-cycles obeys
   \[
   c_4(H_{m,n})-c_4(G_{m,n})=\begin{cases}
      +2,&(m,n)=(3,3),\\
      -2,&\text{otherwise}.
   \end{cases}
   \]
   In particular, these two connected planar graphs are nonisomorphic.
4. \(H_{m,n}\) is obtained from \(G_{m,n}\) by deleting exactly two edges and adding exactly two different edges: a single degree-preserving \(2\)-switch.

The exceptional grid \(G_{2,2}=C_4\) is identified by \(C^2\) even among **all** finite simple graphs. Consequently, among rectangular grids with both side lengths at least two, the sole graph identified by \(C^2\), even relative to the class of connected planar graphs, is \(C_4\). The planar-witness assertion, rather than unrestricted non-identifiability alone, is the principal refinement of existing general results.

## Assumptions and scope

All graphs are finite, loopless, simple and undirected. The logic uses only the adjacency predicate and equality, with no named coordinates, vertex colours, embedding, or order. A rectangular grid has vertex set \(\{(i,j):0\le i<m,\ 0\le j<n\}\) and edges at Manhattan distance one. The invariant \(c_4(X)\) counts subsets of four vertices spanning a simple cycle of length four, each unoriented cycle once; chords, if present, do not disqualify a cycle. In the present construction no such chord ambiguity affects the count.

Two-variable logic with counting is denoted \(C^2\). Its equivalence with ordinary colour refinement on finite graphs is classical; see the references. Planarity and connectedness are properties of the **witness**, not extra relations available to the logic.

## Proof

**1. Explicit construction.** Write \(a,b,c,d\) for four distinct vertices. The switch replaces existing edges \(ac,bd\) by previously absent edges \(ad,bc\). For \(3\le m\le n\), choose
\[
 a=(0,0),\quad b=(m-1,n-1),\quad c=(1,0),\quad d=(m-2,n-1).
\]
For \(m=2\) and \(n\ge3\), \(n\ne4\), choose
\[
 a=(0,0),\quad b=(1,n-1),\quad c=(1,0),\quad d=(0,n-1).
\]
For the single exceptional strip \((m,n)=(2,4)\), instead choose
\[
 a=(0,0),\quad b=(0,3),\quad c=(0,1),\quad d=(0,2).
\]
In each case the four vertices are distinct; both removed edges exist and both added edges are absent. The replacement is therefore a valid simple-graph \(2\)-switch.

**2. Colour refinement and counting logic.** In the first two cases, half-turn rotation of the grid exchanges \(a\) with \(b\) and \(c\) with \(d\). In the exceptional strip, reflection across the middle of the long side has the same exchange property. Hence at every colour-refinement round \(t\), the original grid assigns equal colours to \(a,b\) and to \(c,d\), respectively.

Induct on \(t\) to show that the colour of *each named vertex* in the switched graph equals its colour in the original grid. This is immediate at round zero. At any subsequent round, vertices outside \(\{a,b,c,d\}\) have unchanged neighbour multisets. At \(a\) and \(b\), one neighbour is replaced by another having the same round-\(t\) colour (\(c\) and \(d\)); at \(c\) and \(d\), one neighbour is replaced by another having the same round-\(t\) colour (\(a\) and \(b\)). The updated colour signatures agree vertex-by-vertex. This completes the induction and proves \(C^2\)-equivalence. The argument establishes all-round equivalence, not merely agreement of terminal colour counts.

**3. Connectivity.** Every removed edge is a boundary edge of a unit grid square and thus lies on a three-edge detour. The two deleted edges belong to distinct unit squares, and the indicated detours avoid the other deleted edge. Thus deleting both edges does not disconnect the grid. Adding edges cannot destroy connectivity.

**4. Planarity.** For \(m\ge3\), the four endpoints occur around the external rectangular boundary in cyclic order \(a,d,b,c\). After removal of the two boundary edges, draw the new edge \(ad\) immediately outside the boundary arc from \(a\) to \(d\), and \(bc\) immediately outside the complementary boundary arc from \(b\) to \(c\). The arcs are disjoint, giving a plane embedding. For \(m=2\), \(n\ne4\), draw the new edges along the exterior of the two opposite long sides of the strip. For \((m,n)=(2,4)\), the resulting graph has four degree-two vertices and four degree-three vertices. It has no subdivision of \(K_5\), which would require five branch vertices of degree at least four, and no subdivision of \(K_{3,3}\), which would require six branch vertices of degree at least three. Kuratowski's theorem therefore proves that this graph is planar.

**5. Counting four-cycles.** The original grid has \(c_4(G_{m,n})=(m-1)(n-1)\), since its simple four-cycles are precisely the elementary unit squares. Each deleted boundary edge belongs to exactly one original four-cycle, and these two cycles are distinct. Exactly two four-cycles are lost. A new four-cycle containing both added edges would also need either both removed edges, or the two old edges \(ab\) and \(cd\); neither possibility occurs. Thus every new four-cycle contains exactly one added edge and corresponds to a length-three path, avoiding the deleted edges, between its endpoints.

If \(m\ge3\), the original Manhattan distance from \(a\) to \(d\), and from \(b\) to \(c\), is \(m+n-3\). This is at least four unless \((m,n)=(3,3)\). Consequently there are no new four-cycles in the nonexceptional cases. At \((3,3)\), each new edge has exactly two surviving length-three paths in the original grid (of the three monotone paths, one uses a deleted edge). Four new cycles are created, resulting in net change \(+2\).

If \(m=2\), \(n\ne4\), the old distance for each added edge is \(n-1\). It is at least four when \(n\ge5\); when \(n=3\) it is two, and the bipartite grid has no length-three walk between vertices at even distance. Hence no new four-cycles occur. For \((m,n)=(2,4)\), each added edge connects vertices at distance two in the original bipartite grid, again precluding a length-three path. The net change is therefore \(-2\) in every remaining case.

**6. The sharp exceptional case.** A graph indistinguishable from \(C_4\) by colour refinement has exactly four vertices, each of degree two. The only simple two-regular graph on four vertices is \(C_4\). Thus \(C_4\) is identified even among arbitrary simple graphs.

## Verification

The standalone program `verify.py` constructs both graphs and independently computes their round-by-round colour-refinement signatures, connectivity, planarity, and four-cycle counts, using NetworkX 3.6.1 for standard graph operations and planarity. `verification_output.json` records a successful complete parameter-grid test for every \(2\le m\le n\le18\), except \((m,n)=(2,2)\), totalling 152 cases. The code checks the exact change \(\pm2\), not merely nonisomorphism. The arbitrary-size theorem is proved above; finite tests are supplementary.

Reproduce with `python verify.py`. Expected environment: Python 3.11+ and NetworkX 3.6.1. No external data files are required.

## Relationship to prior work

Immerman and Lander established the correspondence between two-variable counting logic and colour refinement. Arvind, Köbler, Rattan and Verbitsky (2015) give a complete unrestricted characterization of colour-refinement-identified graphs; in particular their Lemma 6 explains why equitable-degree-preserving edge replacements retain refinement colours. Kiefer, Schweitzer and Selman (2015) independently characterize \(C^2\)-identified graphs. Such unrestricted results imply non-identifiability of many grids but **do not alone assert connected planar competitors or prescribe the exact four-cycle gap**. The contribution here is an explicit, uniform, single-switch construction producing connected planar competitors for every nontrivial grid and the sharp exception at \(C_4\).

## Limitations

The claim concerns one-dimensional colour refinement, equivalently \(C^2\), and **not** higher-dimensional Weisfeiler–Leman or unrestricted first-order logic. No claim is made that the switched witnesses remain rectangular grids or bipartite. General unrestricted non-amenability is already covered by earlier classification work. An independently discovered planar switch construction may precede this account; the literature comparison cannot exclude unindexed specialist examples.

## References

1. N. Immerman and E. Lander, “Describing Graphs: A First-Order Approach to Graph Canonization,” *Complexity Theory Retrospective*, pp. 59–81 (1990), DOI: 10.1007/978-1-4612-4478-3_5.
2. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, “Graph Isomorphism, Color Refinement, and Compactness,” arXiv:1502.01255, first posted 2015-02-04; ECCC TR15-032, revision 2 (2015), especially Lemma 6 and Theorem 9.
3. S. Kiefer, P. Schweitzer and E. Selman, “Graphs Identified by Logics with Counting,” arXiv:1503.08792, first posted 2015-03-30; in *Mathematical Foundations of Computer Science* (2015), especially Theorem 17.
