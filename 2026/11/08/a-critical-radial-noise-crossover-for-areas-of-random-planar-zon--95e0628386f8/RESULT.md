# A critical radial-noise crossover for areas of random planar zonotopes

## Finding

Let \(\Theta_1,\Theta_2,\ldots\) be independent, uniform directions in \([0,2\pi)\). Independently, let \(\xi_1,\xi_2,\ldots\) be independent copies of a bounded, real random variable with \(\mathbb E\xi=0\) and \(v=\mathbb E\xi^2>0\). Fix \(r>0\), \(\tau>0\), and \(\beta\ge0\). For every sufficiently large integer \(n\), form the planar random zonotope
\[
 Z_{n,\beta}=\sum_{i=1}^n[0,R_{i,n}u(\Theta_i)],\qquad
 R_{i,n}=r(1+\tau n^{-\beta}\xi_i),\quad
 u(\theta)=(\cos\theta,\sin\theta),
\]
where all \(R_{i,n}>0\). For \(\beta=0\), additionally assume \(\tau\|\xi\|_\infty<1\). Let \(A_{n,\beta}\) be its Euclidean area and \(\alpha=2/\pi\). The exact expectation, for every admissible \(n\ge2\), is
\[
 \mathbb E A_{n,\beta}=\alpha r^2\binom n2.
\]
Define an \(L^2\)-convergent, non-Gaussian series with independent unit exponential variables \(E_1,E_2,\ldots\):
\[
 Q_r=-\frac{2r^2}{\pi}\sum_{m=1}^\infty\frac{E_m-1}{4m^2-1}.
\]
Let \(G\sim N(0,1)\) be independent of the series. Then the **complete crossover** is
\[
\begin{array}{ll}
0\le\beta<1/2:&\displaystyle
 n^{\beta-3/2}\left(A_{n,\beta}-\mathbb EA_{n,\beta}\right)
 \ \Longrightarrow\ N\!\left(0,\alpha^2r^4\tau^2v\right),\\[5pt]
\beta=1/2:&\displaystyle
 n^{-1}\left(A_{n,1/2}-\mathbb EA_{n,1/2}\right)
 \ \Longrightarrow\ Q_r+\alpha r^2\tau\sqrt v\,G,\\[5pt]
\beta>1/2:&\displaystyle
 n^{-1}\left(A_{n,\beta}-\mathbb EA_{n,\beta}\right)
 \ \Longrightarrow\ Q_r.
\end{array}
\]
At the critical exponent \(\beta=1/2\), the Gaussian and non-Gaussian terms are **independent**, and neither disappears. In particular, radial standard deviation of order \(n^{-1/2}\) is the sharp transition scale. The exponential series has variance \(r^4(1/4-2/\pi^2)\), strictly negative third cumulant, and essential supremum \(r^2/\pi\).

## Assumptions and scope

All randomness is on one probability space with independent sequences of directions and radial noises. The noise is bounded, centered, and has strictly positive variance. The coupling with \(n\) is explicit: for every row \(n\), use the first \(n\) variables but radii depend on \(n\). Positivity of the radii is required, and holds automatically eventually when \(\beta>0\). No Gaussian hypothesis on radial noise is made; the Gaussian component is a central-limit outcome. The area is the ordinary Lebesgue area in \(\mathbb R^2\), not normalized by \(n^2\). All convergence statements are in distribution as \(n\to\infty\).

## Proof

**1. Determinantal area formula.** The Minkowski sum of \(n\) segments in the plane has area
\[
 A_{n,\beta}=\sum_{1\le i<j\le n} |\det(R_{i,n}u(\Theta_i),R_{j,n}u(\Theta_j))|
 =\sum_{i<j}R_{i,n}R_{j,n}|\sin(\Theta_i-\Theta_j)|.
\]
This follows, for instance, by repeatedly adding a segment and integrating the width perpendicular to it; induction yields the sum of parallelogram areas. Since the angular difference is uniform, \(\mathbb E|\sin(\Theta_i-\Theta_j)|=\alpha\), proving the mean.

