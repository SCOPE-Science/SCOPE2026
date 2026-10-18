# Graph-like neighborhood complexes with edge-disjoint four-cycles

## Finding
Let \(G\) be a finite, connected, simple graph with \(v\) vertices, \(e\) edges, and exactly \(k\geq1\) distinct unoriented simple four-cycles. Suppose **no edge belongs to two distinct four-cycles**. Then its Lovász open-neighborhood complex has the complete homotopy type
\[
\mathcal N(G)\simeq
\begin{cases}
\displaystyle\bigvee^{\,2e-2v+1-2k}S^1,&G\text{ non-bipartite},\\[2mm]
\displaystyle\bigl(\bigvee^{\,e-v+1-k}S^1\bigr)\sqcup
\bigl(\bigvee^{\,e-v+1-k}S^1\bigr),&G\text{ bipartite}.
\end{cases}
\]
A zero-fold wedge is a point. Both multiplicities are nonnegative. Thus each component has a free fundamental group and free integral first homology of the stated rank; all higher integral homology vanishes.

More concretely, start with the canonical bipartite double-cover graph \(D(G)\), fill each of the \(2k\) lifted four-cycles by a pair of triangles, and call the resulting finite simplicial complex \(W(G)\). There are a homotopy equivalence \(\mathcal N(G)\simeq W(G)\) and \(4k\) elementary simplicial collapses taking \(W(G)\) to a graph obtained from \(D(G)\) by deleting precisely one suitable edge of each lifted square. These deletions preserve connected components.

## Definitions and exact scope
A four-cycle is a cyclic sequence of four distinct vertices joined consecutively by graph edges; diagonals are permitted. Cycles are identified up to reversal and cyclic permutation. Four-cycles are **edge-disjoint**, not necessarily vertex-disjoint: distinct four-cycles may share vertices, even two vertices, so no stronger vertex-intersection condition is implicit.

For a vertex \(u\), write \(N(u)=\{w:\{u,w\}\in E(G)\}\). The open-neighborhood complex \(\mathcal N(G)\) consists of all vertex subsets contained in some \(N(u)\), including the empty face. Let \(D(G)\) have vertices \(u_L,u_R\) for \(u\in V(G)\) and, for every undirected edge \(uv\), edges \([u_L,v_R]\) and \([v_L,u_R]\).

## Proof

**1. Common-neighbor bound, including the needed uniqueness.** Any two distinct vertices \(x,y\) have at most two common neighbors. Indeed, if they shared \(a,b,c\), the squares \(x-a-y-b-x\) and \(x-a-y-c-x\) would be different and share \(xa\), a contradiction. If they share exactly two, say \(a,b\), then \(x-a-y-b-x\) is the uniquely determined square with opposite pair \(\{x,y\}\). Every pair of opposite vertices therefore determines at most one square. Three distinct vertices cannot have two common neighbors, by the same overlapping-squares argument.

Importantly, this proof **does not** assert that different squares share at most one vertex: that stronger assertion is false. For example, the two cycles \(x-a-y-b-x\) and \(x-y-c-d-x\), with only the eight edges shown, are edge-disjoint four-cycles sharing \(x,y\). The common-neighbor bound and uniqueness of an *opposite pair* are the properties needed below.

**2. Nerve of the original neighborhood cover.** For each \(u\in V(G)\), let \(F_u=\Delta(N(u))\), the full simplex on its nonempty neighborhood. These simplices cover \(\mathcal N(G)\); every nonempty finite intersection is a simplex and hence contractible. The finite simplicial nerve lemma identifies the homotopy type of \(\mathcal N(G)\) with the nerve \(\mathcal I\): a set of centers \(U\) is a face exactly when \(\bigcap_{u\in U}N(u)\ne\varnothing\).

**3. A second good cover of the filled double cover.** For each square \(a-b-c-d-a\), adjoin to \(D(G)\) the diagonal \([b_R,d_R]\) and triangles \([a_L,b_R,d_R]\) and \([c_L,b_R,d_R]\), as well as the diagonal \([a_R,c_R]\) and triangles \([b_L,a_R,c_R]\) and \([d_L,a_R,c_R]\). Let \(W(G)\) be the union of \(D(G)\) with these added faces. The diagonals are distinct for different squares: coincidence of a right-side diagonal would give the same pair of opposite vertices and hence, by Step 1, the same square. This remains true even when two squares share two (non-equivalently positioned) vertices.

For each center \(u\), let \(F'_u\subset W(G)\) be the union of all edges \([u_L,w_R]\) with \(w\in N(u)\) and all added triangles with apex \(u_L\), together with their faces. It is a cone on \(u_L\), and the \(F'_u\) cover \(W(G)\).

