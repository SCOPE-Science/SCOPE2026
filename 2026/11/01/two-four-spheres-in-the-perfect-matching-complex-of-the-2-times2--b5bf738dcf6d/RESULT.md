# Two four-spheres in the perfect-matching complex of the \(2\times2\times3\) honeycomb

## Finding

Let \(H_{2\times2\times3}\) be the hexagonal honeycomb graph bounding a triangular-lattice hexagon with consecutive side lengths \(2,2,3,2,2,3\). Its **perfect-matching complex** \(\mathcal M_p(H_{2\times2\times3})\), whose vertices are graph edges and whose simplices are subsets of perfect matchings, satisfies

\[
\boxed{\mathcal M_p(H_{2\times2\times3})\simeq S^4\vee S^4.}
\]

In particular, its only nonzero reduced integral homology is \(\widetilde H_4\cong\mathbb Z^2\). This is a homotopy statement, not merely an assertion about homology over one field.

## Assumptions and scope

The graph is finite and simple, with 32 vertices and 41 edges. Here is an exact constructive convention, fixing all labels required by the verification. Use the triangular-lattice basis \(e_1=(1,0)\), \(e_2=(1/2,\sqrt3/2)\), writing a point as its integer basis coordinates \((i,j)\). The six consecutive polygon corners in these coordinates are

\[
(0,0),\ (2,0),\ (2,2),\ (-1,5),\ (-3,5),\ (-3,3).
\]

List all unit triangular cells with centroids in the closed polygon, in lexicographic order of the integers \((i,j)\) producing them and with the triangle \(\{(i,j),(i+1,j),(i,j+1)\}\) before \(\{(i+1,j+1),(i+1,j),(i,j+1)\}\). Their 32 cells form the graph vertices. Two cells are adjacent when they share a unit lattice edge. Sort the 41 resulting pairs of cell indices lexicographically and number the graph edges from 0 to 40. This is the standard planar dual construction for lozenge tilings of the hexagonal region; adjacent triangles form one lozenge. A graph perfect matching therefore gives a lozenge tiling.

Every graph perfect matching has 16 edges. The 50 perfect matchings are exactly the facets of the complex. The theorem refers to this particular complete perfect-matching subcomplex, not to the larger ordinary matching complex.

## Proof

**Finite construction.** Enumerate all elementary triangular cells by the exact half-plane inequalities for the six polygon sides, with rational centroid coordinates. Form the graph by unit-edge incidence. For each perfect matching, choose any uncovered graph vertex, recursively select an incident graph edge, and continue on the remaining vertices. Distinct edge sets are deduplicated. This exhaustive procedure yields 50 perfect matchings, each of 16 edges. It is independently checked by a bipartite matching-count dynamic program and by MacMahon's plane-partition product, both giving 50. The same geometric procedure for side lengths \((2,2,2)\) gives 24 vertices, 30 edges, 20 matchings and 66,370 augmented faces, agreeing with the 66,369 nonempty faces of that earlier case.

**A complete acyclic pairing.** Encode a face \(F\) by the bitmask \(\sum_{e\in F}2^e\). Form exactly the union of the power sets of all 50 perfect matching facets. There are 2,517,788 distinct faces *including the empty face*. Sequentially, for each graph-edge index \(e=0,\ldots,40\), perform the element pairing

\[
(F,F\cup\{e\})\quad\text{whenever }e\notin F\text{ and both faces remain unpaired}.
\]

Remove both members of each pair before advancing to the next edge index. This is a finite, deterministic algorithm; `check_honeycomb_223.py` reproduces all exact integer sets and comparisons. The standard successive-element-pairing lemma (Theorem 8 of Bayer--Jelić Milutinović--Vega) establishes that the union of these pairs is acyclic. There is no reliance on a finite sample to claim acyclicity for a larger parameter range: the specified complex is finite, and every face is enumerated.

There are exactly 1,258,893 pairs. The only unpaired faces have graph-edge index sets

\[
\{1,11,12,21,35\}\quad\text{and}\quad\{1,10,16,20,37\}.
\]

They both contain five vertices of the simplicial complex and hence have dimension four. No other nonempty face is critical; the empty face is paired in the first element pairing. For reproducibility, the nonzero pairing stages \((e,\text{number of pairs})\) are

\[
\begin{gathered}
(0,1011306),(1,215384),(5,31579),(8,146),(11,3),\\
(14,95),(16,305),(18,66),(20,3),(22,3),\\
(31,1),(32,1),(35,1).
\end{gathered}
\]

All other stages make zero pairs. The displayed counts exhaust the augmented face set, since \(2(1,258,893)+2=2,517,788\).

**Homotopy conclusion.** Forman's discrete-Morse theorem supplies a CW complex homotopy equivalent to the perfect-matching complex, with one 0-cell (because the empty face was paired) and the two critical four-cells, and no other cells. Both four-cells attach to the unique zero-cell by the constant attaching map, giving precisely \(S^4\vee S^4\).

## Verification

Run `python3 check_honeycomb_223.py` using Python's standard library; no third-party modules, online databases or files outside this package are required. The independent bipartite matching count, MacMahon product, enumerated matching facets, face vector, 41 successive pairing stages, terminal critical faces and Euler characteristic are asserted inside the checker. Expected marker: `HONEYCOMB_2_2_3_TWO_4_SPHERES_OK`. Actual output is `honeycomb_223_verification.json`.

The full face vector in degrees 0 through 15 is

\[
(41,706,6186,31566,104477,241386,407750,517618,501141,371866,210600,89700,27900,6000,800,50).
\]

The independently accumulated reduced Euler characteristic is \(2\), agreeing with the two even-dimensional spheres. Unlike a homology-only computation, the explicit critical-cell pattern and acyclicity theorem prove the integral homotopy equivalence.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega introduced and studied perfect-matching complexes of honeycomb graphs. Their main results classify all single-layer \(H_{1\times m\times n}\) cases and establish \(\mathcal M_p(H_{2\times2\times2})\simeq S^3\vee S^3\). Their conclusion expressly identifies larger honeycomb instances as requiring another approach. Their theorem for the symmetric side-two hexagon does not imply the topology when one side is enlarged to three.

Chandrakar and Singh later classify perfect-matching complexes of polygonal **line** tilings and two-row square grids; these do not encompass the two-dimensional hexagonal array \(H_{2\times2\times3}\). Enumeration of lozenge tilings or MacMahon's count determines the number of maximal simplices, not the homotopy type of their union. The proof above supplies the latter for the first nonsymmetric three-dimensional side-length triple beyond the earlier side-two case.

## Limitations

This claim is restricted to side lengths \((2,2,3)\). It does not assert a uniform classification of \(H_{2\times2\times n}\) for larger \(n\), an integral symmetry representation, an equivalence for the ordinary matching complex, or an independent external audit. A published or unindexed mathematically equivalent earlier classification remains a possible literature risk, notwithstanding the stated comparisons. The verification is an exhaustive finite computation with a mathematically justified acyclic pairing, not an unbounded numerical extrapolation.

## References

1. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electron. J. Combin. **30** (2023), #P2.45, arXiv:2209.02803 (first public 2022-09-06), doi:10.37236/11525. Definitions 1 and 7, Theorems 6 and 8, the side-two case and Section 5.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first public 2024-07-08), Ann. Comb. (2025). Sections 1, 3--5.
3. R. Forman, *A User's Guide to Discrete Morse Theory*, Sém. Lothar. Combin. **48** (2002), B48c.
4. G. Kuperberg, *Symmetries of Plane Partitions and the Permanent--Determinant Method*, J. Combin. Theory Ser. A **68** (1994), 115--151.
