# A lacunarity dichotomy for pointwise Lipschitz norm attainment on convergent sequences

## Finding
Let \(t_1>t_2>\cdots>0\) satisfy \(t_n\to0\), and give \(M=\{0\}\cup\{t_n:n\ge1\}\subset\mathbb R\) the Euclidean metric. For a real Banach space \(Y\), write \(\operatorname{Lip}_0(M,Y)\) for the maps \(f:M\to Y\) with \(f(0)=0\), equipped with their Lipschitz norm. Say that \(f\) attains its *pointwise Lipschitz norm* if some \(p\in M\) satisfies
\[
\sup_{q\in M\setminus\{p\}}\frac{\|f(q)-f(p)\|}{|q-p|}=\|f\|_{\mathrm{Lip}}.
\]
Denote this subset by \(\operatorname{PNA}(M,Y)\).

**Theorem (complete lacunarity/spaceability dichotomy).** The following are equivalent:

1. \(\displaystyle\lim_{n\to\infty}t_{n+1}/t_n=0\).
2. \(\operatorname{PNA}(M,\mathbb R)=\operatorname{Lip}_0(M,\mathbb R)\).
3. \(\operatorname{PNA}(M,Y)=\operatorname{Lip}_0(M,Y)\) for every nonzero real Banach space \(Y\).

If condition 1 fails, then for *every* nonzero real Banach space \(Y\), there is a linear isometric embedding
\[
T:\ell_\infty(\mathbb N;\mathbb R)\longrightarrow\operatorname{Lip}_0(M,Y)
\]
whose nonzero images do not attain their pointwise Lipschitz norms. If \(0<\delta<\limsup_n t_{n+1}/t_n\), the embedding can moreover be chosen to satisfy
\[
\sup_{n\ge1}\frac{\|T(a)(t_n)\|}{t_n}
\le\left(1-\frac\delta2\right)\|a\|_\infty
\qquad(a\in\ell_\infty).
\]
Consequently the complement of pointwise norm attainment contains an isometric *closed* copy of \(\ell_\infty\), together with zero, exactly on the nonsuperlacunary side of the dichotomy.

## Assumptions and scope
The sequence is strictly decreasing, positive, and converges to zero; no regularity or monotonicity of its adjacent ratios is assumed. Targets are arbitrary nonzero *real* Banach spaces. Zero maps are regarded as pointwise norm attaining. The theorem is a statement about pointwise attainment, not merely strong attainment at a fixed pair of points. It concerns this specific one-accumulation-point class of compact metric spaces, not all compact metrics.

## Proof
**Step 1: exact adjacent-slope model.** Set \(\Delta_n=t_n-t_{n+1}>0\). For any bounded sequence \(s=(s_n)_{n\ge1}\) in \(Y\), define
\[
f_s(0)=0,\qquad f_s(t_n)=\sum_{j=n}^\infty\Delta_j s_j.
\]
The series converges absolutely since \(\sum_{j=n}^\infty\Delta_j=t_n\), and
\[
\frac{f_s(t_n)-f_s(t_{n+1})}{\Delta_n}=s_n.
\]
Every slope between distinct points of \(M\) is a positive weighted average of consecutive \(s_j\)'s, over a finite interval or a tail. Hence
\[
\|f_s\|_{\mathrm{Lip}}=\sup_{n\ge1}\|s_n\|.
\]
Conversely, for any \(f\in\operatorname{Lip}_0(M,Y)\), its consecutive slopes \(s_n=(f(t_n)-f(t_{n+1}))/\Delta_n\) are bounded; telescoping and \(f(t_n)\to f(0)=0\) recover the displayed series. Thus the adjacent-slope model is exact and onto.

**Step 2: sufficiency.** Suppose \(t_{n+1}/t_n\to0\) and \(f=f_s\ne0\); set \(S=\|f\|_{\mathrm{Lip}}=\sup_n\|s_n\|\). If some \(\|s_n\|=S\), the adjacent pair \((t_n,t_{n+1})\) strongly attains the norm. Otherwise, take indices \(n_k\to\infty\) with \(\|s_{n_k}\|\to S\). Since
\[
\frac{f(t_n)}{t_n}
=\left(1-\frac{t_{n+1}}{t_n}\right)s_n
+\frac{t_{n+1}}{t_n}\frac{f(t_{n+1})}{t_{n+1}},
\]
and \(\|f(t_{n+1})/t_{n+1}\|\le S\), it follows that
\[
\left\|\frac{f(t_{n_k})}{t_{n_k}}-s_{n_k}\right\|
\le 2S\frac{t_{n_k+1}}{t_{n_k}}\to0.
\]
Thus \(\sup_n\|f(t_n)\|/t_n=S\), so the fixed point \(p=0\) witnesses pointwise norm attainment. This works for every real Banach target.

**Step 3: nonsuperlacunarity produces an isometric \(\ell_\infty\) of nonattainers.** Assume \(\limsup_n t_{n+1}/t_n>0\), and choose \(0<\delta\) strictly below this limsup. Inductively select increasing integers \(n_k\) so that
\[
\frac{t_{n_k+1}}{t_{n_k}}\ge\delta,
\qquad n_{k+1}\ge n_k+2,
\qquad t_{n_{k+1}}\le\frac\delta2 t_{n_k}.
\]
The infinitely many indices with ratio at least \(\delta\) allow this thinning, because \(t_n\to0\). Choose a mapping \(\psi:\mathbb N\to\mathbb N\) in which each positive integer occurs infinitely often (for instance the successive rows \(1;1,2;1,2,3;\ldots\)). Fix a unit vector \(y_0\in Y\). For \(a=(a_j)\in\ell_\infty(\mathbb N;\mathbb R)\), define the slope sequence
\[
s_{n_k}(a)=\left(1-\frac1{k+1}\right)a_{\psi(k)}y_0,
\qquad s_n(a)=0\quad(n\notin\{n_k:k\ge1\}),
\]
and set \(T(a)=f_{s(a)}\). The map is linear. Every coordinate \(a_j\) reappears with attenuation tending to one, so
\[
\|T(a)\|_{\mathrm{Lip}}
=\sup_k\left(1-\frac1{k+1}\right)|a_{\psi(k)}|
=\|a\|_\infty.
\]
Thus \(T\) is an isometric embedding and its range is closed.