**2. Exact projection and variance.** Write \(h_n(z_i,z_j)=R_{i,n}R_{j,n}|\sin(\Theta_i-\Theta_j)|\), \(\mu_n=\alpha r^2\), and \(g_n(z_i)=\alpha r(R_{i,n}-r)\). Conditional expectation gives \(\mathbb E[h_n(z_i,Z_j)\mid z_i]-\mu_n=g_n(z_i)\). The Hoeffding decomposition is the *exact identity*
\[
 A_{n,\beta}-\mathbb E A_{n,\beta}
 =(n-1)\sum_{i=1}^n g_n(z_i)+D_n,
\quad D_n=\sum_{i<j}\bigl(h_n(z_i,z_j)-\mu_n-g_n(z_i)-g_n(z_j)\bigr).
\]
The kernel in \(D_n\) has zero conditional mean at either argument, so its pair terms are uncorrelated, including pairs sharing one index. Moreover \(D_n\) is uncorrelated with the first sum. Put \(q_n=\tau^2vn^{-2\beta}\). Directly evaluating \(\mathbb E\sin^2=1/2\) yields
\[
 \operatorname{Var}(A_{n,\beta})=
 \binom n2r^4\left[\frac{(1+q_n)^2}{2}-\alpha^2\right]
 +6\binom n3\alpha^2r^4q_n.
\]
The first-order term alone has variance
\(n(n-1)^2\alpha^2r^4q_n\). Its remainder has variance
\[
 \operatorname{Var}(D_n)=\binom n2r^4\left[\frac{(1+q_n)^2}{2}-\alpha^2-2\alpha^2q_n\right].
\]
These formulas are exact for all admissible finite \(n\), not asymptotic estimates.

**3. Fixed-length angular fluctuation law.** At radius \(r\), the angular kernel \(r^2|\sin(x-y)|\) has constant first Hoeffding projection. Its absolutely convergent Fourier series is
\[
 |\sin t|=\frac2\pi-\frac4\pi\sum_{m=1}^\infty\frac{\cos(2mt)}{4m^2-1}.
\]
With \(S_{m,n}=\sum_{j=1}^n e^{2im\Theta_j}\), the centered fixed-radius area \(A_n^{(0)}\) therefore satisfies the **exact finite-\(n\) identity**
\[
 \frac{A_n^{(0)}-\mathbb EA_n^{(0)}}n
 =-\frac{2r^2}{\pi}\sum_{m\ge1}\frac{|S_{m,n}|^2/n-1}{4m^2-1}.
\]
For every fixed \(M\), the multivariate real central limit theorem for the \(2M\) orthogonal Fourier coordinates shows that \((|S_{m,n}|^2/n)_{m\le M}\) converges jointly to \(M\) independent unit exponentials. The discarded Fourier tail has variance bounded, *uniformly in \(n\ge2\)*, by
\[
 \frac{4r^4}{\pi^2}\sum_{m>M}(4m^2-1)^{-2}.
\]
Indeed the centered cosine kernels for distinct harmonics are pairwise orthogonal and are individually degenerate. This bound tends to zero, proving convergence to \(Q_r\) without relying on a finite harmonic cutoff as a proof. Furthermore
\[
 \sum_{m\ge1}(4m^2-1)^{-1}=\frac12,\qquad
 \sum_{m\ge1}(4m^2-1)^{-2}=\frac{\pi^2-8}{16}.
\]
Thus \(Q_r\) has variance \(r^4(1/4-2/\pi^2)\), and its third cumulant is
\[-2\sum_{m\ge1}\left(\frac{2r^2}{\pi(4m^2-1)}\right)^3<0.\]
Each summand is bounded above by its positive coefficient, giving \(Q_r\le r^2/\pi\). The bound is the essential supremum: constrain finitely many independent exponentials to be arbitrarily close to zero and control the independent mean-zero tail by its vanishing variance.

