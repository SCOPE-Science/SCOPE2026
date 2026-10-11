# Sharp essential-norm dichotomy for induced free Banach-lattice operators

## Finding
For every pair of real Banach spaces \(E,F\), every bounded linear map \(T:E\to F\), and every \(1\le p\le\infty\), let
\[\mathscr F_p(T):\mathrm{FBL}^{(p)}[E]\longrightarrow\mathrm{FBL}^{(p)}[F]\]
be the canonical lattice homomorphism induced by \(T\). The distance from this map to the compact operators is
\[
\operatorname{dist}\bigl(\mathscr F_p(T),\mathcal K(\mathrm{FBL}^{(p)}[E],\mathrm{FBL}^{(p)}[F])\bigr)
=\begin{cases}0,&\operatorname{rank}T\le1,\\\|T\|,&\operatorname{rank}T\ge2.\end{cases}
\]
In the first case the induced map actually has rank at most two. In the second case, every classical approximation number of the induced map equals \(\|T\|\). In particular the inducing construction is not operator-norm continuous at any rank-one limit of rank-two maps: for \(T_\varepsilon=\operatorname{diag}(1,\varepsilon)\) and \(T_0=\operatorname{diag}(1,0)\) on real Euclidean two-space, \(\|T_\varepsilon-T_0\|=\varepsilon\), but \(\|\mathscr F_p(T_\varepsilon)-\mathscr F_p(T_0)\|\ge1\) for every \(\varepsilon>0\).

## Assumptions and scope
All spaces and operators are **real**. The two free Banach lattices are the canonical \(p\)-convex free lattices with convexity constant one, in the concrete positively homogeneous functional model of Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky. For \(1\le p<\infty\), write \(\|f\|_p\) for the supremum of
\[\left(\sum_{j=1}^{N}|f(u_j)|^p\right)^{1/p}\]
over finite families \(u_j\in E^*\) for which \(\sup_{x\in B_E}(\sum_{j=1}^N|u_j(x)|^p)^{1/p}\le1\). For \(p=\infty\), use the supremum norm of a positively homogeneous function on \(B_{E^*}\). In either case \(\|\mathscr F_p(T)\|=\|T\|\) and
\[ (\mathscr F_p(T)f)(y^*)=f(T^*y^*)\quad(y^*\in F^*). \]
The essential norm is measured against **all** compact linear operators between the corresponding Banach lattices, not just lattice homomorphisms. Approximation numbers are defined by \(a_n(A)=\inf\{\|A-R\|:\operatorname{rank}R<n\}\), for positive integers \(n\).

## Proof
**Step 1: the one-dimensional range.** If \(\operatorname{rank}T\le1\), factor \(T\) through a real space \(L\) of dimension at most one. Functoriality factors \(\mathscr F_p(T)\) through \(\mathrm{FBL}^{(p)}[L]\). For \(\dim L=1\), positive homogeneity determines each element from its values at the two points of \(S_{L^*}\), so \(\mathrm{FBL}^{(p)}[L]\) has dimension two; the zero-dimensional case is zero. Hence the induced map has finite rank at most two and essential norm zero.

**Step 2: a localized norm estimate in two dimensions.** Let \(G\) be a real two-dimensional Banach space. By the finite-dimensional functional representation of the free \(p\)-convex lattice, the restriction of \(\mathrm{FBL}^{(p)}[G]\) to \(S_{G^*}\) identifies it with \(C(S_{G^*})\) under an equivalent lattice norm. Fix \(q\in S_{G^*}\) and \(x\in S_G\) with \(q(x)=1\). For \(0<\eta<1\), choose a neighborhood \(U\) of \(q\) on which \(u(x)>1-\eta\). If \(f\ge0\) is a continuous function on \(S_{G^*}\), supported in \(U\), and \(\sup f\le1\), regard it as the positively homogeneous function on \(G^*\). Then
\[\|f\|_{\mathrm{FBL}^{(p)}[G]}\le(1-\eta)^{-1}.\]
Indeed, write each nonzero functional in an admissible test family as \(u_j=r_jv_j\), with \(r_j\ge0\) and \(v_j\in S_{G^*}\). The numerator is at most the \(\ell_p\)-norm of the \(r_j\) whose \(v_j\) lie in \(U\), while the denominator tested at \(x\) is at least \((1-\eta)\) times this norm. When \(p=\infty\), the same estimate follows immediately from the supremum norm.

**Step 3: two-dimensional noncompactness at full norm.** Let \(S:G\to F\) be a rank-two operator. Compactness of \(S_G\) supplies \(x\in S_G\) with \(\|Sx\|=\|S\|\), and Hahn–Banach gives \(y_0^*\in S_{F^*}\) with \(y_0^*(Sx)=\|S\|\). Put \(q=S^*y_0^*/\|S\|\in S_{G^*}\). Since \(S\) has rank two, choose \(z^*\in F^*\) with \(S^*z^*\) linearly independent of \(S^*y_0^*\). Choose distinct positive numbers \(t_n\downarrow0\) and set
\[y_n^*=(y_0^*+t_nz^*)/\|y_0^*+t_nz^*\|,\qquad q_n=S^*y_n^*/\|S^*y_n^*\|.\]
The points \(q_n\) are distinct, converge to \(q\), and \(\|S^*y_n^*\|\to\|S\|\). Choose pairwise disjoint open arcs around the \(q_n\), all contained in the neighborhood \(U\) of Step 2. Continuous functions \(f_n:S_{G^*}\to[0,1]\) supported in these arcs and satisfying \(f_n(q_n)=1\) exist. The finite-dimensional functional representation puts every \(f_n\) in \(\mathrm{FBL}^{(p)}[G]\); Step 2 gives \(\|f_n\|_p\le(1-\eta)^{-1}\). Since the supports are disjoint, \(f_n\to0\) pointwise, with a uniform supremum bound. Dominated convergence against every finite signed Borel measure shows weak convergence to zero in \(C(S_{G^*})\), hence also in \(\mathrm{FBL}^{(p)}[G]\) by equivalence of norms.

