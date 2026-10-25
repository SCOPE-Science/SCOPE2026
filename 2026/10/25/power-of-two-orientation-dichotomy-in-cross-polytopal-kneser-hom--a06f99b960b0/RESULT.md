# Power-of-two orientation dichotomy in cross-polytopal Kneser homology

## Finding
For integers \(n\ge3\), \(m\ge2n\), let \(X_{n,m}\) be the simplicial complex whose vertices are the \(n\)-subsets of \([m]\), with a face precisely when its vertices are pairwise intersecting. This is the independence complex of the Kneser graph on \(n\)-subsets of an \(m\)-element set. Set
\[
d_n=\tfrac12\binom{2n}{n},\qquad p_n=d_n-1,\qquad
\varepsilon_n=\begin{cases}1&\text{if }n-1\text{ is a power of }2,\\0&\text{otherwise.}\end{cases}
\]
Every \(2n\)-subset \(S\) of \([m]\) supports an induced copy \(X_{n,S}\cong\partial C_{d_n}\cong S^{p_n}\), the boundary of a cross-polytope of dimension \(d_n\). The images of its integral fundamental classes generate an \(S_m\)-stable subgroup \(L_{n,m}\) of \(\widetilde H_{p_n}(X_{n,m};\mathbb Z)\). The result is the integral lattice isomorphism
\[
L_{n,m}\cong
\operatorname{Ind}_{S_{2n}\times S_{m-2n}}^{S_m}
(\operatorname{sgn}_{2n}^{\varepsilon_n}\boxtimes\mathbf1),
\]
and the inclusion is split as a homomorphism of abelian groups (the splitting is not asserted to respect \(S_m\)). Consequently \(L_{n,m}\) is torsion-free and primitive in integral homology. Its rational character is
\[
\chi_{L_{n,m}}(\sigma)=
\sum_{\substack{S\subseteq[m],\ |S|=2n\\\sigma S=S}}
\operatorname{sgn}(\sigma|_S)^{\varepsilon_n}.
\]
For \(\varepsilon_n=0\), the full symmetric-group quotient has nonzero rational homology in degree \(p_n\):
\[
H_{p_n}(|X_{n,m}|/S_m;\mathbb Q)\ne0.
\]
For \(n=3\), the known rational Betti-number equality implies that these spheres span *all* degree-nine rational homology, with explicit complete character
\[
\chi_{3,m}(\sigma)=[t^6]
\prod_{\ell\ge1}(1+(-1)^{\ell-1}t^\ell)^{c_\ell(\sigma)},
\]
where \(c_\ell(\sigma)\) is the number of \(\ell\)-cycles of \(\sigma\).

## Assumptions and scope
The graph \(KG(n,m-2n)\) has one vertex for each \(n\)-subset of \([m]\), with edges joining disjoint pairs. The complex \(X_{n,m}\) is its ordinary simplicial independence complex; \(S_m\) acts by permuting the ground set. All homology is ordinary reduced simplicial homology unless stated otherwise, with the induced actions on oriented chains. The representation assertion is **integral for the specified sublattice only**, and **rational for all degree-nine homology only when \(n=3\)**. Dimensions and coefficient rings are part of the theorem.

## Proof
**Cross-polytope sphere.** Fix \(S\subseteq[m]\) of size \(2n\). Two distinct \(n\)-subsets of \(S\) are disjoint exactly when they are complementary in \(S\). Hence the induced subcomplex on the \(\binom{2n}{n}=2d_n\) vertices from \(S\) is the join of \(d_n\) two-point discrete complexes, i.e. \(\partial C_{d_n}\cong S^{p_n}\). Denote its oriented integral fundamental cycle by \(z_S\); its sign depends on a choice of orientation.

