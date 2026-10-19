# Sharp covariance-aligned Landweber confidence radii and a half-order spectral transition

## Finding
Fix a matrix \(A\in\mathbb R^{m\times n}\) of full column rank, with \(m\ge n\ge2\), the observation model \(y=Ax^\dagger+\varepsilon\), \(\varepsilon\sim N(0,\sigma^2 I_m)\), and a Landweber iteration starting at zero. Assume the source ball \(x^\dagger=B^\nu w\), \(\|w\|_2\le M\), with \(B=A^{\mathsf T}A\), \(\nu,M,\sigma>0\). For a fixed positive integer \(K\) and a fixed step \(0<\omega<1/\lambda_{\max}(B)\), let \(\Gamma_K\) be the exact iterate covariance.

**Sharp simultaneous coverage law.** Among regions that are ellipsoids centered at the Landweber iterate with shape matrix \(\Gamma_K\), the unique smallest deterministic Mahalanobis radius giving frequentist coverage at least \(1-\alpha\) uniformly over the source ball, for \(0<\alpha<1\), is

\[
 r_*=\sqrt{F_{n,\Delta_K^2}^{-1}(1-\alpha)},\qquad
 \Delta_K=\frac M\sigma\max_{\lambda\in\operatorname{spec}(B)}
 \frac{(1-\omega\lambda)^K\lambda^{\nu+1/2}}
 {1-(1-\omega\lambda)^K}.
\]

Here \(F_{n,d^2}\) is the CDF of a noncentral chi-square law with \(n\) degrees of freedom and noncentrality \(d^2\); its inverse is the usual left-continuous quantile. This formula is exact, not just sufficient, and a source-ball boundary vector in a maximizing eigendirection attains the worst coverage.

**Sharp half-order transition.** Set \(n=m=2\), \(B_t=\operatorname{diag}(1,t)\), \(A_t=B_t^{1/2}\), \(\omega=1/2\), and hold \(K,M,\sigma,\alpha,\nu\) fixed as \(t\downarrow0\). Then

\[
\begin{aligned}
0<\nu<1/2:&\quad
 r_*(t)\sim \frac{2M}{\sigma K}t^{\nu-1/2}\longrightarrow\infty,\\
\nu=1/2:&\quad \Delta_K(t)\longrightarrow\frac{2M}{\sigma K},\\
\nu>1/2:&\quad \Delta_K(t)\longrightarrow
\frac{M}{\sigma}\frac{2^{-K}}{1-2^{-K}}>0.
\end{aligned}
\]

In the last two cases the sharp radius tends to a finite positive noncentral-chi-square quantile. By contrast, even a triangle-inequality radius built using the **exact** Euclidean bias supremum instead of an overestimate diverges as \(\Theta(t^{-1/2})\) for every fixed \(\nu>0\). Thus the sufficient radius of Abhishek and Holman, Theorem 3.6, can be arbitrarily conservative; at and above the half-order threshold it diverges while the smallest valid covariance-aligned radius remains bounded.

## Assumptions and scope
Let \(\lambda_1,\ldots,\lambda_n>0\) be the eigenvalues of \(B\). Fix \(K\ge1\), \(\nu,M,\sigma>0\), \(0<\alpha<1\), and \(0<\omega\lambda_{\max}(B)<1\). Define \(G=I-\omega B\) and the Landweber map \(x_0=0\), \(x_{j+1}=x_j+\omega A^{\mathsf T}(y-Ax_j)\). Define

\[
\Gamma_K=\sigma^2 B^{-1}(I-G^K)^2,
\qquad \mathcal E_r(y)=\{u\in\mathbb R^n:\|\Gamma_K^{-1/2}(u-x_K(y))\|_2\le r\}.
\]

Full column rank and the strict step restriction ensure \(\Gamma_K\succ0\). The phrase *smallest radius* always refers to this specified centered, fixed-shape family \(\mathcal E_r\), not arbitrary confidence sets, data-dependent radius choices, or an unknown covariance estimated from randomized low-rank factors. The finite-dimensional source ball varies with \(B\); it is the same mathematically defined smoothness class used in source-condition regularization theory.

