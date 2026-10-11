# Graph-like neighborhood complexes with edge-disjoint four-cycles

## Finding
Let \(G\) be any finite connected simple graph with \(v\) vertices and \(e\) edges. Suppose that \(G\) has exactly \(k\geq1\) distinct unoriented simple four-cycles, and **no edge of \(G\) lies in two distinct four-cycles**. Its Lovász open-neighborhood complex \(\mathcal N(G)\) has the following complete homotopy type:
\[
\mathcal N(G)\simeq
\begin{cases}
\displaystyle \bigvee^{\,2e-2v+1-2k}S^1,
  &G\text{ non-bipartite},\\[2mm]
\displaystyle\left(\bigvee^{\,e-v+1-k}S^1\right)
  \sqcup\left(\bigvee^{\,e-v+1-k}S^1\right),
  &G\text{ bipartite}.
\end{cases}
\]
Here a wedge of zero circles is a point. The displayed exponents are nonnegative under the hypotheses. In particular, the fundamental group of every component is free of the indicated rank, its integral first homology is free abelian of the same rank, and all integral homology in degrees at least two vanishes.

More structurally, form the canonical bipartite double cover \(D(G)\) of \(G\). Attach a triangulated two-disc along **each of its \(2k\) lifted four-cycles**, obtaining a simplicial complex \(W(G)\). There is a homotopy equivalence \(\mathcal N(G)\simeq W(G)\), and \(W(G)\) simplicially collapses onto the graph obtained by deleting one suitable edge from each lifted four-cycle. The edges can be chosen simultaneously without changing any connected component.

## Assumptions and scope
A four-cycle means an unoriented cyclic sequence of four distinct vertices whose consecutive pairs are edges; diagonals are allowed. Cycles are identified under cyclic rotation and reversal. The condition is that all such cycles are pairwise **edge-disjoint**. They may share a vertex, and triangles, longer cycles, bridges, vertices of arbitrarily large degree, and nonplanar structure are allowed. There are no isolated vertices because \(G\) is connected and has at least four vertices.

The open-neighborhood complex \(\mathcal N(G)\) consists of all nonempty vertex sets contained in \(N_G(u)=\{w:uw\in E(G)\}\) for at least one vertex \(u\), together with the empty face. It is not the closed-neighborhood complex. The double cover \(D(G)\) has vertices \(u_L,u_R\) for each \(u\in V(G)\), and edges \(u_Lv_R,v_Lu_R\) for each \(uv\in E(G)\).

## Proof
**1. Common-neighbor intersections.** Suppose two distinct vertices \(x,y\) have three common neighbors \(p,q,r\). Then \(x-p-y-q-x\) and \(x-p-y-r-x\) are different four-cycles sharing the edge \(xp\), contrary to the hypothesis. Thus \(N_G(x)\cap N_G(y)\) has at most two vertices. If its cardinality is two, say \(\{p,q\}\), then \(x-p-y-q-x\) is the unique four-cycle containing this opposite pair. Different four-cycles cannot share two vertices: if the shared vertices are adjacent, they share an edge; if opposite, the four-cycles together yield at least three common neighbors or a repeated edge, violating the preceding observation. Hence two four-cycles intersect in at most one vertex.

**2. The first good cover.** Cover \(\mathcal N(G)\) by the full simplices \(F_u=\Delta(N_G(u))\), indexed by \(u\in V(G)\). Each nonempty finite intersection is a simplex, hence contractible. Its nerve \(\mathcal I\) has a face on a set of centers \(U\) exactly when the vertices of \(U\) have a common neighbor. The finite simplicial nerve lemma gives \(\mathcal N(G)\simeq\mathcal I\).

**3. A matching good cover of a double-cover complex.** For each four-cycle \((a,b,c,d)\) in cyclic order, insert into \(D(G)\) the new right-side edge \(b_Rd_R\) and the triangles \([a_L,b_R,d_R]\), \([c_L,b_R,d_R]\). Also insert the new right-side edge \(a_Rc_R\) and the triangles \([b_L,a_R,c_R]\), \([d_L,a_R,c_R]\). Call the resulting simplicial complex \(W(G)\). Because distinct four-cycles have at most one vertex in common, no new right-side edge is duplicated.

For each center \(u\), let \(F'_u\) be the union of all edges \([u_L,w_R]\) for \(w\in N_G(u)\) together with all added triangles having apex \(u_L\), and all their faces. This is a cone on \(u_L\), even when several four-cycles pass through \(u\). The \(F'_u\) cover \(W(G)\). For two different centers \(u,w\), the intersection \(F'_u\cap F'_w\) is empty if they have no common neighbor; is a point if they have one common neighbor; and is the added right-side edge joining their two common neighbors if they have two. For three or more centers, any nonempty intersection is a point, since two distinct centers have at most two common neighbors, and sharing both with a third would produce overlapping four-cycles. Thus all nonempty finite intersections are contractible, and the nerve is again \(\mathcal I\). A second application of the nerve lemma gives \(W(G)\simeq\mathcal I\), hence \(\mathcal N(G)\simeq W(G)\).

