# An abscissa law for exact essential norms of \(\ell_1\)-to-Nakano embeddings

## Finding

Let \((p_n)_{n\ge1}\) be **any** sequence of finite real exponents with \(p_n\ge1\). Its full Nakano sequence space \(Y=\ell_{(p_n)}\) consists of scalar sequences \(y=(y_n)\) such that \(\sum_n (|y_n|/\lambda)^{p_n}<\infty\) for some \(\lambda>0\), equipped with the Luxemburg norm
\[
\|y\|_Y=\inf\left\{\lambda>0:\sum_{n=1}^{\infty}(|y_n|/\lambda)^{p_n}\le1\right\}.
\]
Let \(J:\ell_1\longrightarrow Y\) be the canonical inclusion. Define the (possibly infinite) exponent-series abscissa
\[
s_* = \inf\left\{t>0:\sum_{n=1}^{\infty}e^{-tp_n}<\infty\right\}\in[0,\infty],
\qquad r_* =\frac{1}{1+e^{-s_*}},
\]
where the infimum of the empty set is \(\infty\) and \(e^{-\infty}=0\). Write \(\|J\|_{\mathrm{ess}}=\inf_{K\text{ compact}}\|J-K\|\), and \(a_k(J)=\inf_{\operatorname{rank}F<k}\|J-F\|\). With \(B_{\ell_1}\) the closed unit ball, the Hausdorff measure of noncompactness of a bounded subset \(B\subset Y\) is \(\chi(B)=\inf\{\rho>0:B\text{ is covered by finitely many open }Y\text{-balls of radius }\rho\}\).

**Theorem.** For real or complex scalars and all such exponent sequences,
\[
\boxed{\quad\|J\|=1,\qquad\|J\|_{\mathrm{ess}}=\lim_{k\to\infty}a_k(J)=\chi\bigl(J(B_{\ell_1})\bigr)=r_*\quad}.
\]
The inclusion is therefore never compact. If the exponents are nondecreasing, its abscissa has the elementary expression
\[
\boxed{\quad s_*=\limsup_{n\to\infty}\frac{\log n}{p_n}\quad}.
\]
For the natural logarithmic family \(p_n\sim\gamma\log n\) with \(\gamma>0\), the common essential quantity is exactly \((1+e^{-1/\gamma})^{-1}\). The values range continuously from \(1\) to \(1/2\) as \(\gamma\) increases from zero toward infinity; the infimum \(1/2\) is actually attained by exponent sequences that grow faster than \(\log n\).

## Assumptions and scope

The exponents are finite at every coordinate but may oscillate, remain bounded, or diverge. \(Y\) is the **full** Luxemburg space, not the closure of finitely supported sequences (the Nakano heart). An infinite sum that converges at some scale is allowed even when it diverges at smaller scales. Essential norms and approximation numbers concern bounded linear maps \(\ell_1\to Y\). No monotonicity is required for the main equality; monotonicity is required only for the displayed limsup formula. The measure \(\chi\) uses finite covers by arbitrary centers in \(Y\), not centers restricted to the image of the unit ball.

## Proof

**1. Elementary operator facts.** The inclusion is contractive: whenever \(\sum_n|x_n|\le1\), each \(|x_n|\le1\), and hence \(\sum_n|x_n|^{p_n}\le\sum_n|x_n|\le1\). Since \(\|e_n\|_Y=\|e_n\|_{\ell_1}=1\), we have \(\|J\|=1\). For any bounded \(T:\ell_1\to Y\), the canonical-basis expansion gives
\[
\|T\|=\sup_{n\ge1}\|Te_n\|_Y.
\]

