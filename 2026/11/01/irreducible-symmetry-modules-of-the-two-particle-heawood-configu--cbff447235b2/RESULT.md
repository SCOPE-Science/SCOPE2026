# Irreducible symmetry modules of the two-particle Heawood configuration space

## Finding
Let \(H\) be the Heawood graph (the fourteen-vertex point–line incidence graph of the Fano plane), and let \(B_2(H)=\operatorname{UConf}_2(|H|)\) be the space of **unordered pairs of distinct points on its geometric realization**. Its full graph automorphism group is \(G=\operatorname{Aut}(H)\cong\operatorname{PGL}_2(7)\), of order \(336\). Write \(V_8=H_1(H;\mathbb Q)\), with its natural \(G\)-action.

The complete reduced rational homology of \(B_2(H)\), including its full symmetry representation, is
\[
H_1(B_2(H);\mathbb Q)\cong V_8,\qquad
H_2(B_2(H);\mathbb Q)\cong V_8\oplus V_6,
\]
where \(V_8\) and \(V_6\) are **distinct absolutely irreducible rational** \(G\)-representations of dimensions \(8\) and \(6\), respectively. All higher rational homology is zero, and the space is connected. The complete characters, organized by whether an automorphism preserves or exchanges Fano points and lines and by its order, are:

| Bipartition action | Element order | Number | \(\chi_{H_1}=\chi_{V_8}\) | \(\chi_{H_2}\) | \(\chi_{V_6}\) |
|---|---:|---:|---:|---:|---:|
| Preserves | 1 | 1 | 8 | 14 | 6 |
| Preserves | 2 | 21 | 0 | −2 | −2 |
| Preserves | 3 | 56 | −1 | −1 | 0 |
| Preserves | 4 | 42 | 0 | 2 | 2 |
| Preserves | 7 | 48 | 1 | 0 | −1 |
| Exchanges | 2 | 28 | −2 | −2 | 0 |
| Exchanges | 6 | 56 | 1 | 1 | 0 |
| Exchanges | 8 | 84 | 0 | 0 | 0 |

These eight rows cover every one of the \(336\) automorphisms. Both positive-degree representations have **zero globally invariant subspace**. Consequently
\[
\widetilde H_i(|B_2(H)|/G;\mathbb Q)=0\qquad(i\ge0).
\]
The new claim is the complete **unordered-configuration equivariant character and its two-irreducible decomposition**. Previously computed mod-two homology for the **ordered** configuration space, and general graph-configuration results, are acknowledged as prior work and not claimed as novel.

## Assumptions and scope
A Fano point is a nonzero vector of \(\mathbb F_2^3\); a line is a triple \(\{a,b,a+b\}\). The Heawood graph has seven point vertices, seven line vertices and 21 incidence edges, and girth six. Its order-168 color-preserving automorphisms are \(\operatorname{GL}_3(\mathbb F_2)\), and any polarity adds the other 168 automorphisms. The unordered configuration space consists of **two unlabeled, mutually distinct particles** on the geometric graph; it is not the ordinary matching, neighborhood or independence complex.

For this sufficiently subdivided graph, the classical discrete two-particle cubical model has a cell for each unordered set of two vertices or open edges whose closures are disjoint. The sufficient-subdivision conditions hold because every vertex is essential, the distance between distinct essential vertices is at least one edge, and the girth exceeds three. The canonical deformation from the continuous to this discrete model respects graph automorphisms. We use rational coefficients except when explicitly describing finite-field rank computations; no integral torsion classification is asserted.

