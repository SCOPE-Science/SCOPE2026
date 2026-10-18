# Origin-free sharp quantitative weighted-perimeter monotonicity for nested Euclidean balls

## Finding
For any integer \(d\ge2\), any \(\lambda\ge0\), and any two positive-radius Euclidean balls \(B(a,r)\subseteq B(b,R)\) in \(\mathbb R^d\), set
\[
E_\lambda(a,r)=\int_{\partial B(a,r)} e^{\lambda\|x\|_2^2}\,d\mathcal H^{d-1}(x),\qquad M=\max\{R,\|a\|_2,\|b\|_2\}.
\]
Then
\[
\boxed{\log E_\lambda(b,R)-\log E_\lambda(a,r)\ge \frac{(d-1)(R-r)}{M}.}
\]
Proper inclusion makes the right-hand side strictly positive. The coefficient \(d-1\) is the largest universal coefficient valid for all nonnegative \(\lambda\), centers, and radii: for \(\lambda=0\) and concentric balls with \(r\uparrow R\), the ratio of the two sides tends to \(1\).

The same inequality holds for every nonzero positive mixture of these radial weights,
\[
\phi(t)=\int_{[0,\infty)}e^{\lambda t^2}\,d\mu(\lambda),\qquad E_\phi(a,r)=\int_{\partial B(a,r)}\phi(\|x\|_2)\,d\mathcal H^{d-1}(x),
\]
provided \(\mu\) is a nonzero positive Borel measure satisfying \(\int e^{\lambda T^2}\,d\mu(\lambda)<\infty\) for every finite \(T\ge0\). The same sharp coefficient applies uniformly across this class.

Among the one-parameter exponential weights \(e^{\lambda\|x\|_2^2}\) with real \(\lambda\), nonnegative \(\lambda\) are exactly those admitting unrestricted monotonicity over every pair of nested Euclidean balls: for \(\lambda<0\) even concentric origin-centered balls lose monotonicity at sufficiently large radii.

## Assumptions and scope
The balls are closed, compact, full-dimensional, with strictly positive radii. Inclusion is equivalent to \(\|b-a\|_2+r\le R\). The weight is radial about the *fixed* origin, which need not lie in either ball. Surface measure is ordinary \((d-1)\)-dimensional Hausdorff measure. The same statements hold for the corresponding open balls since their boundary spheres coincide. A weight mixture is assumed finite at every finite radius and not identically zero. No assertion is made for arbitrary convex bodies, for which nonconstant weighted perimeter can violate monotonicity.

