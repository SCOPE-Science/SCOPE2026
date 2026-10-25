# Multiplicity-free fiber symmetry in lexicographic path–clique independence homology

## Finding
Let \(P_m\) be the path on \([m]\), let \(K_n\) be the complete graph on \(n\) vertices, and let \(X_{m,n}=\operatorname{Ind}(P_m[K_n])\), with \(m\ge4\) and \(n\ge2\). The product group \(G_{m,n}=(S_n)^m\) permutes the colors independently within the \(m\) complete-graph fibers. Put \(U_n=\ker(\mathbb Q^n\xrightarrow{\mathrm{sum}}\mathbb Q)\), and regard \(U_n^{(i)}\) as a representation supported in the \(i\)-th factor.

For an independent set \(T\subseteq[m]\), delete its closed neighborhood \(N[T]\) in the path. Let \(b_1,\ldots,b_s\) be the positive vertex lengths of the path components of \(P_m\setminus N[T]\). Say that \(T\) is *admissible* when every \(b_j\) is congruent to \(0\) or \(2\pmod 3\), with the empty list admissible, and then set
\[
d(T)=|T|+\sum_{j=1}^{s}\left\lfloor\frac{b_j+1}{3}\right\rfloor-1.
\]
For every integer \(d\ge0\), there is a \(G_{m,n}\)-module isomorphism
\[
\boxed{\widetilde H_d(X_{m,n};\mathbb Q)\cong
\bigoplus_{\substack{T\in\operatorname{Ind}(P_m)\\T\ \mathrm{admissible},\ d(T)=d}}
\bigboxtimes_{i=1}^{m} E_i(T),\qquad
E_i(T)=\begin{cases}U_n,&i\in T,\\ \mathbb Q,&i\notin T.\end{cases}}
\]
The sum is empty, hence zero, when no admissible set has the designated degree. **Every nonzero displayed constituent is irreducible over \(\mathbb Q\), and no constituent occurs twice**: the full fiberwise homology representation is multiplicity-free in every degree.

Under the diagonal copy of \(S_n\) in \(G_{m,n}\), this gives the closed representation formula
\[
\boxed{\left.\widetilde H_d(X_{m,n};\mathbb Q)\right|_{S_n}
\cong\bigoplus_{p=0}^{d+1}\left(U_n^{\otimes p}\right)^{\oplus a_{m,d,p}},\quad
a_{m,d,p}=\binom{p+1}{3(d+1)-m}\binom{d+1}{p}.}
\]
Here \(U_n^{\otimes0}=\mathbb Q\), and binomial coefficients with out-of-range lower indices are zero. For \(g=(\sigma_1,\ldots,\sigma_m)\in G_{m,n}\), the degree-\(d\) character is exactly
\[
\chi_d(g)=\sum_{\substack{T\ \mathrm{admissible}\\d(T)=d}}
\prod_{i\in T}\left(|\operatorname{Fix}(\sigma_i)|-1\right).
\]
Consequently the invariant subspace under the full fiber group is one-dimensional, concentrated in degree \(m/3-1\) when \(m\equiv0\pmod3\), or in degree \((m-2)/3\) when \(m\equiv2\pmod3\); it is zero in every degree when \(m\equiv1\pmod3\).

## Assumptions and scope
The lexicographic product has vertex set \([m]\times[n]\); two distinct vertices \((i,a)\) and \((j,b)\) are adjacent exactly when \(|i-j|=1\), or when \(i=j\) and \(a\ne b\). Its independence simplices choose at most one color per fiber, and the chosen fiber positions form an independent set in \(P_m\). All homology groups are reduced, all coefficients in this representation theorem are rational, and the graph and all group actions are finite. The empty simplex is present in the augmented chain complex. The action concerns independent permutations of the \(n\) colors in each fiber; path reversal is not included in the asserted group representation.

