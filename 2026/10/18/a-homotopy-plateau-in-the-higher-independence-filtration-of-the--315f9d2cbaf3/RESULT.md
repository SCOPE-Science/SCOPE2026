# A homotopy plateau in the higher-independence filtration of the Möbius–Kantor graph

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the sixteen-vertex Möbius–Kantor graph, and let \(\operatorname{Ind}_r(M)\) be the simplicial complex of vertex subsets for which every connected component of the induced subgraph contains at most \(r\) vertices. For the three integer stages \(r=2,3,4\), the integral homotopy types are
\[
\operatorname{Ind}_{2}(M)\simeq\bigvee^{3}S^{6},\qquad
\operatorname{Ind}_{3}(M)\simeq\bigvee^{3}S^{6},\qquad
\operatorname{Ind}_{4}(M)\simeq\bigvee^{21}S^{7}.
\]
More strongly, the **natural inclusion** \(\operatorname{Ind}_{2}(M)\hookrightarrow\operatorname{Ind}_{3}(M)\) is a homotopy equivalence: it induces a unimodular isomorphism on integral sixth homology. Thus, in the restriction of this filtration to the three indices \(2,3,4\), the reduced sixth-dimensional persistence module over every field has exactly three intervals \([2,4)\). No claim about filtration stages outside these three indices is made.

## Assumptions and scope
Use the vertex labels \(u_0,\ldots,u_7,v_0,\ldots,v_7\), with subscripts interpreted modulo \(8\). The undirected graph \(M\) has the \(24\) edges
\[
\{u_i,u_{i+1}\},\qquad\{u_i,v_i\},\qquad\{v_i,v_{i+3}\},\qquad 0\le i<8.
\]
Encode \(u_i\) by bit \(i\) and \(v_i\) by bit \(8+i\) in a \(16\)-bit nonnegative integer mask. A mask belongs to \(\operatorname{Ind}_r(M)\) if and only if each connected component in the induced graph of its selected vertices has cardinality at most \(r\). This is the *higher independence complex* introduced by Paolini and Salvetti; it is neither the ordinary independence complex (the \(r=1\) stage) nor the edge matching complex. Everything below is over \(\mathbb Z\), unless explicitly noted.

## Proof
**1. Exhaustive face membership.** Examine each of the \(2^{16}=65{,}536\) masks. Two implementations, one using induced-graph flood-fill and one using union-find, independently test the connected-component bound. They agree for every mask and all three stages. Including the empty face, the numbers of admitted masks are \(6{,}813\), \(15{,}197\), and \(21{,}973\) for \(r=2,3,4\), respectively. The same enumeration verifies all three inclusion relations on faces.

**2. Acyclic discrete-Morse reductions.** At each stage independently, start with all masks unmatched. For vertex bit \(j=0,1,\ldots,15\), pair each still-unmatched allowable face not containing \(j\) with the allowable face obtained by adding \(j\), if the latter is also unmatched; visit eligible masks in numerical order. Orient all codimension-one incidences downwards except reverse matched incidences. Complete topological sorting of the entire resulting oriented face-poset graph proves acyclicity, not merely the absence of short cycles. In the reduced (empty-face-including) convention, the critical-cell counts, written by dimension, are
\[
\begin{array}{c|c|c|c}
 r & \text{faces including empty}&\text{matched pairs}&\text{critical cells by dimension}\\\hline
 2 &6813&3401& c_4=1,\ c_5=4,\ c_6=6\\
 3 &15197&7591& c_5=3,\ c_6=9,\ c_7=3\\
 4 &21973&10963& c_5=1,\ c_6=12,\ c_7=33,\ c_8=1.
\end{array}
\]
The empty face is paired in each case, so the ordinary geometric Morse CW model has one additional basepoint in degree zero. In particular, every such CW model is simply connected.

**3. Exact integral boundaries.** Orient simplices by increasing vertex labels, compute signed face incidences, and eliminate the matched face pairs algebraically along the acyclic gradient. Exact Smith-normal-form calculations over \(\mathbb Z\), with all nonzero diagonal factors equal to \(1\), give
\[
\begin{array}{c|c}
 r & \text{nonzero Smith factors of Morse differentials}\\\hline
 2 & \partial_5:(1),\quad\partial_6:(1,1,1)\\
 3 & \partial_6:(1,1,1),\quad\partial_7:(1,1,1)\\
 4 & \partial_6:(1),\quad\partial_7:(1^{11}),\quad\partial_8:(1).
\end{array}
\]
The matrices satisfy \(\partial^2=0\). The resulting reduced integral homology is \(\mathbb Z^3\) in degree six at \(r=2,3\), and \(\mathbb Z^{21}\) in degree seven at \(r=4\), with no other reduced integral homology and no torsion. As these CW complexes are simply connected, successive applications of the Hurewicz theorem show they are respectively \(5\)-connected, \(5\)-connected, and \(6\)-connected. Choose maps from the respective wedges of spheres representing bases in these first nonzero homology degrees. Those maps are integral homology equivalences between simply connected CW complexes and therefore homotopy equivalences by the homological Whitehead theorem. This proves all three stated homotopy types without assuming that rational Betti numbers determine integral homotopy.