**2. The series threshold on subsets.** For every subset \(S\subset\mathbb N\) (including finite subsets and the empty set), put
\[
s(S)=\inf\{t>0:\sum_{n\in S}e^{-tp_n}<\infty\},\qquad A(S)=e^{s(S)},
\]
allowing \(A(S)=\infty\). For a finite partition \(\mathbb N=S_1\sqcup\cdots\sqcup S_m\), convergence of the positive series over the union is equivalent to convergence over each part. Thus
\[
s_* =\max_j s(S_j),\qquad A:=e^{s_*}=\max_j A(S_j).
\]
Finite deletions do not affect \(s(S)\). For nonempty \(S\), if \(A(S)<\infty\), the indicator \(\mathbf1_S\) belongs to \(Y\) and \(\|\mathbf1_S\|_Y\ge A(S)\): every scale \(\lambda<A(S)\) has divergent modular, whereas some larger scale has finite modular and can be enlarged further to make it at most one. If \(A(S)=\infty\), \(\mathbf1_S\notin Y\). More generally, no \(y\in Y\) can satisfy \(|y_n|\ge c>0\) on such an \(S\). Indeed, this would imply \(\sum_{n\in S}(c/\lambda)^{p_n}<\infty\) at a sufficiently large scale \(\lambda\).

**3. Sharp lower bound for every finite cover.** Suppose \(\{e_n:n\ge1\}\) admits a finite cover by balls \(B_Y(y_j,b)\), \(1\le j\le m\), with \(b<1\). Assign each \(n\) to one center within distance \(b\), obtaining a finite partition \(S_1,\ldots,S_m\). For every \(n\in S_j\), coordinate evaluation and \(\|e_n-y_j\|_Y<b\) imply \(|(y_j)_n|>1-b\). Some **infinite** part \(S_j\) has \(A(S_j)=A\): finite parts have abscissa zero, and at least one part is infinite. If \(A=\infty\), the preceding paragraph contradicts \(y_j\in Y\). If \(A<\infty\), choose \(n\in S_j\), restrict the error \(e_n-y_j\) to \(S_j\setminus\{n\}\), and use monotonicity of the Luxemburg norm to obtain
\[
b>\|e_n-y_j\|_Y\ge (1-b)\|\mathbf1_{S_j\setminus\{n\}}\|_Y\ge (1-b)A.
\]
Consequently any radius allowing a finite cover obeys \(b\ge A/(1+A)\) (or \(b\ge1\) if \(A=\infty\)). In particular,
\[
\chi\bigl(J(B_{\ell_1})\bigr)\ge r_*.
\]
For a compact \(K:\ell_1\to Y\), the set \(\{Ke_n:n\ge1\}\) is relatively compact. Finite covering of this set to arbitrary accuracy shows that \(\{e_n\}\) admits finite covers of radii arbitrarily close to \(\|J-K\|\). Hence \(\|J-K\|\ge r_*\), proving \(\|J\|_{\mathrm{ess}}\ge r_*\).

**4. Finite-rank upper bound.** If \(A=\infty\), the zero operator already yields \(\|J\|_{\mathrm{ess}}\le1=r_*\). Suppose \(A<\infty\). Then necessarily \(p_n\to\infty\): otherwise infinitely many exponents would be bounded by some finite constant, and no positive exponential parameter could make the series converge. Put \(c=1/(1+A)\), \(r=A/(1+A)\), and fix \(\lambda>r\). Since \(\lambda>cA\), the series \(\sum_n(c/\lambda)^{p_n}\) converges. Since \(\lambda>r=1-c\) and \(p_n\to\infty\), also \(\sup_{n>N}((1-c)/\lambda)^{p_n}\to0\). Choose \(N\) so that
\[
\sum_{j>N}(c/\lambda)^{p_j}
+\sup_{n>N}((1-c)/\lambda)^{p_n}\le1.
\]
The vector \(\mathbf1_{\{j>N\}}\) belongs to \(Y\) by finite threshold. Define a finite-rank operator
\[
K_Nx=\sum_{j\le N}x_je_j+c\left(\sum_{j>N}x_j\right)\mathbf1_{\{j>N\}}.
\]
For \(n\le N\), \((J-K_N)e_n=0\). For \(n>N\), the error has value \(1-c\) at coordinate \(n\), value \(-c\) at other tail coordinates, and zero on the head. Its modular at scale \(\lambda\) is bounded by the preceding displayed sum, so \(\|(J-K_N)e_n\|_Y\le\lambda\). The \(\ell_1\) basis norm formula now yields \(\|J-K_N\|\le\lambda\). Letting \(\lambda\downarrow r\) proves \(\|J\|_{\mathrm{ess}}\le r\) with finite-rank approximants. Since every finite-rank map is compact and the ranks of \(K_N\) are finite, it also proves \(\lim_k a_k(J)=r\). The compact set \(\overline{K_N(B_{\ell_1})}\) admits arbitrarily fine finite nets; using \(\|J-K_N\|\le\lambda\) gives \(\chi(J(B_{\ell_1}))\le\lambda\), hence equality with \(r\).

