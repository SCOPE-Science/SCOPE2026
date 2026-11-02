# Dimension–sluggishness transition for resetting diffusion: a unique radial mode and a reset-information phase diagram

## Finding

Consider isotropic Itô diffusion with diffusivity \(D(x)=|x|^{-\alpha}\), restarted at the origin at independent Poisson times. There is a sharp geometric threshold at \(\alpha=d-2\): the stationary **spatial** density is strictly decreasing in radius on or below that threshold and has exactly one off-origin radial maximum above it. The same threshold separates negative and positive divergences in a precisely specified point-anchored reset-information functional, with an exceptional logarithm-of-logarithm boundary in two dimensions.

For every integer \(d\ge2\), every real \(\alpha\ge0\), and reset rate \(\rho>0\), set \(\omega_d=2\pi^{d/2}/\Gamma(d/2)\), \(m=(\alpha+2)/2\), \(\nu=(d-2)/(\alpha+2)\). The stationary probability **per unit Euclidean volume** at radius \(r=|x|>0\) is
\[
p_{d,\alpha,\rho}(r)=\frac{2\rho^{1+\nu/2}}{\omega_d\Gamma(\nu+1)(\alpha+2)^{\nu+1}}\,r^{\alpha-(d-2)/2}K_\nu\!\left(\frac{\sqrt\rho}{m}r^m\right).
\]
Here \(K_\nu\) denotes the modified Bessel function of the second kind. The radial-distance density, by contrast, is \(\omega_d r^{d-1}p(r)\), and is **not** the object whose modes are classified.