**4. The integral map induced by inclusion.** The actual inclusion is checked on integral chains, not inferred from matching homology dimensions. A saturated basis for the source \(\ker(\partial_6)\) is the three columns of
\[
K=\begin{pmatrix}
0&1&-1\\0&0&-1\\-1&0&1\\1&0&0\\0&1&0\\0&0&1
\end{pmatrix}.
\]
Its top three-by-three minor has determinant \(1\). Lift these three Morse cycles through the matched pairs to *actual integral simplicial six-cycles* in \(\operatorname{Ind}_2(M)\). Direct signed boundary evaluation gives zero in every case; the lifted cycles respectively have \(206\), \(250\), and \(226\) nonzero simplex coefficients. View them in \(\operatorname{Ind}_3(M)\) and apply its integer Morse projection. Relative to the nine critical six-cells, their images are the columns of
\[
I=\begin{pmatrix}
0&-1&1\\0&1&0\\0&0&0\\-1&1&0\\0&1&-1\\0&0&1\\0&1&0\\0&-1&0\\1&0&0
\end{pmatrix}.
\]
The target's boundary from its three critical seven-cells to its nine critical six-cells is
\[
D=\begin{pmatrix}
1&0&0\\-1&0&0\\1&0&0\\-1&0&0\\0&-1&0\\0&0&-1\\0&0&-1\\0&0&0\\0&0&-1
\end{pmatrix}.
\]
The checker verifies \(\partial_6 I=0\), \(\partial_6D=0\), and that the upper six-by-six minor of the nine-by-six block matrix \([D\mid I]\) has determinant \(+1\). Since \(\partial_6\) has rank three, its integral kernel has rank six and is a primitive lattice. Consequently the six columns of \([D\mid I]\) form the whole integral kernel, so the images of \(I\) constitute an integral basis of the target homology modulo the columns of \(D\). The inclusion thus induces an isomorphism \(H_6(\operatorname{Ind}_2(M);\mathbb Z)\cong H_6(\operatorname{Ind}_3(M);\mathbb Z)\). Both spaces have simply connected CW models and the same integral homology in all degrees, hence this inclusion is a homotopy equivalence by Whitehead's homology theorem.

## Verification
Run `python3 verify.py > check.json` from the directory containing this document, with Python 3.10 or later and SymPy installed. The output should have `status` equal to `VERIFIED` and should match the supplied `certificate.json` after JSON parsing. The script reconstructs the graph; enumerates all masks at all three stages by both graph-membership algorithms; verifies every gradient-matching incidence and its global acyclicity; computes the exact integral Morse matrices, Smith factors and homology; constructs genuine integral six-cycles; and proves the inclusion map is unimodular via an explicit determinant-one minor. The complete oriented incidence counts are \(35{,}120\), \(89{,}088\), and \(135{,}760\) for \(r=2,3,4\). These checks are reproducible same-study computations, not an external independent audit.

## Relationship to prior work
Deshpande and Singh, *Higher Independence Complexes of graphs and their homotopy types* (arXiv:2001.05448, first posted 2020-01-15), define exactly the induced-component-size complex used here and classify complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect ary trees (see their introduction and Sections 3–5). None of their graph-family theorems applies to the sixteen-vertex cubic, cyclic Möbius–Kantor graph. Deshpande, Shukla and Singh (arXiv:2001.06775, first posted 2020-01-19) give connectivity bounds and homotopy assertions for chordal graphs; the Möbius–Kantor graph contains induced cycles and is not chordal. Abdelmalek and collaborators (arXiv:2106.10863, first posted 2021-06-21) likewise treat other graph families and structural properties, without the present exact three-stage homotopy classification or inclusion map.

A published exact same-graph classification of \(\operatorname{Ind}_1(M)\) computes \(\bigvee^4S^3\vee S^4\), and another computes its cyclic homology character; these concern the distinct ordinary independence complex and do not imply the homotopy equivalence between \(\operatorname{Ind}_2(M)\) and \(\operatorname{Ind}_3(M)\). Published Möbius–Kantor results for the matching complex, cut complex and graph-metric Vietoris–Rips complex have other defining face predicates. Searches for alternative notations, generalized Petersen graph \(\operatorname{GP}(8,3)\), component-bounded complexes, homotopy equivalences and integral persistence identified no statement that subsumes the present claim; this search outcome is not a proof of absolute novelty.

## Limitations
All asserted homotopy types and inclusions refer to this particular graph and \(r\in\{2,3,4\}\). They do not describe other filtration stages, generalized Petersen graphs as a family, equivariant maps, or homotopy-level barcodes beyond the stated three-stage restriction. The calculation depends on fully executable finite enumeration and integer-linear-algebra certificates; no independently produced mathematical audit is claimed. Previously unindexed work may contain an equivalent statement.

## References
1. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first posted 2020-01-15), https://arxiv.org/html/2001.05448v2.
2. Priyavrat Deshpande, Samir Shukla and Anurag Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775v1 (first posted 2020-01-19), https://arxiv.org/html/2001.06775v1.
3. Fred M. Abdelmalek, Priyavrat Deshpande, Shuchita Goyal, Amit Roy and Anurag Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (first posted 2021-06-21), https://arxiv.org/abs/2106.10863.
4. *Integral homotopy type of the Möbius–Kantor independence complex*, publicly available 2026 mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3, consulted for its explicit ordinary-independence definition and graph specification.
