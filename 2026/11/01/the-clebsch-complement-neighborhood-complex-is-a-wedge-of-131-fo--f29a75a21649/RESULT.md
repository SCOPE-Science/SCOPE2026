# The Clebsch-complement neighborhood complex is a wedge of 131 four-spheres

## Finding
Let \(C\) be the standard five-regular Clebsch graph, with vertex set \(\mathbb F_2^4\) and adjacency when the difference is one of the five vectors \(e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\). Let \(H=\overline C\), its ten-regular complement (the halved five-cube graph). The *open-neighborhood complex* \(\mathcal N(H)\) has as faces the subsets of vertices with a common neighbor in \(H\). Then
\[
\mathcal N(H)\simeq\bigvee^{131}S^4.
\]
In addition, let \(\mathcal D(C)\) consist of vertex subsets whose complements are dominating sets in \(C\). Its complete reduced **integral** homology is
\[
\widetilde H_j(\mathcal D(C);\mathbb Z)\cong
\begin{cases}\mathbb Z^{131},&j=9,\\0,&j\ne9.\end{cases}
\]
Both conclusions hold for these explicitly identified finite graphs. The homotopy equivalence is nonequivariant; no corresponding claim about the homotopy type of \(\mathcal D(C)\) is made.

## Assumptions and scope
Encode vertices as integers \(0,\ldots,15\) standing for four-bit vectors. Two distinct integers \(x,y\) are adjacent in \(C\) precisely when their bitwise XOR belongs to \(\{1,2,4,8,15\}\). The graph is strongly regular with parameters \((16,5,0,2)\), as is verified directly. Its complement has degree ten. All simplicial faces are sets of vertices; the empty set is included by convention, but the Morse matching acts on nonempty faces. Orient a simplex by ascending vertex order. The neighborhood complex uses **open**, not closed, neighborhoods. The dominance complex uses ordinary **closed-neighborhood** domination by the omitted vertex set.

## Proof
**1. A finite model.** For each vertex \(x\), the open neighborhood of \(x\) in \(H\) consists of the ten integers \(y\ne x\) with \(x\oplus y\notin\{1,2,4,8,15\}\). There are sixteen distinct ten-element facets. Enumerating all their nonempty subsets gives exactly \(11{,}804\) faces, with the dimension-\(0\)-through-\(9\) vector
\[
(16,120,560,1740,3312,3240,1920,720,160,16).
\]
The accompanying `verify.py` constructs these sets directly from the graph definition, without a precomputed face table.

**2. Acyclic discrete Morse matching.** In the original face poset, repeatedly choose a codimension-one face with exactly one immediate upper coface, prioritizing larger dimensions and then smaller bit masks. Remove this free face and its unique maximal upper coface. This produces \(4{,}780\) elementary collapse pairs and leaves \(2{,}244\) faces. On the remaining face poset, process vertices in the order \(0,1,\ldots,15\). At vertex \(v\), pair each as-yet-unmatched face not containing \(v\) with its extension by \(v\), when both remain. This produces another \(1{,}050\) pairs. With all \(5{,}830\) pairs reversed, the directed Hasse graph is acyclic by exhaustive topological sorting of all \(11{,}804\) faces and \(65{,}680\) cover incidences. Only one critical vertex, six critical three-simplices and \(137\) critical four-simplices remain. Thus Forman's discrete Morse theorem supplies a CW model with cells only in dimensions \(0\), \(3\), and \(4\), in multiplicities \(1,6,137\).

