# Integral branch-symmetry homology of four-edge theta matching complexes

## Finding
For each integer \(m\ge 2\), let \(\Theta_m^{[4]}\) be the simple graph formed by \(m\) internally vertex-disjoint paths of length four between two common vertices \(u,v\). Let \(K_m=\mathcal M(\Theta_m^{[4]})\) be its ordinary matching complex. Permutations of the \(m\) arms and simultaneous reversal of all arms define an action of \(S_m\times C_2\). Let \(U_m=\ker(\mathbb Z^m\xrightarrow{\sum}\mathbb Z)\), the integral augmentation lattice. Write \(\operatorname{sgn}_m\) for the sign character of \(S_m\), and \(\varepsilon\) for the nontrivial sign character of the pole-exchange \(C_2\).

The **integral equivariant homology theorem** is
\[
\widetilde H_k(K_m;\mathbb Z)\cong
\begin{cases}
U_m\otimes\operatorname{sgn}_m\otimes\varepsilon^{\otimes m},& k=m,\\
0,&k\ne m,
\end{cases}
\]
where the isomorphism is an isomorphism of \(\mathbb Z[S_m\times C_2]\)-modules. Thus for \(\sigma\in S_m\), \(e\in\{0,1\}\), and \(\tau\) the pole interchange, the full rational character is
\[
\operatorname{tr}((\sigma,\tau^e)\mid\widetilde H_m(K_m;\mathbb Q))
=\operatorname{sgn}(\sigma)(-1)^{me}\bigl(|\operatorname{Fix}(\sigma)|-1\bigr).
\]
The nonequivariant homotopy equivalence \(K_m\simeq\bigvee^{m-1}S^m\) is stated only as context: it follows from previously published four-edge-path reductions and is **not** claimed to be new. The new assertion is the integral equivariant module and pole-reversal parity.

## Assumptions and scope
Use graph edges \(A_i=ua_i\), \(B_i=a_ib_i\), \(C_i=b_ic_i\), and \(D_i=c_iv\) on each arm \(1\le i\le m\). All internal vertices belonging to different arms are distinct. A face of \(K_m\) is a set of graph edges having pairwise disjoint endpoints, with the empty face included. The symmetric group permutes all arm subscripts; pole reversal maps \(A_i\leftrightarrow D_i\) and \(B_i\leftrightarrow C_i\). All homology is reduced integral simplicial homology unless another coefficient ring is specified. In this theorem \(m\ge2\), not merely a finite list of tested values.

## Proof
**1. The common core and contractible pieces.** Let \(K_0\) be the matching subcomplex on the \(2m\) edge-vertices \(B_i,C_i\). The only incompatible middle pair on each arm is \(\{B_i,C_i\}\), so
\[
K_0=(\{B_1,C_1\})*\cdots*(\{B_m,C_m\})\cong S^{m-1},
\]
where each parenthesized complex is two isolated vertices. For each \(i\), let \(X_i\) be the induced matching subcomplex on the common middle edge-vertices together with \(A_i,D_i\). Its factor on arm \(i\) is the independence complex of the four-vertex path \(A_i-B_i-C_i-D_i\). This path-independence complex is the three-edge tree with edges \(\{A_i,C_i\}\), \(\{A_i,D_i\}\), and \(\{B_i,D_i\}\); it is contractible. Therefore \(X_i\cong \operatorname{Ind}(P_4)*(S^0)^{*(m-1)}\) is contractible. Any intersection of two or more different \(X_i\) is exactly \(K_0\).

**2. An explicit collapse onto the union.** Set \(Y=\bigcup_{i=1}^m X_i\). Because no matching contains two distinct \(A\)-edges or two distinct \(D\)-edges, any simplex outside \(Y\) contains precisely one \(A_i\) and one \(D_j\) with \(i\ne j\). Such a simplex either contains \(C_i\) or does not. If it does not, its coface obtained by adding \(C_i\) is allowed: \(A_i\) excludes \(B_i\), while \(D_j\) is on another arm. Pair each outside simplex without \(C_i\) with the coface obtained by adding \(C_i\). Process lower members in decreasing order of simplex cardinality. At each step all other strict cofaces of that lower member have already been removed, so it is a free face of its paired upper member. Every outside simplex belongs to exactly one pair. Hence \(K_m\searrow Y\) by elementary simplicial collapses. These particular collapse pairs need not themselves be invariant under pole reversal; the **inclusion** \(Y\hookrightarrow K_m\) is equivariant and a homotopy equivalence, which suffices to identify the integral group action in homology.