**4. Sharp triangular-array crossover.** Define \(D_n^{(0)}\) as the fixed-radius degenerate sum using the *same* directions \(\Theta_i\). Because \(\xi\) is bounded, the centered degenerate kernels obey
\[
 \mathbb E\bigl[\bigl(d_n(Z_1,Z_2)-d_0(\Theta_1,\Theta_2)\bigr)^2\bigr]
 =O(n^{-2\beta})\quad\text{for }\beta>0.
\]
Pairwise orthogonality implies \(\|D_n-D_n^{(0)}\|_2=O(n^{1-\beta})\). Consequently, for \(\beta>0\), the difference divided by \(n\) vanishes in \(L^2\). For every \(\beta\ge0\), the first term in the decomposition has the explicit form
\[
 (n-1)\sum_i g_n(Z_i)
 =(n-1)\alpha r^2\tau n^{-\beta}\sum_{i=1}^n\xi_i.
\]
The ordinary central limit theorem gives \(n^{-1/2}\sum_i\xi_i\Rightarrow N(0,v)\). If \(\beta<1/2\), \(\|D_n\|_2=O(n)\) is negligible on the larger scale \(n^{3/2-\beta}\); the radial term gives the first limit. If \(\beta>1/2\), the radial term is negligible on scale \(n\), and step 3 gives the third limit. At \(\beta=1/2\), both terms survive: the angular limit depends only on \((\Theta_i)\), while the Gaussian radial limit depends only on \((\xi_i)\); these sequences are independent for every \(n\), proving independence in their joint limit and the middle formula.

## Verification

Reproduce with `python verify_zonogon.py` (Python 3, NumPy). The verifier directly computes planar Minkowski-sum hull areas from all segment-endpoint subset sums for 126 small cases, comparing with the determinantal formula. It checks the exact Fourier tail constants, exact mean and variance against independent random-angle sampling at three sizes, the non-Gaussian limiting-series variance and third cumulant, and all four finite-\(n\) radial-noise regimes \(\beta\in\{0,1/4,1/2,3/4\}\) at \(n=90\). The exact proof above, not the numerical trials, supplies the infinite-\(n\) conclusion.

## Relationship to prior work

Vitale's 1991 work provides the expected absolute determinant/zonoid framework, not this triangular fluctuation law. Donoho and Tanner's 2008 preprint studies face counts of random cube images (which are zonotopes), not their area fluctuation crossover. Schneider's 2022 full-text study proves a Gaussian limit for a *fixed* generator law under a nondegeneracy condition; its Theorem 3 does not cover generator radii shrinking toward a fixed length with \(n\). De Wet's 1987 paper surveys the general degenerate U-statistic spectral theorem; Silverman's 1978 circle-distance study gives relevant fixed-circle empirical-process behavior. Those general results are acknowledged; the claimed additional content is the **geometric triangular critical scale and independent Gaussian–exponential-series convolution**, with exact radial-angular variance splitting. Fixed-length non-Gaussian behavior alone is not claimed novel.

## Limitations

The theorem is restricted to planar zonotopes with independent uniform angles and bounded independent radial noise. Boundedness is sufficient for the stated proof, not asserted necessary. The crossover is pointwise in each fixed exponent \(\beta\), not a Berry–Esseen bound uniform in \(\beta\) or in \(\tau\). It does not provide a finite-sample density for area, or extend to higher-dimensional volumes. The full 1978 Silverman article and full 1991 Vitale article were not retrieved during the literature comparison; historical priority remains provisional. Independent scientific validation has not been performed.

## References

1. T. de Wet, “Degenerate U- and V-statistics,” *South African Statistical Journal* **21** (1987), 99–129; DOI: 10.37920/sasj.1987.21.2.1. Issue dated 1987 (original public release day not independently established).
2. B. W. Silverman, “Distances on circles, toruses and spheres,” *Journal of Applied Probability* **15** (1978), 136–143; DOI: 10.2307/3213243.
3. R. A. Vitale, “Expected Absolute Random Determinants and Zonoids,” *Annals of Applied Probability* **1** (1991), 293–300; DOI: 10.1214/aoap/1177005938.
4. D. Donoho and J. Tanner, “Counting the Faces of Randomly-Projected Hypercubes and Orthants, with Applications,” arXiv:0807.3590, first posted 2008-07-23.
5. R. Schneider, “Random zonotopes and valuations,” arXiv:2202.06774, first posted 2022-02-14; Theorem 3 and Section 4.
