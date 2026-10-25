# Rational \(S_5\)-homology of the Petersen matching complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \([5]=\{1,2,3,4,5\}\), and two vertices are joined precisely when those subsets are disjoint. Let \(X=\operatorname{Match}(P)\) be its **ordinary matching complex**, with one simplicial vertex per graph edge and one face per pairwise vertex-disjoint set of graph edges. The five-label permutation group \(S_5=\operatorname{Aut}(P)\) acts on \(X\).

**Theorem.** As rational \(S_5\)-representations, the only nonzero reduced homology groups of \(X\) are
\[
\widetilde H_2(X;\mathbb Q)\cong \operatorname{sgn}\otimes\mathbb Q^{[5]},\qquad
\widetilde H_3(X;\mathbb Q)\cong\ker\!\left(\mathbb Q^{\binom{[5]}2}\xrightarrow{I}\mathbb Q^{[5]}\right)\cong S^{(3,2)},
\]
where \(I(e_{\{i,j\}})=e_i+e_j\). The first module is a **reducible**, sign-twisted five-point permutation representation; the second is the **irreducible** five-dimensional Specht module of partition \((3,2)\).

Equivalently, if \(f(\sigma)\) is the number of fixed labels of \(\sigma\in S_5\) and \(c_2(\sigma)\) its number of transposition cycles, then for **every** \(\sigma\in S_5\),
\[
\operatorname{tr}(\sigma\mid\widetilde H_2)=\operatorname{sgn}(\sigma)f(\sigma),\qquad
\operatorname{tr}(\sigma\mid\widetilde H_3)=\binom{f(\sigma)}2+c_2(\sigma)-f(\sigma).
\]
All other reduced rational homology vanishes. The quotient \(X/S_5\) has vanishing reduced rational homology, whereas \(X/A_5\) has exactly one reduced rational homology class, in degree two. These statements concern rational homology of geometric quotients; contractibility is not asserted.

## Assumptions and scope
The graph is the **ten-vertex** Petersen graph itself, not the one-dimensional matching complex \(\operatorname{Match}(K_5)\), even though these happen to be isomorphic as graphs. Its 15 graph edges are encoded lexicographically from pairs of disjoint two-subsets of \([5]\). An oriented simplex is the increasing list of graph-edge indices. The ordinary boundary of an oriented \(k\)-simplex removes its \(j\)-th vertex with coefficient \((-1)^j\). A label permutation maps graph edges to graph edges; the sign of the induced permutation of the ordered simplex is included in its chain action. This fixes all normalization and sign conventions.

The theorem determines rational representations under the **entire** automorphism group and its two specified subgroups. It does not assert an isomorphism of integral group-ring modules, a homotopy-equivariant sphere decomposition, or results for arbitrary graphs.

## Proof
**1. Exact chain ranks.** There are precisely \((15,75,145,90,6)\) simplices in dimensions zero through four, respectively. Write \(\partial_k:C_k(X;\mathbb Z)\to C_{k-1}(X;\mathbb Z)\) for the signed simplicial boundary. An exhaustive exact reconstruction yields ranks over \(\mathbb F_2\)
\[
(\operatorname{rank}\partial_1,\operatorname{rank}\partial_2,\operatorname{rank}\partial_3,\operatorname{rank}\partial_4)=(14,61,79,6).
\]
The verifier checks \(\partial_{k-1}\partial_k=0\) as **integer matrices**, not merely modulo two. Since rank over \(\mathbb Q\) is at least rank modulo two, \(\operatorname{rank}_{\mathbb Q}\partial_1\ge14\), but it is at most 14 because all edges have augmented sum zero. Hence the first rank is exactly 14 over \(\mathbb Q\). The relation \(\partial_1\partial_2=0\) bounds the next rank by \(75-14=61\), so it is exactly 61. The supplied certificate gives eleven linearly independent integer vectors in \(\ker\partial_3\), with an explicitly verified unimodular coordinate minor, bounding the third rank above by \(90-11=79\); the modulo-two lower bound makes it exactly 79. Finally the six columns of \(\partial_4\) are independent modulo two, so the rational fourth rank is six. Therefore the reduced rational Betti vector is \((0,0,5,5,0)\).

**2. The degree-three representation.** Let \(K=\ker(\partial_3\otimes\mathbb Q)\), of dimension eleven. The file `kernel_certificate.json` contains an integer basis \(z_1,\ldots,z_{11}\) of \(K\). The verifier reconstructs all 90 coordinates of these vectors, checks every integer boundary is zero, and checks that their eleven specified coordinate rows form a matrix with the supplied two-sided **integer inverse**. Thus the certificate is a rigorous finite proof of the kernel dimension and coordinates, not a floating-point rank estimate. The first six basis vectors span \(\operatorname{im}\partial_4\): this follows because each of the six boundary columns has zero coordinates along the last five basis vectors and both spaces have dimension six.