If \(u\ne v\), the intersection \(F'_u\cap F'_v\) contains only right-side faces. It is empty when \(N(u)\cap N(v)\) is empty; a single vertex when there is exactly one common neighbor; and exactly the diagonal edge joining the two common neighbors when there are two. The last assertion follows because the unique square \(u-a-v-b-u\) contributes the edge \([a_R,b_R]\) to both cones. Since three different centers cannot all have two common neighbors, intersections involving three or more centers, if nonempty, are single right vertices. All nonempty multiple intersections of the \(F'_u\) are therefore contractible. Their nerve has precisely the same faces as \(\mathcal I\), so a second nerve-lemma application gives
\[
\mathcal N(G)\simeq\mathcal I\simeq W(G).
\]

**4. Collapses, with no overlap assumptions beyond edge-disjointness.** For each original square \(a-b-c-d-a\), first collapse the triangle \([a_L,b_R,d_R]\) with its outer edge \([a_L,b_R]\), then collapse the remaining triangle \([c_L,b_R,d_R]\) with the inserted diagonal \([b_R,d_R]\). The first outer edge is a free face: any triangle containing it must originate from a square using the original graph edge \(ab\), and edge-disjointness makes this square unique. After the first collapse, the right diagonal lies in just one triangle, because Step 1 makes the corresponding opposite-pair square unique. Perform the analogous two collapses in the other lift, first along \([b_L,a_R]\) and then along \([a_R,c_R]\).

Across different original squares, all chosen outer edges are distinct because original four-cycle edge sets are disjoint, and all inserted diagonals are distinct because each opposite pair determines at most one square. Consequently these free-face collapses do not interfere, even if squares share vertices. There are \(4k\) collapses in total, leaving a graph \(D'\) with \(2v\) vertices and \(2e-2k\) edges: the old double-cover edges except one edge per lifted square.

In \(D(G)\), each removed old edge belongs to a lifted four-cycle, and its other three old edges survive **all** removals because the original four-cycles were edge-disjoint. Therefore a length-three path remains between its endpoints, so deleting these edges changes no connected component.

**5. Component ranks and homotopy classification.** The parity-path criterion for a connected graph shows that \(D(G)\) has two components, each isomorphic to \(G\), when \(G\) is bipartite, and otherwise is connected. The same holds for \(D'\). A graph with \(V'\) vertices, \(E'\) edges and \(c\) components has total cycle rank \(E'-V'+c\), and each connected component is a wedge of that many circles.

For a non-bipartite \(G\), \(c=1\), whence the rank is \(2e-2k-2v+1\). For bipartite \(G\), each of the two double-cover components has \(v\) vertices and \(e-k\) edges, hence rank \(e-k-v+1\). This completes the formulas and proves the nonnegativity of their exponents. Graph spines have no higher homotopy or homology, and their integral first homology and fundamental groups are free as stated.

## Finite verification and its role
The included `verify.py` computes open-neighborhood complexes and the double-cover comparison complexes from graph data, checks the two cover nerves and proposed free-face collapses, and checks binary homology on all connected labeled unique-square graphs on four through six vertices and nine additional examples. Its finite enumeration corroborates but does not prove this all-graph theorem. The proof above derives the classification without a finite cutoff. The explicit eight-edge, two-square example in Step 1 is also an essential sanity check for the distinction between edge-disjoint and vertex-disjoint cycles.

## Relationship to previous work
Kamibeppu (2008, Theorem 3) treats graphs **without any four-cycle**, and hence does not cover \(k\ge1\). Matsushita (arXiv:1210.2803, Theorem 1.1) identifies the fundamental group of a neighborhood complex with a graph-walk group; this alone neither supplies the homotopy type nor rules out higher-dimensional cells. Shukla (2019, Theorem 2) obtains circle-wedge behavior in restricted low-degree classes, whereas degrees here are unbounded. Tittmann (2024, Theorem 5.38) studies the neighborhood polynomial and its face-counting consequences, not the full homotopy type. Arana–Stehlík (arXiv:2510.03698) study surface-quadrangulation regimes with different intersection structure. The explicit good-cover comparison and collapse classification for any number of pairwise edge-disjoint squares is the result evaluated here; the square-free boundary cases are credited to earlier work.

## Limitations
The theorem requires finiteness, connectedness, and pairwise edge-disjoint *all* four-cycles. It makes no claim for overlapping four-cycles or a direct simplicial collapse of the original \(\mathcal N(G)\), as opposed to the explicitly constructed \(W(G)\). No equivariant form is asserted. A literature comparison can support best-of-knowledge originality without guaranteeing priority over every unindexed result. Exact finite checks are not replacements for the nerve and collapse arguments.

## References
1. A. Kamibeppu, *Homotopy type of the box complexes of graphs without 4-cycles*, RIMS Kôkyûroku 1578 (2008), 67–70, Theorem 3. https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1578-13.pdf.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (2012). https://arxiv.org/abs/1210.2803.
3. S. Shukla, *Homotopy Type of the Neighborhood Complexes of Graphs of Maximal Degree at most 3 and 4-Regular Circulant Graphs*, Electronic Journal of Combinatorics 26 (2019), P2.4. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p4/pdf/.
4. P. Tittmann, *Graph Polynomials: The Eternal Book* (2024 draft), Section 5.2, Theorem 5.38. https://www.researchgate.net/publication/377572474_Graph_Polynomials_The_Eternal_Book.
5. C. Arana and M. Stehlík, *Quadrangulations and the Lovász complex*, arXiv:2510.03698 (2025). https://arxiv.org/abs/2510.03698.
