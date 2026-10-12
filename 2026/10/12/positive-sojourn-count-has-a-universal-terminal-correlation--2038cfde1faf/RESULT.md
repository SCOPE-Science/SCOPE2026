# Positive-sojourn count has a universal terminal correlation

## Finding

Let
\[
X_1,X_2,\ldots
\]
be independent and identically distributed random variables with a continuous distribution symmetric about \(0\), and suppose
\[
\operatorname{Var}(X_1)=\sigma^2\in(0,\infty).
\]
Write
\[
S_k=\sum_{i=1}^kX_i
\]
and let
\[
A_n=\sum_{k=1}^n\mathbf 1_{\{S_k>0\}}
\]
be the number of strictly positive partial sums through time \(n\).

Then
\[
\boxed{
\operatorname{Cov}(A_n,S_n)
=
\frac12\sum_{k=1}^n\mathbb E|S_k|.
}
\tag{1}
\]

For continuous symmetric increments, the Sparre-Andersen discrete arcsine law gives
\[
\boxed{
\Pr(A_n=r)
=
\frac{1}{4^n}
\binom{2r}{r}
\binom{2(n-r)}{n-r},
\qquad
0\le r\le n.
}
\tag{2}
\]
Equivalently, \(A_n\) is beta-binomial with parameters \(n,1/2,1/2\), so
\[
\mathbb E A_n=\frac n2,
\qquad
\operatorname{Var}(A_n)=\frac{n(n+1)}8.
\tag{3}
\]

Because
\[
\operatorname{Var}(S_n)=n\sigma^2,
\]
(1) and (3) give
\[
\boxed{
\operatorname{Corr}(A_n,S_n)
=
\frac{\sqrt2\sum_{k=1}^n\mathbb E|S_k|}
{\sigma n\sqrt{n+1}}.
}
\tag{4}
\]

The central limit theorem and uniform integrability imply
\[
\frac{\mathbb E|S_k|}{\sigma\sqrt{k}}
\longrightarrow
\sqrt{\frac{2}{\pi}},
\]
and therefore
\[
\boxed{
\operatorname{Corr}(A_n,S_n)
\longrightarrow
\frac{4}{3\sqrt{\pi}}.
}
\tag{5}
\]

The limit is universal across continuous symmetric finite-variance increment laws.

For Gaussian increments,
\[
\mathbb E|S_k|
=
\sigma\sqrt{\frac{2k}{\pi}},
\]
so the finite-\(n\) correlation is
\[
\boxed{
\operatorname{Corr}(A_n,S_n)
=
\frac{2}{\sqrt{\pi}}
\frac{\sum_{k=1}^n\sqrt{k}}{n\sqrt{n+1}}.
}
\tag{6}
\]

There is a matching Brownian identity. For standard Brownian motion \(B\), let
\[
\Gamma=\int_0^1\mathbf 1_{\{B_t>0\}}\,dt.
\]
Then
\[
\boxed{
\operatorname{Cov}(\Gamma,B_1)
=
\frac{2}{3\sqrt{2\pi}},
\qquad
\operatorname{Corr}(\Gamma,B_1)
=
\frac{4}{3\sqrt{\pi}}.
}
\tag{7}
\]

Thus the classical arcsine occupation statistic retains substantial positive linear dependence on terminal displacement: the standardized dependence converges to approximately \(0.752\), rather than disappearing.

## Assumptions and scope

Continuity of the increment law is used for the universal Sparre-Andersen marginal (2), because it removes zero partial sums. The exact covariance identity (1) itself only needs independent symmetric integrable increments.

Finite nonzero variance is used for the correlation and its limit. No higher moment is required.

The theorem concerns a mixed first moment and correlation. It does not determine the full joint law of \((A_n,S_n)\).

## Proof

Symmetry gives
\[
\mathbb E S_n=0.
\]
Therefore
\[
\operatorname{Cov}(A_n,S_n)
=
\sum_{k=1}^n
\mathbb E\!\left[
S_n\mathbf 1_{\{S_k>0\}}
\right].
\tag{8}
\]

For each \(k\),
\[
S_n=S_k+(S_n-S_k),
\]
where \(S_n-S_k\) is independent of \(S_k\) and has mean zero. Hence
\[
\mathbb E\!\left[
S_n\mathbf 1_{\{S_k>0\}}
\right]
=
\mathbb E\!\left[
S_k\mathbf 1_{\{S_k>0\}}
\right].
\tag{9}
\]

The distribution of \(S_k\) is symmetric. Thus
\[
\mathbb E\!\left[
S_k\mathbf 1_{\{S_k>0\}}
\right]
=
\frac12\mathbb E|S_k|.
\tag{10}
\]
Summing (10) proves (1).

For continuous symmetric iid increments, the Sparre-Andersen theorem gives (2). The beta-binomial moments give (3). Combining (1), (3), and
\[
\operatorname{Var}(S_n)=n\sigma^2
\]
gives (4).

