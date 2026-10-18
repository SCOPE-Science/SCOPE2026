# Mixed-dimensional integral homotopy of the octahedral two-matching complex

## Finding
Let \(O=K_{2,2,2}\) be the graph of the regular octahedron, with six vertices partitioned into three opposite pairs. Let \(M_2(O)\) be the simplicial complex whose vertices are the twelve graph edges and whose simplices are edge subsets in which every graph vertex has selected degree at most two. There is an integral homotopy equivalence
\[
\boxed{M_2(O)\simeq \bigvee^{3}S^{3}\ \vee\ \bigvee^{7}S^{4}.}
\]
Consequently \(\widetilde H_3(M_2(O);\mathbb Z)\cong\mathbb Z^3\), \(\widetilde H_4(M_2(O);\mathbb Z)\cong\mathbb Z^7\), and all other reduced integral homology groups vanish. The complex is nonpure, with precisely three three-dimensional, sixty four-dimensional, and twenty five-dimensional facets. This homotopy-type statement is more informative than the free ranks alone.

## Assumptions and scope
The graph is simple and undirected. Label its vertices \(0,1,2,3,4,5\), with nonedges \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5\}\). Index its twelve edges lexicographically by \(e_0,\dots,e_{11}\), so
\[
(e_0,\ldots,e_{11})=((0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)).
\]
An edge subset is encoded by a twelve-bit integer, with bit \(i\) marking the presence of \(e_i\). A legal face has selected degree at most two at each of the six original graph vertices. All simplicial orientations order the edge indices increasingly. There are no assertions about larger cross-polytope graphs or other matching thresholds.

## Proof
**Complete face presentation.** Testing each of the \(2^{12}=4096\) bitmasks against the six degree inequalities gives exactly \(772\) faces including the empty face, with nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,196,297,180,20).
\]
The maximal faces occur in the three dimensions claimed above. These counts follow from executable exhaustive enumeration in the accompanying checker; the test is finite and exactly exhausts the stated twelve-edge domain.

**Acyclic discrete-Morse matching.** Exclude the empty face. Starting with the full set of nonempty faces, process indices \(i=0,1,\ldots,11\) in that order. For each index, simultaneously pair every as-yet-unpaired face \(\sigma\) not containing \(e_i\) with \(\sigma\cup\{e_i\}\) whenever both are still present, and delete both from the active set. There are \(377\) pairs and \(17\) critical faces: one dimension-zero, six dimension-three and ten dimension-four faces. Reverse the \(377\) matched edges of the face-poset Hasse diagram and orient every other cover downward. The resulting digraph on \(771\) nonempty faces and \(2928\) cover relations admits a complete topological ordering, as explicitly verified by the checker, so the matching is acyclic. Forman's finite discrete-Morse construction therefore gives a CW complex with exactly these critical cells.

**Integral attaching-degree matrix.** For a mask \(\tau=\{e_{i_0}<\cdots<e_{i_k}\}\), the signed boundary is \(\partial\tau=\sum_j(-1)^j(\tau\setminus\{e_{i_j}\})\). For each matched lower face \(a\) paired with upper face \(b\), eliminate the unit incidence \(\langle\partial b,a\rangle=\pm1\): substitute \(a=-\langle\partial b,a\rangle\sum_{c\ne a}\langle\partial b,c\rangle c\) in the lower-dimensional chain group, recursively until only critical lower faces remain; matched upper cells project to zero. In increasing numerical order of critical four- and five-edge masks, the resulting signed cellular boundary from the ten four-cells to the six three-cells is
\[
D=\begin{pmatrix}
0&0&0&0&-1&-1&0&1&0&1\\
0&-1&1&1&1&0&1&0&1&0\\
-1&0&-1&0&0&1&-1&-1&0&-1\\
1&1&0&-1&0&0&0&0&-1&0\\
0&0&0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0
\end{pmatrix}.
\]
The fourth row equals minus the sum of the first three, and the final two rows are zero; hence \(\operatorname{rank}D\le3\). Its submatrix in rows \(1,2,3\) and columns \(1,2,5\), using one-based indexing, has determinant \(1\). Hence the rank is exactly three and the three nonzero Smith invariant factors are all \(1\). These calculations are also checked directly by integer and rational arithmetic in the attached script.

**Upgrade from homology to homotopy.** The Morse CW complex has a single zero-cell and no cells in dimensions one or two. Its three-skeleton is a wedge of six three-spheres. Each four-cell attaches along a class in \(\pi_3(\bigvee^6S^3)\cong\mathbb Z^6\); the matrix \(D\) completely records these attaching classes, not merely their homology shadows. Unimodular row/column operations on \(D\) are realized by self-homotopy equivalences and cellular handle slides; the three unit invariant factors cancel three three/four-cell pairs. Three three-spheres and seven four-spheres remain, proving the displayed *integral homotopy equivalence*. No higher-dimensional attaching-map obstruction exists because the Morse CW model has no higher cells.

## Verification
Run `python3 verify_octa_two_matching.py` with standard Python. The checker independently tests all face masks and downward closure; counts facets; reconstructs all \(377\) matched pairs; checks all \(2928\) oriented Hasse incidences and acyclicity; reconstructs the full signed Morse matrix by chain substitutions; exhibits a unit \(3\times3\) minor; computes its exact rational rank; and independently calculates full simplicial boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\). Successful execution prints `OCTAHEDRON_TWO_MATCHING_INTEGRAL_HOMOTOPY_CHECKS_OK`. The finite certificate is exhaustive for the specific octahedral graph, but does not prove a formula for any infinite graph family.

## Relationship to prior work
Vega [1] defines and studies two-matching complexes by discrete Morse theory, including wheel and caterpillar families; the octahedral graph is neither. Singh [2] determines higher matching homotopy types for certain *complete* and *complete bipartite* graphs, including the high-threshold cases \(M_{n-2}(K_n)\) and \(M_{n-1}(K_{n,n})\), but does not state the octahedral complete-tripartite result. The octahedral graph also has independently studied **ordinary matching** and **discrete Morse-matching** complexes; neither is \(M_2(O)\), and their distinct homotopy types do not imply the displayed claim. The present computation isolates a natural first fully balanced tripartite example with homology in adjacent degrees and a nonpure face structure.

## Limitations
This is a complete classification for one naturally defined six-vertex graph, not a theorem for arbitrary complete tripartite graphs. The symmetry representation on homology and the inclusion-induced maps from the ordinary matching complex are not determined here. Exhaustive finite verification and the stated topological reduction do not establish that equivalent unpublished or unindexed literature does not exist. An independent mathematical audit has not been performed.

## References
[1] Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406, first public posting 2019-09-23, https://arxiv.org/abs/1909.10406. The preprint's stated families and its element-matching construction were inspected.

[2] Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first public posting 2020-06-24, https://arxiv.org/abs/2006.13632. Theorem 1.1, Theorem 1.2 and their graph hypotheses were inspected.

[3] Robin Forman, *A User's Guide to Discrete Morse Theory*, Séminaire Lotharingien de Combinatoire 48 (2002), Art. B48c; background discrete Morse equivalence theorem.
