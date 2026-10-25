# The Paley-19 tournament out-neighborhood complex is a mixed sphere wedge

## Finding
Let \(P_{19}\) be the tournament with vertex set \(\mathbb Z/19\mathbb Z\) and \(i\to j\) when \(j-i\) is a nonzero quadratic residue modulo \(19\). Let \(\mathcal N^+(P_{19})\) be the simplicial complex whose faces are the subsets of an out-neighborhood of some vertex. Then
\[
\mathcal N^+(P_{19})\simeq S^2\vee\bigvee^{78}S^3.
\]
Thus its reduced **integral** homology is \(\mathbb Z\) in degree \(2\), \(\mathbb Z^{78}\) in degree \(3\), and zero in all other degrees. By the directed neighborhood--Hom equivalence of Dochtermann--Singh [1], the directed-edge Hom complex \(\operatorname{Hom}(\overrightarrow K_2,P_{19})\) has the same homotopy type.

## Assumptions and scope
The orientation uses the residue set \(Q=\{1,4,5,6,7,9,11,16,17\}\). Vertices are represented by integers \(0,\ldots,18\), and simplices by their vertex-set bit masks. The ordinary **out-neighborhood complex** is meant: a nonempty vertex subset \(\sigma\) is a face if \(\sigma\subseteq N^+(v)\) for some \(v\). This is not the directed flag complex consisting of transitive subtournaments. No group-equivariant or persistence classification is claimed.

## Proof
**Finite complex.** The out-neighborhood of vertex \(i\) is \(i+Q\). Consequently the faces are exactly all subsets of the \(19\) specified nine-element out-neighborhoods. Exact submask enumeration gives the face vector, from dimensions \(0\) through \(8\),
\[
(19,171,969,2223,2394,1596,684,171,19).
\]
There are \(8247\) faces including the empty face and \(40033\) covering relations in the augmented face poset. Their Euler characteristic is \(-76\).

**Acyclic matching.** Start with the entire augmented face poset. For each vertex \(v=0,1,\ldots,18\) in order, pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both remain unmatched. This gives \(4081\) pairs, including the pair of the empty face and a singleton. A directed-acyclicity certificate checks all \(40033\) poset covering relations: orient matched relations upward and all others downward; a complete topological sort processes all \(8247\) faces. Deleting the empty face and its pair leaves an acyclic matching on the ordinary nonempty face poset with precisely one critical vertex, four critical two-simplices and eighty-one critical three-simplices. Forman's theorem supplies a CW complex with these cells and no others.

**Integral Morse boundary.** Order the four critical two-simplices and eighty-one critical three-simplices by increasing vertex-set mask. Oriented simplices use increasing vertex order. For each matched pair \(\sigma\subset\tau\), eliminate the coefficient of \(\sigma\) by substitution from the oriented boundary \(\partial\tau\); the acyclic matching makes this recursion terminate. The resulting exact integer Morse differential \(D:\mathbb Z^{81}\to\mathbb Z^4\) has the columnwise identity
\[
D_{0j}-2D_{1j}-D_{2j}+D_{3j}=0\qquad(0\le j<81).
\]
Its submatrix with rows \(0,1,2\) and columns \(0,1,4\) is
\[
\begin{pmatrix}0&1&0\\0&1&1\\-1&0&-2\end{pmatrix},
\]
with determinant \(-1\). Therefore \(D\) has rank exactly \(3\) over \(\mathbb Q\), and its rank-three image is a primitive subgroup of \(\mathbb Z^4\). The nonzero Smith invariant factors are all \(1\), yielding the stated integral homology groups.

**Upgrade to homotopy.** The Morse CW model has a single zero-cell and no one-cells, hence is simply connected. Its two-skeleton is a wedge of four two-spheres. Each three-cell attaches along an element of \(\pi_2(\bigvee^4 S^2)\cong\mathbb Z^4\), determined exactly by the corresponding column of \(D\). Integer basis changes bringing \(D\) to Smith normal form are realized by homotopy equivalences of the two-sphere wedge and elementary changes among three-cell attachments. Three three-cells cancel three two-spheres, leaving one two-sphere and seventy-eight trivially attached three-cells. This proves the asserted wedge homotopy type.

## Verification
Run `python3 verify.py` using Python 3 and the standard library; the terminal JSON contains `"status":"VERIFY_OK"`. The code reconstructs every face and covering relation, checks the full directed graph of matching orientations is acyclic, evaluates every entry of the signed Morse boundary, verifies the displayed relation and unimodular minor, and independently repeats the reduction with reversed vertex priority. The latter has six critical two-cells, eighty-three critical three-cells, and exact rational Morse-boundary rank five, again producing ranks one and seventy-eight. The main argument rests on finite exhaustive certificates plus standard theorems of discrete Morse theory and CW homotopy theory; finite experiments alone would not establish a statement about an infinite family, and none is claimed.

## Relationship to prior work
Dochtermann and Singh [1, Sections 4--5] introduce the directed out-neighborhood complex, prove the equivalence to directed-edge Hom complexes, give a complete five-vertex tournament table, and establish general homological vanishing and realization results. These do not imply the displayed order-nineteen Paley homotopy type. Govc [2, Section 3 and Proposition 3.4] determines homotopy types for **directed flag complexes** of doubly regular tournaments including order nineteen; this is a different construction. For instance, the vertices \(\{1,4,6\}\) form a directed three-cycle lying inside the out-neighborhood of \(0\) in \(P_{19}\), hence a face of \(\mathcal N^+(P_{19})\), but not of its directed flag complex. A published Paley-19 directed-flag computation [3] also addresses that distinct construction; it is not evidence of the neighborhood result.

## Limitations
This is a single canonical finite tournament, not a uniform formula for all Paley orders or for all doubly regular tournaments. Its complete nonequivariant integral homotopy type is established, but its affine-group action, integral equivariant lattice, functorial maps, and higher-order cases are not determined. The originality comparison is limited to identified searchable records and inspected primary texts; independently discoverable equivalent work might exist. No independent audit has been performed.

## References
[1] A. Dochtermann and A. Singh, “Homomorphism complexes, reconfiguration, and homotopy for directed graphs,” arXiv:2108.10948, first posted 2021-08-24, Sections 4--5, especially Theorems 4.3 and 4.12.

[2] D. Govc, “Computing Homotopy Types of Directed Flag Complexes,” arXiv:2006.05333, first posted 2020-06-09, Section 3 and Proposition 3.4.

[3] “Affine symmetry identifies the Paley-19 directed flag complex and its homology character,” publicly indexed research record, 2026, at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-symmetry-identifies-the-paley-19-directed-flag-complex-an--9f50497a76ce/RESULT.md .