## Proof
**1. Exact error and covariance.** The finite geometric sum gives

\[
x_K=(I-G^K)x^\dagger+(I-G^K)B^{-1}A^{\mathsf T}\varepsilon.
\]

Therefore \(x^\dagger-x_K=G^K B^\nu w-Z\), where \(Z\) is centered Gaussian with covariance \(\Gamma_K\) as displayed above (the sign of \(Z\) is immaterial). Orthogonally diagonalize \(B=U\operatorname{diag}(\lambda_i)U^{\mathsf T}\). The eigenvalues of \(\Gamma_K\) are

\[
\gamma_i=\sigma^2\frac{[1-(1-\omega\lambda_i)^K]^2}{\lambda_i}>0.
\]

**2. Maximized noncentrality.** The squared Mahalanobis norm of the deterministic error mean is

\[
\big\|\Gamma_K^{-1/2}G^KB^\nu w\big\|_2^2
=\sum_{i=1}^n
\left[\frac{(1-\omega\lambda_i)^K\lambda_i^{\nu+1/2}}
{\sigma[1-(1-\omega\lambda_i)^K]}\right]^2
 (U^{\mathsf T}w)_i^2.
\]

Over \(\|w\|_2\le M\) this has maximum \(\Delta_K^2\), attained at \(w=M Ue_i\) for an eigenvalue maximizing the displayed ratio. For a fixed \(w\), the squared whitened reconstruction error has exactly the noncentral chi-square distribution \(\chi_n^2(d(w)^2)\).

**3. Worst coverage and minimality.** For every \(r>0\), the CDF \(F_{n,d^2}(r^2)\) is strictly decreasing as \(d^2\) increases. One proof uses the classical Poisson mixture: \(\chi_n^2(d^2)\) is a mixture of central \(\chi_{n+2J}^2\) laws with \(J\sim\operatorname{Poisson}(d^2/2)\); increasing the Poisson parameter strictly shifts mass toward distributions obtained by adding independent squared standard normals. Hence

\[
\inf_{\|w\|_2\le M}\Pr_{B^\nu w}\{x^\dagger\in\mathcal E_r(Y)\}
=F_{n,\Delta_K^2}(r^2).
\]

The right side is continuous and strictly increasing in \(r>0\), from zero to one. Its unique \((1-\alpha)\)-quantile is therefore both sufficient and necessary. No independence among different candidate truths is required: coverage is evaluated separately for each fixed truth.

**4. Singular-spectrum transition.** For \(B_t=\operatorname{diag}(1,t)\), \(\omega=1/2\), put

\[
h_{K,\nu}(\lambda)=\frac{(1-\lambda/2)^K\lambda^{\nu+1/2}}{1-(1-\lambda/2)^K}.
\]

As \(t\downarrow0\), the binomial expansion gives

\[
h_{K,\nu}(t)=\frac{2}{K}t^{\nu-1/2}(1+O(t)),
\qquad h_{K,\nu}(1)=\frac{2^{-K}}{1-2^{-K}}.
\]

When \(\nu=1/2\), \(2/K\ge 2^{-K}/(1-2^{-K})\). This follows from \(1-2^{-K}=\sum_{j=1}^K2^{-j}\ge K2^{-K}\): every summand is at least \(2^{-K}\). Thus at this threshold \(\Delta_K\to2M/(\sigma K)\). For \(\nu<1/2\) the vanishing eigenvalue dominates, giving \(\Delta_K(t)\sim2Mt^{\nu-1/2}/(\sigma K)\). Since \(\big|\|N(0,I_n)+\mu\|_2-\|\mu\|_2\big|\le\|N(0,I_n)\|_2\), the fixed-level quantile divided by \(\|\mu\|_2\) tends to one as \(\|\mu\|_2\to\infty\), proving the claimed asymptotic for \(r_*\). For \(\nu>1/2\), the small-eigenvalue contribution vanishes and only \(h_{K,\nu}(1)\) remains. Continuity of the noncentral chi-square quantile handles the two bounded regimes.

