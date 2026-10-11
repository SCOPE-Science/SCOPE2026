# The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres
## Finding
For the complete bipartite graph \(K_{4,4}\), let \(M_2(K_{4,4})\) be the simplicial complex whose vertices are the sixteen edges of \(K_{4,4}\) and whose faces are the edge sets in which every graph vertex has degree at most \(2\). Then \(M_2(K_{4,4})\simeq\bigvee^{15}S^5\).

## Assumptions and scope
Let the two parts of \(K_{4,4}\) be \(A=\{a_0,a_1,a_2,a_3\}\) and \(B=\{b_0,b_1,b_2,b_3\}\). Label the edge \(a_i b_j\) by the integer \(4i+j\). The complex \(M_2(K_{4,4})\) has these sixteen edges as vertices; a set \(\sigma\) is a face exactly when every vertex of the graph \((A\sqcup B,\sigma)\) has degree at most \(2\). All statements refer to the ordinary geometric realization of this finite abstract simplicial complex.

## Proof
Enumerating all nonempty subsets of the sixteen graph edges subject to the degree bound gives \(7342\) faces. On their face poset, use the fixed edge order
\[
7,2,5,10,1,11,13,9,12,15,8,0,4,3,14,6.
\]
At each stage with edge \(e\), pair every still-unmatched face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever both faces are still unmatched. This gives \(3663\) matched Hasse pairs. The only unmatched faces are one vertex and fifteen faces of dimension \(5\).

A complete orientation check supplies the needed nonstandard lemma rather than assuming the greedy matching is acyclic: orient each unmatched Hasse cover from the lower face to the higher face and reverse each matched cover. There are exactly \(37728\) nonempty-face Hasse covers. A topological sort visits all \(7342\) vertices of the resulting directed graph, so the matching is acyclic. Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(M_2(K_{4,4})\) with one \(0\)-cell and fifteen \(5\)-cells and no cells in dimensions \(1,2,3,4\). Its \(4\)-skeleton is a point, hence every \(5\)-cell has the unique constant attaching map \(S^4\to *\). Thus the CW complex is \(\bigvee^{15}S^5\), proving the claim.

## Verification
The standalone verifier `verify.py` reconstructs the complex from the degree condition and checks the matching and every directed Hasse edge. It obtains the face vector
\[
(16,120,528,1428,2304,2040,816,90),
\]
where the entries count faces in dimensions \(0\) through \(7\). The critical-face counts are one in dimension \(0\) and fifteen in dimension \(5\). Independently of the Morse conclusion, exact row reduction over \(\mathbf F_2\) gives boundary ranks
\[
(15,105,423,1005,1299,726,90)
\]
for \(\partial_1,\ldots,\partial_7\), hence reduced Betti number \(15\) only in degree \(5\). The Euler characteristic is \(-14\), so the reduced Euler characteristic is \(-15\). `certificate.json` records these counts and the sixteen critical masks.

## Relationship to prior work
Singh defines these higher matching complexes and emphasizes that exact homotopy types are known only for relatively few graph classes. For complete bipartite graphs, Singh's Theorem 1.2 covers \(M_r(K_{m,n})\) when \(m>r\ge n\), and the balanced family \(M_{n-1}(K_{n,n})\simeq S^{(n-1)^2-1}\). Neither clause applies to \(M_2(K_{4,4})\): here \(r=2<n=4\), while the balanced theorem gives the different complex \(M_3(K_{4,4})\simeq S^8\). Reiner and Roberts compute characteristic-zero homology of chessboard complexes with multiplicities and bounded-degree graph complexes, which can control rational homology but does not supply the homotopy equivalence proved here. Vega's two-matching paper develops discrete-Morse methods for leaf attachments, wheels, and perfect caterpillars rather than this complete-bipartite case.

## Limitations
The result is specific to \(K_{4,4}\) at degree bound \(2\). It does not assert a formula for \(M_2(K_{n,n})\) for larger \(n\), does not compute the natural \(S_4\times S_4\) action on homology, and does not claim shellability. The independent homology calculation is a finite cross-check, not a substitute for the acyclic matching used to obtain the homotopy type.

## References
1. Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 2020-06-24; later Discrete Mathematics 345 (2022), 112761.
2. Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406, first posted 2019-09-23.
3. Victor Reiner and Joel Roberts, *Minimal Resolutions and the Homology of Matching and Chessboard Complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154, DOI 10.1023/A:1008728115910.
4. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
