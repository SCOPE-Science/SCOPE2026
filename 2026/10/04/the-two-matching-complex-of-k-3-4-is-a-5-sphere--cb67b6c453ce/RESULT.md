# The two-matching complex of \(K_{3,4}\) is a 5-sphere
## Finding
For the complete bipartite graph \(K_{3,4}\), the two-matching complex \(M_2(K_{3,4})\) is homotopy equivalent to \(S^5\).

Here the two-matching complex of a graph \(G\) is the simplicial complex whose vertices are the edges of \(G\) and whose faces are edge sets in which every graph vertex has degree at most \(2\). This is the first unequal complete-bipartite instance immediately beyond the exact parameter regimes treated in the closest higher-matching-complex paper: the known shellable regime has the matching bound at least the smaller bipartition size, while the balanced boundary case \(M_2(K_{3,3})\) is handled separately.

## Assumptions and scope
The graph is the simple complete bipartite graph with parts \(A=\{a_1,a_2,a_3\}\) and \(B=\{b_1,b_2,b_3,b_4\}\). A face is any subset of the twelve edges such that every vertex of \(A\cup B\) is incident to at most two selected edges. No claim is made for \(M_2(K_{3,n})\) with \(n>4\), nor for higher matching bounds.

## Proof
Index the twelve edges in row-major order by
\[
e_{4(i-1)+(j-1)}=a_i b_j,\qquad 1\le i\le3,\quad1\le j\le4.
\]
Apply sequential elementary discrete-Morse matchings to the nonempty face poset, toggling the edges in the order
\[
e_7,e_4,e_6,e_3,e_2,e_0,e_{10},e_1,e_9,e_8,e_{11},e_5.
\]
At a step for edge \(e\), pair every currently unmatched face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever the latter is also currently unmatched and remains a two-matching. Because each stage is an elementary matching on the residual poset, the union is a discrete-Morse matching; the embedded verifier additionally checks acyclicity directly on every oriented Hasse edge.

Exhaustive reconstruction gives \(1081\) faces including the empty face, with face vector
\[
(12,66,204,360,324,114).
\]
The matching contains \(539\) pairs and leaves exactly two critical nonempty cells: one vertex, namely \(e_7=a_2b_4\), and one five-simplex whose six edges are
\[
\{a_1b_1,a_1b_2,a_2b_2,a_2b_3,a_3b_1,a_3b_4\}.
\]
Forman's discrete Morse theorem therefore gives a CW complex with one zero-cell and one five-cell and no cells in dimensions \(1\) through \(4\). The attaching map of the five-cell has target a point, so the resulting CW complex is \(S^5\). Hence the original complex is homotopy equivalent to \(S^5\).

## Verification
The standalone program `verify_m2_k34.py` reconstructs the complex directly from the degree constraints. It checks all \(1081\) faces, all \(114\) facets, all \(4488\) nonempty Hasse covers, every matching pair, and acyclicity by a full topological sort of the Morse-oriented Hasse graph. It independently forms the simplicial boundary matrices over \(\mathbb F_2\) and computes their ranks in two elimination orientations; both routes give
\[
(11,55,149,211,113),
\]
so the ordinary Betti vector is \( (1,0,0,0,0,1)\), consistent with the Morse proof. Running `python3 verify_m2_k34.py` ends with `VERIFY_OK`.

## Relationship to prior work
Singh's higher-matching-complex paper gives a closed homotopy formula for \(M_r(K_{m,n})\) when, after ordering the parts with \(m>n\), one has \(m>r\ge n\), and separately proves \(M_{n-1}(K_{n,n})\simeq S^{(n-1)^2-1}\). For \(K_{3,4}\) with \(r=2\), the ordered parameters are \(m=4\), \(n=3\), and \(r=2<n\), so neither theorem applies. The full text explicitly gives \(M_2(K_{3,2})\) as the shelling example and \(M_2(K_{3,3})\) as the balanced sphere boundary case, but does not state the \(K_{3,4}\) homotopy type. Vega's two-matching-complex work treats different graph families, including wheels and perfect caterpillars. Earlier work of Reiner and Roberts computes rational homology for broad chessboard-type complexes; rational homology alone does not imply the present homotopy-sphere statement.

The topology ownership source is Miyata--Ramos, which treats \(d\)-matching complexes as topological graph complexes and is classified primarily in MSC 55U10 in the checked MSC2020 record. Singh's publication record for the exact higher-matching setting is likewise indexed under MSC 55U10 in the checked MSC2020 database record.

## Limitations
The theorem is an exact finite homotopy computation, not a classification of the unresolved region \(r<\min(m,n)\). The originality assessment is limited to the inspected primary texts, indexed searches, and the available prior ledger. A rational-homology calculation for this parameter may be implicit in older representation-theoretic formulas, but such a calculation would not imply the discrete-Morse homotopy equivalence proved here.

## References
1. Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632; DOI:10.1016/j.disc.2021.112761.
2. Dane Miyata and Eric Ramos, *The graph minor theorem in topological combinatorics*, arXiv:2012.01679; DOI:10.1016/j.aim.2023.109203.
3. Julianne Vega, *Two-Matching Complexes*, arXiv:1909.10406.
4. Victor Reiner and Joel Roberts, *Minimal Resolutions and the Homology of Matching and Chessboard Complexes*, DOI:10.1023/A:1008728115910.