If \(0\le\alpha\le d-2\), then \(p'(r)<0\) for all \(r>0\). If \(\alpha>d-2\), there is exactly one radial maximizer \(r_*\), with
\[
0<r_*<\left(\frac{\alpha(\alpha+2-d)}{\rho}\right)^{1/(\alpha+2)}.
\]
When \(d\ge3\) and \(\alpha=d-2\), \(p(0)=\rho/[(d-2)\omega_d]\) exists, is positive, and exceeds all \(p(r)\) for \(r>0\).

Define, for \(\varepsilon>0\), the explicit *point-anchored reset-information functional*
\[
I_\varepsilon=\rho\int_{\mathbb R^d}p(x)\log\frac{p(x)}{p(\varepsilon e_1)}\,dx.
\]
For \(d\ge3\) and \(\alpha\ne d-2\),
\[
I_\varepsilon/\rho=(\alpha+2-d)\log(1/\varepsilon)+O(1).
\]
At \(d\ge3\), \(\alpha=d-2\), the limit is finite and **strictly negative**. In dimension \(d=2\), the boundary is instead
\[
I_\varepsilon/\rho=\begin{cases}-\log\log(1/\varepsilon)+O(1),&\alpha=0,\\\alpha\log(1/\varepsilon)-\log\log(1/\varepsilon)+O(1),&\alpha>0.\end{cases}
\]
All asymptotic limits are for \(\varepsilon\downarrow0\), with \(d,\alpha,\rho\) fixed.

## Assumptions and scope

Let \(B_s\) be Brownian motion in \(\mathbb R^d\) with generator \(\Delta\), started at zero. Define \(A_s=\int_0^s|B_u|^\alpha\,du\), let \(T_t\) be the continuous inverse of \(A_s\), and let \(X_t=B_{T_t}\). For \(\alpha=0\), this is ordinary Brownian motion. For \(\alpha>0\), this time change specifies the behavior at the singular origin and realizes the Itô generator \(L=|x|^{-\alpha}\Delta\) away from the origin. Independent resets to zero occur at rate \(\rho\). The process is regenerative; the stationary law is the probability distribution of \(X_{E_\rho}\) for independent \(E_\rho\sim\operatorname{Exp}(\rho)\). The boundary prescription is essential: other stochastic-calculus conventions are different processes.

## Proof

**Heat kernel and normalization.** Put \(\beta=(d+\alpha)/(\alpha+2)=\nu+1\). Direct substitution into \(\partial_t q=\Delta(r^{-\alpha}q)\) yields the nonnegative fundamental solution from the origin
\[
q_t(r)=\frac{\alpha+2}{\omega_d\Gamma(\beta)}\frac{r^\alpha}{[(\alpha+2)^2t]^\beta}\exp\!\left[-\frac{r^{\alpha+2}}{(\alpha+2)^2t}\right].
\]
Indeed \(\partial_t q-\Delta(r^{-\alpha}q)=0\) for every \(r,t>0\); the change of variable \(z=r^{\alpha+2}/[(\alpha+2)^2t]\) gives \(\omega_d\int_0^\infty q_t(r)r^{d-1}dr=1\). Its mass concentrates at zero as \(t\downarrow0\). Equivalently, the radial time-changed Brownian motion is a Bessel-type self-similar diffusion whose entrance law is this kernel. Regeneration gives the unique stationary density \(p(r)=\rho\int_0^\infty e^{-\rho t}q_t(r)dt\). The standard positive-argument Bessel integral
\[
\int_0^\infty t^{-\beta}e^{-\rho t-a/t}dt=2(a/\rho)^{(1-\beta)/2}K_{\beta-1}(2\sqrt{a\rho})
\]
with \(a=r^{\alpha+2}/(\alpha+2)^2\) proves the displayed stationary formula and its normalization without arbitrary constants.

**Strict radial mode dichotomy.** Differentiating the stationary equation away from zero gives
\[
p''(r)+\frac{d-1-2\alpha}{r}p'(r)+\left[\frac{\alpha(\alpha+2-d)}{r^2}-\rho r^\alpha\right]p(r)=0.
\]
Consequently, setting \(H(r)=r^{d-1-2\alpha}p'(r)\),
\[
H'(r)=r^{d-3-2\alpha}p(r)\big[\rho r^{\alpha+2}-\alpha(\alpha+2-d)\big].
\]
The stretched-exponential asymptotic of \(K_\nu\) ensures \(H(r)\to0\) as \(r\to\infty\), and positivity of \(K_\nu\) ensures \(p(r)>0\). If \(\alpha\le d-2\), the bracket is positive for every \(r>0\), so \(H\) increases strictly to zero and is strictly negative everywhere. If \(\alpha>d-2\), put \(R=[\alpha(\alpha+2-d)/\rho]^{1/(\alpha+2)}\). Now \(H\) decreases strictly on \((0,R)\), increases strictly on \((R,\infty)\), and is negative on \([R,\infty)\). The small-radius expansions below show \(p'(r)>0\) for sufficiently small positive \(r\), whence exactly one zero of \(H\) lies in \((0,R)\); this is the unique maximum.

**Reset-point information.** Standard small-argument Bessel expansions yield for \(d\ge3\)
\[
p(r)\sim\frac{\rho}{(d-2)\omega_d}r^{\alpha+2-d},
\]
whereas for \(d=2\)
\[
p(r)\sim\frac{\rho}{2\pi}r^\alpha\log(1/r).
\]
At \(d\ge3\), \(\alpha=d-2\), the first display yields a finite strictly positive center value. All cases satisfy \(\int p|\log p|dx<\infty\): near zero, \(\omega_d r^{d-1}p(r)\) scales as \(r^{\alpha+1}\) up to a logarithm, and the tail decays stretched-exponentially. Hence \(I_\varepsilon/\rho=\int p\log p\,dx-\log p(\varepsilon)\); the stated asymptotics follow by taking logarithms of the preceding exact expansions. At the finite-center critical line the strict radial decrease gives \(\int p\log[p/p(0)]dx<0\). This proves strictness and all regimes.

## Verification

The accompanying standalone `verify.py` evaluates the Bessel resolvent and the exponential-time heat-kernel integral independently, tests radial normalization by numerical quadrature, checks radial signs and the mode upper bound on representative parameter grids, and checks small-radius coefficients. It passed 99 deterministic numerical checks. Independent symbolic differentiation also returned the identically zero PDE residual for \(q_t\) and the identically zero residual for the derived stationary-density ODE. These finite checks do not establish the quantified infinite-domain theorem; the analytical calculations above do.

## Relationship to prior work

Frimpong, Bresque and Roldán [1] establish the one-dimensional sluggish resetting law, discuss singular reset entropy, and explicitly identify extension to higher dimensions and a suitable regularized information quantity as open directions. Sandev, Fumeron, Henkel and Lenzi [2] calculate the planar inverse-square-diffusivity case (\(d=2,\alpha=2\)) with several stochastic interpretations; that case is a specialization of the density here, not the claimed new dimension-dependent phase diagram. Evans and Majumdar [3] establish arbitrary-dimensional resetting for ordinary Brownian diffusivity (\(\alpha=0\)); those classical cases are also covered but not claimed as new. The reset-information expression is motivated by established resetting-thermodynamics conventions [4], but its exact use of the density evaluated at \(\varepsilon e_1\) is defined specifically here. The asserted contribution is the joint \((d,\alpha)\) mode classification and precisely normalized reset-point asymptotics, not invention of the underlying Bessel identities or renewal resolvent.

## Limitations

The origin is defined by the explicit Itô time change, not by arbitrary extensions of a singular SDE. The object classified for radial modes is the **spatial density**, not the distribution of radius. The point-anchored functional is a mathematical regularization, not necessarily a realizable finite-lattice entropy production or the full thermodynamic entropy. The exact \(O(1)\) constants in its divergent cases are not classified. Other stochastic-calculus conventions, anisotropic diffusivities, noncentral resetting, first-passage optimizations, and arbitrary spatially heterogeneous coefficients are outside scope. Known general diffusion Green-function identities might subsume parts of the explicit density, so historical priority requires independent assessment.

## References

[1] T. D. Frimpong, L. Bresque, E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first submitted 2026-10-15), https://arxiv.org/html/2610.21962v1 .

[2] T. Sandev, S. Fumeron, M. Henkel, E. K. Lenzi, *Heterogeneous planar diffusion with axisymmetric power-law decaying diffusion coefficient under stochastic resetting*, arXiv:2609.24427 (first submitted 2026-09-21), https://arxiv.org/abs/2609.24427 .

[3] M. R. Evans, S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension*, arXiv:1404.4574 (2014), https://arxiv.org/abs/1404.4574 .

[4] J. Fuchs, S. Goldt, U. Seifert, *Stochastic thermodynamics of resetting*, arXiv:1603.01141 (2016), https://arxiv.org/abs/1603.01141 .
