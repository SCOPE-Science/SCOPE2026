# A stochastic valley and a sharp nonlinear dependence scale for leaves of uniform labeled trees

## Finding

For each integer \(n\ge4\), choose a tree uniformly from the \(n^{n-2}\) labeled trees on \([n]=\{1,\ldots,n\}\). Let \(D_n\) be the degree of vertex \(1\), and \(L_n\) the total number of leaves (vertices of degree one). Put \(m=n-2\), \(q=n-1\), \(r=(n-2)/(n-1)\), and \(K_n=D_n-1\in\{0,\ldots,m\}\).

If \(E_{q,t}\) denotes the number of empty boxes after \(t\) independent uniform placements in \(q\) boxes, then the following **complete finite conditional law** holds:
\[
 L_n\mid (K_n=k)\ \overset{\mathrm d}=\ E_{q,m-k}+\mathbf1_{\{k=0\}},\qquad 0\le k\le m.
\]
In particular,
\[
 g_n(k):=\mathbb E[L_n\mid K_n=k]
 = \mathbf1_{\{k=0\}}+q r^{m-k}.
\]
The conditional distributions have a **unique stochastic valley at degree two**, in the following precise strict first-order sense:
\[
 L_n\mid(D_n=1)\ >_{\mathrm{st}}\ L_n\mid(D_n=2),
\]
\[
 L_n\mid(D_n=d+1)\ >_{\mathrm{st}}\ L_n\mid(D_n=d)
 \quad\text{for every }2\le d\le n-2.
\]
Here strict stochastic dominance means dominance for every increasing test function for which expectations exist and a strict inequality for at least one threshold, equivalently non-strict inequalities of all upper tails with at least one strict upper tail. No total ordering is claimed between the degree-one law and every higher-degree law.

The linear covariance vanishes exactly, although there is nonlinear dependence:
\[
 \operatorname{Cov}(D_n,L_n)=0,
 \qquad
 \eta_n^2:=\frac{\operatorname{Var}(\mathbb E[L_n\mid D_n])}
 {\operatorname{Var}(L_n)}>0.
\]
The **sharp asymptotic nonlinear dependence scale** is
\[
 \boxed{\lim_{n\to\infty} n\eta_n^2=1.}
\]
Thus a vertex degree has zero linear predictive covariance with the global leaf count, but the best degree-based nonlinear conditional-mean predictor explains asymptotically exactly a fraction \(1/n\) of the leaf-count variance.

## Assumptions and scope

All trees are unrooted, simple, uniformly selected labeled Cayley trees; vertex \(1\) is a marked vertex, not a recursive-tree root. Degrees are ordinary graph degrees. The random variables are defined for \(n\ge4\); variance normalization is positive in this range. The probability model is exactly uniform over the \(n^{n-2}\) Prüfer sequences. There are no random edge weights, asymptotic conditioning hypotheses, or nonuniform labels. The quantity \(\eta_n^2\) is the conventional correlation ratio, not Pearson correlation squared.

For an explicit finite probability mass function, with \(S(t,j)\) a Stirling number of the second kind, for integers \(0\le e\le q\),
\[
 \Pr(E_{q,t}=e)=\frac{\binom qe(q-e)!\,S(t,q-e)}{q^t},
\]
where \(S(0,0)=1\), \(S(t,j)=0\) when \(j>t\), and \(0^0=1\) in the usual empty-placement convention.

## Proof

**Step 1: The conditional law.** The Prüfer bijection represents a uniform labeled tree by \(m=n-2\) iid uniform letters in \([n]\); the degree of vertex \(i\) equals one plus the number of occurrences of \(i\). Consequently \(K_n\sim\operatorname{Bin}(m,1/n)\). Conditional on \(K_n=k\), the remaining \(m-k\) letters, in their relative order, are independent and uniform on the other \(q=n-1\) labels. All these other vertices are leaves precisely when their boxes are empty; the marked vertex is additionally a leaf precisely when \(k=0\). This proves the displayed conditional distribution and its mass function. Each of the \(q\) unmarked boxes remains empty with probability \(r^{m-k}\), proving the regression formula.

**Step 2: Strict stochastic valley.** Couple the empty-box processes \(E_{q,t}\) simultaneously by adding a uniformly distributed ball at each step. Then \(E_{q,t+1}\le E_{q,t}\) almost surely, with strict inequality with positive probability whenever an empty box can still receive the ball. The conditional laws for \(k\ge1\) compare successive \(t=m-k\), so \(E_{q,m-k-1}\ge E_{q,m-k}\), strictly in distribution for all \(1\le k<m\), as \(m-k\le q-1\). The first comparison is different: \(L_n\mid(K_n=0)\overset{\mathrm d}=1+E_{q,m}\) and \(L_n\mid(K_n=1)\overset{\mathrm d}=E_{q,m-1}\). By adding one ball to \(E_{q,m-1}\), at most one box ceases to be empty. Thus \(1+E_{q,m}\ge E_{q,m-1}\) pointwise under this coupling. The inequality is strict with positive probability because for \(n\ge4\) the newly placed ball can land in an already occupied box. The conditional means satisfy the explicit inequalities
\[
 g_n(0)-g_n(1)=1-r^{m-1}>0,
 \qquad g_n(k+1)-g_n(k)=r^{m-k-1}>0\quad (1\le k<m).
\]
This proves every claimed stochastic ordering and the unique minimum.

