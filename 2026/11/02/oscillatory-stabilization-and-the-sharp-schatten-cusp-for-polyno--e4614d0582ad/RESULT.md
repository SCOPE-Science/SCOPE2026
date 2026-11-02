# Oscillatory stabilization and the sharp Schatten cusp for polynomially damped Gaussian Fock operators

## Finding
Fix \(s>1\), \(\tau>0\), and \(c\in\mathbb C\) with \(\operatorname{Re}(1-c)>0\), and let \(a=1-c\) and \(r=(s|a|)^{-1}\). On the normalized Gaussian Bargmann–Fock space in one complex variable, define on analytic polynomials
\[
(\mathcal T_{s,c,\tau}f)(z)=\frac1{\sqrt s}\int_{\mathbb C}e^{z\overline w/s}(1+|w|^2)^{-\tau}e^{c|w|^2}f(w)\,\frac{e^{-|w|^2}}{\pi}\,dA(w).
\]
The operator has a unique bounded extension precisely when \(r\le1\). For \(r<1\), this extension belongs to every Schatten class \(\mathcal S_p\), \(p>0\). At the critical boundary \(r=1\), it is compact, with singular values
\[
\sigma_j\sim s^{1/2-\tau}j^{-\tau},
\]
and belongs to \(\mathcal S_p\) **exactly when** \(p\tau>1\); it lies in the endpoint weak Schatten class \(\mathcal S_{1/\tau,\infty}\), but not the strong class \(\mathcal S_{1/\tau}\). Equivalently, its singular-value counting function satisfies
\[
N(\varepsilon)\sim \left(\frac{s^{1/2-\tau}}{\varepsilon}\right)^{1/\tau}\qquad(\varepsilon\downarrow0).
\]
There is also an exact approach-to-criticality law. Fix a critical \(a_*\) with \(\operatorname{Re}a_*>0\) and \(|a_*|=1/s\), and for \(0<\rho<1\) set \(a_\rho=a_*/\rho\), \(c_\rho=1-a_\rho\), \(C=s^{1/2-\tau}\), and \(\alpha=p\tau\). Then, as \(\rho\uparrow1\),
\[
\|\mathcal T_{s,c_\rho,\tau}\|_{\mathcal S_p}^p\sim
\begin{cases}
C^p\Gamma(1-\alpha)[p(1-\rho)]^{\alpha-1},&0<\alpha<1,\\
C^p\log\!\dfrac1{1-\rho},&\alpha=1.
\end{cases}
\]
For \(\alpha>1\), these norms instead converge to the finite critical Schatten norm. The leading coefficients and critical exponents do **not** depend on the complex argument of \(a_*\).

For example, choose \(1<s<2\) and \(1-1/s<\beta<1/2\). The positive symbol with \(c=\beta\) gives an unbounded operator, whereas the **same-modulus** chirped symbol with \(c=\beta+i\theta\) gives a compact operator in all \(\mathcal S_p\) whenever \(|\theta|>\sqrt{s^{-2}-(1-\beta)^2}\). Equality corresponds to the critical polynomial Schatten threshold. Thus quadratic oscillations can restore arbitrarily strong compactness without changing the pointwise modulus of an exponentially growing symbol.

## Assumptions and scope
The Hilbert space is \(\mathcal F^2(\mathbb C)\), with norm \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(w)|^2e^{-|w|^2}dA(w)\); its normalized monomials are \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\). We only define the initial integral operator on **polynomials**, where it is absolutely convergent for each \(z\) because \(\operatorname{Re}a>0\). Whenever bounded, its extension is by Hilbert-space continuity. No assertion that the unbounded multiplier defines a naive whole-space Toeplitz product is made. The exponential kernel is a fixed radial specialization of the two-parameter integral-kernel setting.