## Proof
**1. Canonical equivariant chain splitting.** Write \(K=\operatorname{Ind}(P_m)\) and \(W_i=\mathbb Q\{e_{i,1},\ldots,e_{i,n}\}\). With the base positions ordered increasingly, the augmented simplicial degree-\(q\) chain group is
\[
\widetilde C_q(X_{m,n};\mathbb Q)=
\bigoplus_{\substack{\sigma\in K\\|\sigma|=q+1}}\ \bigotimes_{i\in\sigma} W_i.
\]
In the simplicial differential, deleting the vertex at position \(i\) is the alternating-sign map given by applying the augmentation \(\epsilon_i:W_i\to\mathbb Q\), \(\epsilon_i(e_{i,a})=1\), in factor \(i\). Since \(n\ne0\) in \(\mathbb Q\), there is a \(S_n\)-equivariant direct sum \(W_i=\mathbb Q u_i\oplus U_i\), with \(u_i=n^{-1}\sum_a e_{i,a}\), \(\epsilon_i(u_i)=1\), and \(\epsilon_i(U_i)=0\). Expand every tensor product according to the subset \(T\subseteq\sigma\) of factors chosen from \(U_i\). Deleting a factor in \(T\) vanishes; deleting a factor outside \(T\) preserves \(T\). Thus the full augmented complex is a direct sum of subcomplexes indexed by the faces \(T\) of \(K\). The subcomplex indexed by \(T\), after the standard alternating sign obtained by moving the fixed ordered positions of \(T\) past the variable positions, is the augmented simplicial chain complex of \(\operatorname{lk}_K(T)\), shifted upward by \(|T|\), tensored with \(\bigotimes_{i\in T}U_i\). All these identifications commute with \((S_n)^m\). Hence
\[
\widetilde H_d(X_{m,n};\mathbb Q)\cong
\bigoplus_{T\in K}\widetilde H_{d-|T|}(\operatorname{lk}_K(T);\mathbb Q)\otimes\bigboxtimes_{i\in T}U_i.
\]
The tensor notation on the right includes trivial factors at positions not in \(T\).

**2. Path links.** For an independent set \(T\), its link in \(K\) is precisely \(\operatorname{Ind}(P_m\setminus N[T])\). The remainder is a disjoint union of paths of positive lengths \(b_1,\ldots,b_s\); its independence complex is their simplicial join. For a path of length \(b\), the usual deletion-at-vertex-two decomposition has two contractible pieces and intersection \(\operatorname{Ind}(P_{b-3})\), so for \(b\ge3\) it yields \(\operatorname{Ind}(P_b)\simeq\Sigma\operatorname{Ind}(P_{b-3})\). The initial cases are \(\operatorname{Ind}(P_0)=\{\emptyset\}\) with reduced augmented homology in degree \(-1\), \(\operatorname{Ind}(P_1)\) contractible, and \(\operatorname{Ind}(P_2)\simeq S^0\). Induction gives a contractible complex when \(b\equiv1\pmod3\), and a single rational sphere with degree \(\lfloor(b+1)/3\rfloor-1\) otherwise. The join formula for reduced homology then proves that each link contributes either zero or one \(\mathbb Q\) in degree \(\sum_j\lfloor(b_j+1)/3\rfloor-1\), even when there are no remaining vertices (degree \(-1\)). Substitution into Step 1 gives the first boxed formula, including all boundaries and empty-link cases.

