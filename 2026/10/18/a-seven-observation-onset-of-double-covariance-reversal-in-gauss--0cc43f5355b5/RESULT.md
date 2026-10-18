# A seven-observation onset of double covariance reversal in Gaussian AR(1) sign crossings

## Finding

Let \(n\ge2\) be an integer, \(0\le\rho<1\), and \(X=(X_1,\ldots,X_n)\) be a centered Gaussian vector with \(\mathbb E X_i^2=1\) and \(\mathbb E[X_iX_j]=\rho^{|i-j|}\). Define the sign-crossing count and *demeaned* quadratic energy
\[
Z_n=\sum_{i=1}^{n-1}{\bf1}\{X_iX_{i+1}<0\},\qquad
V_n=\sum_{j=1}^{n}(X_j-\overline X)^2,\quad
\overline X=\frac1n\sum_{j=1}^{n}X_j.
\]
Writing \(\Sigma_{ij}=\rho^{|i-j|}\), \(H=I-\mathbf1\mathbf1^{\mathsf T}/n\), and \(a_i=\Sigma e_i\), define the polynomial
\[
F_n(\rho)=\sum_{i=1}^{n-1}
\left[\rho(a_i^{\mathsf T}Ha_i+a_{i+1}^{\mathsf T}Ha_{i+1})
-2a_i^{\mathsf T}Ha_{i+1}\right].
\]
Then the exact finite-sample mixed moment is
\[
\boxed{\operatorname{Cov}(V_n,Z_n)=\frac{F_n(\rho)}{\pi\sqrt{1-\rho^2}}.}
\]
The following is a **sharp dimension threshold for the possibility of negative covariance**:

1. For every \(2\le n\le6\) and every \(0\le\rho<1\), \(\operatorname{Cov}(V_n,Z_n)>0\).
2. For every \(n\ge7\), the covariance is positive at \(\rho=0\), negative at \(\rho=1/2\), and positive for all \(\rho\) sufficiently close to one. Thus there is at least one covariance-sign reversal in each of the intervals \((0,1/2)\) and \((1/2,1)\). The assertion is **at least two**, not uniqueness of either zero.

More precisely,
\[
F_n(1/2)=\frac{-3n^2+31n-78+(18n+90)2^{-n}-(4n+12)4^{-n}}{3n},
\]
\[
\boxed{F_n(0)=\frac{2(n-1)}n,\qquad
\lim_{\rho\uparrow1}\frac{F_n(\rho)}{(1-\rho)^2}
=\frac{2(n^2-1)}3.}
\]
For every fixed \(0<\rho<1\), a complementary growing-window limit is
\[
\boxed{\lim_{n\to\infty}\frac1n\operatorname{Cov}(V_n,Z_n)
=-\frac{2\rho}{\pi\sqrt{1-\rho^2}}.}
\]
In particular, the signs are not explained by the uncentered energy, whose covariance with crossing count is strictly negative for all positive \(\rho\).

## Assumptions and scope

The vector is jointly Gaussian, stationary, unit-variance, with AR(1) autocorrelation parameter in the nonnegative interval \([0,1)\). Since the Gaussian covariance matrix is positive definite for \(\rho<1\), crossings occur with probability independent of how equality at zero is treated. The energy is the unnormalized sample sum of squares about the *sample mean*, not \(\sum X_j^2\) or a variance about the known population mean. All assertions hold for every stated integer sample size; no asymptotic limit is used to justify a finite-sample sign.

## Proof

