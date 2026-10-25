# Full dihedral–fiber homology characters of cyclic clique blowups

## Finding
For integers \(m\ge3\) and \(q\ge2\), let \(X_{m,q}=\operatorname{Ind}(C_m[K_q])\), with lexicographic (clique-fiber) graph product. The group \(W=(S_q)^m\rtimes D_m\) acts on this complex. The complete graded rational \(W\)-module \(\widetilde H_*(X_{m,q};\mathbb Q)\) is determined by the canonical decomposition and explicit elementwise character formula below. This is the principal claim; the ordinary nonequivariant sphere-wedge phenomenon is acknowledged as a consequence of known simplicial-inflation theory.

Write \(K=\operatorname{Ind}(C_m)\). For each base vertex \(i\), put \(U_i=\ker(\mathbb Q^q\xrightarrow{\mathrm{sum}}\mathbb Q)\). For an independent set \(S\in K\), put \(L_S=\operatorname{Ind}(C_m-N[S])\), with \(N[S]\) the closed graph neighborhood. Let \(\det(S)\) be its one-dimensional oriented exterior-product line, so permuting the vertices of \(S\) changes sign in the ordinary way. There is an equivariant direct sum, natural for the full indicated action,
\[
\widetilde H_p(X_{m,q};\mathbb Q)\cong
\bigoplus_{S\in K}\det(S)\otimes
\widetilde H_{p-|S|}(L_S;\mathbb Q)
\otimes\bigotimes_{i\in S}U_i.
\tag{1}
\]
For \(S=\varnothing\), interpret \(L_S=K\) and the two empty tensor products as trivial lines. Terms indexed by \(S\) are permuted by \(D_m\); the displayed direct sum, rather than each individual summand, is a \(W\)-representation.

