# Two boundary layers for zero-crossing and squared-sum covariance in Gaussian AR(1)

## Finding
Let \(X_1,\ldots,X_n\) be a segment of a centered stationary Gaussian AR(1) process with variance \(\sigma^2>0\), correlation \(\rho^{|i-j|}\), \(-1<\rho<1\), and \(n\ge2\). Define the number of observed zero crossings and the unnormalized sample sum by
\[
Z_n=\sum_{i=1}^{n-1}\mathbf1\{X_iX_{i+1}<0\},\qquad S_n=\sum_{j=1}^nX_j.
\]
The following exact finite-sample identity holds:
\[
\operatorname{Cov}(Z_n,S_n^2)=\frac{\sigma^2 F_n(\rho)}{\pi\sqrt{1-\rho^2}},
\]
where, writing \(t=\rho^n\),
\[
F_n(\rho)=\frac{2}{(1-\rho)^2}\left\{n(\rho-1)(\rho+1)^2+3\rho^2+3\rho+1
+[n(\rho^2-1)-3\rho^2-4\rho-1]t+\rho t^2\right\}.
\]
The negative-autocorrelation endpoint has **two different asymptotic scales**. For every fixed \(c>0\),
\[
F_n(-1+c/\sqrt n)\longrightarrow\frac12-c^2
\]
along either parity. Along *even* sample sizes,
\[
n^3 F_n(-1+c/n^2)\longrightarrow\frac{c^2(c-12)}6,
\]
whereas along *odd* sample sizes,
\[
nF_n(-1+c/n^2)\longrightarrow2c.
\]
Consequently, for all sufficiently large even \(n\), the covariance as a function of \(\rho\in(-1,0)\) is negative, then positive, then negative on three explicitly separated nonempty parameter regions; it has **at least two distinct zeros**. Odd sizes instead have a positive region near \(-1\) and a negative region farther away. No uniqueness or complete finite-sample zero classification is claimed.

## Assumptions and scope
The process is Gaussian, stationary, centered, and has the positive-definite AR(1) correlation matrix for each \(|\rho|<1\). Crossing means a *discrete sign change between consecutive observations*, not a continuous-time level crossing. The square is that of the *total* sum, not the energy \(\sum_jX_j^2\). Replacing the total sum by the sample mean divides the covariance by \(n^2\). All identities are exact for every integer \(n\ge2\); displayed boundary limits hold only for fixed \(c>0\) along the specified growing-size regime.

## Proof
**Bivariate Gaussian identity.** Let \((U,V)\) be centered jointly standard normal with correlation \(\rho\), let \(L\) be any centered jointly Gaussian linear statistic (possibly using further Gaussian coordinates), and write \(a=\operatorname{Cov}(L,U)\), \(b=\operatorname{Cov}(L,V)\). Then
\[
\operatorname{Cov}(\mathbf1\{UV<0\},L^2)
=\frac{\rho(a^2+b^2)-2ab}{\pi\sqrt{1-\rho^2}}.
\tag{1}
\]
Indeed, exponential tilting by \(L\) shifts the means of \((U,V)\) by \((sa,sb)\), and the second derivative at \(s=0\) of the tilted expectation equals the left side. The shifted crossing probability is
\(\Phi(sa)+\Phi(sb)-2\Phi_2(sa,sb;\rho)\), where \(\Phi_2\) is the standard bivariate-normal distribution function with correlation \(\rho\). Its two pure second derivatives at the origin are \(-\rho/(2\pi\sqrt{1-\rho^2})\), and its mixed derivative is \(1/(2\pi\sqrt{1-\rho^2})\); differentiation proves (1). These are identities for \(-1<\rho<1\), so no singular endpoint is used.

Apply (1) after standardizing \(X_j/\sigma\) and taking \(L=S_n/\sigma\). Put
\[
b_i=\sum_{j=1}^n\rho^{|i-j|}
=\frac{1+\rho-\rho^i-\rho^{n-i+1}}{1-\rho}.
\]
Summing over \(i=1,\ldots,n-1\) gives the independent finite-sum representation
\[
F_n(\rho)=\sum_{i=1}^{n-1}\left[\rho(b_i^2+b_{i+1}^2)-2b_ib_{i+1}\right].
\tag{2}
\]
Expanding the geometric sums, or using \(b_i-b_{i+1}=\rho^{n-i}-\rho^i\), reduces (2) to the closed expression in the Finding. No distributional approximation is involved.

