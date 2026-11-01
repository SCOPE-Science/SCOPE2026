# The \(D_4\)-homology character of the four-by-four grid matching complex

## Finding
Let \(G=P_4\square P_4\), the sixteen-vertex Cartesian square grid, and \(\mathcal M(G)\) its ordinary matching complex. The dihedral group \(D_4\) acts by square symmetries. Its complete rational homology representations in the two nonzero reduced degrees are
\[
\widetilde H_4(\mathcal M(G);\mathbb Q)\cong A_1\oplus 2A_2\oplus B_1\oplus E,\qquad
\widetilde H_5(\mathcal M(G);\mathbb Q)\cong E.
\]
Here \(A_1\) is trivial, \(A_2\) is the reflection-sign representation, \(B_1\) assigns a negative sign to quarter-turns but positive sign to axial reflections, and \(E\) is the standard two-dimensional plane representation. The complete character on the five classes ordered as identity, quarter-turns, half-turn, axial reflections, and diagonal reflections is
\[
\begin{array}{c|rrrrr}
&1&r,r^3&r^2&\text{axis}&\text{diagonal}\\\hline
\chi_4&6&2&2&0&-2\\
\chi_5&2&0&-2&0&0
\end{array}.
\]
This determines one rational invariant class in degree four and none in degree five.