For each of the 120 label permutations, the verifier acts on every oriented three-simplex with the induced orientation sign, expresses each of the eleven transformed basis vectors in the certified basis, and checks **every** coefficient of the reconstruction. This gives \(\operatorname{tr}(\sigma\mid K)\) exactly. As \(\partial_4\) is injective and equivariant,
\[
\operatorname{tr}(\sigma\mid\widetilde H_3)=\operatorname{tr}(\sigma\mid K)-\operatorname{tr}(\sigma\mid C_4).
\]
The resulting values, ordered by the cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), are \((5,1,1,-1,1,-1,0)\).

**3. The degree-two representation.** The other character is forced by the Hopf trace identity, using the same signed simplicial action:
\[
\operatorname{tr}(\sigma\mid\widetilde H_2)=-1+\sum_{k=0}^4(-1)^k\operatorname{tr}(\sigma\mid C_k)+\operatorname{tr}(\sigma\mid\widetilde H_3).
\]
Its seven cycle-type values are \((5,-3,1,2,0,-1,0)\). The verifier checks these identities for all 120 permutations, not only for conjugacy-class representatives.

**4. Identification and quotients.** The character of the signed five-point permutation module is \(\operatorname{sgn}(\sigma)f(\sigma)\), exactly the computed degree-two character. The permutation module on unordered pairs has character \(\binom{f(\sigma)}2+c_2(\sigma)\). The incidence map \(I\) in the theorem is surjective over \(\mathbb Q\): a vector orthogonal to its rows would satisfy \(a_i+a_j=0\) for every pair, hence is zero using any triple of distinct indices. Its kernel therefore has the computed degree-three character; standard Young's rule identifies it with \(S^{(3,2)}\). Equality of rational characters determines representations of a finite group in characteristic zero. Averaging the two characters over all of \(S_5\) yields zero invariant dimensions, whereas averaging over \(A_5\) yields respectively one and zero. Rational homology of a quotient by a finite group agrees with the invariant rational homology, for instance by passing to barycentric subdivision and averaging chains. The quotient assertions follow.

## Verification
Run `python3 verify.py` next to `kernel_certificate.json`, using Python 3.9 or later and no third-party packages. The verifier reconstructs the graph, all faces, and all four signed boundary matrices. It verifies exact integer boundary compositions, modulo-two ranks \((14,61,79,6)\), the eleven integer cycles, a two-sided unimodular inverse, the six-dimensional fourth-boundary image, and **all 120** induced group actions and character identities. Successful execution prints `FULL_S5_HOMOLOGY_REPRESENTATIONS_VERIFIED`. The supplied certificate is fully decoded and checked by the program; its coefficients are not trusted without verification.

## Relationship to prior work
Mondal, Mukherjee and Saha study \(\operatorname{Match}(K_n)\), which for \(n=5\) is the Petersen **graph**, rather than its ordinary matching complex [1]. Bate, Everitt, Ford and Ramos study the representation theory of matching complexes of **complete hypergraphs**, and broad asymptotic fibre-closed families; their full paper motivates representation-sensitive questions but does not supply this two-degree \(S_5\) representation for the matching complex of the Petersen graph [2]. Two published computational accounts determine \(\operatorname{Match}(P)\simeq\bigvee^5S^2\vee\bigvee^5S^3\) by integral Morse reductions [3,4]. That nonequivariant homotopy equivalence and its Betti numbers are **not** claimed as new. Both published accounts are explicit about their nonequivariant scope and do not identify the two \(S_5\)-actions here.

The same complex may also be called \(\operatorname{Ind}(L(P))\), the independence complex of the Petersen line graph. Searches using both names and the representation-theoretic and character formulations did not identify a stronger theorem implying these two exact modules. Search absence alone is not a proof of publication priority.

## Limitations
This is one finite canonical graph, not an infinite-family classification. The new assertion is the rational equivariant homology; no integral lattice-module structure is deduced from rational characters. The certificate gives exact finite algebra and exhaustive group actions, but not a computer-independent handwritten elimination of all matrix entries. The homotopy type quoted from earlier work is not independently re-established here as an equivariant homotopy statement. An equivalent unindexed or differently named representation calculation may exist; no unconditional novelty or independent validation is claimed.

## References
[1] A. Mondal, S. Mukherjee and K. Saha, *Discrete Morse theory and the topology of matching complexes of complete graphs*, arXiv:2303.07054, first posted 2023-03-13, https://arxiv.org/abs/2303.07054.

[2] M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750, first posted 2023-12-21, https://arxiv.org/abs/2312.13750.

[3] *The Petersen matching complex is a wedge of five two-spheres and five three-spheres*, published research record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-a-wedge-of-five-two-spheres-and--80050a324367.

[4] *The Petersen matching complex is a mixed-dimensional sphere wedge*, published research record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-bigvee-5-s-2-vee-bigvee-5-s-3--439d72b660a6.
