# Sharp singleton–collision covariance reversals in finite occupancy sampling

## Finding

Let \(X_1,\ldots,X_n\), \(n\ge2\), be independent samples from \(m\ge2\) categories with probabilities \(p_1,\ldots,p_m>0\) summing to one. Put \(N_a=\sum_{j=1}^n\mathbf1\{X_j=a\}\), and define the number of singleton categories and the number of matching unordered sample pairs by
\[
S_n=\sum_{a=1}^m\mathbf1\{N_a=1\},\qquad
Q_n=\sum_{1\le i<j\le n}\mathbf1\{X_i=X_j\}=\sum_{a=1}^m\binom{N_a}{2}.
\]
Write \(s_2=\sum_a p_a^2\). For every \(n\ge3\), their covariance is
\[
\boxed{\operatorname{Cov}(S_n,Q_n)=\binom n2\sum_{a=1}^m p_a(1-p_a)^{n-3}\left[(n-2)(s_2-p_a^2)-n s_2(1-p_a)^2\right].}
\tag{1}
\]
For \(n=2\), it is \(-2s_2(1-s_2)<0\).

If all categories are equally likely, (1) reduces to the **exact sign-reversal law**
\[
\boxed{\operatorname{Cov}(S_n,Q_n)=\binom n2\frac{(m-1)(n-2m)}{m^3}\left(1-\frac1m\right)^{n-3}\quad(n\ge3).}
\tag{2}
\]
Thus, over all integers \(m\ge2,n\ge2\), the covariance is strictly negative for \(n<2m\), exactly zero for \(n=2m\), and strictly positive for \(n>2m\). In particular the zero locus is attained at every alphabet size, and \(\operatorname{Cov}(S_5,Q_5)=5/16\) for \(m=2\).

For an arbitrary **two-category law** \((p,1-p)\), with \(0<p<1\) and \(n\ge3\), the entire probability-dependent sign diagram is
\[
\boxed{\operatorname{Cov}(S_n,Q_n)=n(n-1)\left[p(1-p)^{n-1}+(1-p)p^{n-1}\right]\left[np(1-p)-1\right].}
\tag{3}
\]
For \(n=3\) it is negative for every \(p\). For \(n=4\) it is zero only at \(p=1/2\), otherwise negative. For every \(n\ge5\), define
\[
p_-(n)=\frac{1-\sqrt{1-4/n}}2,\qquad p_+(n)=\frac{1+\sqrt{1-4/n}}2.
\]
Then the covariance is positive exactly for \(p_-(n)<p<p_+(n)\), zero at these two endpoints, and negative elsewhere in \((0,1)\). The \(n=2\) covariance is always negative.

Equivalently, the covariance of the Good–Turing singleton fraction \(S_n/n\) and the unbiased Simpson concentration estimator \(Q_n/\binom n2\) has the identical sign, since both normalizing constants are positive.

## Assumptions and scope

The sampling law has finite support and strictly positive category probabilities. There is no Poissonization and no asymptotic approximation. The matching-pair statistic counts unordered index pairs, including multiple pairs from a category with occupancy at least three. The singleton fraction estimates missing mass in the familiar Good–Turing form; pair matches estimate the quadratic concentration functional \(s_2\). All covariance statements are unconditional under the true sampling law.

The general nonuniform formula is exact but does not impose a universal sign. The classification for arbitrary category probabilities is asserted only for two categories; equation (2) applies to every number of equally likely categories.

## Proof

Let \(Y=\mathbf1\{X_1=X_2\}\) and \(I_a=\mathbf1\{N_a=1\}\). Pair exchangeability gives
\[
\operatorname{Cov}(S_n,Q_n)=\binom n2\sum_{a=1}^m\operatorname{Cov}(I_a,Y).
\tag{4}
\]
For \(n\ge3\), the singleton event \(I_a=1\) and the collision event \(Y=1\) can occur together only when \(X_1=X_2\ne a\) and category \(a\) appears exactly once among the remaining \(n-2\) observations. Independence therefore gives
\[
\mathbb E[I_aY]=(s_2-p_a^2)(n-2)p_a(1-p_a)^{n-3}.
\tag{5}
\]
On the other hand, \(\mathbb E I_a=np_a(1-p_a)^{n-1}\), while \(\mathbb EY=s_2\). Subtracting their product from (5), and summing over \(a\), proves (1).

For \(n=2\), \(Q_2=Y\) and \(S_2=2(1-Y)\). Hence \(\operatorname{Cov}(S_2,Q_2)=-2\operatorname{Var}(Y)=-2s_2(1-s_2)\), strictly negative since \(0<s_2<1\).

