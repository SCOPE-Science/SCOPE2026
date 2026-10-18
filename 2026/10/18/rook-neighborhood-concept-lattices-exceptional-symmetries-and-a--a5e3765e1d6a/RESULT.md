# Rook-neighborhood concept lattices: exceptional symmetries and a sharp Horn-arity gap

## Finding

**Theorem.** Fix integers \(m,n\ge2\). Let \(W=[m]\times[n]\), with symmetric, reflexive incidence \((i,j)I(r,s)\) exactly when \(i=r\) or \(j=s\). Let \(c\) be its two-sided Galois closure on subsets of \(W\), and let \(\mathcal L_{m,n}\) be the concept lattice ordered by extents.

The closed extents are *exactly* the empty set, \(W\), all singletons, the \(m\) complete rows, the \(n\) complete columns, the \(mn\) row-column crosses, and the \(2\binom m2\binom n2\) two-point sets occupying different rows and different columns. Thus
\[
|\mathcal L_{m,n}|=2+2mn+m+n+2\binom m2\binom n2.
\]

The **full order-automorphism group** is
\[
\operatorname{Aut}(\mathcal L_{m,n})\cong
\begin{cases}
\mathfrak S_4,&m=n=2,\\
\mathfrak S_b\wr\mathfrak S_2,&\{m,n\}=\{2,b\},\ b\ge3,\\
\mathfrak S_m\times\mathfrak S_n,&m,n\ge3,\ m\ne n,\\
(\mathfrak S_m\times\mathfrak S_m)\rtimes C_2,&m=n\ge3,
\end{cases}
\]
where the last involution swaps coordinates, and the wreath product permutes the two rows and independently relabels their \(b\) points.

For sound unit-conclusion Horn implication bases, define **iterative width** as the least possible largest antecedent size when repeated forward chaining must compute \(c\); define **direct width** analogously when every closure must be obtained from the original input in one simultaneous application of all applicable rules. With the empty-basis width convention \(0\), the sharp widths are
\[
(\operatorname{width}_{\mathrm{iter}},\operatorname{width}_{\mathrm{direct}})=
\begin{cases}
(0,0),&m=n=2,\\
(2,2),&\min\{m,n\}=2<\max\{m,n\},\\
(3,4),&m,n\ge3.
\end{cases}
\]
In particular, for both dimensions at least three, an unavoidable four-premise direct implication can be replaced by a three-premise iterative basis. The thin two-row family exhibits instead an exceptional symmetry enlargement and a product-lattice decomposition.

## Assumptions and scope

The parameters are finite integers \(m,n\ge2\). All objects and attributes are separate copies of \(W\). The derivation operator for \(S\subseteq W\) collects all attributes incident with every point of \(S\); a second derivation gives \(c(S)=S''\). For \(x=(i,j)\), its incidence neighborhood is the cross
\[
C_{i,j}=(\{i\}\times[n])\cup([m]\times\{j\}).
\]
Therefore \(c(S)\) is the intersection of all crosses containing \(S\), with the intersection over an empty cross family interpreted as \(W\). The lattice of extents is the inclusion-ordered family of fixed points of \(c\). A Horn rule \(P\to y\) is sound when \(y\in c(P)\); its premise size is \(|P|\). No assertion concerns open-neighborhood simplicial complexes or other graph complexes.

## Proof

**Closed extents.** Intersect two distinct crosses. If their row indices coincide, the result is the shared complete row; if their column indices coincide, the result is the shared complete column; otherwise, for \(i\ne r\) and \(j\ne s\),
\[
C_{i,j}\cap C_{r,s}=\{(i,s),(r,j)\}.
\]
Intersecting an additional cross with a complete row or column leaves that row or column or reduces it to one point. Intersecting an additional cross with a two-point diagonal leaves the pair, one point, or nothing. Further intersections introduce no other types. Every listed type is actually achieved: the crosses themselves; rows and columns from shared-index pairs; diagonal two-point sets from distinct-index cross pairs; singletons by cutting such a pair with the cross centered at one of its elements; the empty set by intersecting all crosses; and \(W\) by taking no crosses. Because \(m,n\ge2\), these classes are pairwise distinct. Their disjoint counts give the formula.

**Automorphisms.** Each singleton is a lattice atom, and each closed extent is the join of precisely the atoms it contains. Hence every order automorphism acts faithfully on \(W\) and preserves which pairs of atoms have a join containing a third atom. If \(m,n\ge3\), this nonclosed-pair adjacency is exactly the rook graph: two different points are adjacent precisely when they share a row or column. Its maximal cliques with at least three vertices are exactly the rows and columns. They form two families whose members within each family are disjoint, and whose members across families intersect in one point. An automorphism must permute the two families separately, except that when \(m=n\) it may interchange the families. Independent row and column permutations, together with the square-case coordinate swap, do preserve every cross and every closed extent, giving exactly the stated groups.

For \(m=2\), write the two rows as disjoint sets \(R_1,R_2\) of size \(n=b\). The closure factorizes as
\[
c(S)=f_b(S\cap R_1)\cup f_b(S\cap R_2),\qquad
f_b(T)=\begin{cases}T,&|T|\le1,\\R_i,&T\subseteq R_i,\ |T|\ge2.\end{cases}
\]
Thus \(\mathcal L_{2,b}\cong M_b\times M_b\), where \(M_b\) is the height-two lattice with \(b\) atoms. For \(b\ge3\), the only pairs with nonclosed union are pairs in a common row, so the two complete row classes are intrinsically recognizable. Arbitrary independent permutations of their \(b\) atoms and their interchange preserve the closure, and these exhaust the automorphisms: \(\mathfrak S_b\wr\mathfrak S_2\). At \(b=2\), \(M_2\) is the four-element Boolean lattice and \(M_2\times M_2\) is the Boolean lattice on four atoms, whose automorphism group is \(\mathfrak S_4\). Transposing coordinates treats \(n=2\) symmetrically.