**3. Multiplicity-freeness.** For every \(n\ge2\), the augmentation representation \(U_n\) is a nontrivial irreducible rational representation of \(S_n\) (the sign representation when \(n=2\)). External tensor products of irreducibles are irreducible for the direct product. If \(T\ne T'\), some fiber is represented by \(U_n\) for one and by the trivial representation for the other, so the two constituents are inequivalent. Every link contributes at most one copy by Step 2. This proves multiplicity-freeness and the full fiberwise character formula.

**4. Closed diagonal multiplicities.** Restrict Step 1 to the diagonal subgroup. Every term indexed by \(T\) becomes \(U_n^{\otimes|T|}\). Write \(c_{m,d,p}\) for the number of admissible independent sets of size \(p\) with \(d(T)=d\). The nonequivariant Betti-number formula for lexicographic products of paths and complete graphs in Okura's classification (2021; explicit formula also in Theorem 1.4 of Okura 2023) is, for every positive integer \(n-1\),
\[
\dim_{\mathbb Q}\widetilde H_d(X_{m,n};\mathbb Q)
=\sum_{p\ge0}\binom{p+1}{3(d+1)-m}\binom{d+1}{p}(n-1)^p.
\]
On the other hand, the proved equivariant chain splitting makes the same dimension equal to \(\sum_pc_{m,d,p}(n-1)^p\). Both sides are polynomials in the variable \(n-1\), equal for all integers \(n\ge2\); equality of polynomial coefficients yields \(c_{m,d,p}=a_{m,d,p}\) exactly. This gives the second boxed formula without inferring representations from equal Betti numbers.

**5. Invariants.** For \(T\ne\emptyset\), the product-group constituent contains a nontrivial irreducible factor and therefore has no fixed vectors under the full product group. The empty-set summand is exactly \(\widetilde H_d(\operatorname{Ind}(P_m);\mathbb Q)\), whose degrees are determined in Step 2. This gives the asserted invariant dimensions.

## Verification
The included standalone standard-library program `verify_colored_paths.py` independently enumerates path links and verifies the closed binomial multiplicities for path lengths \(4\) through \(16\) (2,353 contributing links). It additionally constructs the actual augmented face chain complexes for two-color fibers and computes the \(+1\) and \(-1\) eigenspace homology of fiber transpositions over the fields with 101 and 103 elements for 40 involution/field cases. In every case, eigenspace ranks reproduce both the predicted homology dimensions and the predicted trace in each degree. Finally, direct fixed-face signed Euler counts agree with the diagonal formula in 45 tests. The actual execution output is in `verification_output.txt`. These checks are finite corroboration; Steps 1–5 prove the all-parameter result.

## Relationship to prior work
Okura's 2021 classification and 2023 polyhedral-join theorem establish nonequivariant homotopy types and explicit sphere multiplicities for path lexicographic products, from which Step 4 borrows **only numerical Betti counts**. Neither paper computes the \((S_n)^m\)-module or the degree-separated diagonal character. Carnero Bravo's 2023 polyhedral-join paper gives complementary nonequivariant splittings and graph-complex examples, without the stated fiberwise irreducible classification. Fu and Grbić (2018/2020) analyze symmetry induced by actions on the indexing complex for polyhedral **products**; those results do not state the internal complete-graph-fiber action on these polyhedral **joins**, nor the exact admitted subsets and binomial representation decomposition. General simplicial-composition literature provides combinatorial constructions or Betti-number formulas but not the result stated here. The step that uses a pre-existing theorem is clearly identified, and no new nonequivariant sphere-wedge theorem is claimed.

## Limitations
The theorem describes rational representations, not an integral equivariant splitting or equivariant homotopy equivalence. It concerns the natural independent fiber-permutation subgroup; additional path-reversal action has not been calculated. The identification of the diagonal multiplicities uses a published homotopy-classification formula; the explicit general-equivariant link splitting is proved here. Search coverage does not establish absolute priority: an equivalent result using another formulation may be unindexed. The finite checks cannot establish universal statements by themselves.

## References
1. Kengo Okura, *Independence Complex of the Lexicographic Product of a Forest*, arXiv:2109.04181, first posted 2021-09-09 (Theorem 1.3).
2. Kengo Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, arXiv:2303.11984v1, first posted 2023-03-21 (Theorems 1.3 and 1.4, Proposition 5.2).
3. Andrés Carnero Bravo, *Polyhedral Joins and Graph Complexes*, arXiv:2307.14321, first posted 2023-07-26 (Sections 3–4).
4. Xin Fu and Jelena Grbić, *Simplicial G-Complexes and Representation Stability of Polyhedral Products*, arXiv:1803.11047, first posted 2018-03-29 (Sections 1–3).
5. Anton Ayzenberg, *Composition of Simplicial Complexes, Polytopes and Multigraded Betti Numbers*, arXiv:1301.4459, first posted 2013-01-18 (related combinatorial context).