For every compact \(K:\mathrm{FBL}^{(p)}[G]\to\mathrm{FBL}^{(p)}[F]\), it follows that \(\|Kf_n\|\to0\). Evaluation at \(y_n^*\in S_{F^*}\), a norm-at-most-one functional on the target free lattice, gives
\[
\|\mathscr F_p(S)f_n\|\ge|f_n(S^*y_n^*)|=\|S^*y_n^*\|\longrightarrow\|S\|.
\]
Consequently \(\|\mathscr F_p(S)-K\|\ge(1-\eta)\|S\|\). Letting \(\eta\downarrow0\) proves that the essential norm of the induced rank-two map is \(\|S\|\); the reverse inequality follows from \(\|\mathscr F_p(S)\|=\|S\|\).

**Step 4: arbitrary inducing domains.** Let \(T:E\to F\) have rank at least two. For each \(\delta>0\), choose \(x\in S_E\) with \(\|Tx\|>\|T\|-\delta\), and then \(v\in E\) with \(Tv\) independent of \(Tx\). Put \(G=\operatorname{span}\{x,v\}\) and let \(i:G\hookrightarrow E\) denote the isometric inclusion. The restriction \(S=T\circ i\) has rank two and \(\|S\|>\|T\|-\delta\). For any compact \(K:\mathrm{FBL}^{(p)}[E]\to\mathrm{FBL}^{(p)}[F]\), the composition \(K\mathscr F_p(i)\) is compact, and functoriality with \(\|\mathscr F_p(i)\|=1\) yields
\[\|\mathscr F_p(T)-K\|\ge\|\mathscr F_p(S)-K\mathscr F_p(i)\|\ge\|S\|>\|T\|-\delta.\]
Let \(\delta\downarrow0\) and combine with the trivial upper bound \(\|\mathscr F_p(T)\|=\|T\|\).

**Step 5: corollaries.** All finite-rank operators are compact, so for rank at least two the preceding identity forces \(a_n(\mathscr F_p(T))=\|T\|\) for each integer \(n\ge1\). For the stated diagonal maps, \(\mathscr F_p(T_0)\) is finite rank and \(\|\mathscr F_p(T_\varepsilon)\|_{\mathrm{ess}}=1\). Distance to the compact map \(\mathscr F_p(T_0)\) is therefore at least one, despite \(\|T_\varepsilon-T_0\|=\varepsilon\).

## Verification
All estimates follow from the displayed norm definition and from evaluation at norm-one dual functionals. The authors’ later corrigendum concerns order-density over infinite-dimensional generating spaces, which is not invoked in this proof. The only structural input beyond universal functoriality is the established identification \(\mathrm{FBL}^{(p)}[G]\simeq C(S_{G^*})\) for finite-dimensional \(G\); it is specifically used to construct and weakly-nullify the disjoint localized bumps. The argument is analytic and covers arbitrary nonseparable Banach spaces. No finite computation or formal certificate is asserted.

## Relationship to prior work
The 2021 construction of free \(p\)-convex lattices by Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky supplies the norm and universal property. Oikhberg, Taylor, Tradacete and Troitsky (arXiv:2210.00614, first posted 2022-10-02; subsequent open-access journal version) establish the finite-dimensional \(C(S_{G^*})\) representation and investigate injectivity, regularity, extension and weak compactness of induced maps. These are premises, not claimed contributions. The result above concerns the previously unprovided **exact compact-approximation distance for every inducing map** and its abrupt rank transition. General exact approximation-number results for weighted composition maps on ordinary \(C(K)\) spaces do not automatically supply this equality under the non-supremum free-lattice norm when \(p<\infty\).

## Limitations
The argument concerns real free \(p\)-convex Banach lattices and canonical homomorphisms induced by linear maps. It does not classify general lattice homomorphisms, does not assert a corresponding complex result, and does not compute Bernstein, Gelfand or Kolmogorov numbers. The possibility of an equivalent statement hidden in broader composition-operator literature remains a novelty risk. Independent audit has not been performed.

## References
1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices under convexity conditions*, RACSAM 116 (2022), article 15. First online 2021-10-11. DOI: 10.1007/s13398-021-01155-8.
2. T. Oikhberg, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices*, arXiv:2210.00614 (first posted 2022-10-02); Journal of the European Mathematical Society, DOI: 10.4171/JEMS/1552, open-access journal text published online 2024-11-21.
3. D. de Hevia and P. Tradacete, *Free complex Banach lattices*, arXiv:2207.08090 (2022); Journal of Functional Analysis 284 (2023), article 109888. This is related work concerning complex, rather than real, free lattices.
4. N. J. Laustsen and P. Tradacete, *Banach lattices of positively homogeneous functions induced by a Banach space*, arXiv:2404.06497 (first posted 2024-04-09); Proceedings of the Edinburgh Mathematical Society 69 (2026), 544–580, DOI: 10.1017/S0013091525101181 (related composition-operator representation; not used for the proof).
5. T. Oikhberg, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Corrigendum to “Free Banach lattices”*, DOI: 10.4171/JEMS/1802 (2026). The corrigendum concerns the order-density claim for infinite-dimensional inducing spaces, not the finite-dimensional continuous-function representation used here.
