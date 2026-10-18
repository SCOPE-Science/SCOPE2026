# A six-vertex unstable multipath module with integral two-torsion

## Finding
Let \(D=\overleftrightarrow K_{2,4}\) be the loopless digraph whose vertex set is \(\{0,1,2,3,4,5\}\), with arcs in **both** directions between every vertex of \(L=\{0,1\}\) and every vertex of \(R=\{2,3,4,5\}\), and no other arcs. For its multipath complex \(X(D)\),
\[
\widetilde H_2(X(D);\mathbb Z)\cong\mathbb Z^{7}\oplus\mathbb Z/2\mathbb Z,\qquad
\widetilde H_i(X(D);\mathbb Z)=0\quad(i\ne 2).
\]
Moreover, \(D\) itself is a single **unstable dynamical module** under Definitions 4.1, 4.2 and 4.4 of Caputi–Collari–Di Trani–Smith [1]. Thus \(D\) contradicts the conjecture stated in [1, Introduction] that integral torsion in the multipath complex of a dynamical module forces that module to be stable.

## Assumptions and scope
A face of \(X(D)\) is a subset \(F\) of the sixteen directed arcs such that (i) no two arcs of \(F\) have the same source; (ii) no two have the same target; and (iii) the directed graph on \(F\) contains no directed cycle. These are precisely spanning disjoint unions of simple directed paths; isolated vertices are permitted. Chains, orientations and homology use the usual augmented integral simplicial chain complex with each face ordered by the arc ordering below. The claim is solely about this six-vertex digraph and integral reduced homology; it does not assert minimality among all digraphs or any global classification.

## Proof
**Module and instability.** Every vertex of \(D\) has strictly positive indegree and outdegree, so all six vertices are unstable in the sense of [1, Definition 4.1]. The graph \(D\), viewed as a subgraph of itself, is a connected full dynamical region: its boundary is empty, and all directed cycles of \(D\) lie within \(D\). To show minimality, let \(M\) be any nonempty dynamical region, and choose an arc it contains. Definition 4.2(b) implies that if any directed cycle uses an arc of \(M\), then all arcs of that cycle belong to \(M\). The directed two-cycles force both orientations of every undirected edge once either orientation is present. For any distinct \(x,y\in R\), the directed four-cycle \(0\to x\to 1\to y\to0\) connects edges incident to different right vertices. Since the right part has four vertices, the graph whose nodes are the sixteen arcs and whose edges mean co-occurrence in a directed two- or four-cycle is connected. The explicit enumeration in `verify_dual.py` independently checks that the cycle-closure of the first arc contains all sixteen. Hence \(M\) contains all arcs; therefore \(D\) is the unique dynamical module and is unstable.

**Enumeration.** Order the arcs first as \((a,b)\), with \(a\in L\), \(b\in R\) lexicographically, then as \((b,a)\), with \(b\in R\), \(a\in L\) lexicographically. Enumerate each subset in increasing arc-index order and test the three conditions above. The counts of faces having respectively \(0,1,2,3,4\) arcs are
\[
(1,16,80,144,72).
\]
There is no legal five-arc subset, and therefore no higher face. The complex has dimension three. The second verifier constructs the faces recursively rather than searching the complete Boolean lattice, agreeing on the counts.

**Integral boundaries.** Let \(C_{-1}\cong\mathbb Z\) be the reduced augmentation group and \(C_j\) the free abelian group on \((j+1)\)-arc faces. With each face's arcs in increasing index order, the boundary deletes its \(k\)-th arc with sign \((-1)^k\), starting at \(k=0\). Forming all integer boundary matrices and computing exact Smith normal forms gives
\[
\begin{array}{c|c|c}
\text{map}&\text{matrix dimensions}&\text{nonzero Smith factors}\\
\partial_0:C_0\to C_{-1}&1\times16&1^{\times1}\\
\partial_1:C_1\to C_0&16\times80&1^{\times15}\\
\partial_2:C_2\to C_1&80\times144&1^{\times65}\\
\partial_3:C_3\to C_2&144\times72&1^{\times71},2^{\times1}.
\end{array}
\]
The verifier checks each composition of successive maps is zero. The top boundary is injective, since its rank is \(72\). The reduced rank in degree two is \(144-65-72=7\); the remaining reduced ranks are zero. The only nonunit Smith factor in the whole boundary sequence is the factor \(2\) in \(\partial_3\). Because \(\operatorname{im}\partial_2\) is free, the torsion of \(\operatorname{coker}\partial_3\) coincides with that of \(H_2=\ker\partial_2/\operatorname{im}\partial_3\). This proves the claimed integral group, without inferring integral torsion from a field-only calculation.