**4. Exact simplicial collapses.** Each original four-cycle contributes two lifted four-cycles of \(D(G)\). The first is \(a_L-b_R-c_L-d_R-a_L\), filled by two triangles along the diagonal \(b_Rd_R\). The edge \([a_L,b_R]\) lies in exactly one triangle of \(W(G)\), because no original graph edge participates in two four-cycles. Collapse that triangle with the edge. The remaining triangle is then free along the inserted diagonal \([b_R,d_R]\), so collapse it with the diagonal. The second lifted disc collapses in the same way, first using the outer edge \([b_L,a_R]\), then the inserted diagonal \([a_R,c_R]\). For different original four-cycles these chosen outer edges and diagonals are distinct. Performing these \(4k\) elementary collapses removes all triangles and removes exactly one old double-cover edge per lifted four-cycle. Call the resulting graph \(D'\).

Every deleted old edge lies on a lifted four-cycle whose other three old edges remain, so removing it does not change the number of components. In particular \(D'\) has \(2v\) vertices and \(2e-2k\) edges. The standard parity-path argument shows that \(D(G)\), and therefore \(D'\), has two connected components precisely when \(G\) is bipartite; otherwise it has one. The cycle-rank formula for a finite graph with \(c\) components gives \(\beta_1(D')=(2e-2k)-(2v)+c\). When \(G\) is bipartite, the two original double-cover components are isomorphic copies of \(G\), each containing one lift of every four-cycle, so their individual ranks are \(e-v+1-k\). When \(G\) is not bipartite, the unique component has rank \(2e-2v+1-2k\). A connected graph is homotopy equivalent to a wedge of as many circles as its cycle rank. This proves every assertion.

## Verification
The self-contained Python file `verify.py` builds the graph complexes directly and performs exact binary boundary-rank computations, checks the two good-cover nerves face by face, and checks every proposed free-face collapse. It exhaustively tests every connected labeled graph with exactly one four-cycle on \(4,5,6\) vertices: respectively \(9,240,6480\) qualifying graphs, a total of \(6729\). It also tests nine larger two- or three-square examples, including squares sharing one vertex, bipartite and non-bipartite cases, and a maximum-degree-eight case. The deterministic output is provided in `verification_output.txt`. These finite checks corroborate the proof; the all-graph conclusion follows from the symbolic good-cover and collapse arguments, not from finite enumeration.

## Relationship to prior work
Kamibeppu (2008), Theorem 3, identifies the box complex of a **four-cycle-free** graph with its double-cover graph up to equivariant strong deformation retraction; it explicitly excludes graphs possessing even one four-cycle. Matsushita's work (public since 2012; Theorem 1.1 in the inspected preprint) identifies the **fundamental group** of a neighborhood complex with an even-length graph-walk group. That fundamental-group result does not by itself eliminate higher homotopy or give the present graph-like homotopy model. Shukla (2019), Theorem 2, gives a wedge-of-circles-or-point conclusion for most graphs of maximum degree at most three; that restriction excludes the arbitrary-degree graphs here. Tittmann (2024), Theorem 5.38, determines the **neighborhood polynomial** when four-cycles have restricted intersections; face-counting and Euler characteristic do not establish a complete homotopy type. Arana–Stehlík (2025) studies the different regime of non-bipartite surface quadrangulations whose Lovász complexes are surfaces. The present result concerns edge-disjoint-square graphs and gives a two-stage nerve comparison and explicit collapses, beyond the scope of these statements.

## Limitations
The graph has to be finite and connected, and **all** four-cycles must be pairwise edge-disjoint. Overlapping four-cycles can produce noncontractible intersections in the second good cover; the proof does not classify those cases. The theorem makes no assertion about natural equivariance or about a direct simplicial collapse of \(\mathcal N(G)\) itself; the displayed collapse is for the comparison complex \(W(G)\). Novelty comparisons cannot exclude unindexed equivalent proofs. The manuscript does not claim an independent mathematical audit.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public version 2012-10-10. https://arxiv.org/abs/1210.2803.
2. A. Kamibeppu, *Homotopy type of the box complexes of graphs without 4-cycles*, RIMS Kôkyûroku **1578** (2008), 67–70, especially Theorem 3. https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1578-13.pdf.
3. S. Shukla, *Homotopy Type of the Neighborhood Complexes of Graphs of Maximal Degree at most 3 and 4-Regular Circulant Graphs*, Electronic Journal of Combinatorics **26** (2019), P2.4, Theorem 2. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p4/pdf/.
4. P. Tittmann, *Graph Polynomials: The Eternal Book* (2024 draft), Section 5.2, Theorem 5.38. https://www.researchgate.net/publication/377572474_Graph_Polynomials_The_Eternal_Book.
5. C. Arana and M. Stehlík, *Quadrangulations and the Lovász complex* (2025), arXiv:2510.03698, Theorem 1.1. https://arxiv.org/abs/2510.03698.
