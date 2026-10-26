# One-switch distinguished-species dependence and its Poisson-scale boundary

## Finding

Fix integers \(r\ge2\) and \(n\ge2\), and positive relative frequencies \(t_1,\ldots,t_r\) with \(\sum_i t_i=1\). Draw \(n\) independent labels from \(r+1\) categories with probabilities
\[
\Pr(X=*)=1-s,\qquad \Pr(X=i)=s t_i\quad(1\le i\le r),\qquad 0<s<1.
\]
Let \(B\) indicate that the distinguished category \(*\) occurs at least once, and let \(K\) be the total number of distinct observed categories. Set
\[
F_{n,t}(s)=1-s^n+\sum_{i=1}^r\bigl[(1-t_i)^n-(1-s t_i)^n\bigr].
\]
There is exactly one \(\sigma_n(t)\in(0,1)\) satisfying \(F_{n,t}(\sigma_n(t))=0\), and
\[
\boxed{\operatorname{Cov}(B,K)=s^n F_{n,t}(s)}.
\]
Moreover,
\[
\operatorname{Cov}(B,K)<0\quad(0<s<\sigma_n(t)),\qquad
\operatorname{Cov}(B,K)>0\quad(\sigma_n(t)<s<1).
\]
Thus observing the distinguished category has negative covariance with overall sample richness when it is sufficiently dominant, but positive covariance when its occurrence is sufficiently rare. No second switch is possible, even for arbitrarily heterogeneous residual frequencies.

For fixed \(r,t\), let \(z_t>0\) be the unique solution of
\[
\sum_{i=1}^r e^{-z_t t_i}=1.
\]
The location of the finite-sample transition admits the two-term expansion
\[
\boxed{\sigma_n(t)=\frac{z_t}{n}-\frac{z_t^2}{2n^2}
\frac{\sum_i t_i^2e^{-z_t t_i}}{\sum_i t_i e^{-z_t t_i}}
+O_t(n^{-3}).}
\]
In particular, for \(r\) equally likely residual types, \(z_t=r\log r\).

A further dependence boundary accompanies the negative-covariance regime: whenever \(n\ge r+1\) and \(s<\sigma_n(t)\), the conditional laws \(K\mid B=1\) and \(K\mid B=0\) are *incomparable* under first-order stochastic dominance. For example, at \(r=2\), \(t_1=t_2=1/2\), and \(n=2\), the exact switch is \(\sigma_2=1/3\); for \(n=3\), it is \(\sigma_3=(\sqrt{13}-3)/2\).

## Assumptions and scope

Each sample has exactly one label, all category probabilities are strictly positive, and observations are independent with one common categorical law. Only the total mass \(s\) assigned to the \(r\) nondistinguished species varies; their normalized frequency profile \(t\) is held fixed. The integer \(n\) is the fixed sampling effort. The covariance is ordinary unconditioned covariance between the distinguished-species presence indicator and the count of distinct observed species. The asymptotic statement fixes \(r\) and the vector \(t\) while \(n\) tends to infinity.

## Proof

Put \(E_0=\{B=0\}\). Independence gives \(\Pr(E_0)=s^n\). Conditional on \(E_0\), all \(n\) labels are independent with probabilities \(t_1,\ldots,t_r\); thus
\[
\mathbb E[K\mid E_0]=\sum_{i=1}^r[1-(1-t_i)^n].
\]
Unconditionally, summing nonempty-category indicators gives
\[
\mathbb E K=1-s^n+\sum_{i=1}^r[1-(1-st_i)^n].
\]
Since \(\operatorname{Cov}(B,K)=\Pr(E_0)(\mathbb E K-\mathbb E[K\mid E_0])\), the claimed formula follows.

Differentiating the exact polynomial gives
\[
F'_{n,t}(s)=n\left[-s^{n-1}+\sum_i t_i(1-st_i)^{n-1}\right]
\]
and
\[
F''_{n,t}(s)=-n(n-1)\left[s^{n-2}+\sum_i t_i^2(1-st_i)^{n-2}\right]<0
\quad(0<s<1).
\]
Also \(F_{n,t}(1)=0\), whereas
\[
F_{n,t}(0)=1-\sum_i[1-(1-t_i)^n]<0.
\]
The strict inequality follows because the expected number of distinct categories in \(n\ge2\) observations from a nondegenerate \(r\)-category law is strictly greater than one: two different labels occur with positive probability. Finally,
\[
F'_{n,t}(1)=n\left[-1+\sum_i t_i(1-t_i)^{n-1}\right]<0,
\]
so \(F(s)>0\) for \(s<1\) sufficiently close to one. By strict concavity, the superlevel set of \(F\) is an interval; its left boundary is the unique zero \(\sigma_n(t)\) in \((0,1)\). Strict concavity also makes the signs strict on either side. Multiplication by \(s^n>0\) preserves them.

