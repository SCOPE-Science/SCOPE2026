# Complete mod-two Rips persistence of the four-letter permutahedron
## Finding
For the 24 permutations of four labels, equip the vertex set with Kendall's adjacent-transposition distance. Let \(K_r\) be its **inclusive**, graph-metric Vietoris--Rips complex at real scale \(r\ge 0\). Over \(\mathbb F_2\), the complete barcode of nonzero-length intervals in ordinary (unreduced) homology is
\[
\begin{array}{c|l}
\text{degree}&\text{intervals with multiplicity}\\\hline
0&23[0,1),\ [0,\infty)\\
1&13[1,2)\\
2&8[2,3),\ [2,4)\\
4&5[4,5)\\
5&2[4,5)\\
11&[5,6).
\end{array}
\]
There are no other positive-length bars. In particular, degree two has a persistent class across scales two and three, while five degree-four and two degree-five classes coexist at scale four. The full scale-five complex has homotopy type \(S^{11}\), and the complex becomes contractible at scale six.

## Assumptions and scope
Vertices are all \(p=(p_1,p_2,p_3,p_4)\) that permute \(\{0,1,2,3\}\). Edges correspond to swapping a pair of adjacent positions. The distance \(d(p,q)\) is the minimum number of such swaps transforming \(p\) into \(q\); equivalently, if \(r_i\) is the position of \(p_i\) in \(q\), then
\[
 d(p,q)=|\{(i,j):1\le i<j\le4,\ r_i>r_j\}|.
\]
This is the intrinsic shortest-path metric on the 1-skeleton of the three-dimensional permutahedron (also realized combinatorially as the truncated octahedral graph), **not** Euclidean chordal distance in a spatial embedding. The inclusive complex \(K_r\) has a simplex on every finite collection of vertices of pairwise distance at most \(r\). Since all distances lie in \(\{0,1,\ldots,6\}\), the filtration changes only at integral scales. Homology and intervals, except for the stated sphere identification at scale five, are over \(\mathbb F_2\); no claim is made about integral torsion or the other homotopy types.

## Proof
The adjacent-swap graph has 24 vertices and 36 edges. The exhaustive but finite argument below is implemented by two standalone, independently organized Python programs accompanying this statement. All loops are bounded by explicitly defined finite sets; their correctness is reducible to the elementary definitions of a flag complex, simplicial boundary, and linear algebra over \(\mathbb F_2\).

First enumerate the 24 permutations in lexicographic order. Independently compute their pairwise graph distances by breadth-first search on adjacent-swap edges and by the inversion formula; the two agree for every ordered pair. For each scale \(r\in\{0,1,2,3,4\}\), recursively enumerate all increasing vertex tuples whose new vertices are adjacent to all preceding vertices in the graph of distances at most \(r\). Every nonempty clique occurs exactly once. The full face vectors are
\[
\begin{array}{c|l}
r&(f_0,f_1,\ldots)\\\hline
0&(24)\\
1&(24,36)\\
2&(24,96,112,30)\\
3&(24,168,472,618,384,92)\\
4&(24,228,1112,3042,4848,4592,2592,822,112).
\end{array}
\]
To compute boundary ranks, index each dimension's oriented simplices (signs disappear in characteristic two). A column for a simplex is the bitset of all codimension-one faces obtained by deleting one vertex. Reduce columns using the highest set-bit pivot, successively XORing an earlier basis column whenever a pivot repeats; over a field this is exact Gaussian elimination. The boundary ranks, including zero ranks at both ends, are
\[
\begin{array}{c|l}
r&(\operatorname{rank}\partial_0,\operatorname{rank}\partial_1,\ldots)\\\hline
0&(0,0)\\
1&(0,23,0)\\
2&(0,23,73,30,0)\\
3&(0,23,145,326,292,92,0)\\
4&(0,23,205,907,2135,2708,1882,710,112,0).
\end{array}
\]
Thus the reduced Betti numbers at scales \(0,1,2,3,4\) are, respectively, \(\widetilde\beta_0=23\); \(\widetilde\beta_1=13\); \(\widetilde\beta_2=9\); \(\widetilde\beta_2=1\); and \((\widetilde\beta_4,\widetilde\beta_5)=(5,2)\), with no others.