**Primitive independence via maximal facets.** Order the elements of \(S\) as \(s_1,\ldots,s_{2n}\) and identify them temporarily with \([2n]\). Begin with all \(n\)-subsets of \([2n-1]\); remove
\[
A=\{1,\ldots,n\},\qquad B=\{1,n+1,\ldots,2n-1\}
\]
and insert their complements in \([2n]\), respectively
\[
A^c=\{n+1,\ldots,2n\},\quad B^c=\{2,\ldots,n,2n\}.
\]
Call the resulting collection \(F_S\). Each complementary pair contributes exactly one vertex of \(F_S\), so \(F_S\) is a \(p_n\)-simplex of the local sphere. For \(n\ge3\), the union of these \(n\)-subsets equals exactly \(S\).

We show \(F_S\) is a maximal simplex of **the entire** \(X_{n,m}\), including when \(m>2n\). Every \((n-1)\)-subset \(R\) of \(S\) is disjoint from a vertex of \(F_S\). Indeed, put \(T=S\setminus R\), so \(|T|=n+1\). If \(s_{2n}\in R\), the set \(T\subseteq\{s_1,\ldots,s_{2n-1}\}\) contains \(n+1\) different \(n\)-subsets, and at most two were removed when forming \(F_S\); since \(n\ge3\), at least one remains. Otherwise \(T\) consists of \(s_{2n}\) and one \(n\)-subset \(D\) of \(\{s_1,\ldots,s_{2n-1}\}\). If \(D\ne A,B\), it remains in \(F_S\). If \(D=A\), then \(B^c\subseteq T\); if \(D=B\), then \(A^c\subseteq T\). In each case an \(n\)-subset in \(F_S\) avoids \(R\).

Now any vertex \(U\) of \(X_{n,m}\) outside \(F_S\) either lies inside \(S\), when its complementary \(n\)-subset belongs to \(F_S\), or contains an element outside \(S\), when \(|U\cap S|\le n-1\). In the latter case extend \(U\cap S\) to an \((n-1)\)-subset \(R\) of \(S\) and use the preceding paragraph. Thus some member of \(F_S\) is disjoint from \(U\) in either case. This proves maximality.

The integral \(p_n\)-cochain selecting the oriented facet \(F_S\) and vanishing on every other \(p_n\)-simplex is a cocycle: no simplex has \(F_S\) as a proper face. It evaluates to \(\pm1\) on \(z_S\) and to zero on \(z_T\) for every other \(2n\)-subset \(T\), since the vertex union of \(F_S\) is \(S\), which cannot lie in a distinct \(2n\)-set. Adjust each sign so the matrix of pairings is the identity. The resulting integral evaluation homomorphisms split the map \(\bigoplus_{|S|=2n}\mathbb Z[z_S]\to\widetilde H_{p_n}(X_{n,m};\mathbb Z)\), proving both injectivity and primitivity. This is the explicit cocycle method underlying the lower bound of Feng–Wang, now retaining the group action.

**Local orientation.** In the local sphere, take the real permutation space \(V\) with basis the \(n\)-subsets of \(S\). Write \(P\) for the subspace spanned by sums of each complementary pair. The orthogonal complement \(W\) consists of differences within the pairs, has dimension \(d_n\), and carries the signed-permutation action of \(S_{2n}\) on the cross-polytope axes. Its determinant is the degree of the action on the oriented sphere, and
\[
\det(\sigma|_W)=\det(\sigma|_V)\det(\sigma|_P)^{-1}.
\]
For a ground-set transposition, the action on the \(n\)-subsets has exactly \(\binom{2n-2}{n-1}\) two-cycles, so its determinant on \(V\) is \(+1\): the central binomial coefficient is even. On the complementary *pairs*, the induced permutation has exactly \(\tfrac12\binom{2n-2}{n-1}\) two-cycles. Hence
\[
\deg((1\;2)|_{\partial C_{d_n}})
=(-1)^{\binom{2n-2}{n-1}/2}.
\]
Write \(r=n-1\). Legendre's formula gives \(v_2\bigl(\binom{2r}{r}\bigr)=s_2(r)\), where \(s_2(r)\) counts the ones in the binary expansion of \(r\). Thus the exponent is odd exactly when \(r\) is a power of two. Since every one-dimensional character of \(S_{2n}\) is determined by its value on a transposition, the stabilizer acts on \([z_S]\) by \(\operatorname{sgn}_{2n}^{\varepsilon_n}\). Permutations outside \(S\) fix its sphere pointwise. The orbit of the independent classes \([z_S]\) is therefore the stated induced integral lattice, and its character is the fixed-support sum.