For fixed \(\rho\in(-1,1)\), the terms containing \(\rho^n\) vanish exponentially, so
\[
\frac{F_n(\rho)}n\longrightarrow-\frac{2(1+\rho)^2}{1-\rho}<0.
\tag{3}
\]
For fixed \(n\), writing \(\varepsilon=1+\rho\downarrow0\), finite binomial expansion of the closed formula yields
\[
F_n(-1+\varepsilon)=
\begin{cases}
2(n-1)\varepsilon+O_n(\varepsilon^2),&n\text{ odd},\\
-2n\varepsilon^2+O_n(\varepsilon^3),&n\text{ even}.
\end{cases}
\tag{4}
\]
For \(\rho=-1+c/\sqrt n\), the factor \(\rho^n=(-1)^n(1-c/\sqrt n)^n\) is exponentially small in \(\sqrt n\). Substitution in the closed expression gives \(F_n=1/2-c^2+O_c(n^{-1/2})\). For \(\rho=-1+c/n^2\), use \(\rho^n=(-1)^n(1-c/n^2)^n\) and expand its binomial coefficients through the required order, obtaining
\[
F_n=\begin{cases}
\dfrac{c^2(c-12)}{6n^3}+O_c(n^{-4}),& n\text{ even},\\
\dfrac{2c}{n}+O_c(n^{-2}),& n\text{ odd}.
\end{cases}
\tag{5}
\]
All remainder statements are for fixed positive \(c\).

For sufficiently large even \(n\), the three ordered points \(-1+6/n^2<-1+20/n^2<-1+1/\sqrt n\) are in \((-1,0)\). Their respective \(F_n\)-signs are negative, positive, and negative by (5) and the square-root-scale limit. Continuity therefore gives at least two different zeros. For large odd \(n\), the square-root-scale points with \(c=1/2\) and \(c=1\) give opposite signs, guaranteeing at least one zero. The sign of the covariance equals that of \(F_n\) throughout the domain because the prefactor is positive.

## Verification
The standalone standard-library program `verify.py` independently evaluates the finite sum (2), the closed expression, exact Taylor coefficients at the negative unit-root endpoint, and rational boundary regimes. Its completed replay yielded `PASS 413 exact and boundary checks`. These calculations check algebra and finite examples; the preceding analytic derivation establishes the statements for all sizes. To reproduce, run `python3 verify.py` from the folder containing this document.

## Relationship to prior work
Gaussian zero-crossing counts and their moment theory are classical; see Kratz's survey (2006), especially its sections on crossing moments and Wiener-chaos expansions. Sinn and Keller (2010/2011) study *covariances between zero-crossing indicators/counts* and their large-lag behavior. The present object is instead the mixed covariance with the square of a global linear statistic. A formula for covariance with the diagonal energy \(\sum_jX_j^2\) does not imply the stated two-scale law for \(S_n^2\), which also contains all off-diagonal products \(X_iX_j\). The finite identity uses standard Gaussian tools; the value-bearing assertion is the parity-sensitive pair of boundary layers and the resulting negative–positive–negative behavior at even lengths.

## Limitations
The theorem establishes existence, not uniqueness, of crossings of the covariance as a function of \(\rho\). The exactly critical choices \(c=12\) and \(c=1/\sqrt2\) require higher-order analysis for a sign decision. No causal interpretation or inference guarantee for estimators is proved. Complete historical priority cannot be guaranteed; in particular, the full text of Sinn and Keller could not be recovered during source inspection. The source date is the publicly verified date of the historical anchor, not a claim that these new formulas appeared in that work.

## References
1. M. F. Kratz, *Level crossings and other level functionals of stationary Gaussian processes*, Probability Surveys 3 (2006), 230–288. arXiv:math/0612577, first posted 2006-12-20, https://arxiv.org/abs/math/0612577; doi:10.1214/154957806000000087.
2. M. Sinn and K. Keller, *Covariances of zero crossings in Gaussian processes*, Theory of Probability and Its Applications 55 (2011), 485–504; original Russian-language journal volume 55 (2010), doi:10.1137/S0040585X97984991, doi:10.4213/tvp4241.