## Proof
**1. Exact angular integral.** Put \(s=\|a\|_2\), \(\nu=d/2-1\), \(z=2\lambda sr\), and \(\sigma_d=2\pi^{d/2}/\Gamma(d/2)\). Spherical parametrization gives
\[
E_\lambda(a,r)=\sigma_d r^{d-1}e^{\lambda(s^2+r^2)}A_d(z),\quad
A_d(z)=\frac1{\sigma_d}\int_{\mathbb S^{d-1}}e^{zu_1}\,d\sigma(u).
\]
Here \(A_d(0)=1\) and, for positive \(z\), \(A_d(z)=\Gamma(d/2)(2/z)^\nu I_\nu(z)\); \(I_\nu\) is the modified Bessel function of the first kind. Let \(m(z)=A_d'(z)/A_d(z)=I_{\nu+1}(z)/I_\nu(z)\). Since it is the mean of the first coordinate under a nondegenerate exponentially tilted spherical probability law, \(0<m(z)<1\) for \(z>0\), and \(m(0)=0\).

**2. Strict Bessel-ratio barrier.** Set \(c=d-1\). The standard Bessel recurrence yields the Riccati equation
\[
m'(z)=1-m(z)^2-\frac{c}{z}m(z),\qquad z>0.
\]
We establish \(m(z)\ge1-c/z\). For \(0<z\le c\), the right-hand side is nonpositive. On \(z>c\), compare with \(g(z)=1-c/z\). At any point where \(m=g\),
\[
m'(z)-g'(z)=\frac{c(z-1)}{z^2}>0
\]
(the interval \(z>c\ge1\) makes this strictly positive). Since \(m(c)>g(c)=0\), a first downward crossing is impossible. Consequently \(0\le1-m(z)\le c/z\) for all positive \(z\). The limiting cases \(s=0\) or \(\lambda=0\) are treated directly in the formulas below.

**3. A center-versus-radius differential inequality.** Write \(F(s,r)=E_\lambda(a,r)\), which depends only on \(s\). Differentiation yields
\[
\partial_r\log F=\frac c r+2\lambda r+2\lambda s\,m(z),\qquad
\partial_s\log F=2\lambda s+2\lambda r\,m(z)\ge0.
\]
Thus
\[
\partial_r\log F-\partial_s\log F
=\frac c r-2\lambda(s-r)(1-m(z))
\ge\frac c{\max\{s,r\}}.
\]
For \(s\le r\), the left side is at least \(c/r\). For \(s>r\) and positive \(\lambda\), use \(1-m(z)\le c/(2\lambda sr)\) to obtain \(c/r-c(s-r)/(sr)=c/s\). At \(\lambda=0\) the difference is \(c/r\), which is still no smaller than \(c/\max\{s,r\}\). At \(s=0\), the derivative \(\partial_s\log F\) is zero by the even spherical integral, giving the same bound.

**4. Integrate along a nested-ball path.** Let \(a_t=(1-t)a+tb\), \(r_t=(1-t)r+tR\), and \(s_t=\|a_t\|_2\) for \(0\le t\le1\). Nestedness implies \(R-r\ge\|b-a\|_2\). The function \(s_t\) is absolutely continuous with \(|s'_t|\le\|b-a\|_2\le R-r\) almost everywhere. Also \(r_t\le R\), \(s_t\le\max\{\|a\|_2,\|b\|_2\}\), so \(\max\{r_t,s_t\}\le M\). From the positivity of \(\partial_s\log F\), almost everywhere
\[
\begin{aligned}
\frac d{dt}\log F(s_t,r_t)
&=(R-r)\partial_r\log F+s'_t\partial_s\log F\\
&\ge (R-r)(\partial_r\log F-\partial_s\log F)\\
&\ge \frac{c(R-r)}{M}.
\end{aligned}
\]
Integrating over \([0,1]\) proves the claimed inequality. If the inclusion is proper, \(R-r>0\), hence the energy increases strictly.

**5. Mixtures, sharpness, and signed parameter boundary.** The estimate at each \(\lambda\ge0\) has the same multiplicative factor \(e^{c(R-r)/M}\). Integrate in \(\lambda\) against the positive measure \(\mu\) and apply Tonelli to obtain the mixture result. The exponential moment assumption ensures finite positive energies. For \(\lambda=0\) and concentric balls, \(\log E_0(0,R)-\log E_0(0,r)=c\log(R/r)\). Since \(M=R\), the quotient \(\log(R/r)/((R-r)/R)\to1\) as \(r\uparrow R\), proving uniform sharpness. Finally, for real negative \(\lambda\),
\[
E_\lambda(0,r)=\sigma_d r^{d-1}e^{\lambda r^2},\qquad \frac d{dr}\log E_\lambda(0,r)=\frac c r+2\lambda r,
\]
which is negative for \(r>\sqrt{c/(-2\lambda)}\). Thus universal nested-ball monotonicity fails when \(\lambda<0\).

## Verification
The standalone `checker.py` uses a fixed random seed and independently evaluates the exact modified-Bessel formula and a high-order spherical quadrature representation. It tested 720 randomly generated nested-ball inequalities across dimensions \(2,3,4,7\) and five nonnegative exponential parameters; it also checked 800 instances of the Bessel barrier. The recorded local execution passed. These finite checks are diagnostic only; the all-dimensional theorem is established by the analytic argument above. To reproduce, run `python checker.py` with NumPy and SciPy installed. The checker is packaged alongside this document.

## Relationship to prior work
Csató and Giovagnoli (2026) prove inclusion monotonicity for sufficiently increasing radial weights on convex bodies **containing the radial center** and exhibit failure without the origin condition for general convex bodies; their paper does not state this origin-free result restricted to balls or its logarithmic gap. Saracco and Stefani (2023/2024) prove that a nonconstant isotropic weight cannot be inclusion-monotone on **all** convex bodies, which is compatible with the present special-family result. Segura (2021) develops differential inequalities for modified-Bessel ratios; standard ratio recurrences and the Riccati equation are used here, not claimed as new. The claim is the geometric comparison for arbitrary centers, its sharp uniform growth coefficient, and the positive-mixture closure. An equivalent ball-specific inequality in older special-function or geometric-measure literature has not been ruled out independently.

## Limitations
The coefficient is optimal **uniformly over the stated weight class**, not necessarily for each fixed strictly positive parameter. The theorem is restricted to Euclidean balls, nonnegative exponential mixtures, dimensions at least two, and positive finite radii. The conclusion neither contradicts nor strengthens universal all-convex-body monotonicity. Independent review and complete historical priority verification have not been performed.

## References
1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1 (first public October 8, 2026), https://arxiv.org/abs/2610.11677.
2. G. Saracco and G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770; *Mathematische Nachrichten* 297 (2024), 1444–1450, https://arxiv.org/abs/2306.07770.
3. J. Segura, *Monotonicity Properties for Ratios and Products of Modified Bessel Functions and Sharp Trigonometric Bounds*, *Results in Mathematics* 76 (2021), article 221, https://doi.org/10.1007/s00025-021-01531-1.
