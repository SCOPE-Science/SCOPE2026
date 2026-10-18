# Systolic four-cycles and affine homology action of the Paley-13 flag torus

## Finding
Let \(P_{13}\) be the graph on \(\mathbb Z/13\mathbb Z\) in which \(u\) and \(v\) are adjacent precisely when \(v-u\in\{\pm1,\pm3,\pm4\}\), and let \(X=\operatorname{Cl}(P_{13})\). Its vertices, edges and triangles number \(13,39,26\), and \(X\) is a flag triangulation of the torus. Give its one-skeleton the unit-edge path metric.

The least length of a simplicial closed edge path carrying a nonzero class in \(H_1(X;\mathbb Z)\) is \(4\). There are exactly **39 distinct unoriented simple cycles** attaining it. Under the canonical lattice identification
\[
H_1(X;\mathbb Z)\cong L=\{(a,b)\in\mathbb Z^2:a+3b\equiv0\pmod{13}\},
\]
these cycles represent exactly three primitive classes up to sign:
\[
\pm(4,3),\qquad\pm(3,-1),\qquad\pm(1,4),
\]
with **13 distinct cycles for each unoriented class**. Every such cycle is chordless. Of all 78 simple four-cycles in \(P_{13}\), the other 39 are null-homologous rhombus boundaries, each formed by two adjacent triangles.

The natural affine symmetry group \(G=\{u\mapsto mu+t:m\in\{1,3,4,9,10,12\},\ t\in\mathbb Z/13\mathbb Z\}\), of order 78, is transitive on the 39 systoles. Translation acts trivially on integral first homology. With basis \(A=(4,3)\), \(B=(3,-1)\) of \(L\), multiplication of vertices by \(-3\) induces the order-six integral matrix
\[
\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
\]
Thus the affine action on \(H_1(X;\mathbb Z)\) factors faithfully through its order-six multiplier subgroup, permuting the three shortest unoriented directions transitively.

## Assumptions and scope
The complex is the **ordinary unoriented flag/clique complex**, with every triangle included as a two-simplex. A simple cycle is counted up to cyclic re-rooting and reversal, rather than as a directed or rooted walk. A cycle is called systolic if its integral homology class is nonzero and its number of edges is minimal among such cycles. The displayed \(L\)-coordinate description fixes a particular identification of the universal triangular cover. The claim concerns only this 13-vertex torus, not other Paley graphs, continuous geodesic lengths in arbitrary metrics, or the entire cyclic-torus family.

## Proof
**1. Triangular covering.** Give \(\mathbb Z^2\) edges of increments \(\pm e_1\), \(\pm e_2\), \(\pm(e_1+e_2)\) and fill all elementary triangular faces. This is the simply connected equilateral triangular tiling. Label \((a,b)\) by \(a+3b\pmod{13}\). The deck lattice is exactly \(L\), of index 13. The quotient vertices and edges are exactly those of \(P_{13}\). Its two types of elementary face descend to the \(13\) translates of \(\{0,1,4\}\) and the \(13\) translates of \(\{0,3,4\}\). Direct examination of the six-element neighbor set of zero shows that its induced graph is a six-cycle. Thus every clique of size three is one of these 26 triangles, and there are no four-cliques. In particular the quotient of the triangular tiling is precisely \(X\), and \(X\) is a torus with universal cover the plane. The deck-displacement isomorphism identifies \(\pi_1(X)\), and hence integral first homology, with \(L\).

**2. Shortest nonzero displacements.** For any \((a,b)\in\mathbb Z^2\), its distance from the origin in the triangular one-skeleton is
\[
\ell(a,b)=\max\{|a|,|b|,|a-b|\}.
\]
Every permitted step changes each of \(a\), \(b\), \(a-b\) by at most one; conversely, the bound is achieved by taking diagonal steps and then horizontal or vertical steps in the appropriate signs. Direct integer enumeration subject to \(a+3b\equiv0\pmod{13}\) and \(\ell(a,b)\le4\) yields exactly six nonzero possibilities:
\[
(4,3),(-4,-3),(3,-1),(-3,1),(1,4),(-1,-4).
\]
There is therefore no essential closed walk of length at most three, and the integral one-systole is four.