**Independent two-torsion certificate.** All \(144\) triangular faces belong to exactly two of the \(72\) tetrahedral faces, and the facet-adjacency graph is connected. The sum of all tetrahedra is therefore a nonzero mod-two three-cycle (there are no four-simplices). However, an orientation-compatible integral top cycle cannot exist: writing the tetrahedra as increasing arc-index four-tuples, the following cyclic sequence consists of consecutively adjacent facets:
\[
(0,6,9,10),\;(3,6,9,10),\;(3,5,9,10),\;(2,5,9,10),
\;(2,5,10,15),\;(0,5,10,15),\;(0,6,10,15).
\]
The incidence-sign transportation around this loop has product \(-1\). Connectivity of the facet-adjacency graph then forces every integral three-cycle to be zero: adjacent tetrahedral coefficients must agree up to sign, while the displayed loop forces a coefficient to equal its negative. Thus \(H_3(X(D);\mathbb Z)=0\), although \(H_3(X(D);\mathbb F_2)\ne0\). The universal coefficient theorem supplies a nonzero order-two class in \(H_2(X(D);\mathbb Z)\), independently corroborating the Smith computation. The second verifier checks the facet counts, connectivity and sign loop, and computes mod-two boundary ranks \((1,15,65,71)\).

## Verification
Execute `python verify_integral.py` and `python verify_dual.py` with Python 3; the first program requires SymPy with integral Smith normal form, and the second uses only the Python standard library. Each is self-contained and asserts the crucial intermediate values, rather than consuming stored results. The exact captured outputs are `verify_integral.txt` and `verify_dual.txt`. The two construction paths are different (complete Boolean-subset search versus recursive legal-face generation), as are their numerical invariants (integer Smith factors versus mod-two ranks, facet incidences and orientation obstruction). The complete code is included with this record.

## Relationship to prior work
Reference [1] defines the multipath complex and dynamical regions, treats complete bipartite digraphs with **one-way** alternating orientation via chessboard-complex Euler characteristics, and explicitly proposes the stable-module torsion conjecture. The present digraph has **both** arc orientations and is not covered by the one-way computation. Reference [2] develops cycle-free chessboard complexes for complete directed graphs and related general connectivity results, but does not determine this bidirected proper bipartite instance. Reference [3] proves qualitative finiteness and torsion results for classes of multipath complexes and matching comparisons for acyclic digraphs; the latter comparison does not apply here because \(D\) has directed two-cycles. Reference [4] studies bidirectional polygons rather than this complete bipartite graph. Related computations of **discrete-Morse matching complexes** of complete bipartite undirected graphs concern a different simplicial complex and do not imply the present result.

## Limitations
This is an exact, reproducible finite calculation accompanied by an independent geometric torsion obstruction, not an infinite-family classification. The signed Smith reduction is replayed by a general-purpose symbolic integer-algebra library, not by a separately published hand-expanded unimodular transformation. A previously unindexed equivalent calculation might exist. The statement directly refutes the formulation of the conjecture in the 2022 preprint [1]; its appearance or modification in later versions has not been assumed. Independent mathematical review has not been conducted.

## References
[1] L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first public 2022-08-09), especially Introduction, Definition 2.2, and Definitions 4.1–4.4. https://arxiv.org/pdf/2208.04656

[2] S. Vrećica and R. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252v3. https://arxiv.org/pdf/0710.5252

[3] L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1. https://arxiv.org/pdf/2401.01248

[4] L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1. https://arxiv.org/pdf/2601.05670