The exact diagonal eigenvalues on the basis are
\[
\lambda_n=\frac{s^{-n-1/2}}{n!}\int_0^\infty \frac{x^n e^{-a x}}{(1+x)^\tau}\,dx
=\frac{s^{-n-1/2}}{\Gamma(\tau)}\int_0^\infty\frac{u^{\tau-1}e^{-u}}{(a+u)^{n+1}}\,du.
\]
Here complex powers use the analytic principal logarithm on the right half-plane. The full asymptotic, for every fixed admissible \(s,a,\tau\), is
\[
\lambda_n=s^{-1/2}a^{\tau-1}(sa)^{-n}n^{-\tau}\bigl(1+O_{s,a,\tau}(n^{-1})\bigr).
\]
All claims are for fixed parameters except the explicitly stated uniform compact-side approach along \(a_\rho\). The Schatten results apply to every real \(p>0\), including quasi-Banach exponents.

## Proof
**Diagonalization and the exact multiplier.** Insert \(e_n\) into the integral and expand \(e^{z\overline w/s}\) into its power series. Angular orthogonality kills every term except the one of degree \(n\). The radial substitution \(x=|w|^2\) gives the first exact integral for \(\lambda_n\). Apply the Gamma–Laplace identity
\[
(1+x)^{-\tau}=\frac1{\Gamma(\tau)}\int_0^\infty u^{\tau-1}e^{-u(1+x)}\,du,
\]
then evaluate \(\int_0^\infty x^n e^{-(a+u)x}dx=n!(a+u)^{-n-1}\). Absolute integrability for \(\operatorname{Re}a>0\) justifies the interchange even when \(a\) is complex.

**Complex Watson estimate with its leading constant.** Factor \(a^{-n-1}\) from the second multiplier formula and set \(u=v/n\). This gives
\[
\lambda_n=s^{-1/2}(sa)^{-n}a^{-1}n^{-\tau}\frac1{\Gamma(\tau)}
\int_0^\infty v^{\tau-1}e^{-v/n}\left(1+\frac{v}{na}\right)^{-n-1}\,dv.
\]
Since \(\operatorname{Re}a>0\), the integration ray contains no zero of \(1+v/(na)\); moreover \(|1+v/(na)|^2\ge1+2v\operatorname{Re}(a)/(n|a|^2)\). On bounded \(v\)-intervals the integrand converges to \(v^{\tau-1}e^{-v/a}\), while the displayed inequality and a split at \(v=n^{1/3}\) yield a uniformly integrable majorant and an integrable relative error of order \(n^{-1}\) (expand the logarithm on the first part; the tail is exponentially small). The remaining Gamma integral is
\[
\int_0^\infty v^{\tau-1}e^{-v/a}dv=\Gamma(\tau)a^\tau,
\]
using \(\operatorname{Re}(1/a)>0\). This proves the claimed \(\lambda_n\) asymptotic; the same split is uniform as \(a\) ranges over compact subsets of the right half-plane, in particular \(a=a_\rho\) for \(\rho\) near one.