By the central limit theorem,
\[
\frac{S_k}{\sigma\sqrt{k}}
\Rightarrow Z,
\]
where \(Z\) is standard normal. Also
\[
\mathbb E\left[
\left(\frac{S_k}{\sigma\sqrt{k}}\right)^2
\right]=1,
\]
so the absolute values form a uniformly integrable family. Consequently
\[
\frac{\mathbb E|S_k|}{\sigma\sqrt{k}}
\longrightarrow
\mathbb E|Z|
=
\sqrt{\frac{2}{\pi}}.
\tag{11}
\]
Using
\[
\sum_{k=1}^n\sqrt{k}
\sim
\frac23n^{3/2},
\tag{12}
\]
in (4) proves (5). Formula (6) follows from the exact Gaussian absolute first moment.

For the Brownian statement, Fubini and the martingale property give
\[
\begin{aligned}
\mathbb E[\Gamma B_1]
&=
\int_0^1
\mathbb E\!\left[
B_1\mathbf 1_{\{B_t>0\}}
\right]dt\\
&=
\int_0^1
\mathbb E\!\left[
B_t\mathbf 1_{\{B_t>0\}}
\right]dt\\
&=
\frac12\int_0^1\mathbb E|B_t|\,dt\\
&=
\frac{1}{\sqrt{2\pi}}
\int_0^1\sqrt{t}\,dt\\
&=
\frac{2}{3\sqrt{2\pi}}.
\end{aligned}
\]
Lévy's arcsine law gives
\[
\operatorname{Var}(\Gamma)=\frac18,
\]
and
\[
\operatorname{Var}(B_1)=1.
\]
This proves (7).

## Verification

The accompanying checker performs three supplementary replays.

First, it exhaustively enumerates every simple symmetric lattice walk through length \(16\). Although lattice walks can hit zero and therefore do not use the continuous-increment marginal (2), they still satisfy the more general covariance identity (1). The checker verifies this identity exactly with rational arithmetic.

Second, for every
\[
1\le n\le200,
\]
it evaluates (2) directly and verifies normalization, mean \(n/2\), and variance \(n(n+1)/8\).

Third, it evaluates the Gaussian finite-\(n\) correlation formula at increasing sizes and checks convergence toward \(4/(3\sqrt{\pi})\).

The computations are supplementary. The all-\(n\) theorem follows from independence, symmetry, the classical Sparre-Andersen law, and the central limit theorem.

## Relationship to prior work

Erdős and Kac studied the number of positive partial sums and proved the classical arcsine limit for broad independent-increment random walks. That work concerns the marginal occupation statistic.

Döbler developed quantitative convergence to the arcsine law for a symmetric random walk. The inspected full public text treats the occupation-time marginal and its approximation; targeted searches in that text found no covariance or terminal-value formulation.

Ivanovs develops Sparre-Andersen identities for random walks and Lévy processes through exchangeability and time reversal. His full paper explicitly treats positive and negative occupation times and random-walk fluctuation identities, but the inspected random-walk section does not state the covariance of a positive-sojourn count with terminal displacement.

Hartmann and Majumdar compute exact pairwise joint laws among three Brownian global times: occupation time, time of the maximum, and last-passage time. Their article motivates correlation questions among global observables, but the terminal position is not one of those three observables.

The result here links the classical occupation statistic to terminal displacement by an exact covariance identity and shows that the corresponding correlation has the universal nonzero limit \(4/(3\sqrt{\pi})\).

## Limitations

The exact arcsine marginal (2) requires the continuous symmetric iid setting. Lattice walks require tie conventions and generally have a different finite occupation-count law.

The theorem identifies covariance and correlation, not the full joint law.

The covariance identity (1) is elementary once the decomposition at time \(k\) is made. Because fluctuation theory and occupation times have a long literature, an equivalent moment identity may exist in older work under different terminology; this is the principal originality risk.

The Brownian formula is a continuum companion and does not by itself imply the exact finite-\(n\) random-walk identity.

## References

1. J. Ivanovs, “Sparre-Andersen identity and the last passage time,” arXiv:1501.04542, first submitted 2015-01-19; later *Journal of Applied Probability* 53 (2016), 600–605, DOI 10.1017/jpr.2016.24.
2. C. Döbler, “A rate of convergence for the arcsine law by Stein's method,” arXiv:1207.2401, first submitted 2012-07-10.
3. P. Erdős and M. Kac, “On the number of positive sums of independent random variables,” *Bulletin of the American Mathematical Society* 53 (1947), 1011–1020, DOI 10.1090/S0002-9904-1947-08928-X.
4. A. K. Hartmann and S. N. Majumdar, “Exact joint distributions of three global characteristic times for Brownian motion,” *Physical Review E* 111 (2025), 044134, DOI 10.1103/PhysRevE.111.044134.
