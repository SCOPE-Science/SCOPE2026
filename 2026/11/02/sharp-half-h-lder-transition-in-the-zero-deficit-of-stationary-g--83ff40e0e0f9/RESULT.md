# Sharp half-Hölder transition in the zero deficit of stationary Gaussian power series

## Finding

Let \(0<\alpha<1\), \(a>0\), and \(c>0\). Equip the unit circle with the strictly positive, continuous spectral density
\[
w_\alpha(\theta)=a+c\left|2\sin\frac{\theta}{2}\right|^\alpha,\qquad -\pi\le\theta\le\pi,
\]
extended periodically. Let \(\{\xi_n\}_{n\in\mathbb Z}\) be a centered, proper, stationary complex Gaussian sequence with spectral measure \(w_\alpha(\theta)d\theta/(2\pi)\). Put \(f(z)=\sum_{n\ge0}\xi_nz^n\), and let \(N(r)\) count its zeros in \(|z|<r\), with multiplicity. Define its deficit relative to independent Gaussian coefficients by
\[
B_\alpha(r)=\frac{r^2}{1-r^2}-\mathbb E N(r).
\]
Then \(B_\alpha(r)\) increases to a finite, strictly positive constant \(B_\alpha^*\) as \(r\uparrow1\). Writing \(\varepsilon=1-r\), there is a sharp trichotomy:
\[
B_\alpha^*-B_\alpha(r)\sim
\begin{cases}
\displaystyle \frac{c^2}{a^2}\frac{2^{2\alpha}\Gamma(1-2\alpha)}{2\alpha}
\left(\frac{\Gamma(\alpha+1)\sin(\pi\alpha/2)}{\pi}\right)^2\varepsilon^{2\alpha},&0<\alpha<\tfrac12,\\[8pt]
\displaystyle \frac{c^2}{4\pi a^2}\varepsilon\log\frac1\varepsilon,&\alpha=\tfrac12,\\[8pt]
\displaystyle Q_\alpha\varepsilon,&\tfrac12<\alpha<1.
\end{cases}
\]
Here \(Q_\alpha\) is the positive, finite, globally determined constant
\[
Q_\alpha=\frac1{4\pi}\int_{-\pi}^{\pi}
\frac{|w_\alpha'(\theta)|^2+\bigl|(|D|w_\alpha)(\theta)\bigr|^2}{w_\alpha(\theta)^2}\,d\theta,
\]
where \(|D|\) multiplies the Fourier coefficient of frequency \(k\) by \(|k|\). All asymptotic constants are strictly positive. The leading constant is local (depends only on \(a,c,\alpha\)) up to and including the critical exponent, but is a global boundary energy above it.

## Assumptions and scope

The spectral measure is absolutely continuous and strictly positive everywhere. The single cusp is at angle zero. We assume \(0<\alpha<1\) and \(a,c>0\); the law is not asserted for vanishing spectral densities, jumps, spectral atoms, or cusp exponents outside this range. Existence of the stationary proper Gaussian sequence follows from the nonnegative spectral measure. Its marginal variance need not equal one; rescaling the process has no effect on zeros or on the deficit. The Gaussian power series converges almost surely on \(|z|<1\).

Let \(P_s(\theta)=(1-s^2)/(1-2s\cos\theta+s^2)\) denote the Poisson kernel and write
\[
U(s,\theta)=\frac1{2\pi}\int_{-\pi}^{\pi}P_s(\theta-t)w_\alpha(t)\,dt,
\qquad 0\le s<1.
\]
Define the finite energy
\[
B_\alpha^*=\frac1{4\pi}\int_{|z|<1}|\nabla\log U(z)|^2\,dA(z).
\]
In the last display \(U(z)=U(|z|,\arg z)\), and \(dA\) is unnormalized Euclidean area. The integral defines the constant; no closed formula is claimed for it in the nonlinear case.

## Proof

**1. Exact Gaussian-to-harmonic-energy identity.** Stationarity and the geometric series give the covariance on the diagonal,
\[
\mathbb E|f(z)|^2=\frac{U(z)}{1-|z|^2}.
\]
The standard Gaussian zero-intensity identity gives \((4\pi)^{-1}\Delta\log\mathbb E|f|^2\). Since \(U\) is positive and harmonic,
\[
\Delta\log U=-\frac{|\nabla U|^2}{U^2}=-|\nabla\log U|^2.
\]
Integration on the radius-\(r\) disk therefore proves the **exact**, not asymptotic, identity
\[
B_\alpha(r)=\frac1{4\pi}\int_{|z|<r}\frac{|\nabla U(z)|^2}{U(z)^2}\,dA(z).
\tag{1}
\]
As \(U\ge a\), this shows monotonicity and nonnegativity. Write \(g_\alpha(\theta)=|2\sin(\theta/2)|^\alpha\). Then \(U=a+cP_s*g_\alpha\), and the nonconstant Fourier coefficients are those of \(cg_\alpha\).

**2. Exact Fourier coefficients and the unweighted shell.** With \(g_{\alpha,k}=(2\pi)^{-1}\int_{-\pi}^{\pi}g_\alpha(\theta)e^{-ik\theta}\,d\theta\), the beta integral and reflection formula yield, for each integer \(k\ge1\),
\[
g_{\alpha,k}= -A_\alpha\frac{\Gamma(k-\alpha/2)}{\Gamma(k+1+\alpha/2)},
\qquad A_\alpha=\frac{\Gamma(1+\alpha)\sin(\pi\alpha/2)}{\pi}>0.
\tag{2}
\]
In particular \(g_{\alpha,k}=-A_\alpha k^{-1-\alpha}(1+O_\alpha(k^{-1}))\). Parseval for radial and angular derivatives of the harmonic Poisson series, integrated over a shell, gives
\[
\frac1{4\pi}\int_{r<|z|<1}|\nabla (P*g_\alpha)(z)|^2\,dA(z)
=\sum_{k\ge1}k|g_{\alpha,k}|^2(1-r^{2k})=:S_\alpha(r).
\tag{3}
\]
Consequently \(\sum_{k\ge1}k|g_{\alpha,k}|^2<\infty\) for every \(\alpha>0\). Together with \(U\ge a\), equation (1) implies \(B_\alpha^*<\infty\). It is positive because \(g_\alpha\) is not constant.

For \(0<\alpha<1/2\), the gamma-ratio asymptotic and Riemann-sum convergence give
\[
S_\alpha(1-\varepsilon)\sim A_\alpha^2\varepsilon^{2\alpha}
\int_0^\infty\frac{1-e^{-2t}}{t^{1+2\alpha}}\,dt
=A_\alpha^2\frac{2^{2\alpha}\Gamma(1-2\alpha)}{2\alpha}\varepsilon^{2\alpha}.
\tag{4}
\]
Convergence at zero holds because \(2\alpha<1\), and convergence at infinity because \(\alpha>0\). At \(\alpha=1/2\), split the sum at \(k\asymp\varepsilon^{-1}\); using \(k|g_{1/2,k}|^2=A_{1/2}^2k^{-2}(1+O(k^{-1}))\) yields
\[
S_{1/2}(1-\varepsilon)=2A_{1/2}^2\varepsilon\log(1/\varepsilon)+O(\varepsilon),
\qquad A_{1/2}^2=\frac1{8\pi}.
\tag{5}
\]
For completeness, equation (4) follows by comparing \(r^{2k}\) with \(e^{-2\varepsilon k}\) and applying dominated convergence to the rescaled sum; finitely many low frequencies contribute only \(O(\varepsilon)\). In equation (5), frequencies above \(\varepsilon^{-1}\) contribute \(O(\varepsilon)\), while the harmonic sum below that scale produces \(\log(1/\varepsilon)\).

**3. Localization of the nonlinear denominator.** Fix a small angle \(\delta>0\), and divide the outer shell into \(|\theta|<\delta\) and \(|\theta|\ge\delta\). Away from the unique cusp, \(g_\alpha\) is smooth. Its Poisson extension has bounded first derivatives, uniformly as its radius tends to one, on every fixed closed arc that avoids zero. (For example, use the principal-value singular-integral formula for \(|D|g_\alpha\) and smoothness on that arc.) Thus the unweighted and weighted shell energies on \(|\theta|\ge\delta\) are both \(O_\delta(\varepsilon)\).

On \(|\theta|<\delta\), uniform boundary convergence of the Poisson extension of the continuous function \(g_\alpha\) gives, throughout the shell for sufficiently small \(\varepsilon\),
\[
a\le U(z)\le a+c(2\sin(\delta/2))^\alpha+o_{\varepsilon\to0}(1).
\]
Sandwich the integrand in (1) between the reciprocals of the squares of these bounds, multiplied by \(c^2|\nabla(P*g_\alpha)|^2\). For \(0<\alpha\le1/2\), equations (4)–(5) give \(\varepsilon=o(S_\alpha(1-\varepsilon))\). The outer-arc contributions therefore disappear in the normalized ratio. First let \(\varepsilon\downarrow0\), then \(\delta\downarrow0\), to obtain
\[
B_\alpha^*-B_\alpha(1-\varepsilon)
\sim \frac{c^2}{a^2}S_\alpha(1-\varepsilon).
\tag{6}
\]
Combining (4)–(6) proves both singular and critical constants, including \(2A_{1/2}^2=1/(4\pi)\).

**4. Regular regime.** When \(\alpha>1/2\), \(\sum_{k\ne0}k^2|w_{\alpha,k}|^2<\infty\). By Parseval, the radial and angular first derivatives of \(U\) converge in boundary \(L^2\) to \(-|D|w_\alpha\) and \(w_\alpha'\), respectively, as the radius tends to one. Also \(U\to w_\alpha\) uniformly and \(w_\alpha\ge a\). Thus the circle-averaged energy converges to the finite boundary integral defining \(Q_\alpha\). Integrating across a shell of width \(\varepsilon\), accounting for the polar-area factor \(s\to1\), yields
\[
B_\alpha^*-B_\alpha(1-\varepsilon)
=Q_\alpha\varepsilon+o(\varepsilon).
\]
Since \(w_\alpha\) is nonconstant, \(Q_\alpha>0\). This proves the final regime and completes the trichotomy.

## Verification

The accompanying standalone checker `cusp_checker_std.py` uses only the Python standard library. It independently evaluates low Fourier coefficients using midpoint quadrature and compares them to the gamma-function identity and its recurrence; it also evaluates finite Fourier-shell sums against the predicted singular and critical constants. It passed 40 deterministic finite checks. In particular, at \(\varepsilon=10^{-4}\), the ratios of computed unweighted-shell energy to the leading predicted term were approximately \(0.99451\), \(0.86383\), and \(1.05528\) for \(\alpha=1/4\), \(\alpha=2/5\), and \(\alpha=1/2\), respectively. The slower convergence for the exponent near \(1/2\) is consistent with a regular lower-order contribution. Numerical tests are **not** used as a substitute for the Fourier, localization, or boundary-convergence proofs.

## Relationship to prior work

Noda and Shirai (2021, arXiv:2106.02860; subsequently published) established the stationary-Gaussian covariance and expected-zero framework, plus exact asymptotics for finitely dependent sequences whose trigonometric-polynomial spectral densities may vanish. Those formulas are not a finite-deficit *convergence-rate* law for a strictly positive, nondifferentiable cusp. Shirai (2025, arXiv:2501.02586), Theorem 2.1, gives fixed-direction density asymptotics under spectral smoothness at the approached direction and does not cover a cusp at that direction or the integrated three-regime shell law. The earlier Mukeru–Mulaudzi–Nzabanita–Mpanda (2020) work treats fractional Gaussian noise and is cited in Noda–Shirai for a general zero-count estimate; that model has a different near-zero spectral baseline. Full-text access to that earlier paper was not obtained during the literature inspection, leaving a residual priority risk. The logarithmic effect of actual jumps is distinct: this theorem concerns a continuous density, a finite limiting deficit, and the sharp way that limit is approached. Standard Fourier–Sobolev estimates motivate the exponent, but do not alone supply the weighted Gaussian zero-count coefficient or its nonlinear localization argument.

## Limitations

The formula concerns the **expectation** of zeros, not almost-sure asymptotics, fluctuations, higher correlation functions, or the zero process distribution. Only a single explicit positive spectral cusp, exponents \(0<\alpha<1\), and radial disks are treated. The constant \(B_\alpha^*\) is defined by an energy integral; no elementary closed form is claimed. The \(\alpha>1/2\) linear coefficient is inherently global. Independent mathematical audit has not been performed. Existing unindexed treatments of rough spectral data remain a historical-priority risk.

## References

1. K. Noda and T. Shirai, *Expected number of zeros of random power series with finitely dependent Gaussian coefficients*, arXiv:2106.02860, first public 2021-06-05; Journal of Theoretical Probability 36 (2023), 1534–1554.
2. T. Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients*, arXiv:2501.02586, first public 2025-01-05; in particular Theorem 2.1 and Example 2.4.
3. S. Mukeru, M. P. Mulaudzi, J. Nzabanita and M. M. Mpanda, *Zeros of Gaussian power series with dependent random variables*, Illinois Journal of Mathematics 64 (2020), 569–582, DOI: 10.1215/00192082-8720490. Referenced for scope and historical comparison; relevant full text was not accessible during inspection.