## Proof
**1. Finite cubical chain complex.** Label the fourteen graph vertices and orient each of its 21 edges. The unordered two-particle cubical complex has \(91=\binom{14}{2}\) zero-cells (two distinct stationary vertices), \(252=21(14-2)\) one-cells (an oriented edge and a stationary vertex outside its endpoints), and \(168\) two-cells (unordered pairs of vertex-disjoint graph edges). The two-cell boundary for disjoint oriented edges \((a,b)\) and \((c,d)\), with those edges in the specified order, is
\[
\partial[(a,b)\times(c,d)]
=[(b,(c,d))]-[(a,(c,d))]-[((a,b),d)]+[((a,b),c)].
\]
All its terms are valid one-cells. Direct inspection shows \(\partial_1\partial_2=0\). Exact finite-field elimination gives \(\operatorname{rank}_{\mathbb F_3}\partial_1=90\) and \(\operatorname{rank}_{\mathbb F_3}\partial_2=154\); the first is also the rational rank because the one-skeleton is connected and has 91 vertices. For an integral matrix, the rank over \(\mathbb Q\) is at least the rank modulo 3. Therefore
\[
\dim_{\mathbb Q}H_1(B_2(H))=252-90-\operatorname{rank}_{\mathbb Q}\partial_2\le8.
\]

**2. The first-homology map is an isomorphism.** The sum of the two moving particles defines a graph-automorphism-natural homology map \(\phi:H_1(B_2(H);\mathbb Q)\to H_1(H;\mathbb Q)\): on each cubical one-cell (edge, stationary vertex), it sends the cell to its oriented graph edge. This is a chain map together with the map sending a pair of stationary vertices to their sum in graph zero-chains. The Heawood graph has exactly 28 simple six-cycles. Their 21-coordinate oriented edge vectors span its eight-dimensional graph cycle space: the verifier checks their exact mod-three span has rank eight, which forces rational rank eight. Every six-cycle avoids at least one graph vertex. Moving one particle around that cycle while fixing the other at a vertex outside it gives a loop in the unordered configuration space mapped by \(\phi\) to the original graph cycle. Hence \(\phi\) is surjective and \(\dim H_1(B_2(H);\mathbb Q)\ge8\). Combining with the previous upper bound yields an equivariant isomorphism \(H_1(B_2(H);\mathbb Q)\cong H_1(H;\mathbb Q)\), and \(\operatorname{rank}_{\mathbb Q}\partial_2=154\).

The Euler characteristic is \(91-252+168=7\). Since the complex has dimension two, is connected, and its rational first Betti number is eight, its second rational Betti number is \(7-1+8=14\). This proves rational homology concentration without extrapolating from mod-three computations. It does not say that rational and mod-two homology coincide.

**3. Exact equivariant Lefschetz characters.** The group \(G\) acts on every cubical chain group as a signed permutation representation. For a given graph automorphism \(g\), an edge reversal contributes a sign \(-1\), and interchanging the two distinct edge factors of a square also contributes \(-1\). The verifier lists all \(336\) automorphisms (168 collineations plus their compositions with a polarity), calculates signed fixed-cell traces \(t_0(g),t_1(g),t_2(g)\), and calculates the graph-cycle trace \(a(g)\) from its vertex and oriented-edge fixed traces:
\[
a(g)=\operatorname{tr}(g\mid C_1(H))
-\operatorname{tr}(g\mid C_0(H))+1.
\]
Because the map in Step 2 is a \(G\)-equivariant first-homology isomorphism, \(\chi_{H_1}(g)=a(g)\). Lefschetz then gives
\[
\chi_{H_2}(g)=t_0(g)-t_1(g)+t_2(g)-1+a(g).
\]
Evaluating these formulas for every group element gives precisely the eight-row table. An **independent** kernel-basis calculation reduces the complete two-cell boundary matrix modulo 101, obtains a 14-vector basis of its kernel, acts by all 336 signed square permutations, and compares its direct top-kernel trace with the Lefschetz formula for every group element. The two implementations agree in all 336 cases. Since characteristic 101 has the same verified boundary rank and does not divide 336, the finite-field comparison is a strong independent check of the rational character, not a substitute for the preceding rational proof.

