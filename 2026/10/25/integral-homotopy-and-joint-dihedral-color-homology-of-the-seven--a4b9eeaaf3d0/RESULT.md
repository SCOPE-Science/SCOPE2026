# Integral homotopy and joint dihedral–color homology of the seven-cycle categorical product

## Finding

Let \(G=C_7\times K_3\) denote the **categorical** product of graphs and \(X=\operatorname{Ind}(G)\) its ordinary independence complex. There is an integral homotopy equivalence
\[
X\simeq S^3\vee S^4\vee S^4\vee S^4.
\]
Thus \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^3\), and every other reduced integral homology group vanishes. In particular no integral torsion occurs in this twenty-one-vertex example.

The commuting cycle rotations/reflections and color permutations give an action of \(D_7\times S_3\). Its complete reduced *rational* homology representation is
\[
\widetilde H_3(X;\mathbb Q)\cong\varepsilon_{D_7}\boxtimes\operatorname{sgn}_{S_3},\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbf1_{D_7}\boxtimes(\operatorname{sgn}_{S_3}\oplus V_{\mathrm{std}}).
\]
Here \(\varepsilon_{D_7}\) is trivial on rotations and equals \(-1\) on reflections, and \(V_{\mathrm{std}}\) is the two-dimensional standard representation of \(S_3\). The full group quotient has zero reduced rational homology in positive degrees; this does **not** assert that the quotient is contractible.

## Assumptions and scope

The graph's twenty-one vertices are \((i,c)\) with \(i\in\mathbb Z/7\mathbb Z\) and \(c\in\{0,1,2\}\). Two distinct vertices are adjacent if and only if their cycle coordinates differ by \(\pm1\) modulo seven and their colors differ. A simplex of \(X\) is precisely a set of pairwise nonadjacent vertices. Rotation \(r(i,c)=(i+1,c)\), reflection \(s(i,c)=(-i,c)\), and color relabeling \(\pi(i,c)=(i,\pi(c))\) give the stated action. No analogous conclusion for other cycle lengths or color numbers is claimed.

## Proof

**Exact finite homotopy certificate.** Index vertices by \(3i+c\); use bitmasks to encode faces. The standalone `c7k3_equivariant_checker.py` recursively enumerates *every* independent set without truncation, using the first available vertex as a decision pivot. The list including the empty face has 5,282 members, with nonempty face numbers by size \(1,\ldots,9\) equal to \((21,168,658,1365,1554,1022,402,84,7)\). The independently re-generable fixed vertex order in the program constructs 2,639 disjoint face pairs on the augmented face poset; four critical faces remain: one in dimension three (bitmask 132225) and three in dimension four (bitmasks 166145, 590402, 592130). The empty face is paired with a vertex. Deleting that augmented pair leaves a standard discrete-Morse matching with one critical zero-cell and the same four positive-dimensional cells.

For every face-cover incidence, reverse its orientation exactly when it belongs to a matched pair. The program builds and topologically sorts **all 25,242** directed cover incidences on **all 5,282** faces. This establishes global acyclicity, rather than relying on a merely local test. Discrete Morse theory gives a CW complex with one zero-cell, one three-cell and three four-cells, and no other cells. Its three-skeleton is \(S^3\).

Orient each simplex by increasing vertex index. For the critical three-cell \(c\), define an integral projection \(P_3\) on every oriented three-simplex: \(P_3(c)=1\); \(P_3\) is zero on upper-matched three-simplices; and, whenever a three-simplex \(\sigma\) is paired as the lower face of \(\tau\), put
\[
P_3(\sigma)=-[\tau:\sigma]^{-1}\!\sum_{\substack{\rho\subset\tau,\;\dim\rho=3\\\rho\ne\sigma}}[\tau:\rho]P_3(\rho).
\]
All incidence coefficients are \(\pm1\), and the acyclic matching makes this recurrence finite. Apply this projection to the oriented boundaries of all three critical four-simplices. The exact computed integral Morse differential is \((0,0,0)\). Since \(\pi_3(S^3)\cong\mathbb Z\) and the degree of each four-cell attaching map is precisely its cellular boundary coefficient, all three attachments are null-homotopic. This proves the asserted integral wedge homotopy type and rules out torsion.

