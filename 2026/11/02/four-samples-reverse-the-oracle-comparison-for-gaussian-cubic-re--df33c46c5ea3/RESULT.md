# Four samples reverse the oracle comparison for Gaussian cubic regression control variates

## Finding
Let \(n\ge 2\) be an integer, let \(X_1,\dots,X_n\) be independent standard normal draws, and suppose a function is evaluated only on these draws:
\[
f(x)=\mu+b x+c x^3,\qquad \mu,b\in\mathbb R,\quad c\ne0.
\]
The cubic is the first nonlinear odd Gaussian-polynomial component not contained in the constant-plus-linear control space; it is therefore a natural minimal test of finite-sample regression adjustment. The desired Gaussian integral is \(\mu\). Fit the response \(f(X_i)\) by ordinary least squares with an intercept and the single centered control \(X_i\), and use its fitted intercept \(\widehat\mu_n\) as the integral estimate. The regression exists and is unique almost surely.

Then for every \(n\ge2\), the estimate is unbiased and has the **exact** finite-sample risk
\[
\boxed{
\mathbb E[(\widehat\mu_n-\mu)^2]
=c^2\frac{6(n^5+4n^4-13n^3+176n^2-168n+480)}
{n^3(n+1)(n+3)(n+5)}.}
\]
The population-variance-optimal **fixed linear control coefficient** is \(b+3c\). Its fixed-coefficient sample-average estimate has error variance \(6c^2/n\). Surprisingly, fitting the coefficient *on the same observations* is strictly worse than this oracle within the fixed-coefficient class for \(n=2,3\), but **strictly better for every \(n\ge4\)**. At \(n=4\), the respective risks are \(8c^2/7\) and \(3c^2/2\).

This is a comparison to fixed-coefficient control-variate estimates using the same random nodes, **not** a claim of optimality against arbitrary integration rules or procedures that exploit complete knowledge of the integrand.

## Assumptions and scope
All arithmetic and regressions are exact. Only \(n\) independent draws from \(N(0,1)\) and their corresponding function evaluations are used. The control is \(h(x)=x\), whose target expectation is zero. Almost surely \(Q=\sum_i(X_i-\overline X)^2>0\) when \(n\ge2\). Define the fitted slope and intercept by
\[
\widehat b_n=\frac{\sum_i(X_i-\overline X)f(X_i)}{Q},
\qquad \widehat\mu_n=\overline f-\widehat b_n\overline X.
\]
Affine changes in the response show it suffices to analyze \(\mu=b=0\), \(c=1\); the general estimation error is then scaled by \(c\). No sampling weights, independent pilot fit, extra evaluation, or cross-fitting are involved.

## Proof
**1. Reduction to a centered Gaussian decomposition.** Set
\[
M=\overline X,\quad R_i=X_i-M,\quad
Q=\sum_iR_i^2,\quad T=\sum_iR_i^3,\quad U=\sum_iR_i^4.
\]
The standard Gaussian projection theorem gives \(M\sim N(0,1/n)\), independent of the residual vector \(R\) in the \((n-1)\)-dimensional hyperplane \(\sum_iR_i=0\). For the cubic response, the sample slope equals \(3M^2+3MT/Q+U/Q\), and its fitted intercept satisfies the exact identity
\[
H_n:=\widehat\mu_n\big|_{\mu=b=0,c=1}
=-2M^3+M\left(\frac{3Q}{n}-\frac UQ\right)
+\frac Tn-\frac{3M^2T}{Q}.
\tag{1}
\]
The simultaneous sign reversal \(X_i\mapsto-X_i\) maps \(H_n\mapsto-H_n\). Every term is integrable (for example \(U/Q\le Q\) and \(|T|/Q\le\sqrt Q\)), so \(\mathbb E H_n=0\). Thus the original estimator is unbiased.

**2. Required Gaussian moments.** Put \(d=n-1\), \(L=3Q/n-U/Q\). The squared radius \(Q\) has a chi-square law with \(d\) degrees of freedom. The direction \(R/\sqrt Q\) is independent of \(Q\) and uniform on the unit sphere of the residual hyperplane. Its projector has diagonal entries \(d/n\) and off-diagonal entries \(-1/n\).

Wick's identity for the centered Gaussian residual vector gives
\[
\mathbb E U=\frac{3d^2}{n},\qquad
\mathbb E U^2=\frac{3d(3n^3+23n^2-63n+45)}{n^2},\qquad
\mathbb E T^2=\frac{6d(n-2)}{n}.
\tag{2}
\]
For completeness, the second identity follows from
\(\mathbb E R_i^8=105(d/n)^4\) and, for distinct \(i,j\),
\(\mathbb E(R_i^4R_j^4)=9(d/n)^4+72(d/n)^2n^{-2}+24n^{-4}\).
The third uses
\(\mathbb E R_i^3R_j^3=9\operatorname{Var}(R_i)\operatorname{Var}(R_j)\operatorname{Cov}(R_i,R_j)+6\operatorname{Cov}(R_i,R_j)^3\).