For an element \(g=(f,\tau)\in W\), where \(\tau\in D_m\) and \(f_i\in S_q\) acts on the color in source fiber \(i\) before moving it to fiber \(\tau(i)\), let \(\operatorname{cyc}(\tau|_S)\) denote its cycles on a \(\tau\)-invariant independent set \(S\). Let \(\mathcal E(L_S,\tau)\) be the reduced signed Lefschetz number
\[
\mathcal E(L_S,\tau)=\sum_{\substack{J\in L_S\\\tau J=J}}
(-1)^{|J|-1}\operatorname{sgn}(\tau|_J).
\tag{2}
\]
The empty face contributes \(-1\). Whenever \(\widetilde H_*(L_S;\mathbb Q)\) is nonzero, it is concentrated in a unique degree \(h(S)\), so the exact character is
\[
\chi_p(g)=\sum_{\substack{S\in K,\ \tau S=S\\
\widetilde H_{h(S)}(L_S)\ne0\\p=|S|+h(S)}}
\operatorname{sgn}(\tau|_S)(-1)^{h(S)}\mathcal E(L_S,\tau)
\prod_{c\in\operatorname{cyc}(\tau|_S)}
\left(\#\operatorname{Fix}\left(\prod_{i\in c} f_i\right)-1\right).
\tag{3}
\]
Products of fiber permutations follow the cyclic order of the \(\tau\)-orbit; different starting points give conjugate products and hence the same number of fixed colors. For \(S=\varnothing\), the product is \(1\). Formula (3), together with the explicit gap test below, is finite, exact and valid for every dihedral permutation, every independent collection of fiber permutations, and every degree. It is not a claim that these representations are irreducible.

## Assumptions and scope
The base cycle has labeled vertices \(\mathbb Z/m\), with edges between consecutive residues. In \(C_m[K_q]\), vertices \((i,a)\) and \((j,b)\) are adjacent when \(i,j\) are adjacent in the cycle, or when \(i=j\) and \(a\ne b\). Thus a face chooses at most one color in each selected base fiber and chooses nonadjacent base fibers. Reduced homology uses the augmented simplicial chain complex, with \(\widetilde C_{-1}=\mathbb Q\) and boundary of a vertex equal to the empty face. All characters refer to that natural simplicial action and not to an unspecified choice of sphere decomposition.

For nonempty independent \(S=\{s_1,\ldots,s_k\}\) in cyclic order, let positive gaps \(d_j=s_{j+1}-s_j\pmod m\) with \(d_j\ge2\) and \(\sum_jd_j=m\). If \(k=1\), use the sole gap \(d_1=m\). The graph \(C_m-N[S]\) is a disjoint union of paths on \(\ell_j=\max(d_j-3,0)\) vertices, with empty paths allowed. If some \(\ell_j\equiv1\pmod3\), the link homology vanishes; otherwise it has rank one, in degree
\[
h(S)=\sum_{j=1}^k\left\lfloor\frac{\ell_j+1}{3}\right\rfloor-1.
\tag{4}
\]
For \(S=\varnothing\), write \(m=3t+r\), where \(r\in\{0,1,2\}\). The unique nonzero link homology degree is \(h(\varnothing)=t-1\) for \(r=0,1\) and \(h(\varnothing)=t\) for \(r=2\); its rank is \(2\) for \(r=0\) and \(1\) otherwise. Accordingly the ordinary rational Betti numbers are the explicit polynomials
\[
\widetilde\beta_p(X_{m,q})=
\sum_{\substack{S\in K\\h(S)\text{ exists}\\p=|S|+h(S)}}
\operatorname{rank}\widetilde H_{h(S)}(L_S;\mathbb Q)\,(q-1)^{|S|}.
\tag{5}
\]
When \(m=3\) or \(4\), the reduced degree-zero term is included without assuming connectedness.

## Proof
**Equivariant chain splitting.** Choose in each color permutation module the canonical invariant vector \(e_i=q^{-1}\sum_{a=1}^qe_{i,a}\). The decomposition \(\mathbb Q^q=\mathbb Qe_i\oplus U_i\) is preserved by all color permutations and by transportation of one fiber to another. An oriented simplex in \(X_{m,q}\) chooses, for every selected base fiber, one basis vector from this permutation module. Expanding every selected fiber into either its \(e_i\)-component or its \(U_i\)-component yields a direct sum of augmented chain complexes indexed by the fixed subset \(S\) of fibers carrying a \(U_i\) factor. Under the augmented boundary, every \(U_i\) factor has augmentation zero and cannot be removed; every \(e_i\) factor has augmentation one. The remaining \(e_i\)-fibers therefore form precisely the augmented chain complex of \(L_S\). Move the \(U_i\) factors to the front in the exterior orientation: this gives the determinant line \(\det(S)\), a homological shift by \(|S|\), and the link boundary with its standard signs. Thus the splitting is a chain-level isomorphism, and equation (1) follows on homology. It is equivariant since the decomposition into \(e_i\) and \(U_i\), exterior orientation, and link action are all natural under \(W\). In particular, this is a direct sum, not a conjectural or unresolved spectral sequence.

**Gap and degree calculation.** Removing a selected vertex together with its two neighbors leaves exactly the interiors of the cyclic gaps, of respective lengths \(\max(d_j-3,0)\). For an empty path the independence complex is the formal \((-1)\)-sphere in augmented homology. The standard path deletion/link recurrence gives: an independence complex of a path on \(3a\) vertices has reduced homology \(\mathbb Z\) in degree \(a-1\), on \(3a+1\) vertices it is contractible, and on \(3a+2\) vertices it has reduced homology \(\mathbb Z\) in degree \(a\). The independence complex of a disjoint union is a join; reduced degrees add plus one for every join. This proves (4), its vanishing criterion, and rank one. The corresponding standard cycle recurrence gives the explicitly stated empty-set case. Together these show every link has either zero homology or exactly one nonzero degree. The integer path and cycle recurrence shows the link groups appearing in the rational decomposition are free abelian; the rational splitting alone is not used to assert an integral group-module splitting.

**Complete elementwise character.** Only \(\tau\)-fixed labels \(S\) contribute to the trace of the direct sum. Transporting the exterior orientation of the \(U\)-fiber subset contributes \(\operatorname{sgn}(\tau|_S)\). A permutation of the tensor factors around an orbit \(c\) has trace equal to the trace of the composite on a single \(U\), which is \(\#\operatorname{Fix}(\prod_{i\in c}f_i)-1\). Because the link homology occupies only degree \(h(S)\), the reduced simplicial Hopf trace formula equals \((-1)^{h(S)}\) times the signed fixed-face sum (2). Multiplying the three factors yields (3), including nontrivial rotations, both reflection types, and arbitrary color permutations. Identity substitution yields (5), so one statement controls ranks and all symmetry characters.

## Verification
Run \(\texttt{python3 VERIFY.py}\) with Python 3 standard library. It generates faces independently from the defining lexicographic graph, reconstructs mod-two simplicial homology by exact elimination, and compares it to (5) in fourteen nontrivial cases. It checks 1332 signed fiber-character Euler identities and 864 complete dihedral-plus-fiber **chain-character** equalities, including reflections, rotations and multiple fiber permutations. The script prints \(\texttt{CYCLE_CLIQUE_BLOWUP_VERIFICATION_OK}\) and \(\texttt{FULL_WREATH_EQUIVARIANT_CHAIN_SPLITTING_VERIFIED 864}\) on successful completion. These finite checks are not substituted for the preceding general chain-isomorphism proof.

## Relationship to prior work
Björner, Wachs and Welker's vertex-inflation/poset-fiber techniques already give broad nonequivariant wedge decompositions; the ordinary sphere-wedge assertion and rank-polynomial consequences of inflation are not presented as novel. Okura (2021) explicitly treats independence complexes of lexicographic products over forests and computes path cases, rather than the complete dihedral action for cyclic bases. Berghoff (2020) treats homology via marked independent sets and neighbor-deleted subgraphs and identifies the relevance of cycle links, not the full semidirect-product representation of clique-fiber cycle blowups. Vander Meulen and Van Tuyl (2017) study shellability and vertex decomposability of lexicographic products. The 2026 generalized-inflation treatment concerns nonequivariant homotopy. A distinct previously reported path-blowup fiber-module calculation does not imply the rotation/reflection trace formula (3) on closed cycles, since a path has no rotational action. The present additional information is the simultaneous **all-element** action of \((S_q)^m\rtimes D_m\), complete orientations and link Lefschetz factors, with a concrete cycle-gap evaluation.

## Limitations
The proof establishes rational representation theory and a rational rank formula, but does not assert a canonical integral module splitting: the rational invariant vector \(e_i\) has denominator \(q\). In particular no integral semidirect-product representation equivalence is claimed. Prior general inflation theory may implicitly lead to parts of the result after further work, and unindexed equivalent equivariant statements remain a priority risk. The formula is combinatorial rather than an irreducible-character decomposition; for arbitrary elements its finite sums may be large. No new classification is asserted for arbitrary base graphs or unequal clique fibers.

## References
1. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267v1, first publicly available 2020-08-14, https://arxiv.org/abs/2008.06267 .
2. K. Okura, *Independence complex of the lexicographic product of a forest*, arXiv:2109.04181v1, first publicly available 2021-09-09, https://arxiv.org/abs/2109.04181 .
3. K. Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, arXiv:2303.11984v1, first publicly available 2023-03-21, https://arxiv.org/abs/2303.11984 .
4. A. Björner, M. Wachs and V. Welker, *Poset fiber theorems*, Transactions of the American Mathematical Society 357 (2005), 1877–1899; general inflated-complex homotopy decomposition.
5. K. N. Vander Meulen and A. Van Tuyl, *Shellability, vertex decomposability, and lexicographical products of graphs*, Contributions to Discrete Mathematics 12 (2017), 63–68, https://cdm.ucalgary.ca/article/download/62777/46841/179282 .
6. A. Ayzenberg and T. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (2026), https://arxiv.org/abs/2602.08694 ; supporting comparison only, not the time-window lead.
