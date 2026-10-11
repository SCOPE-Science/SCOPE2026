# A perfect discrete-Morse matching for the ternary three-cube neighborhood complex

## Finding

Let \(G=H(3,3)=K_3\mathbin{\square}K_3\mathbin{\square}K_3\) be the graph on the 27 ternary triples, joining two distinct triples exactly when they differ in one coordinate. Let \(\mathcal N(G)\) be the **open** Lovász neighborhood complex: a nonempty vertex set is a simplex when all its vertices are adjacent to some common vertex of \(G\). Then \(\mathcal N(G)\) has an **optimal discrete-Morse matching on its original simplicial face poset**: its entire five-dimensional triangulation has exactly 672 matched face pairs and critical-cell vector \((1,3,56,0,0,0)\) in dimensions zero through five. This vector meets every weak Morse inequality with equality, over every field, so the matching is perfect. Its exact consequences are that \(\mathcal N(G)\) is connected and

\[
\pi_1(\mathcal N(G))\cong\mathbb Z^3,\qquad
H_i(\mathcal N(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^3,&i=1,\\
\mathbb Z^{56},&i=2,\\
0,&i\ge3.
\end{cases}
\]

Moreover, this matching constructs a CW model with exactly one \(0\)-cell, three \(1\)-cells, 56 \(2\)-cells, and no higher cells, attaining the smallest possible number of critical cells in **each dimension** for any matching of this triangulation. In particular, all integral homology is torsion-free. The existence of this perfect matching on the original complex is the principal contribution; the homology and fundamental-group formulas are consequences and are not presented as separately novel results.

## Assumptions and scope

Use vertex IDs \(9a+3b+c\), for \(a,b,c\in\{0,1,2\}\), and orient every edge from the smaller to the larger ID. A simplex is a nonempty subset of the six-element open neighborhood of a vertex. This is not a Vietoris–Rips complex, a closed-neighborhood complex, or the original graph regarded as a one-dimensional CW complex. All homology groups have integral coefficients unless otherwise indicated. The statement concerns this single explicitly specified graph; no claim is made for arbitrary Hamming parameters.

## Proof

**Exact face structure.** Enumerating, for each of the 27 vertices, all nonempty subsets of its six neighbors and deduplicating yields 1,404 nonempty simplices. Their face vector, in dimensions zero through five, is

\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(27,243,540,405,162,27).
\]

Thus the Euler characteristic is \(27-243+540-405+162-27=54\).

**A two-dimensional Morse model.** Apply a sequential vertex-toggle matching to all nonempty simplices. At a stage labeled by vertex \(v\), pair each as-yet-unmatched face \(\sigma\) that omits \(v\) with \(\sigma\cup\{v\}\), provided the latter is also still unmatched. Use the vertex order

`21,11,26,18,13,1,6,20,5,10,8,24,17,14,16,25,22,0,19,2,4,15,12,23,3,9,7`.

This gives 672 disjoint matched pairs, and leaves exactly one critical vertex, three critical edges and 56 critical triangles. For a complete acyclicity certificate, direct every codimension-one face incidence from upper to lower except along a matched pair, where the arrow is reversed. A topological sort processes all 1,404 simplices and all 4,698 such directed incidences. Since no directed cycle remains, Forman's discrete Morse theorem produces a CW complex of the stated cell counts and dimension. Independent exact mod-two boundary ranks establish Betti vector \((1,3,56,0,0,0)\), equal term-by-term to the critical-cell vector. By the weak Morse inequalities, no discrete-Morse matching on this complex can have fewer critical cells in any of these dimensions; this one is perfect over every field. Unlike a mere dimension-reduction existence theorem, the matching is an explicit optimal acyclic matching on the original triangulation.

**Fundamental group.** The 26 vertex-edge matching pairs yield a spanning tree: its edges are distinct, contain no cycle, and connect all 27 vertices. Killing these tree edges in the usual edge-path presentation leaves 217 edge generators with 540 triangular relators. Every matched edge-triangle pair gives a triangular relation that can be solved for its matched edge. The recursive elimination of all 214 such edge generators is well-founded, as checked from the explicit matching, leaving three generators \(g_1,g_2,g_3\), corresponding to the oriented edges with endpoint IDs \((11,13)\), \((1,18)\), and \((11,20)\).

For a triangle \(a<b<c\), the defining edge-path relation is \(e_{ab}e_{bc}e_{ac}^{-1}=1\). After the 214 substitutions and free/cyclic reduction, the 540 relations comprise 485 empty words and 55 nonempty words: 30 of length four, 21 of length six, and four of length eight. Every resulting relator has exponent sum zero in each of the three generators; hence all lie in the commutator subgroup of the free group. Three of the explicit relators are

\[
g_3^{-1}g_1^{-1}g_3g_1=1,\quad
g_2^{-1}g_3^{-1}g_2g_3=1,\quad
g_2^{-1}g_3g_1^{-1}g_3^{-1}g_2g_1=1.
\]

For example, they occur at triangles with vertex IDs \((1,2,6)\), \((2,7,10)\), and \((0,11,12)\), respectively. The first two say that \(g_3\) commutes with \(g_1\) and \(g_2\); then the third says that \(g_1\) commutes with \(g_2\). Thus these relations kill the entire commutator subgroup, while all other relations already lie in that subgroup. The presented group is exactly \(\mathbb Z^3\), not merely a group with this abelianization.

**Integral homology.** The connected two-dimensional Morse CW model has one zero-cell, three one-cells and 56 two-cells. Its first cellular differential is zero, and its first homology is the abelianization \(\mathbb Z^3\) just obtained. Hence its second cellular differential into \(\mathbb Z^3\) is also zero, and its second cellular homology is \(\mathbb Z^{56}\). There are no cells in higher degrees. Homotopy invariance transfers these groups to \(\mathcal N(G)\).

## Verification

The standalone Python 3 program `verify.py` reconstructs the graph from ternary coordinates and independently enumerates every simplex. It checks the face vector, matching pairs, critical cells, all codimension-one incidences, and global acyclicity via directed-graph topological sorting. It verifies that the 26 matched vertex-edge incidences form a spanning tree, recursively eliminates all 214 matched edge-triangle variables, reconstructs **all 540** original triangular relations, checks the three explicit commutator witnesses and exponent-balance of every residual relation, and computes all boundary ranks over \(\mathbb F_2\). Reproduce with `python3 verify.py` from the directory containing the file.

The mod-two boundary ranks in degrees one through five are \((26,214,270,135,27)\); they provide an independent finite check of Betti numbers \((1,3,56,0,0,0)\) but are not used to infer integral torsion-freeness. The integral assertion follows instead from the group presentation and the two-dimensional Morse model.

## Relationship to prior work

Kozlov proves that the open-neighborhood complex of a graph and its graph-homomorphism complex \(\operatorname{Hom}(K_2,G)\) have the same simple homotopy type. This motivates studying exact examples but does not compute this 27-vertex case. Matsushita identifies the fundamental group of an open-neighborhood complex with an even graph-walk fundamental group. Behal and Chih subsequently determine a closely related graph-walk fundamental group for Hamming graphs, obtaining a free abelian group in the ternary case. Consequently, the rank-three fundamental-group statement is **not claimed as independently novel**; the explicit integral second-homology calculation and two-dimensional Morse construction supply the specific additional information.

Kahle studies neighborhood complexes of random graphs and proves a **general dimension bound**: if a graph contains no \(K_{a,b}\), its neighborhood complex deformation-retracts to dimension at most \(a+b-3\). In \(H(3,3)\), distinct vertices have at most two common neighbors, so the \(K_{2,3}\)-free condition applies and the existence of some two-dimensional deformation model is **already covered** by Kahle. That theorem, however, neither constructs the stated matching on the original face poset nor proves its cell-by-cell optimality. Shukla's classification treats graphs of maximum degree at most three and four-regular circulant graphs, not the six-regular Hamming graph considered here. Targeted searches did not identify a published optimal matching with critical vector \((1,3,56,0,0,0)\) for this particular simplicial complex. The numerical homology should not be isolated from the known general results and portrayed as the main novelty.

## Limitations

A minimal or canonical attaching-map description of the 56 two-cells is not established. The existence of a two-dimensional homotopy model already follows from Kahle's \(K_{2,3}\)-free theorem; the stronger point here is that the specific face-poset Morse matching reaches all optimal critical-cell counts simultaneously. The calculation does **not** determine the full homotopy type beyond the described CW model, nor the higher homotopy groups. The existence of an unindexed equivalent calculation cannot be excluded. The reduction relies on an exhaustive finite acyclicity certificate, reproduced by the accompanying program; this is an exact finite proof for this graph, not a statement about other Hamming graphs.

## References

1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first submitted 2005-03-28; primary MSC 57Q10. https://arxiv.org/abs/math/0503613
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first submitted 2012-10-10. https://arxiv.org/abs/1210.2803
3. K. Behal and T. Chih, *Fundamental Groups of Hamming Graphs*, arXiv:2308.02938, first submitted 2023-08-05. https://arxiv.org/abs/2308.02938
4. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first submitted 2005-12-04. https://arxiv.org/abs/math/0512077
5. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first submitted 2018-02-13. https://arxiv.org/abs/1802.04526