Radial independence and the chi-square moments
\(\mathbb E Q^k=\prod_{j=0}^{k-1}(d+2j)\) yield
\[
\mathbb E L=\frac{6d}{n(n+1)},\qquad
\mathbb E L^2=\frac{12d(2n^2-9n+45)}{n^2(n+3)(n+5)},
\tag{3}
\]
\[
\mathbb E\frac{T^2}{Q}=\frac{6d(n-2)}{n(n+3)},\qquad
\mathbb E\frac{T^2}{Q^2}=\frac{6d(n-2)}{n(n+1)(n+3)}.
\tag{4}
\]
In particular, the potentially troublesome ratios have finite moments for every integer \(n\ge2\); at \(n=2\), \(T=0\) identically.

**3. Exact variance.** Separate equation (1) into \(A=-2M^3+ML\) and \(B=T/n-3M^2T/Q\). Their covariance vanishes: \(A\) is odd in \(M\), whereas \(B\) is even in \(M\), independently of \(R\). Standard normal moments give
\(\mathbb E M^2=1/n\), \(\mathbb E M^4=3/n^2\), and \(\mathbb E M^6=15/n^3\). Therefore
\[
\mathbb E H_n^2
=\frac{60}{n^3}-\frac{12\,\mathbb E L}{n^2}
+\frac{\mathbb E L^2}{n}
+\frac1{n^2}\left(\mathbb E T^2-6\mathbb E\frac{T^2}{Q}
+27\mathbb E\frac{T^2}{Q^2}\right).
\tag{5}
\]
Substituting (2)--(4) and combining rational terms yields the boxed formula.

**4. Sharp integer boundary and oracle comparison.** Since
\(\mathbb E[X^4]=3\), the population projection coefficient of \(X^3\) onto \(X\) is \(3\). The residual \(X^3-3X\) has variance \(15-18+9=6\). Thus the best fixed-coefficient control-variate average has variance \(6/n\) in the normalized case. Direct subtraction gives
\[
\mathbb E H_n^2-\frac6n
=-\frac{6P(n)}{n^3(n+1)(n+3)(n+5)},
\qquad P(n)=5n^4+36n^3-161n^2+168n-480.
\tag{6}
\]
Here \(P(2)=-420\) and \(P(3)=-48\). For every integer \(n\ge4\), the decomposition
\(P(n)=n^2(5n^2+36n-161)+168n-480\)
is strictly positive, because both summands are positive for \(n\ge4\). This establishes the exact and unique crossing at four observations. The sample risks are \(6\), \(37/18\), \(8/7\) for \(n=2,3,4\), respectively.

## Verification
Running `python3 verify.py` with the Python standard library reproduces the rational formulas and threshold for every integer \(2\le n\le200\), checks the estimator reduction on randomly chosen rational samples, and performs separately labeled, fixed-seed Gaussian simulation diagnostics. The script passed 1,790 exact-rational assertions plus the simulation diagnostics. The proof above, rather than the finite checks, establishes the universal statement.

## Relationship to prior work
Portier and Segers (2018), Sections 2--3, identify ordinary least-squares regression intercepts with control-variate integration, and prove asymptotic distributional results. Their generic regression identities determine the *estimator* used here, but do not give the specific finite-sample cubic-Gaussian second moment or the strict four-sample reversal. Leluc, Portier, Segers and Zhuman (2022), Sections 2--4, treat least-squares control-variate quadrature and adaptive importance sampling with asymptotic variance and concentration bounds, without the stated same-sample cubic exact risk. Blanchet, Chen, Lu and Ying (2023) study regression-adjusted control variates via sample splitting and minimax integration, a distinct estimator and objective. The familiar fixed-coefficient oracle minimizes variance **within the fixed-coefficient class**; its inequality does not order nonlinear data-dependent estimates such as the fitted intercept.

## Limitations
This is a deliberately minimal Gaussian-polynomial model, not a general dominance theorem for regression control variates. The sample-size threshold can change for other sampling laws, integrands, controls, or fitting procedures. The result compares exactly matched random nodes and only a single linear control. Source inspection and research-record searches cannot prove exhaustive historical novelty; an uncatalogued specialized earlier computation remains possible. External independent validation has not been performed.

## References
1. F. Portier and J. Segers, *Monte Carlo integration with a growing number of control variates*, first public arXiv version 2018-01-05, https://arxiv.org/abs/1801.01797.
2. R. Leluc, F. Portier, J. Segers and A. Zhuman, *A Quadrature Rule combining Control Variates and Adaptive Importance Sampling*, first public arXiv version 2022-05-24, https://arxiv.org/abs/2205.11890.
3. J. Blanchet, H. Chen, Y. Lu and L. Ying, *When can Regression-Adjusted Control Variates Help? Rare Events, Sobolev Embedding and Minimax Optimality*, first public arXiv version 2023-05-25, https://arxiv.org/abs/2305.16527.
