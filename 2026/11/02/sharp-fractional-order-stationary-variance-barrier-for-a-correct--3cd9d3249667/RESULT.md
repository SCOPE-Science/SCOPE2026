# Sharp fractional-order stationary-variance barrier for a corrected fractional Ornstein–Uhlenbeck theta scheme

## Finding
For fractional Ornstein–Uhlenbeck dynamics driven by fractional Brownian motion with Hurst exponent \(1/2<H<1\), the stationary variance of a stable theta discretization has an exact polylogarithmic formula. Within the step-dependent family \(\theta_h=1/2+cah\), the unique choice that eliminates the second-order relative stationary-variance defect for every such Hurst exponent is \(c=1/12\). This choice also makes the deterministic amplification factor the \([2/2]\) Padé approximant to the exponential, but a strictly negative, *noninteger-order* invariant-variance defect remains:
\[
\frac{V_{h,\theta_h}}{V_*}-1
=\frac{\zeta(-2H)}{\Gamma(2H+1)}(ah)^{2H+1}
+O_H((ah)^{2H+2}).
\]
The coefficient is nonzero for all \(1/2<H<1\), so the order \(2H+1\) is sharp. This identifies a noise-correlation barrier to the higher stationary-variance accuracy suggested by matching the deterministic exponential propagation.

## Assumptions and scope
Let \(a>0\), \(\sigma>0\), and \(1/2<H<1\). Let \(B^H=(B_t^H)_{t\in\mathbb R}\) be a two-sided standard fractional Brownian motion with covariance of increments normalized by \(\mathbb E(B_t^H-B_s^H)^2=|t-s|^{2H}\). The continuous linear equation is
\[
dX_t=-aX_t\,dt+\sigma\,dB_t^H.
\]
Its unique stationary solution is the fractional Ornstein–Uhlenbeck convolution, with variance
\[
V_*=\frac{\sigma^2\Gamma(2H+1)}{2a^{2H}}.
\]
Set \(x=ah>0\). A theta step, driven by the *actual correlated increments* of the same fractional Brownian motion, is
\[
(1+\theta x)X_{n+1}=(1-(1-\theta)x)X_n+\sigma\Delta B_n^H,
\qquad \Delta B_n^H=B^H_{(n+1)h}-B^H_{nh}.
\]
Write \(A=1+\theta x\), \(B=1-(1-\theta)x\), \(C=A+B=2+(2\theta-1)x\), and \(r=B/A\). The exact formula below applies whenever \(0<r<1\). This includes fixed \(0\le\theta\le1\) for sufficiently small \(x\), and all \(x>0\) for \(\theta=1/2+x/12\). The asymptotic statements are for fixed \(a,\sigma,H\) as \(h\downarrow0\) (with fixed \(c\) when relevant); constants need not be uniform as \(H\) approaches its endpoints.

## Proof
**Stationary filtered noise and exact formula.** The normalized increments \(\xi_n=h^{-H}\Delta B_n^H\) form a centered stationary Gaussian sequence with covariance
\[
\gamma_H(0)=1,\qquad \gamma_H(k)=\tfrac12\big[(k+1)^{2H}-2k^{2H}+(k-1)^{2H}\big],\quad k\ge1.
\]
For \(0<r<1\), the recursion has the unique stationary causal solution
\[
X_n=\frac{\sigma h^H}{A}\sum_{j=0}^{\infty}r^j\xi_{n-1-j},
\]
with convergence in \(L^2\) (absolute-summable filter). Its variance is
\[
V_{h,\theta}=\frac{\sigma^2h^{2H}}{A^2(1-r^2)}\left[1+2\sum_{k\ge1}\gamma_H(k)r^k\right].
\]
With the standard polylogarithm \(\operatorname{Li}_s(r)=\sum_{k\ge1}r^k/k^s\), direct second-difference summation yields the exact identity
\[
1+2\sum_{k\ge1}\gamma_H(k)r^k
=\frac{(1-r)^2}{r}\operatorname{Li}_{-2H}(r).
\]
Since \(1-r=x/A\) and \(1+r=C/A\), we obtain
\[
\boxed{V_{h,\theta}=\sigma^2 h^{2H}\frac{x}{ABC}\operatorname{Li}_{-2H}(B/A).}
\]
The continuous variance follows independently from the fractional-noise covariance kernel: \(\sigma^2H(2H-1)\int_0^\infty\int_0^\infty e^{-a(u+v)}|u-v|^{2H-2}\,du\,dv=\sigma^2\Gamma(2H+1)/(2a^{2H})\).