**5. Comparison with normwise bias inflation.** In the same family, the exact Euclidean bias supremum is

\[
 b_K(t)=M\max\{2^{-K},(1-t/2)^K t^\nu\}\longrightarrow M2^{-K}>0.
\]

Meanwhile the smaller eigenvalue of the covariance is \(\gamma_{\min}(t)=\sigma^2[1-(1-t/2)^K]^2/t\sim\sigma^2 K^2t/4\). Thus the common triangle-inequality inflation \(b_K(t)/\sqrt{\lambda_{\min}(\Gamma_K)}\sim(2M2^{-K}/(\sigma K))t^{-1/2}\). Using a looser upper bound on \(b_K\) only increases this radius. The sharp radius grows strictly more slowly for \(0<\nu<1/2\) and stays bounded for \(\nu\ge1/2\), completing the contrast.

## Verification
The standalone `verify_landweber.py` checks the full covariance geometric-sum identity, spectral maximization of the whitened bias, coverage at the noncentral quantile, and singular-spectrum limits for multiple dimensions and smoothness exponents. The code uses exact formulas and numerical linear algebra, but finite tests do not establish the universal theorem. All limiting statements above follow analytically from the binomial expansion and quantile convergence.

## Relationship to prior work
Abhishek and Holman (arXiv:2610.00882v1, §3.3–3.5, especially Theorem 3.6) already obtain the exact Gaussian reconstruction-error covariance, the Euclidean source-condition bias estimate, and a valid ellipsoid by combining central chi-square quantiles with a triangle-inequality inflation. Their work also develops randomized low-rank approximations for practical pixelwise uncertainty. Those are prior results, not new claims here. The result above adds an exact *source-ball worst-case* noncentrality and optimal radius within the specified ellipsoid family, together with the sharp \(\nu=1/2\) singular-spectrum transition and quantified degeneration of normwise inflation.

General noncentral chi-square distributions, Gaussian confidence balls, and spectral regularization are classical. In particular Baraud's *Confidence balls in Gaussian regression* (2004) studies Gaussian confidence balls under a different statistical parameter setting, and Stark's *Affine minimax confidence intervals for a bounded normal mean* (1992) treats minimax bounded-mean intervals. The novel claim is **not** invention of noncentral chi-square calibration or global optimality among all possible confidence sets; it is the explicit Landweber/source-ball sharp spectral calibration and its singular-spectrum consequence. The related classical literature creates an acknowledged residual overlap risk.

## Limitations
The theorem requires exact covariance, deterministic \(K\) and \(\omega\), known \(M,\nu,\sigma\), positive definite normal matrix, strict nonnegative Landweber filter \(0<\omega\lambda_{\max}(B)<1\), and Gaussian isotropic observation noise. It does not assess estimated smoothness, approximate or randomized covariance, data-dependent stopping, global confidence-set optimality, or infinite-dimensional singular covariance operators. The sharp family \(B_t\) approaches rank deficiency without reaching it; each \(t>0\) remains full rank. Confidence coverage is frequentist, not a posterior probability assigned to a fixed truth after observing data.

## References
- A. Abhishek and S. Holman, *Uncertainty Quantification for Landweber Iteration with Randomized Normal-Operator Approximation*, arXiv:2610.00882v1 (first posted 2026-10-01), §§3.3–3.6, https://arxiv.org/html/2610.00882v1 .
- Y. Baraud, *Confidence balls in Gaussian regression*, *Annals of Statistics* **32** (2004), 528–551, arXiv:math/0406425, https://arxiv.org/abs/math/0406425 .
- P. B. Stark, *Affine minimax confidence intervals for a bounded normal mean*, *Statistics & Probability Letters* **13** (1992), 39–44, https://doi.org/10.1016/0167-7152(92)90234-V .