**Boundedness, compactness and singular-value counting.** The asymptotic gives
\[
|\lambda_n|=s^{-1/2}|a|^{\tau-1}r^n n^{-\tau}(1+O(n^{-1})).
\]
If \(r>1\), the norms of the images of the normalized basis are unbounded, precluding any bounded extension. If \(r\le1\), the diagonal defines a bounded extension, uniquely because the polynomials are dense. If \(r<1\), its singular values are exponentially summable in every positive power. If \(r=1\), \(|\lambda_n|\sim Cn^{-\tau}\) and \(C=s^{1/2-\tau}\). This implies compactness, \(\sum_n|\lambda_n|^p<\infty\) exactly for \(p\tau>1\), and the weak endpoint bound. Although \(|\lambda_n|\) need not be exactly ordered for small \(n\), the asymptotic counting law \(\#\{n:|\lambda_n|>\varepsilon\}\sim (C/\varepsilon)^{1/\tau}\) also gives the asserted asymptotic for decreasingly rearranged singular values.

**Sharp crossover.** Along \(a_\rho=a_*/\rho\), one has \(r=\rho\), and the preceding asymptotic is uniform, giving
\[
\|\mathcal T_{s,c_\rho,\tau}\|_{\mathcal S_p}^p
=C^p\rho^{p(1-\tau)}\sum_{n\ge1}\rho^{pn}n^{-p\tau}+O(1).
\]
The error is bounded uniformly as \(\rho\uparrow1\) by summability of \(n^{-p\tau-1}\); finitely many initial eigenvalues are continuous and bounded in \(\rho\). For \(0<\alpha<1\), comparison with the Gamma integral yields \(\sum_{n\ge1}\rho^{pn}n^{-\alpha}\sim\Gamma(1-\alpha)[-p\log\rho]^{\alpha-1}\). For \(\alpha=1\), that sum is exactly \(-\log(1-\rho^p)\). Since \(-\log\rho\sim1-\rho\), both displayed divergences follow. When \(\alpha>1\), uniform dominated convergence gives the limiting finite critical norm. The critical amplitude \(C\) depends only on \(s,\tau\), not on \(\arg a_*\).

**Same-modulus chirp comparison.** If \(1<s<2\) and \(1-1/s<\beta<1/2\), then \(a=1-\beta>1/2\), so the source integral converges. For the positive symbol, \(s|a|<1\), so \(r>1\). Adding the purely imaginary parameter \(i\theta\) changes the modulus neither of the symbol nor of its polynomial damping, but replaces \(a\) with \(1-\beta-i\theta\). Then \(s|a|\) crosses one at the stated exact value of \(|\theta|\), proving all three regimes.

## Verification
The included `check.py` evaluates both exact moment representations by independent quadratures for six parameter combinations and four finite indices, then checks the complex Watson factor numerically at a larger finite index. Execution returned `CHECK_OK`. Numerical quadrature verifies only finite identities and asymptotic trends; it is not an infinite-dimensional proof. The proof above supplies the unrestricted parameter ranges, the uniform error and endpoint summation.

## Relationship to prior work
Dong, Wang and Zhu (2026) introduce the two-parameter Fock Toeplitz-type family and derive boundedness, compactness and Schatten conditions under symbol growth hypotheses; their published main results do not give the present exact complex Gaussian plus polynomial-envelope spectral trichotomy, weak Schatten boundary or universal norm-divergence constants. Dong and Zhu (2025) determine Schatten spectra for bare canonical Gaussian kernels; the unweighted Gaussian case is acknowledged as prior work, and \(\tau>0\) is essential to the new critical class. Arreortúa-Reyes, Loaiza and Macías-Durán (2026) clarify diagonalization and domain subtleties for radial Toeplitz symbols; the radial Gamma-moment formula is not claimed as new. Existing smooth radial logarithmic-spectral-filter work treats bounded positive inverse-polynomial symbols and Dixmier traces, not a growing complex Gaussian compensated by an oscillatory radial phase. Related nonradial Fock Gaussian zero-product constructions produce all-Schatten effects from phase cancellation but neither state nor imply the present critical power law for a normal diagonal family. The new claim is the complete combined critical phase diagram, exact exponent/constants, and same-modulus oscillatory stabilization for the specified family.

## Limitations
This is a one-dimensional Gaussian Fock theorem for the stated two-parameter kernel specialization, \(\tau>0\), and \(\operatorname{Re}(1-c)>0\). It does not characterize arbitrary symbols, all two-parameter kernels or the operator defined on every Fock vector by an unbounded-symbol pointwise Toeplitz formula. The constants are fixed-parameter asymptotics, uniform only along the stated approach to the critical boundary. Standard Gamma-moment diagonalization and the undamped Gaussian case are prior mathematics. Possible implicit coverage in the broad older radial Toeplitz literature remains a priority risk. No independent audit has been performed.

## References
1. X. Dong, Z. Wang and K. Zhu, *Two-parameter Toeplitz-type operators between Fock spaces*, arXiv:2610.24318v1, first public 2026-10-16, https://arxiv.org/abs/2610.24318.
2. X. Dong and K. Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672v1, first public 2025-09-20, https://arxiv.org/abs/2509.16672.
3. G. J. Arreortúa-Reyes, M. Loaiza and J. Macías-Durán, *On Toeplitz operators with radial symbols acting on the Fock space*, Journal of Mathematical Sciences 298 (2026), 459–468, https://doi.org/10.1007/s10958-026-08328-z.
4. Classical Gamma–Laplace integral, Watson's lemma and Abelian asymptotics for polylogarithmic series; their required special forms are proved or derived above.