**3. The integral homology lattice.** The relative chain groups of \((Y,K_0)\) split into contributions from the \(m\) pairs \((X_i,K_0)\), since all intersections lie in \(K_0\). By natural relative homology and contractibility of \(X_i\), the connecting homomorphism is an isomorphism
\[
\partial_i:H_m(X_i,K_0;\mathbb Z)\xrightarrow{\cong}\widetilde H_{m-1}(K_0;\mathbb Z)\cong\mathbb Z.
\]
The long exact sequence of \((Y,K_0)\), together with the preceding direct sum splitting, gives the integral exact sequence
\[
0\longrightarrow \widetilde H_m(Y;\mathbb Z)
\longrightarrow\widetilde H_{m-1}(K_0;\mathbb Z)\otimes\mathbb Z^m
\xrightarrow{\,1\otimes\sum\,}\widetilde H_{m-1}(K_0;\mathbb Z)
\longrightarrow\widetilde H_{m-1}(Y;\mathbb Z)\longrightarrow0.
\]
The sum map is onto, and in all other degrees the long exact sequence vanishes. It follows that
\[
\widetilde H_m(K_m;\mathbb Z)\cong\widetilde H_{m-1}(K_0;\mathbb Z)\otimes U_m,
\]
with all other reduced homology zero. This identification is natural for the full group because inclusions of pairs and connecting maps are equivariant, permutations merely permute the relative summands, and pole exchange preserves each pair \((X_i,K_0)\). It is an **integral** statement, not an inference from a rational character.

**4. Orientation signs.** The canonical generator of \(\widetilde H_{m-1}(K_0;\mathbb Z)\) is the join of the oriented zero-cycles \([B_i]-[C_i]\). Swapping any two join factors of degree zero contributes \(-1\) to the orientation of their join, so an arm permutation contributes \(\operatorname{sgn}(\sigma)\). Pole reversal interchanges each \(B_i,C_i\) and sends every zero-cycle to its negative, contributing \((-1)^m\). Thus this one-dimensional integral orientation lattice is \(\operatorname{sgn}_m\otimes\varepsilon^{\otimes m}\), proving the asserted \(S_m\times C_2\) module. Since the permutation module on arms has trace \(|\operatorname{Fix}(\sigma)|\), its augmentation kernel has rational trace \(|\operatorname{Fix}(\sigma)|-1\); multiplying by the orientation character gives the displayed formula.

## Verification
The included `verify_theta.py` program uses only the Python standard library. It generates complete matching simplices from graph endpoints and separately from the structural arm restrictions, then proves agreement for each \(2\le m\le7\). It executes and checks the entire free-face collapse for each case; computes complete mod-two boundary ranks; and checks 320 signed, fixed-simplex Lefschetz characters against the formula, including every \(S_m\times C_2\) action for \(m\le5\). At \(m=7\), the test handles 68,526 simplicial faces and verifies 20,412 elementary collapse pairs. These computations are independent finite cross-checks: the argument in the Proof section covers **all** \(m\ge2\) and proves the integral claim.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, publicly submitted on November 7, 2024 (version 2 dated September 23, 2026), prove a four-edge-path contraction/suspension statement in Proposition 7. Iterating that non-equivariant statement already supplies the sphere-wedge homotopy type of these multitheta graphs; **it does not identify the integral action of arm permutations and pole reversal**. The present contribution consists specifically of the natural integral augmentation-lattice identification and character formula, obtained by an equivariant relative sequence after an invariant-subcomplex inclusion. Bate, Everitt, Ford and Ramos, *Homology of matching complexes and representations of symmetric groups* (2026), determine representations for complete-hypergraph matching complexes; their objects and representation statements differ. Indexed literature on Dutch-windmill matching complexes concerns blade symmetries of a different graph family, while generalized-theta configuration-space homology is not matching-complex homology. The similarity of representation shapes is not the same theorem.

## Limitations
The theorem does not claim a new nonequivariant homotopy type; such a claim would be subsumed by published path-suspension results. The displayed integral module is for the ordinary matching complex, equal arm length four, and precisely the natural subgroup \(S_m\times C_2\) of graph automorphisms. It does not assert a description for arbitrary unequal arm lengths or an equivariant homotopy equivalence to a wedge of spheres. Finite checks cannot replace its integral proof. Source indexing is incomplete, and the possibility of an unindexed equivalent representation calculation remains a bibliographic risk; no independent external audit is claimed.

## References
1. Margaret Bayer, Marija Jelić Milutinović, Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first public version November 7, 2024; updated September 23, 2026), especially Proposition 7. https://arxiv.org/abs/2411.04601
2. Michael Bate, Brent Everitt, Samuel Ford, Eric Ramos, *Homology of matching complexes and representations of symmetric groups*, Proceedings of the American Mathematical Society 154 (2026), 1467–1478, DOI:10.1090/proc/17573. https://doi.org/10.1090/proc/17573
