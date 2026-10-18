# The full octahedral character of the cuboctahedral matching complex

## Finding
Let \(Q_3\) be the graph of the three-dimensional cube, let \(C=L(Q_3)\) be the cuboctahedral graph, and let \(K=\mathcal M(C)\) be its **ordinary matching complex** (faces are sets of pairwise vertex-disjoint edges of \(C\)). Its full automorphism group is \(G=\operatorname{Aut}(C)\cong S_4\times C_2\), of order \(48\). There is precisely one nonzero reduced integral homology group:
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{57}.
\]
We determine **the complete natural rational representation** of \(G\) on this group. Write \(V=S^{(3,1)}\) for the three-dimensional standard \(S_4\)-representation, \(V'=V\otimes\operatorname{sgn}\), and \(W=S^{(2,2)}\) for the two-dimensional irreducible. Write \(\varepsilon\) for the nontrivial central \(C_2\)-character; the precise splitting of \(G\) is specified below. Then
\[
\boxed{\begin{aligned}
\widetilde H_3(K;\mathbb Q)\cong &\ \bigl(\mathbf1\oplus2\operatorname{sgn}\oplus5V\oplus2V'\oplus5W\bigr)\boxtimes\mathbf1\\
&\oplus\bigl(\mathbf1\oplus2\operatorname{sgn}\oplus2V\oplus2V'\oplus4W\bigr)\boxtimes\varepsilon.
\end{aligned}}
\]
Consequently the central antipodal cube involution has \(34\) positive and \(23\) negative rational eigenvalues on third homology. The invariant dimension for the **full** group is exactly \(1\). The result identifies the natural homology character; it does not assert an integral decomposition into rational irreducibles.

## Assumptions and scope
Label the cube vertices by integers \(0,\ldots,7\), interpreted as three-bit words, and join two words when their XOR is one of \(1,2,4\). List the resulting twelve cube edges in increasing lexicographic order and call this list \(Q\). The vertices of \(C\) are the elements of \(Q\); an edge joins two cube edges when they share an endpoint. List these twenty-four cuboctahedral edges lexicographically as \(e_0,\ldots,e_{23}\). A matching of \(k\) such edges is an oriented \((k-1)\)-simplex with canonical increasing edge-index orientation. The empty matching belongs to the **augmented** simplicial chain complex in degree \(-1\), only for reduced-homology bookkeeping.

Every cube symmetry is uniquely \(g_{p,t}\), where \(p\in S_3\), \(t\in\{0,1\}^3\), and its action on a cube word \(x\) is \((g_{p,t}x)_i=x_{p(i)}\oplus t_i\). This induces a permutation of the twenty-four \(e_j\). Identify the \(S_4\) quotient with its action on the four **unoriented antipodal pairs of cube vertices**; identify the central \(C_2\) coordinate with the homomorphism \(g_{p,t}\mapsto(-1)^{|t|}\), with \(|t|\) Hamming weight. This is a particular direct-product splitting; \((-1)^{|t|}\) is **not** in general the Euclidean determinant, which also includes \(\operatorname{sgn}(p)\). The central inversion has \(t=(1,1,1)\) and lies in the negative sector. The \(S_4\)-factor is fixed by this convention throughout the character statement.

## Proof
**The full symmetry group.** The twelve vertices and twenty-four edges of \(C\) are reconstructed directly from \(Q\). The eight triples of cube edges incident to each cube vertex are exactly the triangles of \(C\): three pairwise intersecting edges in the triangle-free cube must meet at one cube vertex. Each vertex of \(C\) belongs to exactly two such triangles; their triangle-intersection graph is the cube. Hence every automorphism of \(C\) induces an automorphism of the cube, and conversely; \(\operatorname{Aut}(C)=\operatorname{Aut}(Q_3)\). Cube automorphisms are exactly the forty-eight signed coordinate permutations \(g_{p,t}\). Their action on the four opposite vertex pairs yields the \(S_4\) quotient with kernel consisting of the identity and central inversion. The parity map \((-1)^{|t|}\) distinguishes these two kernel elements. Therefore \(G\cong S_4\times C_2\) as asserted.

**Integral homology.** There are exactly \(2649\) augmented faces (including the empty face), with cardinality distribution
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)=(1,24,204,744,1116,528,32).
\]
The verifier constructs a finite unit-coefficient matching on the augmented face poset. Process the edge indices \(j=23,22,\ldots,0\); at stage \(j\), pair every still-unmatched face \(F\) not containing \(e_j\) to \(F\cup\{e_j\}\) whenever both are unmatched faces, then mark both used. Exactly \(1296\) pairs result, leaving **precisely fifty-seven critical faces, all of cardinality four**. To certify acyclicity, direct each matched facet-incidence from lower to upper face and each unmatched facet-incidence from upper to lower. An exact topological sort visits all \(2649\) nodes of the resulting \(9960\)-arrow directed graph. No directed cycle exists. Each matched signed augmented boundary coefficient is \(\pm1\), so integral algebraic discrete Morse cancellation is valid without division by a nonunit. Its reduced chain complex has fifty-seven degree-three generators and zero generators elsewhere; all reduced differentials therefore vanish. This proves the integral homology assertion and rules out torsion.

**Signed Lefschetz traces.** For every \(g\in G\), equivariant Euler--Poincaré and concentration in degree three yield
\[
\chi_3(g)=\operatorname{tr}\bigl(g\mid\widetilde H_3(K;\mathbb Q)\bigr)
=\sum_{F\in K\cup\{\varnothing\}}(-1)^{|F|}\operatorname{sgn}(g|_F)\mathbf1_{gF=F}.
\]
The empty face contributes \(1\). If a \(g\)-invariant face contains an orbit \(O\) of length \(s\) on the twenty-four cuboctahedral edges, the chain-orientation sign from this orbit is \((-1)^{s-1}\); combining it with its cardinality sign \((-1)^s\) yields \(-1\). Thus there is a second, orbit-compressed formula:
\[
\chi_3(g)=\sum_{\substack{\mathcal A\text{ a family of orbits of }g\\
\bigcup\mathcal A\text{ is a matching of }C}}(-1)^{|\mathcal A|}.
\]
Both formulas have been evaluated independently for all forty-eight automorphisms, with exact integer agreement. Using cycle types for the induced permutation of the four antipodal axes, the **complete ten-class character table** is:

| \(S_4\) cycle type | Elements per central sign | \(\chi_3(\cdot,+)\) | \(\chi_3(\cdot,-)\) |
|---|---:|---:|---:|
| \((1,1,1,1)\) | 1 | 57 | 11 |
| \((2,1,1)\) | 6 | 1 | 3 |
| \((2,2)\) | 3 | 13 | -1 |
| \((3,1)\) | 8 | -3 | -1 |
| \((4)\) | 6 | -5 | -3 |

**Irreducible decomposition.** Project the two class-table columns onto the central \(\pm1\)-eigenspaces by taking their half-sum and half-difference. The resulting \(S_4\)-characters, in the displayed class order, are
\[
\chi_+=(34,2,6,-2,-4),\qquad \chi_-=(23,-1,7,-1,-1).
\]
Taking ordinary character inner products with the five rational irreducibles \(\mathbf1,\operatorname{sgn},V,V',W\), using class weights \((1,6,3,8,6)\), gives the respective nonnegative integer multiplicity vectors
\[
(1,2,5,2,5)\quad\text{and}\quad(1,2,2,2,4).
\]
Their dimensions are \(34\) and \(23\), and they reconstruct all ten traces exactly. The trivial \(S_4\)-constituent appears once in each central sector; only the positive one is fixed by \(G\). This proves the stated full-group character and invariant dimension.

## Verification
The accompanying self-contained `verify_cuboctahedral_character.py` uses only Python 3's standard library. Run `python3 verify_cuboctahedral_character.py` in the directory containing this result. It independently rebuilds both the cube and cuboctahedral graph, enumerates all matchings, verifies all \(1296\) integer-unit pairs and the global topological sort, enumerates all \(48\) distinct graph symmetries and both signed character formulas, compares the ten class values and checks character inner products. It ends in `VERIFY_OK`. The finite exhaustive computation is a proof for this exact finite graph, not a claim concerning arbitrarily large graphs.

## Relationship to prior work
Engström's 2005 claw-free independence-complex paper establishes general connectivity machinery: because \(K=\operatorname{Ind}(L(C))\), it supplies background but not a full homology character. Bayer--Jelić Milutinović--Vega prove a homotopy-type theorem for **outerplanar** matching complexes, but \(C\) is not outerplanar (it has \(24>2\cdot12-3\) edges); their paper also does not identify this representation.

The directly matching published computation *The cuboctahedral matching complex is a wedge of \(57\) three-spheres* already gives the full **nonequivariant** integral homotopy type and is credited; its entire `RESULT.md` was compared to this statement. It does **not** supply the ten conjugacy-class traces, the \(S_4\times C_2\) decomposition, the central \((34,23)\) eigenspaces, or the one-dimensional full-group invariant. Those are the findings here. The published full symmetry study for the **two-particle configuration space** of the same graph describes a different CW complex, with \(H_1\) and \(H_2\) dimensions \(14,43\), so its characters do not imply this result. A further published symmetry calculation concerns the ordinary matching complex of the **octahedral**, rather than cuboctahedral, graph, with eleven first-homology dimensions, again a distinct object.

## Limitations
The irreducible decomposition is over \(\mathbb Q\); no claim is made about splitting the integral homology lattice into irreducible summands or about the equivariant homotopy type. The analysis concerns the single graph \(L(Q_3)\) and does not establish a formula for all line graphs of hypercubes or all planar matching complexes. Literature indexing is incomplete; specialized unindexed equivalent character computations are a residual possibility. An independent scientific audit has not been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, submitted 17 December 2005; full HTML text at https://arxiv.org/html/math/0512420v1.
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, submitted 7 November 2024; Theorem 2 and Conjecture 11.
3. *The cuboctahedral matching complex is a wedge of \(57\) three-spheres*, published scientific result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-cuboctahedral-matching-complex-is-a-wedge-of-57-three-sphere--42f20681b118 (full `RESULT.md` read).
4. *Full symmetry modules of the cuboctahedral two-particle configuration space*, published scientific result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-full-symmetry-modules-of-the-cuboctahedral-two-particle-configur--5d6ece5c784b (different space).
5. *The full octahedral symmetry representation of the matching complex*, published scientific result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-full-octahedral-symmetry-representation-of-the-matching-comp--c700eceb52bb (different graph).
