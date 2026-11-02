# Full symmetric-group homology of the Petersen ordinary matching complex

## Finding
Let \(P\) be the Petersen graph, realized as the Kneser graph \(\operatorname{KG}(5,2)\), and let \(X=\mathcal M(P)\) be its **ordinary matching complex**. The automorphism group \(S_5\) acts by permuting the underlying five symbols. The complete reduced rational homology representations are
\[
\widetilde H_2(X;\mathbb Q)\cong\operatorname{sgn}\otimes\mathbb Q[\{1,2,3,4,5\}],
\qquad
\widetilde H_3(X;\mathbb Q)\cong S^{(3,2)},
\]
where the first factor is the sign-twisted five-point permutation module and \(S^{(3,2)}\) is the five-dimensional irreducible rational Specht representation. All other reduced rational homology groups vanish.

The two symmetry quotients have sharply different rational homology:
\[
\widetilde H_j(X/S_5;\mathbb Q)=0\ \text{for all }j,
\qquad
\widetilde H_j(X/A_5;\mathbb Q)\cong
\begin{cases}\mathbb Q,&j=2,\\0,&j\ne2.\end{cases}
\]
These are new **equivariant** assertions, not new claims about the already published ordinary homotopy type.

## Assumptions and scope
The ten graph vertices are the two-element subsets of \(\{1,\ldots,5\}\); two vertices are joined exactly when the two subsets are disjoint. The graph has fifteen edges, sorted lexicographically by their endpoint indices. A simplex of \(X\) is any set of pairwise vertex-disjoint graph edges. The action of \(S_5\) on these edges induces signed simplicial chain maps. Each simplex is oriented by increasing edge index, and a permutation of simplex vertices contributes its ordinary orientation sign.

All coefficients and representations in the theorem are **rational**. The earlier nonequivariant integral homotopy result \(X\simeq \bigvee^5 S^2\vee\bigvee^5 S^3\) is used only for context; the new representation calculation can be checked directly without invoking it. In particular no integral-module splitting, equivariant homotopy equivalence, or family-wide result is asserted.

## Proof
**Finite chain complex.** Directly list all matchings: for each \(0\le d\le4\), take the \((d+1)\)-subsets of fifteen edges and retain exactly those with mutually disjoint endpoints. This exhaustively gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(15,75,145,90,6).
\]
Let \(C_d\) be the resulting rational simplicial chain groups, with the usual signed deletion boundary. The canonical \(S_5\)-action commutes with these boundaries.

**Exact fixed-chain computation.** For any representative \(g\in S_5\), enumerate the orbits of \(\langle g\rangle\) on the oriented \(d\)-simplices. If following an orbit once around reverses its orientation, its invariant subspace is zero. Otherwise sum the orbit's oriented simplices with their induced signs: this is one invariant-chain basis vector. Project the ordinary signed boundary to the basis of invariant chains using the coefficient at each orbit representative. Ordinary rational Gaussian elimination determines the ranks of these **complete** invariant boundary matrices. In characteristic zero, averaging over a finite group is exact, hence
\[
H_d\big(C_\bullet^{\langle g\rangle}\big)
\cong H_d(C_\bullet)^{\langle g\rangle}.
\]
The following is the complete exact certificate. Entries in the third column are the ranks of boundaries from degree one through four, and the final pair lists invariant dimensions in degrees two and three. A partition denotes the cycle lengths of \(g\).

| Cycle type | Invariant chain dimensions, degrees 0–4 | Boundary ranks, degrees 1–4 | \((\dim H_2^{\langle g\rangle},\dim H_3^{\langle g\rangle})\) |
| --- | --- | --- | --- |
| \((1,1,1,1,1)\) | \((15,75,145,90,6)\) | \((14,61,79,6)\) | \((5,5)\) |
| \((2,1,1,1)\) | \((9,36,68,45,3)\) | \((8,28,39,3)\) | \((1,3)\) |
| \((2,2,1)\) | \((9,37,69,44,4)\) | \((8,29,37,4)\) | \((3,3)\) |
| \((3,1,1)\) | \((5,25,51,30,2)\) | \((4,21,27,2)\) | \((3,1)\) |
| \((3,2)\) | \((3,12,24,15,1)\) | \((2,10,13,1)\) | \((1,1)\) |
| \((4,1)\) | \((5,18,34,21,1)\) | \((4,14,19,1)\) | \((1,1)\) |
| \((5)\) | \((3,15,29,18,2)\) | \((2,13,15,2)\) | \((1,1)\) |

All degree-zero invariant homology groups have dimension one, and degrees one and four have dimension zero, for all seven classes. In particular the identity row gives exactly five homology dimensions in each of degrees two and three.