**3. Exact carriers.** Every essential four-edge cycle lifts to a four-step geodesic to one of those six nonzero deck displacements. For each of the three unoriented displacement directions, every such geodesic consists of three steps of one permitted type and one step of another type, allowing four cyclic placements of the exceptional step. Each base vertex of \(\mathbb Z/13\mathbb Z\) provides four rooted representations, while every unoriented four-cycle has four roots at each fixed orientation. Consequently each unoriented displacement pair gives exactly \(13\) cycles. Since there are three pairs, there are \(39\) essential four-cycles. They are chordless: a diagonal chord would divide a four-edge loop into two triangular face boundaries, making it null-homologous.

If a simple four-cycle has zero displacement, its lift is a simple four-step cycle in the triangular tiling. The only such cycles are elementary rhombi, each the union of two edge-adjacent triangles. Every edge of \(X\) is incident to exactly two triangles and gives one such rhombus boundary; these are distinct and number \(39\). Thus all \(78\) simple four-cycles are classified, with no hidden nonessential simple four-cycles.

**4. Affine action.** The six residues \(\{\pm1,\pm3,\pm4\}\) form the multiplicative square subgroup of \((\mathbb Z/13\mathbb Z)^\times\), generated by \(-3\). Therefore the 78 affine maps displayed in the finding preserve every edge and triangle. In the triangular covering, multiplication by \(3\) is lifted by \((a,b)\mapsto(-b,a-b)\). Relative to the lattice basis \(A=(4,3)\), \(B=(3,-1)\), whose determinant is \(-13\), this is the order-three matrix \(\bigl(\begin{smallmatrix}0&1\\-1&-1\end{smallmatrix}\bigr)\). Multiplication by \(-1\) lifts to negation; hence \(-3\) acts by the claimed order-six matrix. Translations lift to translations of the plane and therefore act trivially on \(H_1\). The multiplier action permutes the three unoriented systolic directions, and translations move each direction's 13 cycles transitively. This proves the stated single orbit.

## Verification
The accompanying executable `verify.py` constructs the 13-vertex graph from first principles and exhaustively enumerates 39 edges, 26 triangles, no four-cliques, and 78 distinct unoriented simple four-cycles. It checks that every vertex link is a six-cycle, determines each four-cycle's lifted displacement, verifies the counts \(39+13+13+13=78\), and identifies the 39 null-homologous rhombi as those paired to graph edges. It enumerates all deck-lattice vectors of edge length at most four, checks the index-13 lattice basis and affine homology action, and verifies transitivity of the full 78-element affine group on the systoles. Run `python3 verify.py` using only the Python standard library. The reported successful end marker is `VERIFY_OK`.

The exhaustive finite computation supports the exact graph-specific classifications; the covering-space argument independently explains why the integer displacements characterize all homology classes, rather than merely the cycles in an arbitrary finite search.

## Relationship to prior work
Datta and Upadhyay describe the cyclic triangulations \(T_{n,1,k}\), including the torus \(T_{13,1,3}\) isomorphic to \(X\), and their symmetry properties. Jones and Mačaj explicitly identify the 13-vertex, 39-edge, 26-triangle Paley embedding in a hexagonal torus with affine symmetry. Those previously known triangulation, genus, and symmetry facts are not claimed as new. The finding is the **integral shortest-cycle classification, all-carrier census, three primitive homology directions, and their induced integral symmetry action**. A separately indexed calculation for \(T_{n,1,3}\) treats \(n\ge17\) and therefore does not imply the 13-vertex statement.

## Limitations
The proof does not give a closed formula for the systoles of arbitrary \(T_{n,1,3}\), nor a classification of longer cycles. The complete-text coverage of every possible alternate name for this 13-vertex torus cannot be guaranteed. No independent external audit has been performed. Distances and counts refer to the combinatorial unit-edge metric and integral homology, not arbitrary smooth torus metrics.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433, first public 2004-03-25, especially the cyclic \(T_{n,1,k}\) construction and automorphism discussion, https://arxiv.org/abs/math/0403433.
2. G. A. Jones and M. Mačaj, *Regular dessins with primitive automorphism groups*, arXiv:2303.11808, §4, Example 6 and Figure 5, https://arxiv.org/abs/2303.11808.