One inclusion-map rank is not implied by the Betti numbers alone. At scale two, reducing the 112 columns of \(\partial_2\) while tracking their linear dependencies gives a basis of 39 two-cycles. Embed each cycle's triangles in the triangle basis at scale three. Reduce their columns jointly against the 326-dimensional space of boundaries of scale-three tetrahedra. The combined rank is 327, so
\[
\operatorname{rank}_{\mathbb F_2}\bigl(H_2(K_2)\longrightarrow H_2(K_3)\bigr)=327-326=1.
\]
The remaining eight scale-two classes die at scale three, and the surviving one dies by scale four (where second homology vanishes). All other positive-dimensional homology degrees have disjoint successive-scale support, forcing the displayed births and deaths. The connectedness of the scale-one graph gives the degree-zero intervals.

Finally, each permutation has exactly one vertex at distance six, its reverse in relative order. These 12 forbidden pairs form a perfect matching on all 24 vertices. Consequently, at scale five \(K_5\) is the independence complex of 12 disjoint edges: the simplicial join of 12 zero-spheres, homeomorphic to \(S^{11}\). At scale six every pair is permitted and \(K_6\) is the full 23-simplex. This gives the final two intervals, and completes the proof.

A second program does **not** reuse the chain-group rank calculation: it independently enumerates the 17,372 nonempty simplices present by scale four and performs standard filtration-ordered boundary matrix reduction (birth, dimension, vertex tuple), explicitly pairing every positive-dimensional class with its death. It reproduces all claimed intervals through scale four, including the nontrivial persistence-map rank.

## Verification
From the directory containing the attached programs, run `python3 verify_ranking_rips.py` followed by `python3 verify_persistence.py`. Both use only Python's standard library. The first must print `VERIFY_OK`, and the second `PERSISTENCE_OK`. Both reconstruct the entire data from the defining permutations; no cached distance tables, boundary matrices, or previously computed ranks are required. The second verifies all 17,372 nonempty simplices with births up to scale four. Scale five and scale six have conceptual join/simplex proofs rather than exponential face enumeration.

## Relationship to prior work
Adamaszek established general links between clique complexes of graph powers and graph-metric Rips complexes, with homotopy theorems and examples. Adamaszek--Adams analyzed a circle and finite cyclic samples using winding fractions; that methodology motivates study of explicit metric-space filtrations but does not calculate this permutation metric. Saleh, Titz Mite, and Witzel calculated graph-metric Rips complexes of Platonic solids, explicitly pointing to other polyhedra as a direction. The permutahedron is an Archimedean polyhedron, not one of the five Platonic solids. The separate permutahedral-lattice approach of Choudhary, Kerber, and Raghvendra uses the permutahedron to approximate filtrations of *other point sets*, rather than taking a shortest-path metric on the permutahedron's vertices.

Published finite graph-metric Rips calculations for the truncated tetrahedron and truncated cube concern different graphs; despite both the truncated cube and permutahedron having 24 vertices, their graph distance functions and cliques differ. Searches using adjacent-transposition/Kendall-tau, permutahedron, truncated octahedron, Rips, persistent homology, flag complexes, and graph powers did not identify the complete barcode stated here. Those searches cannot prove absolute originality.

## Limitations
The result is specific to the four-label ranking metric and to characteristic two. It does not determine integral homology at intermediate scales, homotopy types at scales two through four, higher-degree symmetric groups, or Euclidean realizations. Exhaustive finite computation is a proof for the precisely defined finite object, not an extrapolation to all permutahedra. A prior equivalent computation absent from the consulted literature remains possible.

## References
1. M. Adamaszek and H. Adams, “The Vietoris--Rips complexes of a circle,” arXiv:1503.03669v1 (first publicly posted 2015-03-12), *Pacific Journal of Mathematics* 290 (2017), 1--40; primary MSC 55U10.
2. M. Adamaszek, “Clique complexes and graph powers,” arXiv:1104.0433, *Israel Journal of Mathematics* 196 (2013), 295--319.
3. N. Saleh, T. Titz Mite, and S. Witzel, “Vietoris--Rips complexes of Platonic solids,” arXiv:2302.14388, *Innovations in Incidence Geometry* 21 (2024), 17--34.
4. A. Choudhary, M. Kerber, and S. Raghvendra, “Polynomial-Sized Topological Approximations Using the Permutahedron,” arXiv:1601.02732.
5. Public comparative findings: “The graph-metric Rips filtration of the truncated tetrahedron” and “A mixed-dimensional Rips wedge for the truncated cube,” published-finding corpus research repository (2026).
