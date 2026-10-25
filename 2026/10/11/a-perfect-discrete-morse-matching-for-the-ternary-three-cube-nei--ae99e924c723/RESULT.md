# A perfect discrete-Morse matching for the ternary three-cube neighborhood complex

## Finding

Let \(G=H(3,3)=K_3\mathbin{\square}K_3\mathbin{\square}K_3\) be the graph on the 27 ternary triples, where distinct triples are adjacent precisely when they differ in one coordinate. Let \(\mathcal N(G)\) be its **open** Lovász neighborhood complex: a nonempty set is a simplex if its vertices have a common adjacent vertex in \(G\). The original five-dimensional simplicial face poset of \(\mathcal N(G)\) admits an explicit acyclic matching with 672 matched pairs and critical-cell vector
\[
(c_0,c_1,c_2,c_3,c_4,c_5)=(1,3,56,0,0,0).
\]
This matching is perfect: every \(c_i\) equals the corresponding Betti number over every field. In particular, it gives a two-dimensional CW model with one vertex, three edges and 56 two-cells, and
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
The substantive result is the **optimal matching on the original face poset**, not an independent claim to have discovered the free-abelian graph-walk group or the existence of some abstract two-dimensional deformation retract.

## Definitions, normalization and exact scope

Label each triple \((a,b,c)\in\{0,1,2\}^3\) by \(9a+3b+c\), and orient each simplex edge from the lower to the higher label. For every vertex \(v\), its six open neighbors form a maximal face of the construction. Enumerate all nonempty subsets of all these open neighborhoods and deduplicate. The resulting simplicial complex is neither the closed-neighborhood complex, nor the clique/Rips complex of the graph. All matching incidences are **codimension-one face incidences**; the empty simplex is not part of the matching. The theorem concerns only \(H(3,3)\), without extrapolation to other Hamming graphs.

## Proof and explicit finite certificate

**Faces and Euler characteristic.** The 27 open neighborhoods yield exactly 1,404 nonempty simplices, with face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(27,243,540,405,162,27).
\]
Thus \(\chi=27-243+540-405+162-27=54\). These counts are directly enumerable using subsets of the six-element open neighborhoods.

**Matching and acyclicity.** On the initially unmatched face set, process vertices successively in the exact order

`21,11,26,18,13,1,6,20,5,10,8,24,17,14,16,25,22,0,19,2,4,15,12,23,3,9,7`.

At the stage for vertex \(v\), pair an as-yet-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if both faces are still unmatched. Processing candidate faces in increasing bit-mask order gives 672 disjoint pairs, leaving exactly one unpaired vertex, three edges, and 56 triangles. Orient every face-poset cover relation downward, except reverse each paired incidence. There are exactly 4,698 such oriented incidences; a topological sort visits **all 1,404 faces**, so the directed graph is acyclic. By Forman's discrete-Morse theorem this is a valid acyclic matching, giving a CW model with the indicated cells and no cells above dimension two.

For an independent homological check, enumerate the simplicial boundary matrices over \(\mathbb F_2\). Their ranks in degrees one through five are
\[
(26,214,270,135,27),
\]
so the Betti numbers over \(\mathbb F_2\) are \((1,3,56,0,0,0)\). The integral argument below separately proves that these ranks are the Betti numbers over every field. The weak Morse inequalities then show that **no** acyclic matching of this face poset can use fewer critical cells in **any** degree.

**Fundamental group.** The 26 matched vertex-edge incidences form a spanning tree of the 27 vertices (the corresponding edges are distinct, cycle-free and connected). In the usual edge-path presentation, kill those tree edges. The remaining 217 oriented edges are generators subject to 540 triangle boundary relators: for each \(a<b<c\),
\[
e_{ab}e_{bc}e_{ac}^{-1}=1.
\]
Each of the 214 matched edge-triangle incidences expresses its matched edge uniquely in terms of the other two sides of that triangle. The recursion for these substitutions is well-founded, leaving exactly three generators \(g_1,g_2,g_3\), indexed by the surviving oriented edges \((11,13),(1,18),(11,20)\).