For the uniform law substitute \(p_a=1/m\) and \(s_2=1/m\) into (1). Its bracket becomes
\[
(n-2)\frac{m-1}{m^2}-n\frac1m\frac{(m-1)^2}{m^2}
=\frac{(m-1)(n-2m)}{m^3}.
\]
The sum's prefactor \(\sum_a p_a(1-p_a)^{n-3}\) is \((1-1/m)^{n-3}\), proving (2). Every other factor in (2) is strictly positive. Together with the \(n=2\) calculation, this proves the claimed strict sign diagram and exact zero at \(n=2m\).

Finally consider two categories. For \(n\ge3\), a singleton occurs if and only if the occupancy profile is \((1,n-1)\) or \((n-1,1)\); these mutually exclusive profiles have total probability
\[
\mathbb P\{S_n=1\}=n\left[p(1-p)^{n-1}+(1-p)p^{n-1}\right].
\tag{6}
\]
On this event the matching-pair count is \(\binom{n-1}{2}\), whereas unconditionally it has expectation \(\binom n2[p^2+(1-p)^2]\). Thus
\[
\begin{aligned}
\operatorname{Cov}(S_n,Q_n)
&=\mathbb P\{S_n=1\}\left[\binom{n-1}{2}-\binom n2\left(p^2+(1-p)^2\right)\right]\\
&=\mathbb P\{S_n=1\}(n-1)\left[np(1-p)-1\right],
\end{aligned}
\]
which yields (3). The first two factors in (3) are positive. Since \(0<p(1-p)\le1/4\), the sign for \(n\le4\) follows. For \(n\ge5\), solving \(np(1-p)=1\) gives the two distinct roots \(p_-(n),p_+(n)\); the concave quadratic is greater than one between the roots and smaller outside. This completes the classification.

## Verification

`artifacts/verify.py` independently evaluates exact expectations by exhaustive enumeration of labeled sample sequences for small rational categorical laws. It checks these against (1), tests the closed uniform formula and strict sign classification for larger rational parameter grids, and checks the complete two-category factorization and phase boundaries. All arithmetic is rational, with no rounding. The script reports `CHECKS_PASS 2334` when executed under Python 3.

These checks are finite cross-checks; the universal statements are established by the probability calculation and inequalities above.

## Relationship to prior work

Barbour and Gnedin, *Small counts in the infinite occupancy scheme* (arXiv:0809.4387, first released 2008-09-25), study covariances and joint asymptotics of occupancy frequency counts, particularly with infinitely many boxes and growing samples. This supplies background for \(S_n\) but does not present the finite-uniform \(n=2m\) singleton/pair-collision sign boundary in the inspected text.

Källberg, Leonenko and Seleznjev, *Statistical Inference for Rényi Entropy Functionals* (arXiv:1103.4977), study coincidence-based generalized \(U\)-statistics, including the quadratic estimator underlying \(Q_n\), emphasizing inference and asymptotic normality rather than a covariance classification with singleton counts.

Ben-Hamou, Boucheron and Ohannessian, *Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications* (arXiv:1412.8652), treat singleton counts, missing mass and Good–Turing estimation. The inspected portions develop concentration and variance bounds, rather than exact covariance with the empirical Simpson concentration estimator.

A prior finding on richness and unbiased Gini–Simpson diversity establishes a universal covariance sign for the **total number of observed categories**, not for the **number of singleton categories**. A separate finite-uniform result classifies covariance of richness with each frequency count. Neither implies equations (1)–(3), since neither addresses the joint moment between \(S_n\) and the pair statistic \(Q_n\). The latter is a weighted sum over all frequency classes, not a single frequency count. Both prior results concern natural neighboring problems and were explicitly compared.

## Limitations

This does not claim novel occupancy moment technology; the pairwise conditioning used in (4)–(5) is elementary. Broader pre-existing multinomial factorial-moment tables or ecological estimator covariance formulas could imply the expressions without using these statistic names. Such historical coverage is a genuine priority risk. The identified contribution is the explicit exact **reversal and zero locus** between two standard ecological estimators, plus the two-category probability-phase boundary. No general sign phase diagram is asserted for arbitrary nonuniform laws with three or more categories. Covariance signs do not establish conditional stochastic ordering or association.

## References

1. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387, first submitted 2008-09-25. https://arxiv.org/abs/0809.4387
2. D. Källberg, N. Leonenko and O. Seleznjev, “Statistical Inference for Rényi Entropy Functionals,” arXiv:1103.4977, first submitted 2011-03-25. https://arxiv.org/abs/1103.4977
3. A. Ben-Hamou, S. Boucheron and M. I. Ohannessian, “Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications,” arXiv:1412.8652, first submitted 2014-12-30. https://arxiv.org/abs/1412.8652
