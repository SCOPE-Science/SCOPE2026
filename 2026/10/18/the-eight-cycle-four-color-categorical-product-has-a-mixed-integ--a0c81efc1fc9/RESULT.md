# The eight-cycle four-color categorical product has a mixed integral sphere wedge

## Finding
Let \(C_8\) be the cycle on eight vertices, \(K_4\) the complete graph on four vertices, and \(\operatorname{Ind}(G)\) the independence complex of a simple graph \(G\). For the **categorical** graph product, not the Cartesian or strong product, there is an integral homotopy equivalence
\[
\operatorname{Ind}(C_8\times K_4)\simeq
\left(\bigvee^{3}S^{4}\right)\vee
\left(\bigvee^{6}S^{5}\right).
\]
Thus the only nonzero reduced integral homology groups are \(\widetilde H_4\cong\mathbb Z^3\) and \(\widetilde H_5\cong\mathbb Z^6\). In particular, this case is torsion-free. This is a homotopy classification, not just a homology calculation.

## Assumptions and scope
The graph has the exactly specified vertex set \(\{(i,c):i\in\mathbb Z/8\mathbb Z,\ c\in\{0,1,2,3\}\}\), with an edge between \((i,c)\) and \((j,d)\) if and only if \(j-i\equiv\pm1\pmod 8\) and \(c\ne d\). Its independence complex consists of every finite vertex subset containing no edge, including the empty face in the augmented chain convention. Every parameter in the assertion is fixed: cycle length eight and four colors. The claim does not include larger cycles or other complete-graph factors.

## Proof
Encode a vertex \((i,c)\) as bit \(4i+c\) of a nonnegative integer. Recursively enumerating subsets by excluding a vertex or including it and excluding its neighbors produces exactly 196,226 distinct nonempty independent faces. The largest faces contain 16 vertices. The full cardinality-by-face-size vector, including the empty face, is
\[
(1,32,400,2560,9400,21440,33040,37728,34488,26336,16896,8864,3648,1120,240,32,2).
\]
An independent 16-state circular transfer-matrix count gives the same vector, so the enumeration is also checked by a second formulation.

Construct a face-poset matching by processing the fixed sequence of vertex-bit indices
\[
(4,12,24,2,28,10,18,27,21,9,19,8,6,17,13,15,29,3,5,1,7,14,0,31,20,30,26,22,25,11,23,16).
\]
At each index, pair every as-yet-unmatched face lacking that vertex to its one-vertex extension whenever both remain unmatched. This creates 98,106 disjoint covering pairs, leaving one critical vertex, five critical four-cells, and eight critical five-cells. To certify that this is a discrete-Morse matching, direct every unmatched covering incidence downward and every matched incidence upward. Enumerating all 1,457,216 nonempty Hasse covering incidences, a topological sort of this directed graph removes all 196,226 vertices; hence it is acyclic.

With the critical cells ordered by their integer bit masks, the signed integral Morse differential from degree five to degree four is exactly
\[
\partial_5=\begin{pmatrix}
0&0&1&0&-1&0&-1&-1\\
0&0&0&0&0&0&0&0\\
0&0&1&0&-1&0&-1&-1\\
-1&0&0&0&0&-1&0&0\\
0&0&0&0&0&0&0&0
\end{pmatrix}.
\]
All entries are reconstructed as signed gradient-path counts using the rule that a matched lower cell is eliminated by its unit-coefficient occurrence in the boundary of its matched upper cell. The first and third rows agree, and the remaining nonzero row is independent; therefore the matrix has rank two. Its minor on rows one and four and columns one and three has determinant one (indices counted from one). Hence its two nonzero Smith invariant factors are both units. The reduced Morse complex has no nonzero cells outside degrees four and five, in addition to a single zero-cell.

The Morse CW complex therefore has a four-skeleton which is a wedge of five four-spheres. Its eight five-cell attaching maps represent integer degree vectors in \(\pi_4(\bigvee^5S^4)\cong\mathbb Z^5\), so the displayed integral matrix determines these maps completely; there are no higher attaching terms in this degree. Integral elementary basis changes implement the unit Smith diagonalization, and the resulting two unit four/five cell pairs cancel up to homotopy. The remaining cells yield exactly three four-spheres and six five-spheres, proving the assertion.

## Verification
The standalone Python 3 standard-library program `verify.py` constructs the graph, enumerates the complete independence complex, verifies all oriented covering incidences and matching acyclicity, computes the complete signed Morse boundary, checks its rank and a unit maximal minor, and independently recomputes the full face vector using a 16-state transfer algorithm. It also repeats the computation with a second explicit vertex order: that matching leaves one critical zero-cell, seven four-cells, and ten five-cells, and has integral boundary rank four with a unit maximal minor. Both calculations yield three degree-four and six degree-five sphere summands. Running `python3 verify.py` prints the two certificates and the final homotopy conclusion. No nonstandard packages or external files are required.

## Relationship to prior work
Antolín Camarena and Carnero Bravo (arXiv:2307.12401v1, July 23, 2023), in their classification of independence complexes of categorical products, determine the cases of cycle lengths divisible by three and of lengths four and five, and prove that for other cycle lengths only two consecutive homological dimensions and certain Moore-space possibilities remain. Their Question 24 asks whether the integral homology in the remaining cases is always torsion-free. The paper reports finite free-homology computations for the eight-cycle with three colors, but does not state the present four-color eight-cycle homotopy classification. The path-factor theorems in Carnero Bravo (arXiv:2505.06457v1, May 9, 2025) do not identify this four-color cyclic product. A separately indexed calculation for the seven-cycle with four colors produces a mixed wedge in one lower pair of dimensions; that adjacent calculation alone supplies no natural suspension equivalence or attaching-map information for the eight-cycle. These comparisons are relative to inspected material; they do not establish global uniqueness.

## Limitations
The result concerns only \(\operatorname{Ind}(C_8\times K_4)\). It neither resolves the all-parameter torsion question nor proves a natural suspension map relating different cycle lengths. Both complete discrete-Morse certificates and the integral boundary are finite, executable evidence for this one graph; no numerical evidence is extrapolated to an infinite family. An inaccessible or unindexed equivalent earlier result remains possible.

## References
1. Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (July 23, 2023), https://arxiv.org/abs/2307.12401 .
2. Andrés Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v1 (May 9, 2025), https://arxiv.org/html/2505.06457v1 .
3. Shuchita Goyal, Samir Shukla, and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, 2021, https://cdm.ucalgary.ca/article/view/71284 .