For the asymptotic location set \(x=ns\) and \(H(x)=1-\sum_i e^{-xt_i}\). On every compact positive interval, uniformly,
\[
F_{n,t}(x/n)=H(x)+\frac{x^2}{2n}\sum_i t_i^2e^{-xt_i}+O_t(n^{-2}),
\]
because \((1-xt_i/n)^n=e^{-xt_i}[1-x^2t_i^2/(2n)+O_t(n^{-2})]\), while \((x/n)^n\) and each \((1-t_i)^n\) are exponentially negligible. Since \(H(0)=1-r<0\), \(H\) strictly increases to one, and \(H'(x)=\sum_i t_i e^{-xt_i}>0\), its unique root \(z_t\) is positive. Choose fixed positive arguments bracketing \(z_t\). Uniform convergence and the strict finite-sample sign switch place \(x_n=n\sigma_n(t)\) between them, implying \(x_n\to z_t\). The displayed expansion and positive \(H'(z_t)\) then give, by a one-dimensional Taylor expansion,
\[
x_n=z_t-\frac{z_t^2}{2n}\frac{\sum_i t_i^2e^{-z_t t_i}}{\sum_i t_i e^{-z_t t_i}}+O_t(n^{-2}),
\]
which proves the stated two-term formula after division by \(n\).

For the stochastic-incomparability claim, write \(K_1\) and \(K_0\) for random variables with the conditional laws of \(K\) given \(B=1\) and \(B=0\), respectively. The covariance identity also yields
\[
\mathbb E K_1-\mathbb E K_0=\frac{\operatorname{Cov}(B,K)}{\Pr(B=1)\Pr(B=0)}<0
\]
when \(s<\sigma_n(t)\). Therefore \(K_1\) cannot stochastically dominate \(K_0\). Conversely, \(K_0\le r\) almost surely, but when \(n\ge r+1\), the probability that every category appears is strictly positive. This event entails \(B=1\) and \(K_1=r+1\); hence \(K_0\) cannot stochastically dominate \(K_1\). These two observations prove incomparability.

## Verification

The included `verify.py` independently enumerates the entire labelled sample space using exact rational probabilities for 48 cases with \(r\in\{2,3\}\), \(n\in\{2,3,4,5\}\), nonuniform and uniform residual weights, and four values of \(s\). Every enumerated covariance agrees exactly with \(s^n F_{n,t}(s)\). A full-support three-sample witness confirms that all three species can occur together in the negative-covariance regime. Additional bisection checks for three residual profiles compare \(n\sigma_n(t)\) to the predicted limiting root for \(n=100,500,2000\). The general sign theorem and two-term expansion are analytic; finite checks are not substitutes for proof.

## Relationship to prior work

Cohen, Routtenberg, and Tong (2021) study multinomial missing-mass estimation, in which unseen categories and their probabilities are fundamental; their mathematical development emphasizes mean-squared estimation risk, Fisher information and bounds rather than conditional richness under a distinguished species. The 2026 occupancy-indicator covariance analysis titled *Occupied-box indicators have a strictly positive precision matrix* supplies a general finite covariance matrix for all presence indicators. Its pairwise formula already implies the raw covariance in this note after summing one row; **the raw finite covariance is not claimed as an independent novelty**. The contribution assessed here is the global and unique sign classification along the natural one-species-vs-community concentration path, its explicit sharp two-term transition asymptotic, and the associated conditional stochastic-order obstruction. The 2026 work *A one-switch covariance law for occupancy richness and frequency counts* varies observed frequency class \(r\) under equiprobable boxes, not one species' probability under arbitrary other-species heterogeneity.

## Limitations

The sign transition assumes a fixed relative probability profile among nondistinguished categories, and is not a theorem for arbitrary paths through the full multinomial simplex. The stochastic-order statement requires at least \(r+1\) observations and is not a claim of general negative association or of a conditional likelihood-ratio order. The asymptotic remainder constant depends on the fixed positive profile \(t\); no uniformity is claimed as some \(t_i\to0\) or \(r\to\infty\). The elementary covariance formula is encompassed by known occupancy-indicator formulas. Historical priority for the specific uniqueness and asymptotic boundary remains subject to older urn references or unindexed equivalent arguments; searches do not prove uniqueness of this result in the literature.

## References

1. Shir Cohen, Tirza Routtenberg and Lang Tong, “Non-Bayesian Parametric Missing-Mass Estimation,” arXiv:2101.04329, first submitted 2021-01-12; subsequent IEEE Transactions on Signal Processing article (2022). https://arxiv.org/abs/2101.04329.
2. “Occupied-box indicators have a strictly positive precision matrix,” public mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-occupied-box-indicators-have-a-strictly-positive-precision-matri--0606274d4166 .
3. “A one-switch covariance law for occupancy richness and frequency counts,” public mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813 .