Performing the substitutions and free/cyclic reductions for **all 540** original triangle relators yields 485 empty words and 55 nonempty words: 30 of length four, 21 of length six and four of length eight. Every resulting word has exponent sum zero in each of the three generators. Three specific nonempty relations are
\[
\begin{aligned}
g_3^{-1}g_1^{-1}g_3g_1&=1 &&\text{from triangle }(0,7,8),\\
g_2^{-1}g_3^{-1}g_2g_3&=1 &&\text{from triangle }(0,4,7),\\
g_2^{-1}g_3g_1^{-1}g_3^{-1}g_2g_1&=1 &&\text{from triangle }(4,8,23).
\end{aligned}
\]
These are exact ordered, cyclically reduced relators using the stated vertex labels, edge orientations, matching order and generator order. The first two relations make \(g_3\) commute with \(g_1\) and \(g_2\). Under those two relations the third reduces to \(g_2^{-1}g_1^{-1}g_2g_1=1\), making \(g_1\) and \(g_2\) commute. Therefore the three relations kill the entire commutator subgroup of the free group on \(g_1,g_2,g_3\). Conversely, **all** 540 reduced relations lie within that commutator subgroup, because all are exponent-balanced. Consequently the quotient group is exactly \(\mathbb Z^3\), not merely a group with abelianization \(\mathbb Z^3\).

**Integral homology.** The one-vertex, three-edge, 56-face Morse CW model has zero first cellular differential. Since its fundamental group is \(\mathbb Z^3\), its first integral homology is \(\mathbb Z^3\). The second cellular differential maps \(\mathbb Z^{56}\) into \(\mathbb Z^3\) with quotient \(H_1\cong\mathbb Z^3\); it therefore vanishes. Thus \(H_2\cong\mathbb Z^{56}\), with no torsion, and all higher integral homology groups vanish. This integral statement is **not** deduced from modular boundary ranks alone. The CW equivalence transfers it to the original neighborhood complex.

## Reproducibility and certificate boundaries

The included Python 3 program `verify.py` constructs the graph from its coordinates rather than loading an external graph or matching certificate. It enumerates faces, reconstructs the stated matching, verifies that the 4,698 oriented cover incidences form a directed acyclic graph, checks the matched tree and all 214 edge-triangle substitutions, and examines all 540 original triangular relators. It verifies that the three displayed commutator *words* occur among the relators and that every residual relator is exponent-balanced, and recomputes the mod-two boundary ranks. The three **triangle-to-word assignments** displayed above were additionally checked by a separate direct reconstruction of the substitutions; the standalone script tests membership of the displayed words without asserting their triangle locations. Run the provided script as `python3 verify.py` from the record directory. This finite exhaustive algorithm proves only the explicitly stated finite case.

## Relationship to established results

Kozlov proved that \(\mathcal N(G)\) and \(\operatorname{Hom}(K_2,G)\) have the same simple homotopy type for any graph; this does not give an optimal original-face-poset matching for the particular Cartesian product here. Matsushita related the fundamental group of neighborhood complexes to graph-walk groups, and Behal–Chih computed free-abelian graph-walk groups of ternary Hamming graphs. The group conclusion is consequently overlapping, not presented as a separate novelty claim.

Kahle's \(K_{a,b}\)-free lemma applies with \((a,b)=(2,3)\): any two vertices of \(H(3,3)\) have at most two common neighbors, so \(\mathcal N(G)\) already admits *some* deformation retract of dimension at most two. Such a dimension bound does not construct an optimal acyclic matching on the **unsubdivided original face poset** or determine its critical-cell vector. Shukla's neighborhood-complex classifications cover maximum degree at most three and specified four-regular circulants, not the six-regular graph considered here. The distinguishing result is thus the explicit 672-pair matching satisfying all Morse lower bounds simultaneously, not the abstract dimension bound or easy Euler arithmetic.

## Limitations

No classification for general \(H(d,q)\), canonical attaching maps for the 56 two-cells, exact higher homotopy groups, or general graph-complex decomposition is asserted. An unindexed equivalent optimal matching may have been published under another description. The minimal number of critical cells is asserted *degree by degree for acyclic matchings of this original triangulation*, not an absolute minimal number of cells among arbitrary CW models outside that category.

## References

1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, https://arxiv.org/abs/math/0503613.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, https://arxiv.org/abs/1210.2803.
3. K. Behal and T. Chih, *Fundamental Groups of Hamming Graphs*, arXiv:2308.02938, https://arxiv.org/abs/2308.02938.
4. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, https://arxiv.org/abs/math/0512077.
5. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, https://arxiv.org/abs/1802.04526.