**The joint representation.** The same executable constructs an integral three-cycle representing a primitive generator: it cancels the complete signed boundary by gradient-path elimination and checks \(P_3(z)=1\). One explicit geometric description is the join of four two-point sets \(\{(0,0),(6,2)\}\), \(\{(1,0),(2,1)\}\), \(\{(3,1),(4,2)\}\), \(\{(5,2),(6,0)\}\); every cross-pair is a nonedge, so their join is an embedded \(S^3\) with sixteen signed tetrahedra. The verifier also checks the primitive degree of the constructed cycle directly. Applying every one of the 84 dihedral–color transformations to its signed chain and evaluating \(P_3\) gives
\[
\operatorname{tr}(g\mid\widetilde H_3)=(-1)^{b}\operatorname{sgn}(\pi),
\]
where \(b=0\) for a rotation and \(b=1\) for a reflection. This gives the first representation.

For completeness, signed simplex enumeration computes the reduced Lefschetz number \(\sum_k(-1)^k\operatorname{tr}(g\mid\widetilde H_k)\) exactly: each setwise fixed face contributes the sign of the induced permutation of its ordered vertices. Since only homology dimensions three and four occur, the fourth-homology trace is the reduced Lefschetz number *plus* the third-homology trace. For every \(g=(r^a s^b,\pi)\), the result is
\[
\operatorname{tr}(g\mid\widetilde H_4)=\operatorname{sgn}(\pi)+\#\operatorname{Fix}(\pi)-1.
\]
This is the character of \(\mathbf1_{D_7}\boxtimes(\operatorname{sgn}_{S_3}\oplus V_{\mathrm{std}})\), establishing the second representation. Averaging characters over the full finite group yields zero positive-degree rational homology for the geometric quotient, by rational transfer.

## Verification

Run `python3 c7k3_equivariant_checker.py` (standard-library Python 3 only). It regenerates all faces, checks every matching pair, tests the complete directed Hasse diagram for acyclicity, computes the exact signed integral Morse boundary, constructs and checks a primitive three-cycle, and checks all 84 group elements by independently recomputing signed simplicial Lefschetz traces and action on the three-cycle. Successful completion prints `C7_K3_EQUIVARIANT_HOMOTOPY_VERIFIED`. These are exhaustive exact finite calculations for the specified graph, with explicit rationale connecting combinatorial certificates to homotopy and representation claims.

## Relationship to prior work

Antolín Camarena and Carnero Bravo prove that for cycle lengths congruent to one modulo three in this range, only two consecutive dimensions may carry reduced homology and possible Moore summands remain; their Theorem 23 is a constraint, *not* the homotopy type or the representation above. Their paper explicitly mentions computational evidence of free homology for the same graph and asks a general torsion-freeness question (Question 24). That evidence is credited, and no previously observed free-homology nonvanishing is claimed as new. A separate recorded calculation for \(C_7\times K_4\) proves a three- and four-sphere wedge with different ranks for **four colors**, without implying the present three-color integral differential or the joint dihedral–color characters. Published results for multiples of three cycle length, or for four- and five-cycles, do not cover this parameter.

## Limitations

This is a complete but **finite** result only for \(C_7\times K_3\), not a solution of the all-parameter torsion-freeness question. The full integral group-ring module structure and quotient integral torsion are not determined. The rational representation follows from exact character computations, not a canonical splitting over integers. The source comparison cannot rule out unindexed equivalent work. No external independent audit has been performed.

## References

- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public 2023-07-23), Theorem 23, Question 24. https://arxiv.org/abs/2307.12401 ; published in *Homology, Homotopy and Applications* 26 (2024), DOI 10.4310/HHA.2024.v26.n2.a17.
- *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors* (2026), public comparison record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-torsion-free-mixed-dimensional-sphere-wedge-for-the-seven-cycl--50b8be4e4c8f