**5. Monotone exponents.** Suppose \(p_n\) is nondecreasing, and set \(\sigma=\limsup_{n\to\infty}(\log n)/p_n\). If \(t>\sigma\), choose \(\sigma<q<t\). Eventually \(p_n\ge (\log n)/q\), so \(e^{-tp_n}\le n^{-t/q}\), a summable series. Conversely, if \(0<t<\sigma\), choose \(t<q<\sigma\). For arbitrarily large \(N\), \(p_N<(\log N)/q\), and monotonicity gives
\[
\sum_{n=1}^{N}e^{-tp_n}\ge N e^{-tp_N}\ge N^{1-t/q}\longrightarrow\infty
\]
along these indices. Thus the series diverges for every \(t<\sigma\), proving \(s_*=\sigma\), including \(\sigma=0\) and \(\sigma=\infty\). The stated logarithmic formula follows by substitution.

## Verification

The proof establishes all infinite-dimensional bounds analytically, using only modular comparisons, finite partitions, compactness of images of bounded sets, and explicit finite-rank maps. The critical infimum at \(s_*\) need not be attained by the series: no boundary convergence assumption was used. The two endpoint cases \(s_*=0\) and \(s_*=\infty\) are included, as are oscillatory and bounded exponent sequences. For a direct reproduction, compute the convergence abscissa of \(\sum e^{-tp_n}\), then evaluate \((1+e^{-s_*})^{-1}\); for monotone exponents replace the abscissa with the displayed limsup.

## Relationship to prior work

Vuillermot (2026) treats continuous and compact embeddings of modular sequence spaces, including bounded-exponent Nakano instances and related compactness criteria, but does not state the precise noncompact essential-norm law above for full unbounded-exponent Nakano targets. Sanchiz (2025) establishes qualitative noncompactness of Nakano inclusions and strict-singularity criteria, not their exact distances to compact maps or finite-cover radii. Kiwerski and Tomaszewski (2022) give general essential-norm formulas for multipliers between Köthe sequence spaces under the hypothesis that the source is reflexive or the target is order-continuous. Neither hypothesis holds here in the genuinely unbounded-exponent case: \(\ell_1\) is not reflexive, while a sparse subsequence of unbounded exponents supports an indicator with nonvanishing tail norm in the full target. Their theorem consequently does not directly imply this quantitative law. These comparisons do not establish absolute historical priority beyond inspected sources.

## Limitations

The formula concerns the **canonical** inclusion with unit coefficient sequence, the full Luxemburg convention, and finite exponents \(p_n\ge1\). It does not classify all nonconstant diagonal multipliers or other modulars. The logarithmic limsup requires a nondecreasing exponent sequence, although the abscissa formula does not. No assertion about attaining the essential-distance infimum by a single finite-rank operator is made. Priority risk persists from older general theory of measures of noncompactness or full nonseparable sequence-space inclusions expressed in different terminology. Independent publication-priority and mathematical audit have not been performed.

## References

1. P.-A. Vuillermot, *Continuous and compact embeddings for a class of modular sequence spaces*, arXiv:2610.19745v1 (first public 2026-10-14), https://arxiv.org/html/2610.19745v1.
2. M. Sanchiz, *A note on the strict sigularity of the inclusion between Nakano sequence spaces*, arXiv:2512.16633v1 (2025), https://arxiv.org/html/2512.16633v1.
3. T. Kiwerski and J. Tomaszewski, *Essential norms of pointwise multipliers acting between Köthe spaces: The non-algebraic case*, arXiv:2212.06723 (2022), https://arxiv.org/abs/2212.06723.