**Direct width.** If a set \(S\) contains no pair of points with different rows and columns, all its points lie in one row or one column; two distinct points already generate its closure. Otherwise choose two diagonal points \(p=(i,j)\), \(q=(r,s)\), with \(i\ne r\), \(j\ne s\). Exactly two crosses contain them both: \(C_{i,s}\) and \(C_{r,j}\). If \(S\) fits both, then \(S=\{p,q\}\). If it fits exactly one, one additional point of \(S\) rules out the other. If it fits neither, two further witnesses rule out the two crosses. Consequently, for every \(S\), some subset \(T\subseteq S\) of at most four points satisfies \(c(T)=c(S)\). This gives a direct unit-conclusion basis of premise width at most four: include \(T\to y\) for each \(|T|\le4\) and \(y\in c(T)\setminus T\).

When \(m,n\ge3\), choose the four corners of a two-by-two subboard as \(S\), and choose \(y\) outside both selected rows and both selected columns. No single cross contains all of \(S\), so \(y\in c(S)=W\). Every three-point subset of \(S\), however, is contained in a cross avoiding \(y\), hence cannot imply \(y\). Any single-pass basis deriving \(y\) from \(S\) must therefore contain an applicable rule with all four points as antecedent. The sharp direct width is four.

**Iterative width.** For \(m,n\ge3\), use three kinds of sound rules: any two distinct cells in one row imply every cell of that row; any two distinct cells in one column imply every cell of that column; and any three cells in pairwise distinct rows and columns imply every cell of \(W\). Let \(T\) be any set saturated under these rules. If it contains two complete rows, then each column has at least two points and becomes complete, so \(T=W\); the dual holds for two complete columns. If it contains one complete row and any off-row point, the column of that point becomes complete; an additional point outside the resulting cross forces a second complete row, hence \(W\). Thus a proper saturated \(T\) is a row, a column, a cross, or a set with no repeated row or column. In the last case the three-point rule forces \(|T|\le2\), so it is empty, a singleton, or a diagonal pair. All of these sets are closed by the first part. Therefore the rules compute \(c\) by forward chaining. For a lower bound, a three-point partial matching has closure \(W\), but every subset of size at most two is closed; no sound rule with at most two premises can introduce any new point. The sharp iterative width is three.

For \(\min\{m,n\}=2\) and larger dimension at least three, the factorized closure displayed above is computed directly and iteratively by pairwise within-row saturation. No singleton has any nontrivial consequence, so width two is necessary and sufficient. At \(m=n=2\), every subset is closed and the empty basis works.

## Verification

The included standalone Python program `artifacts/verify.py` checks Galois closures against the proposed disjoint normal forms for all \(2^{mn}\) subsets of boards of dimensions \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). It independently tests iterative saturation for the first five boards, gives explicit four-premise and three-matching lower-bound witnesses where applicable, and checks every independent thin-board row permutation and row swap for widths \(3\) and \(4\). Run `python3 artifacts/verify.py`; the expected last line is `VERIFY_OK closure_family=PASS concept_counts=PASS arity_bounds=PASS thin_symmetry=PASS`. These finite checks are corroboration, not an all-parameter proof.

## Relationship to prior work

Formal-context concept lattices are canonically represented as intersection lattices of their attribute neighborhoods, as discussed and proved, in generality, by Rawson, Myers, Green, Robinson, and Joslyn (2023). That general representation is used here, not claimed new. Adaricheva and Ninesling (2018) study canonical direct and binary-direct Horn bases and explicitly distinguish direct single-application closure from repeated forward chaining; this distinction is likewise not claimed new. The rook graph is the line graph of a complete bipartite graph, a standard graph-theoretic identification. The contribution assessed here is the exact board-specific closure normal form together with its exceptional automorphism enlargement and the sharp \((3,4)\) arity separation in thick boards. Published results on *simplicial open-neighborhood complexes* of rook graphs concern a different construction and do not, by their reported statements, yield this Galois-closure classification. General graph-edge adjacency context results for complete graphs concern a different underlying graph. The publication-priority search has limitations noted below.

## Limitations

The proof applies only to complete rectangular boards with both sides at least two and to the stated symmetric reflexive incidence. The direct/iterative width concerns maximal antecedent size, not minimum rule count or total basis size. The structural and arity results have not been independently externally audited. A potentially equivalent result under two-equivalence-relation or database-dependency terminology may exist despite the searches; the inspected literature establishes context but does not certify priority. The executable check covers finitely many parameter pairs only.

## References

1. K. Adaricheva and T. Ninesling, *Direct and Binary Direct Bases for One-set Updates of a Closure System*, arXiv:1810.08684, first public version 2018-10-19. https://arxiv.org/abs/1810.08684
2. M. G. Rawson, A. Myers, R. Green, M. Robinson, and C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first public version 2023-07-21. https://arxiv.org/abs/2307.11681
3. K. Adaricheva, J. B. Nation, and R. Rand, *Ordered direct implicational basis of a finite closure system*, Discrete Applied Mathematics 161 (2013), 707–723; original preprint arXiv:1110.5805 (2011), https://arxiv.org/abs/1110.5805. Background only, not the age anchor.