**Gaussian sign–quadratic lemma.** Suppose \(U,V,Y\) are jointly centered Gaussian with \(\operatorname{Var}(U)=\operatorname{Var}(V)=1\), \(\operatorname{Corr}(U,V)=r\in(-1,1)\), \(a=\operatorname{Cov}(Y,U)\), and \(b=\operatorname{Cov}(Y,V)\). Then
\[
\operatorname{Cov}(Y^2,{\bf1}\{UV<0\})
=\frac{r(a^2+b^2)-2ab}{\pi\sqrt{1-r^2}}. \tag{1}
\]
To verify this rather than assume a differentiable indicator, approximate the indicator by smooth bounded functions and use the twice-iterated Gaussian integration-by-parts formula. Equivalently, use the Gaussian heat equation for covariance perturbations. For variances \(s,t>0\) and covariance \(c\), the crossing probability is \(G(s,t,c)=\pi^{-1}\arccos(c/\sqrt{st})\). At \((s,t,c)=(1,1,r)\), its derivatives give
\[
\mathbb E\partial_{uu}{\bf1}\{UV<0\}
=2G_s=\frac r{\pi\sqrt{1-r^2}},\quad
\mathbb E\partial_{vv}{\bf1}\{UV<0\}=2G_t=\frac r{\pi\sqrt{1-r^2}},\quad
\mathbb E\partial_{uv}{\bf1}\{UV<0\}
=G_c=-\frac1{\pi\sqrt{1-r^2}}.
\]
These derivatives are understood distributionally; the smooth approximations converge against the Gaussian density and its derivatives. Substitution into
\(\operatorname{Cov}(Y^2,f(U,V))=a^2\mathbb E f_{uu}+2ab\mathbb E f_{uv}+b^2\mathbb E f_{vv}\)
proves (1). Polarization of (1) gives, for a symmetric deterministic matrix \(B\),
\[
\operatorname{Cov}(X^{\mathsf T}BX,{\bf1}\{X_iX_{i+1}<0\})
=\frac{\rho(a_i^{\mathsf T}Ba_i+a_{i+1}^{\mathsf T}Ba_{i+1})-2a_i^{\mathsf T}Ba_{i+1}}{\pi\sqrt{1-\rho^2}}.\tag{2}
\]
Set \(B=H\) and sum over \(i\) to obtain the stated exact identity.

**Midparameter calculation and negative sign.** Let \(Q_n=\sum_j X_j^2\). Applying (1) with \(Y=X_j\), and using \(\rho^{|j-i|}\) for the correlations, yields
\[
\pi\sqrt{1-\rho^2}\operatorname{Cov}(Q_n,Z_n)
=-2\rho(1-\rho^2)\sum_{d=0}^{n-2}(n-d-1)\rho^{2d}.\tag{3}
\]
Since \(V_n=Q_n-(\sum_jX_j)^2/n\), let
\(s_i=\sum_{j=1}^n\rho^{|j-i|}=(1+\rho-\rho^i-\rho^{n-i+1})/(1-\rho)\).
Equations (2) and (3) show that
\[
F_n(\rho)=-2\rho(1-\rho^2)\sum_{d=0}^{n-2}(n-d-1)\rho^{2d}
-\frac1n\sum_{i=1}^{n-1}
\bigl[\rho(s_i^2+s_{i+1}^2)-2s_i s_{i+1}\bigr].\tag{4}
\]
At \(\rho=1/2\), \(s_i=3-2^{1-i}-2^{i-n}\). Substitution into the finite geometric sums (4), using \(\sum_{d=0}^{m-1}(m-d)q^d=[m-(m+1)q+q^{m+1}]/(1-q)^2\), gives the displayed expression for \(F_n(1/2)\). For \(n\ge7\), its nonexponential part is \(-3(n-6)(n-13/3)\le-8\), while \((18n+90)2^{-n}\le27/16\); the remaining \(-(4n+12)4^{-n}\) term is negative. Consequently \(F_n(1/2)<0\) for every \(n\ge7\).

**Small-window positivity.** Exact polynomial simplification of (2) gives the following factorizations for \(2\le n\le6\):
\[
\begin{array}{c|c|l}
n&k_n&P_n(\rho)\\\hline
2&1&1\\
3&4/3&1+\rho^2\\
4&1/2&3-2\rho+5\rho^2+\rho^3+3\rho^4\\
5&4/5&2-3\rho+3\rho^2+\rho^3+4\rho^4+\rho^5+2\rho^6\\
6&1/3&5-12\rho+5\rho^2-\rho^3+14\rho^4+5\rho^5+11\rho^6+3\rho^7+5\rho^8
\end{array}
\]
with \(F_n(\rho)=k_n(1-\rho)^2(1+\rho)P_n(\rho)\). The polynomials for \(n=2,3\) are manifestly positive. For \(n=4,5,6\), positivity throughout \([0,1]\) follows from their strictly positive Bernstein-basis coefficients. In increasing Bernstein index, those lists are respectively
\[
\begin{aligned}
n=4:&\quad(3,5/2,17/6,17/4,10),\\
n=5:&\quad(2,3/2,6/5,23/20,5/3,7/2,10),\\
n=6:&\quad(5,7/2,61/28,57/56,1/5,11/56,9/4,77/8,35).
\end{aligned}
\]
Here the degree-\(m\) Bernstein functions \(\binom mj\rho^j(1-\rho)^{m-j}\) are nonnegative and sum to one. Each coefficient list follows directly from the power coefficients \(a_j\) via \(b_k=\sum_{j=0}^ka_j\binom kj/\binom mj\). This proves strict positivity for every \(n\le6\) in the stated range.