**Small-step expansion.** Write \(t=-\log r>0\). For fixed \(1/2<H<1\), the classical polylogarithm expansion at the positive real argument approaching one is
\[
\operatorname{Li}_{-2H}(e^{-t})
=\Gamma(2H+1)t^{-2H-1}+\zeta(-2H)+O_H(t).
\]
Consequently
\[
\frac{V_{h,\theta}}{V_*}
=\frac{2}{ABC}\left(\frac{x}{t}\right)^{2H+1}
+\frac{2\zeta(-2H)}{\Gamma(2H+1)}\frac{x^{2H+1}}{ABC}
+O_H(x^{2H+2}).
\]
For constant \(\theta\), \(t=x+(1/2-\theta)x^2+O(x^3)\) and \(2/(ABC)=1+3(1/2-\theta)x+O(x^2)\). Therefore
\[
\frac{V_{h,\theta}}{V_*}=1+(1-H)(1-2\theta)x+O_H(x^2).
\]
For \(\theta=1/2+cx\) with fixed real \(c\), exact rational expansion gives
\[
\frac{t}{x}=1+(1/12-c)x^2+O(x^4),\qquad
\frac{2}{ABC}=1+(1/4-3c)x^2+O(x^4).
\]
Substituting, and noting \(2H+2<4\), yields
\[
\boxed{\frac{V_{h,\theta_h}}{V_*}=1+(1-H)(1/6-2c)x^2+
\frac{\zeta(-2H)}{\Gamma(2H+1)}x^{2H+1}+O_H(x^{2H+2}).}
\]
Because \(1-H>0\), the coefficient of \(x^2\) vanishes if and only if \(c=1/12\); the uniqueness assertion is within this specified linear-in-\(x\) theta family.

**Sharp fractional obstruction and global filter stability.** At \(c=1/12\),
\[
r=\frac{1-x/2+x^2/12}{1+x/2+x^2/12},
\]
which is the classical diagonal \([2/2]\) Padé rational approximation to \(e^{-x}\). Its numerator equals \(((x-3)^2+3)/12>0\), while the denominator exceeds the numerator by \(x>0\); hence \(0<r<1\) for every \(x>0\). The function \(\zeta(s)\) has no zero on \(-2<s<-1\) and is negative there, so \(\zeta(-2H)/\Gamma(2H+1)<0\), proving that the remaining defect is nonzero, strictly negative and exactly of order \(h^{2H+1}\). The stationary filter therefore exists at every positive step for this corrected scheme.

## Verification
The accompanying standalone \(verify.py\) recomputes the exact polylogarithmic covariance identity against independent finite correlated-increment sums; checks the Padé amplification and its positive stability domain; evaluates small-step asymptotic coefficients at several Hurst exponents against the predicted \(\zeta\)-constant; and tests the theta-family second-order coefficient. The program requires Python 3 and the \(mpmath\) numerical package (documented inside the file). The proof above—not finite numerical tests—establishes the universal parameter statements and sharp exponent.

## Relationship to prior work
Abreu, Fermín, Mordecki and Torres (2026, arXiv:2609.37019, first publicly posted 2026-09-29) analyze pathwise finite-horizon backward Euler convergence for fractional-noise stochastic functional differential equations with distributed state memory. Their full accessible text establishes consistency/convergence estimates but does not state a polylogarithmic stationary variance, a theta-family bias coefficient, or the corrected-Padé fractional-order barrier. Garrido-Atienza, Kloeden and Neuenkirch (2009) establish existence/convergence of discretized stationary solutions under dissipative drift; this is substantially broader as a qualitative stationary-solutions theorem but does not, in the accessible descriptions, identify the exact quantitative coefficient here. Gehringer and Li (2020) study continuous fractional Ornstein–Uhlenbeck functional limit theorems rather than discretization-invariant bias. The classical covariance of fractional Gaussian noise and the polylogarithm expansion are standard ingredients and not claimed as new.

## Limitations
This statement concerns only a linear scalar model, additive *unmodified* fractional Brownian increments, the stationary **one-time variance**, and the specified theta family. It does not assert a pathwise convergence rate of order \(2H+1\), independence of fractional increments, an optimal algorithm among arbitrary discretizations, or preservation of full temporal covariance. The \(H\downarrow1/2\) and \(H\uparrow1\) limits are not uniform in the expansion; at the Brownian endpoint, an additional cancellation occurs for ordinary midpoint stepping. The full text of the plausible 2009 stationary-discretization predecessor was not obtainable during the comparison; historical priority requires independent confirmation. There has been no independent mathematical audit.

## References
1. A. Abreu, L. Fermín, E. Mordecki, S. Torres, *Consistency and Convergence of the Backward-Euler Scheme for Stochastic Functional Differential Equations Driven by Fractional Brownian Motion*, arXiv:2609.37019v1, 2026-09-29, https://arxiv.org/abs/2609.37019.
2. M. J. Garrido-Atienza, P. E. Kloeden, A. Neuenkirch, *Discretization of stationary solutions of stochastic systems driven by fractional Brownian motion*, Applied Mathematics and Optimization 60 (2009), 151–172, https://doi.org/10.1007/s00245-008-9062-9.
3. J. Gehringer, X.-M. Li, *Functional Limit Theorems for the Fractional Ornstein–Uhlenbeck Process*, Journal of Theoretical Probability 35 (2022), 426–456, first online 2020-10-22, https://doi.org/10.1007/s10959-020-01044-7.
4. Classical polylogarithm expansion (Jonquière expansion), standard analytic continuation formula for \(\operatorname{Li}_s(e^{-t})\) at \(t\downarrow0\).
