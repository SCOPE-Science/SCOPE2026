# Pentagon correction for ordinary four-cut complexes of girth-five graphs

## Finding
For a finite simple graph \(G\) on \(n\ge8\) vertices with no triangles or quadrilaterals, write \(c_4(G)\) for the number of connected induced four-vertex subsets and \(c_5(G)\) for the number of unoriented five-cycles. Set
\[
b(G)=\binom{n-1}{3}-c_4(G)+c_5(G).
\]
Then \(b(G)\) is a nonnegative integer and the combinatorial Alexander dual of the ordinary four-cut complex satisfies
\[
\Delta_4(G)^\vee\simeq\bigvee^{b(G)} S^2.
\]
Consequently, its original cut complex has complete reduced integral homology
\[
\widetilde H_i(\Delta_4(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{b(G)},&i=n-5,\\
0,&i\ne n-5.
\end{cases}
\]
The zero-fold wedge is interpreted as a point. No assertion is made that the original cut complex itself is a wedge of spheres.

## Assumptions and scope
Graphs are finite and simple and need not be connected. The girth hypothesis means that no three-cycle or four-cycle occurs (forests qualify). A four-cut complex has facets \(V(G)\setminus A\), where \(|A|=4\) and \(G[A]\) is disconnected. A combinatorial Alexander dual contains a face \(S\) precisely when the complementary set is not a face of the original complex. Hence a set \(S\) belongs to \(D=\Delta_4(G)^\vee\) exactly when **every** four-subset of \(S\) induces a connected graph; all subsets of size below four automatically qualify.

## Proof
**1. Classify the faces.** Every connected induced four-set is a tree, necessarily an induced three-edge path or a three-leaf star. If a five-set has all four-subsets connected, deleting each vertex leaves a connected graph. Its induced graph has minimum degree at least two; a simple graph with five vertices, girth at least five and minimum degree two is precisely an induced pentagon. Conversely each pentagon has five connected four-subsets. No six-set qualifies: choose a pentagon inside it and an outside vertex. The outside vertex has at most one neighbor on the pentagon, otherwise there is a triangle or quadrilateral; among the other four or more pentagon vertices are three inducing a disconnected graph. Together with the outside vertex they violate the four-subset condition. Thus \(D\) has the entire two-skeleton of the simplex on \(n\) vertices, one tetrahedron for each connected four-set, and one four-simplex for each pentagon; it has no higher faces.

**2. Prove the integral boundary ranks with unit minors.** Write \(\partial_j\) for signed simplicial boundaries in \(D\). The complete two-skeleton gives \(\operatorname{rank}\partial_1=n-1\) and \(\operatorname{rank}\partial_2=\binom{n-1}{2}\), with saturated images. Each star tetrahedron has the triangle of its three leaves as a private two-face: a second vertex adjacent to all three would yield a quadrilateral. For an induced path \(a-b-c-d\), the triangle \(\{a,b,d\}\) contains only the edge \(ab\). A connected four-set containing this triangle must have a fourth vertex adjacent to \(d\) and to either \(a\) or \(b\). The choice \(b\) uniquely recovers \(c\), since two such vertices would form a quadrilateral. An alternative neighbor of \(a\) and \(d\), if present, is unique and closes the original path to a pentagon. Thus a path tetrahedron not contained in a pentagon has a private two-face.

Two distinct pentagons cannot share an induced four-vertex path: their different fifth vertices would be two common neighbors of its endpoints and produce a quadrilateral. For each pentagon, its five distinct path tetrahedra therefore form a disjoint block. Label its cycle consecutively \(v_0,\ldots,v_4\) modulo five, and use the five triangles \(\{v_i,v_{i+1},v_{i+3}\}\). Each lies in exactly two of the five path tetrahedra and no tetrahedron outside that pentagon. The selected signed boundary submatrix is, up to changing row and column signs, the oriented incidence matrix of a five-cycle. It has rank four and possesses a unit determinant minor of order four. The private star and nonpentagon-path triangles, together with the unit minors of these disjoint pentagon blocks, give a unit maximal minor of size \(c_4(G)-c_5(G)\) in \(\partial_3\).

The boundary of every pentagon four-simplex is a relation among its five path tetrahedra; the pentagons have disjoint such path supports. Consequently \(\operatorname{rank}\partial_3\le c_4(G)-c_5(G)\), so the displayed minor proves equality and proves that \(\operatorname{im}\partial_3\) is a primitive sublattice. The disjoint supports also give an identity subminor of order \(c_5(G)\) for \(\partial_4\), making \(\operatorname{im}\partial_4\) primitive and of rank \(c_5(G)\). Since \(\partial_3\partial_4=0\), equality of their ranks with \(\operatorname{rank}\ker\partial_3\) forces \(\ker\partial_3=\operatorname{im}\partial_4\): their quotient is finite yet torsion-free because \(\operatorname{im}\partial_4\) is primitive.

**3. Recover homology and homotopy.** The only nonzero reduced integral homology of \(D\) is
\[
\widetilde H_2(D;\mathbb Z)\cong\mathbb Z^{\binom{n-1}{3}-c_4(G)+c_5(G)}.
\]
Indeed the complete two-skeleton contributes \(\binom{n-1}{3}\) two-cycles and the primitive image of \(\partial_3\) removes \(c_4-c_5\) independent ones. The complete two-skeleton also makes \(D\) simply connected. The Hurewicz theorem supplies spherical representatives for a basis of \(H_2\), and the simply connected homology form of Whitehead's theorem identifies \(D\) with the displayed wedge of two-spheres. Integral combinatorial Alexander duality on the \(n\)-vertex set yields \(\widetilde H_i(\Delta_4(G);\mathbb Z)\cong \widetilde H^{n-i-3}(D;\mathbb Z)\), giving the complete original homology formula.

## Verification
The independent standard-library script `girth_five_four_cut_check.py` reconstructs the graph and both local incidence patterns from graph edges. It checks the girth restrictions, star private-face assertion, uniqueness of pentagon membership for path tetrahedra, support of path-triangle boundary rows, all qualifying five-sets, absence of qualifying six-sets, and a characteristic-two rank equality. The finite checks are consistent with the integral argument but are not a proof by finite sampling. Reproduced instances are: Petersen graph \((n,c_4,c_5,b)=(10,70,12,26)\), dodecahedral graph \((20,140,12,841)\), eight-cycle \((8,8,0,27)\), nine-cycle \((9,9,0,47)\), and a pentagon with three isolated vertices \((8,5,1,31)\).

## Relationship to prior work
The ordinary cut-complex definition and Alexander duality framework are due to Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue [1]. Their work determines the two-cut topology of the Petersen graph, and their sequel [2] treats graph disjoint unions, grid graphs, squared paths, and related symmetry modules. Existing high-girth four-cut results require **girth at least six** and correspond exactly to the special case \(c_5(G)=0\). The present statement is the first-girth-boundary extension: each pentagon contributes one independent integral correction, not merely an Euler-characteristic observation. The specific Petersen four-cut rank \(26\) has already appeared in earlier computations and is cited here only as a consistency check, not claimed anew.

## Limitations
The new theorem applies only when three-cycles and four-cycles are absent. It determines homotopy type of the Alexander dual and integral homology of the original cut complex, but not the latter's homotopy type, shellability, or its automorphism representation. The finite checker tests five examples; the infinite-family conclusion is supplied entirely by the preceding proof. No assertion of bibliographic uniqueness beyond the inspected literature is made.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first arXiv version 2023-04-26), https://arxiv.org/abs/2304.13675.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (2024-07-11), https://arxiv.org/abs/2407.08158.