For each \(n\), let \(k\) be the least integer with \(n_k\ge n\). Positivity of the \(\Delta_j\)'s, disjointness of the selected intervals and the thinning conditions give
\[
\begin{aligned}
\|T(a)(t_n)\|
&\le\|a\|_\infty\sum_{\ell\ge k}\Delta_{n_\ell}\\
&\le\|a\|_\infty\bigl(t_{n_k}-t_{n_k+1}+t_{n_{k+1}}\bigr)\\
&\le\left(1-\frac\delta2\right)\|a\|_\infty t_{n_k}\\
&\le\left(1-\frac\delta2\right)\|a\|_\infty t_n.
\end{aligned}
\]
This proves the quantitative base-point bound and excludes \(p=0\) as a pointwise norming point whenever \(a\ne0\).

Now fix an isolated point \(p=t_m\). For \(a\ne0\), every individual consecutive slope satisfies \(\|s_j(a)\|<\|a\|_\infty\). Each slope between \(t_m\) and another nonzero \(t_j\) is a *finite* positive weighted average of consecutive slopes, so its norm is strictly less than \(\|a\|_\infty\). As \(j\to\infty\), those slopes converge to \(\|T(a)(t_m)\|/t_m\) in norm (before taking norms, the quotient converges to \(T(a)(t_m)/t_m\)), which the displayed quantitative bound puts strictly below \(\|a\|_\infty\). A convergent sequence of numbers each below \(\|a\|_\infty\), with limit below it, has supremum below it; the finitely many remaining points cause no exception. The slope to \(0\) is likewise strictly below the norm. Therefore no \(t_m\) pointwise norms \(T(a)\). All nonzero members of the closed isometric copy fail pointwise norm attainment.

This proves the contraposition of 2 implying 1, and at the same time the stronger counterexamples for every target. The implications among 1–3 are immediate from Step 2, scalar targets, and Step 3. \(\square\)

## Verification
The analytic proof gives exact expressions and inequalities for arbitrary, not only finite, sequences. Key independently checkable identities are the telescoping equality \(\sum_{j=n}^\infty\Delta_j=t_n\), the norm isometry from adjacent slopes, and the sparse-support estimate \(\sum_{\ell\ge k}\Delta_{n_\ell}\le\Delta_{n_k}+t_{n_{k+1}}\). They require no numerical approximation. Illustrative boundary models are \(t_n=2^{-n^2}\), whose adjacent ratios tend to zero, and \(t_n=2^{-n}\), whose ratios equal \(1/2\). A finite rational-arithmetic sanity test on a truncation of the latter confirmed the predicted strict base-point and isolated-point inequalities; such a truncation is not evidence for the infinite-dimensional part of the proof.

## Relationship to prior work
Choi, Jung, Lee and Roldán introduced pointwise norm attainment and exhibited the particular compact subset \(\{0\}\cup\{2^{-n^2}:n\ge1\}\) on which every scalar Lipschitz function pointwise norms (their Proposition 2.7 in the 2023 preprint). The present theorem supplies a necessary-and-sufficient criterion for *every* decreasing sequence converging to zero, covers arbitrary nonzero Banach targets, and provides a closed isometric \(\ell_\infty\) subspace of the nonattainers when the criterion fails.

Their subsequent 2024 preprint establishes a universal large subspace of Lipschitz functions failing *strong* norm attainment, and constructs functions failing pointwise attainment on the entire real line. Neither statement yields the present dichotomy: a function can fail strong attainment while attaining its pointwise norm, and restricting a Lipschitz function to a compact sequence can change its norm-attainment behavior. Earlier large-subspace results for strong attainment likewise do not imply the pointwise classification.

## Limitations
Only one-accumulation-point compact subsets of a real ray, with the inherited distance and strictly decreasing enumeration, are classified. This finding does not classify arbitrary compact subsets of \(\mathbb R\), trees with branching, or general metric spaces. The boundedness of the constructed slope sequences does not by itself prove their failure of pointwise attainment; the base-point gap and the isolated-point limit argument are essential. No claim of completeness of external literature indexing or independent validation is made.

## References
1. G. Choi, M. Jung, H. J. Lee and Ó. Roldán, *Embeddings of infinite-dimensional spaces in the sets of norm-attaining Lipschitz functions*, arXiv:2312.00393v1 (first public version, 2023-12-01), especially Definition 2.1 and Propositions 2.7–2.8. Journal version: *On the spaceability of the sets of norm-attaining Lipschitz functions*, Mathematische Nachrichten 298 (2025), 3686–3713, doi:10.1002/mana.70055.
2. G. Choi, M. Jung, H. J. Lee and Ó. Roldán, *Linear structures of norm-attaining Lipschitz functions and their complements*, arXiv:2404.07599v1 (2024-04-11), especially Theorem 2.2 and Propositions 4.2–4.5; Nonlinear Analysis 267 (2026), 114063.
3. *Infinite dimensional spaces in the set of strongly norm-attaining Lipschitz maps*, arXiv:2204.12529v1 (2022), Sections 2–3 (background on strong, not pointwise, attainment).