**4. Irreducible constituents and quotient.** Exact character sums over all 336 automorphisms give
\[
\langle\chi_{H_1},\chi_{H_1}\rangle_G=1,
\quad\langle\chi_{H_2},\chi_{H_1}\rangle_G=1,
\quad\langle\chi_{H_2},\chi_{H_2}\rangle_G=2.
\]
Set \(\chi_6=\chi_{H_2}-\chi_{H_1}\). The displayed equalities imply \(\langle\chi_6,\chi_6\rangle_G=1\) and \(\langle\chi_6,\chi_{H_1}\rangle_G=0\). Since the first-homology constituent occurs with multiplicity one in the **actual** second-homology representation, the complementary \(\chi_6\) is an actual six-dimensional representation character. Each norm-one complex character is irreducible, giving the asserted absolutely irreducible rational splitting. Both characters have group average zero, as the complete table shows. For any finite simplicial/cubical group action, rational homology of the geometric quotient is the invariant rational homology (after equivariant subdivision). The space is connected, so the quotient is rationally acyclic.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The script derives the Fano incidence graph, all \(91+252+168\) cells and both boundaries; checks \(\partial_1\partial_2=0\); computes boundary ranks modulo 2, 3, 5 and 101; enumerates all 28 six-cycles and verifies they span \(H_1(H)\); enumerates all 336 automorphisms, computes signed fixed-cell characters, and independently checks the entire top-kernel character on a 14-vector mod-101 basis. It also verifies every complete character multiplicity and invariant statement. `verify_output.txt` contains the exact recorded output. The integral graph geometry, transfer to continuous configurations and rational rank inequalities are proved above; no numerical log alone is treated as an infinite proof.

## Relationship to prior work
Barnett and Farber, *Topology of Configuration Space of Two Particles on a Graph, I* (2009), give the ordered deleted-product model, an equivariant deformation and general graph-configuration methods. Farber and Hanbury, *Part II* (2010), analyze mature nonplanar graphs and their ordered homology, including the graph-cycle map. Neither inspected theorem states a full \(336\)-element homology character for the **unordered** Heawood configuration space or this decomposition.

The closest same-graph research record, *Mod-two homology of the ordered two-point Heawood configuration space* (2026, published-finding corpus identifier `cbd791988700`), calculates \((1,16,29)\) over \(\mathbb F_2\) for the **ordered** model; this is a different double-cover space and uses a different coefficient field. It does not provide the unordered rational characters. The earlier two-particle Petersen and dodecahedral representation calculations concern different graphs; the general *Exchange-sign Borel–Moore homology of two-point graph configurations* concerns compact-support/Borel–Moore homology with a nontrivial local system, not the ordinary singular homology here. These distinctions were checked at the claim level, not just by titles.

## Limitations
The theorem treats the two-unordered-particle space of a single canonical graph and its rational group representations. The mod-two boundary ranks differ from the characteristic-three ranks; consequently **no integral homology torsion classification** is inferred. The result does not assert an integral representation-lattice decomposition, quotient homotopy type, or analogous formula for arbitrary cubic graphs. Earlier general deleted-product and graph-braid results may imply some nonequivariant ranks; those are not claimed as new. A relevant unindexed equivariant calculation under deleted-product terminology remains a publication-priority risk; external validation is not asserted.

## References
1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1, first submitted 2009-03-12; *Algebraic & Geometric Topology* 9 (2009), 593–624.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300v1, first submitted 2010-05-13; *Algebraic & Geometric Topology* 10 (2010), 2203–2227.
3. *Mod-two homology of the ordered two-point Heawood configuration space*, 2026, published-finding corpus record `2026/10/11/SCOPE-mod-2-homology-of-the-ordered-two-point-heawood-configuration-sp--cbd791988700`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mod-2-homology-of-the-ordered-two-point-heawood-configuration-sp--cbd791988700 .
4. *Exchange-sign Borel–Moore homology of two-point graph configurations*, 2026, published-finding corpus record `2026/10/11/SCOPE-exchange-sign-borel-moore-homology-of-two-point-graph-configurat--68e49e70a285`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exchange-sign-borel-moore-homology-of-two-point-graph-configurat--68e49e70a285 .
5. J. C. Baez, *Heawood Graph*, AMS Visual Insight (2015-08-01), https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/ .