**Step 3: Zero covariance without independence.** Label exchangeability gives \(\operatorname{Cov}(D_i,L_n)\) equal for each \(i\). But the sum of the degrees is the deterministic \(2(n-1)\). Summing covariances therefore proves \(\operatorname{Cov}(D_n,L_n)=0\). On the other hand \(g_n(0)\ne g_n(1)\) and both events have positive probability, proving dependence and \(\eta_n^2>0\).

**Step 4: Sharp correlation-ratio asymptotic.** Write \(K=K_n\) and \(h_n(K)=g_n(K)-g_n(0)\). From the regression formula,
\[
 h_n(K)= q r^m(r^{-K}-1)-\mathbf1_{\{K\ge1\}}.
\]
As \(n\to\infty\), \(K_n\Rightarrow P\), where \(P\sim\operatorname{Pois}(1)\). For every fixed integer \(k\ge0\), \(q r^m(r^{-k}-1)\to k/e\). Moreover, since \(q(1-r)=1\),
\[
 0\le q r^m(r^{-k}-1)
 =\sum_{j=0}^{k-1}r^{m-j-1}\le k\quad(0\le k\le m).
\]
All fourth moments of \(K_n\) are uniformly bounded (each of its factorial moments of fixed order at most one). It follows by truncation and uniform integrability that the first two moments of \(h_n(K_n)\) converge to those of \(h(P)=P/e-\mathbf1_{\{P\ge1\}}\). A direct Poisson moment calculation gives
\[
 \lim_{n\to\infty}\operatorname{Var}(g_n(K_n))
 =\operatorname{Var}(h(P))=e^{-1}-2e^{-2}=\frac{e-2}{e^2}>0.
\]

For the denominator, let \(p_n=(1-1/n)^{n-2}\) and \(p_{2,n}=(1-2/n)^{n-2}\). Empty-box indicators in the unconditioned Prüfer code give the **exact** variance
\[
 \operatorname{Var}(L_n)=n p_n(1-p_n)+n(n-1)(p_{2,n}-p_n^2).
\]
Since \(p_n\to e^{-1}\), \(p_{2,n}\to e^{-2}\), and \(n(p_{2,n}-p_n^2)\to-e^{-2}\),
\[
 \lim_{n\to\infty}\frac{\operatorname{Var}(L_n)}{n}
 =e^{-1}-2e^{-2}=\frac{e-2}{e^2}.
\]
The ratio of these two nonzero limits yields \(n\eta_n^2\to1\) without a claim of any central limit theorem. This finishes the proof.

## Verification

The included Python 3 program `verify.py` independently enumerates all Prüfer words for \(4\le n\le8\), comparing the exact full conditional distribution for every attainable marked degree with the Stirling-number occupancy expression. Separately, for \(4\le n<20\), it verifies rational normalization, conditional means, every stated finite stochastic upper-tail comparison, strictness, zero covariance, and the positivity of the nonlinear correlation ratio. A successful invocation prints **2842 exact assertions passed**. These are finite checks, not a substitute for the coupling and uniform-integrability proofs. Large-\(n\) floating-point outputs are illustrative only.

## Relationship to prior work

The Prüfer correspondence, Cayley's enumeration, occupancy counting by Stirling numbers, and ordinary degree distributions of labeled trees are classical. Ekhad and Zeilberger, *Automated Counting and Statistical Analysis of Labeled Trees with Degree Restrictions* (arXiv:2201.07326, first publicly posted 2022-01-18), give a general degree-restricted enumerator, exact moments of counts of specified vertex degrees, and asymptotic degree-count covariance/normality. In particular, they cover the baseline global leaf-count variance scale used in Step 4, and their general enumeration can be specialized to marked-degree/leaf-count counts; this paper does **not** claim those enumerations as intrinsically new. What is isolated here is the strict conditional first-order stochastic valley, despite exact zero degree–leaf covariance, together with the sharp \(1/n\) nonlinear explained-variance scale.

Olsson, *The Probability of Random Trees Being Isomorphic* (arXiv:2205.06625), treats different conditioned tree-count questions and does not state this marked-degree/total-leaves stochastic valley. Related analyses for *random recursive trees*, where attachment times constrain labels, concern a different distribution and are not interchangeable with the uniform Cayley model.

## Limitations

The stochastic comparisons do not assert a total order between the degree-one conditional law and every higher degree. The nonlinear scale pertains to the conditional-mean predictor from a **single marked degree**; it does not quantify prediction from an entire degree profile. Historical priority is not independently certified: an earlier equivalent result could appear as a specialization of a multivariate occupancy identity or an unstated consequence of a broad degree-count generating function. The finite checks are not a substitute for the infinite mathematical proof.

## References

1. S. B. Ekhad and D. Zeilberger, *Automated Counting and Statistical Analysis of Labeled Trees with Degree Restrictions*, arXiv:2201.07326, first posted 2022-01-18, https://arxiv.org/abs/2201.07326 .
2. T. Olsson, *The Probability of Random Trees Being Isomorphic*, arXiv:2205.06625, first posted 2022-05-13, https://arxiv.org/abs/2205.06625 .
3. H. Prüfer, *Neuer Beweis eines Satzes über Permutationen*, 1918 (classical Prüfer coding).