More precisely, the integral lattice \(\widetilde H_5(\mathcal M(G);\mathbb Z)\cong\mathbb Z^2\) admits a verified basis in which a clockwise quarter-turn \(r:(i,j)\mapsto(j,3-i)\) and a reflection \(h:(i,j)\mapsto(i,3-j)\) act as
\[
[r]_5=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
[h]_5=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
The nonequivariant integral homotopy equivalence \(\mathcal M(G)\simeq\bigvee^6S^4\vee\bigvee^2S^5\) was established previously and is **not** a new claim here. The new claim is the complete dihedral action on both homology groups, including its integral degree-five form.

## Assumptions and scope
The grid has vertices \((i,j)\) for \(0\le i,j<4\), edges exactly between nearest-neighbor vertices, and a matching is a set of edges with pairwise disjoint endpoints. The matching complex has one simplicial vertex for each of the twenty-four graph edges. Graph-edge order is fixed by visiting grid vertices row-major and recording the downward edge, then the rightward edge, when present. The action permutes these twenty-four edges, with induced orientation signs on simplices in increasing edge-label order. We use \(r\) and \(h\) as defined above; the five irreducible characters of \(D_4\) are normalized by \(A_1=(1,1,1,1,1)\), \(A_2=(1,1,1,-1,-1)\), \(B_1=(1,-1,1,1,-1)\), \(B_2=(1,-1,1,-1,1)\), and \(E=(2,0,-2,0,0)\) in the displayed class order. All chains, cycles, cochains and pairings are over the integers unless specified otherwise.

## Proof
**Complete chain model and independent count.** For every subset of the twenty-four numbered graph edges, retain it if no endpoints are shared. The exact face vector by dimensions \(-1,0,\ldots,7\) is
\[
(1,24,224,1044,2593,3388,2150,552,36),
\]
so there are \(10{,}012\) faces including the empty face. This is verified twice: by exhaustive edge-subset enumeration in increasing edge-label order, and by a vertex-deletion matching-polynomial recurrence. The latter recurrence partitions matchings according to whether a selected grid vertex is unused or is paired with one of its neighbors.

**Integral Morse basis, not just Betti numbers.** On the augmented face poset, toggle the edges in the fixed order
```
1,23,9,0,6,20,18,21,5,19,3,12,7,22,14,11,10,2,16,8,4,17,15,13
```
Pair a currently unpaired face without the toggle edge with its one-edge extension when both remain unpaired. There are exactly \(5{,}002\) augmented pairs, leaving six critical four-simplices and two critical five-simplices. After dropping the empty-face pair, there is in addition one critical vertex. Orient all Hasse incidences downward except matched incidences, which are reversed. An exhaustive topological sort processes all \(10{,}012\) face-poset vertices and all \(47{,}968\) incidences, proving acyclicity. The signed integral Morse differential between the critical five- and four-cells is identically zero.

For each critical cell in degrees four and five, form its integral dual cocycle by elimination along matching pairs, dividing only by the incidence \(+1\) or \(-1\) of each pivot. The supplied checker verifies that all six degree-four and both degree-five cochains annihilate every relevant simplicial boundary. Conversely, starting from each critical cell, cancel all lower-dimensional boundary coefficients in a directed topological elimination order, again with unit pivots. This produces six explicit integer degree-four cycles and two degree-five cycles, whose numbers of nonzero coefficients are respectively \((32,32,48,56,48,50)\) and \((144,170)\). The eight-by-eight cycle–cocycle pairing, separately by degree, is the identity. Consequently these cycles are primitive integral bases of the reduced homology groups and permit exact integral action matrices rather than approximate or mod-two traces.

**Symmetry matrices and character.** For each of the eight square symmetries, map every oriented simplex to the simplex on the permuted graph edges, multiplied by the sign of the induced edge-label permutation. Apply this chain map to each of the eight integral basis cycles and evaluate the integer dual cocycles. The resulting integer matrices satisfy \(r^4=h^2=1\) and \(hrh=r^{-1}\). In degree five they yield precisely the two displayed matrices; in degree four their traces, by element, are
\[
\chi_4(1)=6,\quad\chi_4(r)=\chi_4(r^3)=\chi_4(r^2)=2,\quad
\chi_4(h)=\chi_4(r^2h)=0,\quad\chi_4(rh)=\chi_4(r^3h)=-2.
\]
The degree-five traces are \(2,0,-2,0,0\) by conjugacy class. As an independent second computation, sum the signed fixed-face traces \(\sum_{\sigma\ne\emptyset}(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma)-1\) over all simplices fixed setwise by each symmetry. For all eight elements the result equals \(\chi_4(g)-\chi_5(g)\). This checks the group action against the entire original chain complex independently of the chosen homology cycles.

Finally, taking inner products with the five explicitly normalized dihedral irreducible characters gives the multiplicity vectors \((1,2,1,0,1)\) in degree four and \((0,0,0,0,1)\) in degree five. The trivial multiplicities give the stated invariant-subspace dimensions. These identities prove the claim.

## Verification
Run `python3 verify.py` with standard-library Python. It reconstructs the complete original simplicial complex and independent matching polynomial; checks all oriented Hasse incidences and acyclicity; reconstructs integer cocycles and cycles by signed unit-pivot elimination; checks every cocycle condition and the unimodular pairings; computes all eight integral symmetry matrices and the dihedral relations; and separately recomputes the reduced Lefschetz character by signed setwise fixed simplices. The output terminates in `ALL_VERIFY_OK`. The proof is finite and exhaustive for this one grid; it does not infer an all-grid statement from checked examples.

## Relationship to prior work
The published exact nonequivariant result *The matching complex of the four-by-four Cartesian square grid is a mixed-dimensional sphere wedge* already proves \(\mathcal M(G)\simeq\bigvee^6S^4\vee\bigvee^2S^5\). Its complete result text gives the Morse homotopy computation but neither an induced \(D_4\)-representation nor a character calculation; only the symmetry refinement is asserted here. Chauhan, Sharma and Shukla study three-row Cartesian grids, not the square four-by-four symmetry action. Bayer, Jelić Milutinović and Vega prove the wedge property for outerplanar graphs; the four-by-four square grid is not outerplanar and its representation is outside that theorem. Published dihedral character work on square-grid cut complexes concerns a different simplicial construction. Relevant indexed searches found no theorem covering both stated \(D_4\)-modules, but this does not prove global uniqueness.

## Limitations
The result concerns this one sixteen-vertex grid, its natural dihedral action, and ordinary matching-complex reduced homology. The rational direct-sum decompositions are not asserted as integral splittings of the degree-four lattice. No equivariant homotopy equivalence, stable-width recurrence, or theorem for arbitrary grids is claimed. A complete full-text comparison with the 2026 three-row-grid preprint was unavailable; its checked abstract explicitly confines its main results to three-row grids. Independent mathematical validation has not been performed.

## References
1. *The matching complex of the \(4\times4\) Cartesian square grid is a mixed-dimensional sphere wedge*, public research finding (2026-10-11), full result: https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-matching-complex-of-the-4-times4-cartesian-square-grid-is-a--f1b5ea641880/RESULT.md.
2. P. Chauhan, A. Sharma, and S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1 (first public 2026-09-23).
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1 (first public 2024-11-07), Theorem 2 and Conjecture 11.