**Recovering the character, not guessing it.** For a cyclic generator \(g\) of order \(m\), the invariant dimension \(b_d(g)\) satisfies
\[
m b_d(g)=\sum_{j=0}^{m-1}\chi_d(g^j).
\]
Character values of primitive powers of \(g\) agree because those powers are conjugate in \(S_5\). Induction on element order therefore recovers \(\chi_d(g)\) from the invariant table and the already recovered lower-order character values. For the seven classes in the table order, the resulting characters are
\[
\chi_2=(5,-3,1,2,0,-1,0),\qquad
\chi_3=(5,1,1,-1,1,-1,0).
\]
If \(f(g)\) is the number of fixed symbols and \(\operatorname{sgn}(g)\) its sign, then \(\chi_2(g)=\operatorname{sgn}(g)f(g)\), the character of the sign-twisted five-point permutation module. On the other hand, for the standard four-dimensional representation \(V\),
\[
\chi_{\operatorname{Sym}^2 V}(g)
=\tfrac12\big((f(g)-1)^2+f(g^2)-1\big).
\]
Subtracting the characters of \(\mathbf1\) and \(V\) yields exactly \(\chi_3\); this is the character of \(S^{(3,2)}\). Rational representations of a finite group are semisimple; in particular their characters determine their rational isomorphism class for this symmetric group. This proves both asserted decompositions.

**Quotients.** Rational homology of a finite group quotient of a finite simplicial complex is the invariant part of its rational homology: after barycentric subdivision the quotient cellular chains are invariant chains. Summing the two characters over all 120 permutations gives zero invariants in either positive degree. Summing over the sixty even permutations gives one invariant in degree two and zero in degree three. The complex is connected by the identity-row calculation, proving the quotient assertions.

## Verification
Run `python3 petersen_matching_s5_verify.py` (Python standard library only). It builds all graph edges and the entire simplicial complex, constructs all seven cyclic invariant subcomplexes with signed orientation, and computes **exact rational** boundary ranks using a sparse fraction-based Gaussian elimination. It independently checks signed fixed-simplex Lefschetz numbers, reconstructs both characters from the cyclic invariant ranks by element-order induction, verifies their representation-theoretic formulas, and averages over all 120 permutations for the quotient calculation. The expected complete output is included as `petersen_matching_s5_verification.txt`; the terminating marker is `PETERSEN_MATCHING_S5_EXACT_OK`.

The finite calculation is exhaustive because every simplex and every conjugacy type is explicitly enumerated. The representation formulas and quotient inferences use the indicated mathematical character argument, not an extrapolation from sampled graph sizes. There is no claim of an independent external audit.

## Relationship to prior work
Li [1] proves equivariant strong log-concavity for the graded **unsigned permutation representations on graph matchings**. Its full text explicitly raises the relation to matching-complex homology, but does not compute the signed homology character of this graph. Bate–Everitt–Ford–Ramos [2] develop homology representations for matching complexes of **complete hypergraphs** and asymptotic properties of fibre-closed families; their full text does not analyze the Petersen ordinary matching complex or these seven character values.

Two published Petersen ordinary-matching-complex calculations [3,4] prove the stronger **nonequivariant integral homotopy type** \(\bigvee^5S^2\vee\bigvee^5S^3\). Their complete findings and proofs describe the mixed-dimensional homotopy type and exact Morse certificates, but do not assert the natural \(S_5\)-homology modules or the symmetry quotient homology. Consequently that nonequivariant result is explicitly excluded from the claim of originality: the new result concerns the equivariant action and the contrast between full and alternating symmetry quotients. Related representations of Petersen **perfect-matching** complexes, two-point graph configuration spaces, and the complete-graph matching complex describe different objects, not implications of this result.

## Limitations
Only one finite graph and rational representation theory are treated. No invariant integral lattice or equivariant homotopy classification is asserted. The computations are exact and reproducible but remain subject to independent scientific audit. Equivariant results not indexed under the queried graph or independence-complex terminology could predate this account; absence from search is not a proof of priority.

## References
[1] Shiyue Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828 (first public 2022-02-17), §1 and Remark 1.4, https://arxiv.org/html/2202.08828v2.
[2] Michael Bate, Brent Everitt, Sam Ford and Eric Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750 (first public 2023-12-21), §§1–3, https://arxiv.org/abs/2312.13750.
[3] *The Petersen matching complex is a wedge of five two-spheres and five three-spheres*, public research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-a-wedge-of-five-two-spheres-and--80050a324367.
[4] *The Petersen matching complex is \(\bigvee^{5}S^2\vee\bigvee^{5}S^3\)*, public research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-bigvee-5-s-2-vee-bigvee-5-s-3--439d72b660a6.