**3. Integral attaching degrees.** The three-skeleton of the Morse CW model is a wedge of six three-spheres: all three-cells attach to the unique zero-cell. The Hurewicz theorem in degree three identifies
\[
\pi_3\left(\bigvee^6S^3\right)\cong\mathbb Z^6.
\]
Consequently the six integral degrees of each four-cell attachment determine its homotopy class. Compute the signed integral Morse differential by reducing increasing-vertex-order simplex boundaries along the matched \((3,4)\) gradient pairs. Let \(M\) be the resulting six-by-137 integer matrix, ordered by increasing critical face masks. Its columns numbered \(2,4,9,10,23,26\) (zero-based) form exactly
\[
\begin{pmatrix}
-1&0&0&0&1&-1\\
 1&0&0&0&0& 1\\
-1&-1&0&0&0&0\\
0&0&-1&0&-1&0\\
0&0&0&-1&0&-1\\
0&-1&0&0&0&0
\end{pmatrix},
\]
whose determinant is \(+1\). Hence the degree map \(\mathbb Z^{137}\to\mathbb Z^6\) is split surjective and may be transformed by integral elementary changes of the cell bases into \((I_6\;0)\). These changes are realized by homotopy equivalences on the wedge of three-spheres and elementary four-cell slides. The six degree-one attachments cancel all six three-spheres; the remaining 131 four-cells attach nullhomotopically. Therefore
\[
\mathcal N(H)\simeq\bigvee^{131}S^4.
\]
This argument concerns attaching maps in \(\pi_3\), not just a rational or finite-field boundary rank.

**4. Integral Alexander duality.** Matsushita and Wakatsuki prove that \(\mathcal N(\overline G)\) is the combinatorial Alexander dual of \(\mathcal D(G)\). Applied to \(G=C\), combinatorial Alexander duality on the ground set of sixteen vertices identifies
\[
\widetilde H_j(\mathcal D(C);\mathbb Z)
\cong\widetilde H^{16-j-3}(\mathcal N(H);\mathbb Z).
\]
The right side equals \(\mathbb Z^{131}\) exactly when \(16-j-3=4\), or \(j=9\), and vanishes otherwise. The freeness established in step 3 rules out hidden integral torsion.

## Verification
Run `python verify.py` in this directory, using only the Python standard library. The program reconstructs both graphs and verifies the strongly regular parameters, builds the entire complement-neighborhood face poset, reproduces all matching pairs, checks all directed cover incidences for acyclicity, calculates the **signed integral** Morse degree matrix and its displayed determinant-one minor, and independently computes every simplicial boundary rank over \(\mathbb F_2\) without Morse reduction. The direct mod-two reduced Betti vector is zero except for rank \(131\) in dimension four. It separately tests all \(65{,}536\) vertex subsets against the closed-neighborhood definition of domination in \(C\); their ordinary Euler characteristic is \(-130\), consistent with degree-nine homology of rank \(131\). These finite checks are exhaustive for the specified graphs; their all-integer homotopy inference uses the explicit unimodular minor and the topology explained above. See `verification_output.txt` for a complete deterministic output summary.

## Relationship to prior work
Matsushita and Wakatsuki (first publicly available December 5, 2023) establish the combinatorial Alexander-dual identification and study specified paths, cycles, graph products and chordal graphs. Their theorem supplies the duality in step 4 but does not compute the homotopy of the ten-regular Clebsch complement, so it does not imply the numerical 131-sphere statement on its own. Shukla's published neighborhood classifications concern maximum degree at most three and four-regular circulant graphs, not the present ten-regular graph. A publicly available calculation of the **five-regular** Clebsch neighborhood complex establishes \(\mathcal N(C)\simeq\bigvee^{31}S^2\). This is a distinct graph, though on the same vertex set: the open neighborhoods used here are those of the **complement** \(H\), and the earlier homotopy result does not imply the present one. The numerical result is also phrased equivalently as the homotopy type of \(\operatorname{Hom}(K_2,H)\), by the standard Hom-neighborhood equivalence. The exact resulting 131-sphere classification is not stated in these inspected sources.

## Limitations
The proof concerns one graph and its complement, not all halved cubes or all strongly regular graphs. The Alexander-dual corollary determines integral homology of the dominance complex, not its homotopy type. Neither conclusion classifies the induced group action on homology. The finite proof is independent of sampling, but literature searches cannot rule out obscure or unindexed equivalent work.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first posted 2023-12-05, Theorem 1.1 and Theorem 2.2; DOI 10.1016/j.jcta.2024.105978.
2. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first posted 2018-02-13; Electronic Journal of Combinatorics 26 (2019), P2.4.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; DOI 10.1006/aima.1997.1650.
4. *The 5-regular Clebsch neighborhood complex is a wedge of 31 2-spheres*, public mathematical result at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a (mathematical comparison only; concerns \(\mathcal N(C)\), not \(\mathcal N(\overline C)\)).