**Quotients and the complete triple case.** If \(\varepsilon_n=0\), the induced module is the permutation lattice on \(2n\)-subsets, and over \(\mathbb Q\) it contains a nonzero invariant sum. The primitive injection puts that sum inside \(H_{p_n}(X_{n,m};\mathbb Q)^{S_m}\). For a finite group acting simplicially on a finite complex, barycentric subdivision and rational averaging identify the homology of the orbit space with the invariant rational homology, proving the asserted quotient nonvanishing. For \(n=3\), Feng's rational Betti-number theorem gives \(\dim_{\mathbb Q}\widetilde H_9(X_{3,m};\mathbb Q)=\binom m6\). Our independent embedded-sphere classes already have that dimension, so they exhaust this rational homology. An invariant six-subset is a union of permutation cycles; the restricted sign is \(\prod_{\ell}(-1)^{(\ell-1)e_\ell}\). Extracting the coefficient of \(t^6\) yields the displayed complete character.

## Verification
The included standalone Python 3 program `check_kneser_orientations.py` uses exact integer arithmetic and explicit finite set enumeration. It checks that the proposed distinguished face is maximal for ground-set sizes \((n,m)=(3,6),(3,7),(3,8),(4,8),(4,9),(5,10)\); the program directly tests every possible added \(n\)-subset for every support of size \(2n\). It also constructs the real signed axis permutation determinant for \(n=3,4,5,6\), compares it with the binary power-of-two formula, and tabulates induced characters in small examples. Successful execution ends with `KNESER_CROSSPOLYTOPE_ORIENTATION_CHECKS_OK 3318`. The infinite-dimensional claims are proved above, not inferred from these finite checks.

## Relationship to prior work
Feng and Wang (arXiv:2404.10566v1, first posted 16 April 2024) identified the embedded cross-polytopal sphere construction, an explicit maximal-face witness, and the independent homology classes in their Lemma 9 and Theorem 10. **These independent classes and the rank lower bound are prior work, not claimed as new here.** Feng (arXiv:2610.17394v1, first posted 12 October 2026), Theorem 18, established the full rational Betti numbers for triples, in particular the degree-nine rank; the exact rank is also prior work. The additional statement here is the group-action orientation calculation in *all* subset sizes, including its power-of-two dichotomy, integral induced-module structure and rational symmetry-quotient nonvanishing; for triples it identifies the entire rational module rather than only its dimension. Ramos and White (arXiv:1711.07456v2) provide general FI-graph representation-stability tools, without the present exact Kneser independence-complex module. No claim of independence from these antecedents is made: the proof explicitly uses their theorems.

## Limitations
There may be other homology in the degree \(p_n\) for \(n\ge4\); no description of it is asserted. In the triple case, the rational description does not rule out integral torsion, a problem explicitly left open by Feng (2026). The integral splitting need not be equivariant over \(\mathbb Z\). When \(n-1\) is a power of two, vanishing of invariant vectors in the displayed submodule does not imply vanishing for the entire complex (except in the complete rational triple case). A closely related but unindexed prior formulation could still exist.

## References
- Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1 (16 April 2024), especially Lemma 9 and Theorem 10. https://arxiv.org/pdf/2404.10566
- Z. Feng, *The Rational Homology of Independence Complexes of Kneser Graphs on Triples*, arXiv:2610.17394v1 (12 October 2026), especially Theorem 18 and Section 7. https://arxiv.org/pdf/2610.17394
- E. Ramos and G. White, *Families of Nested Graphs with Compatible Symmetric-Group Actions*, arXiv:1711.07456v2 (22 November 2017). https://arxiv.org/pdf/1711.07456