**Endpoint signs and growing window.** At \(\rho=0\), the columns \(a_i=e_i\) and \(e_i^{\mathsf T}He_{i+1}=-1/n\), proving \(F_n(0)=2(n-1)/n>0\). For \(\epsilon=1-\rho\downarrow0\), write \(d_i=(|1-i|,\ldots,|n-i|)^{\mathsf T}\). Then \(Ha_i=-\epsilon Hd_i+O(\epsilon^2)\); hence
\[
F_n(\rho)=\epsilon^2\sum_{i=1}^{n-1}\|H(d_i-d_{i+1})\|_2^2+O(\epsilon^3)
=\epsilon^2\sum_{i=1}^{n-1}\frac{4i(n-i)}n+O(\epsilon^3)
=\frac{2(n^2-1)}3\epsilon^2+O(\epsilon^3).
\]
Thus \(F_n>0\) sufficiently near one, for every fixed \(n\). Continuity and the negative value at \(1/2\) yield at least two sign changes for every \(n\ge7\).

For fixed \(0<\rho<1\), dividing (3) by \(n\) and taking \(n\to\infty\) gives \(-2\rho\) after multiplication by \(\pi\sqrt{1-\rho^2}\), because the normalized sum tends to \((1-\rho^2)^{-1}\). The second term in (4) is \(O(1)\) uniformly in \(n\) at fixed \(\rho\), since all \(s_i\) are bounded by \((1+\rho)/(1-\rho)\). Therefore \(F_n(\rho)/n\to-2\rho\), which proves the asserted asymptotic.

## Verification

The standalone script `verify_gaussian.py` reconstructs \(F_n\) from the finite covariance-matrix definition, checks the independent finite geometric-sum formula using exact fractions, verifies the closed form at \(\rho=1/2\), symbolically rederives all five small-\(n\) factorizations and their Bernstein coefficients, and verifies the endpoint second-derivative limit for explicit cases. The proof above establishes the unrestricted assertions; finite checks do not replace it. Execute with Python 3 and SymPy: `python verify_gaussian.py`.

## Relationship to prior work

Kratz and León (2006, arXiv:math/0609682, primary MSC 60G15) analyze the second moment and finiteness conditions for continuous Gaussian level-crossing counts. Their theorem concerns crossings of a continuously indexed smooth process, not dependence on a finite-window demeaned quadratic statistic.

Sinn and Keller (2011) investigate covariances **between zero-crossing indicators** for Gaussian processes and AR models. Their published abstract describes four-variate normal orthant formulas and variance of empirical crossing rate; it does not state the mixed covariance with sample quadratic energy. Full text was unavailable during this examination, leaving an explicit historical-priority risk.

Nyberg, Lizana, and Ambjörnsson (arXiv:1711.02926) derive crossing-count cumulants by an independent-interval approximation, including AR(1) examples. The inspected preprint's calculations address the marginal crossing count, not the joint law with demeaned sample energy. Gaussian integration by parts and the bivariate arcsine crossing formula are classical ingredients and are not themselves claimed as new. The finite-sample sharp onset at seven and the positive–negative–positive covariance pattern are the assessed contribution, with priority not independently certified.

## Limitations

The result assumes exact joint Gaussianity and the specified positive AR(1) correlation; arbitrary non-Gaussian time series, negative autoregression, and unequal measurement variances are not included. The theorem asserts at least two sign reversals for \(n\ge7\), without asserting exactly two roots. The covariance sign need not imply stochastic ordering or causal influence. Only self-review has been performed; independent historical-priority or mathematical auditing has not occurred.

## References

1. M. F. Kratz and J. R. León, *On the second moment of the number of crossings by a stationary Gaussian process*, Annals of Probability 34 (2006), 1601–1607; arXiv:math/0609682v1, first publicly posted 2006-09-25; DOI:10.1214/009117906000000142.
2. M. Sinn and K. Keller, *Covariances of zero crossings in Gaussian processes*, Theory of Probability and Its Applications 55 (2011), 485–504; DOI:10.1137/S0040585X97984991.
3. M. Nyberg, L. Lizana, and T. Ambjörnsson, *Zero-Crossing Statistics for Non-Markovian Time Series*, arXiv:1711.02926v1 (2017-11-08); Physical Review E 97 (2018), 032114.
4. S. O. Rice, *Mathematical analysis of random noise*, Bell System Technical Journal (1944–1945); classical level-crossing formula. No novelty is claimed for this formula.
