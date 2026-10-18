# All-noise escape-time phases for an outward Ornstein–Uhlenbeck diffusion

## Finding

For an isotropic outward Ornstein–Uhlenbeck diffusion confined until its first exit from a centered Euclidean ball, noise acts differently in one and in higher spatial dimensions, for **every** positive noise intensity. In dimension one the mean exit time has exactly one global maximizing intensity. In every integer dimension at least two it strictly decreases with noise. In dimension two the small-noise decrease is exponentially small, although the deterministic first-order response vanishes.

Explicitly, with the notation below, write \(U_d(D)=\mathbb E\tau_D\), \(U_0=\kappa^{-1}\log(R/r)\), \(\nu=d/2\), and
\[
 h_\nu(z)=z\int_0^1t^{\nu-1}e^{-z(1-t)}\,dt.
\]
The previously known Ornstein–Uhlenbeck exit-time integral is equivalently
\[
 U_d(D)=\frac1\kappa\int_r^R h_{d/2}\!\left(\frac{\kappa s^2}{2D}\right)\frac{ds}{s}.
\]
The new all-intensity classification is:

* For each \(d\ge2\), \(D\mapsto U_d(D)\) decreases strictly on \((0,\infty)\), and \(0<U_d(D)<U_0\) at every positive \(D\).
* For \(d=1\), \(D\mapsto U_1(D)\) increases strictly up to one finite, positive intensity \(D_*\), then decreases strictly to zero. Its maximum is strictly greater than \(U_0\). It is the **unique** global maximum.
* In the critical dimension \(d=2\), the deficit has the exact identity and asymptotic
\[
 U_0-U_2(D)=\frac1\kappa\int_r^R e^{-\kappa s^2/(2D)}\frac{ds}{s}
 \sim \frac{D}{\kappa^2r^2}e^{-\kappa r^2/(2D)}\qquad(D\downarrow0).
\]
Thus the planar deficit is positive for every positive intensity, yet smaller than every power of \(D\) as \(D\downarrow0\).

The one-dimensional optimizer is characterized with no numerical search over paths. There is a unique \(z_m>1/2\) at which \(h_{1/2}\) is maximized. Let \(k=(R/r)^2>1\). A unique \(a_*\in(z_m/k,z_m)\) solves \(h_{1/2}(ka_*)=h_{1/2}(a_*)\), and
\[
 D_*=\frac{\kappa r^2}{2a_*}.
\]
Here \(h_{1/2}(z)=2\sqrt z\,\operatorname{Dawson}(\sqrt z)\); Dawson's integral has its standard normalization \(\operatorname{Dawson}(x)=e^{-x^2}\int_0^x e^{t^2}\,dt\).

## Assumptions and scope

Let \(d\in\{1,2,3,\ldots\}\), \(\kappa>0\), \(0<r<R<\infty\), and \(D>0\). Let \(B_t\) be standard \(d\)-dimensional Brownian motion and consider
\[
 dX_t=\kappa X_t\,dt+\sqrt{2D}\,dB_t,\qquad |X_0|=r,
 \qquad \tau_D=\inf\{t\ge0:|X_t|\ge R\}.
\]
The initial direction is arbitrary and immaterial by rotation invariance. The zero-noise comparison starts from the same positive radius and obeys \(\tau_0=\kappa^{-1}\log(R/r)\). The excluded case \(r=0\) has a stationary zero-noise trajectory and a different singular limit. All expectations in the theorem are finite for \(D>0\).

The asymptotic expansions for any fixed integer \(d\ne2\) and for large \(D\) are
\[
 U_d(D)=U_0+\frac{(2-d)D}{2\kappa^2}\left(\frac1{r^2}-\frac1{R^2}\right)+O(D^2),\quad D\downarrow0,
\]
\[
 U_d(D)\sim\frac{R^2-r^2}{2dD},\qquad D\to\infty.
\]
The first-order dimension-dependent sign was already obtained in the motivating paper; it is not asserted as new. Nor is the integral representation asserted as new.

## Proof

**1. Radial mean-exit representation.** The generator on a radial twice-differentiable function is
\[
 \mathcal L u(s)=D\left(u''(s)+\frac{d-1}{s}u'(s)\right)+\kappa s u'(s).
\]
The boundary-value problem \(\mathcal Lu=-1\), \(u(R)=0\), with the regular solution at the origin, has
\[
 -u'(s)=\frac{s^{1-d}}D e^{-\kappa s^2/(2D)}\int_0^s t^{d-1}e^{\kappa t^2/(2D)}\,dt
 =\frac{h_{d/2}(\kappa s^2/(2D))}{\kappa s}.
\]
Integrating from \(r\) to \(R\) gives the stated known exact formula. Smoothness in the ball, finiteness and uniqueness of the solution follow from the regular integral; Dynkin's formula for the process stopped at the ball boundary identifies it with the mean first exit time.

**2. All-noise strict monotonicity from dimension two upward.** For \(\nu\ge1\) change variables \(w=z(1-t)\) to get
\[
 h_\nu(z)=\int_0^z\left(1-\frac wz\right)^{\nu-1}e^{-w}\,dw.
\]
For each \(w\) inside the integration interval, the integrand is nondecreasing in \(z\); the domain of integration also grows, and the added interval has positive measure. Thus \(h_\nu\) is strictly increasing, with \(0<h_\nu(z)<1\) for every finite \(z>0\), and \(h_\nu(z)\to1\) as \(z\to\infty\). Since \(z=\kappa s^2/(2D)\) decreases strictly in \(D\), integration proves the complete monotonicity assertion (strict first-order monotonicity, not complete monotonicity in the Laplace-transform sense).

**3. A single peak of the one-dimensional kernel.** Let \(h=h_{1/2}\). Differentiation of its integral representation yields
\[
 h'(z)=1-\left(1-\frac1{2z}\right)h(z).
\]
For \(z\le1/2\), this derivative is positive. For \(z>1/2\), put \(g(z)=z/(z-1/2)\). Then \(h'(z)=-(1-1/(2z))(h(z)-g(z))\). Just to the right of \(1/2\), \(h(z)-g(z)<0\). Standard endpoint Laplace asymptotics of the defining integral give
\[
 h(z)=1+\frac1{2z}+\frac3{4z^2}+O(z^{-3}),\qquad
 g(z)=1+\frac1{2z}+\frac1{4z^2}+O(z^{-3}),
\]
so \(h-g>0\) for all sufficiently large \(z\). At **every** zero of \(h-g\) the derivative of that difference equals \(-g'(z)>0\); therefore it can cross zero only once. Call the unique zero \(z_m\). The sign of \(h'\) shows \(h\) strictly increases on \((0,z_m)\), strictly decreases on \((z_m,\infty)\), and \(h(z)\to1\) from above as \(z\to\infty\).

**4. Unique noise optimum.** Set \(a=\kappa r^2/(2D)\), \(k=(R/r)^2>1\). Changing radial variable to \(z=\kappa s^2/(2D)\) gives
\[
 U_1(D)=\frac1{2\kappa}\int_a^{ka}\frac{h(z)}z\,dz,
 \qquad \frac{dU_1}{da}=\frac{h(ka)-h(a)}{2\kappa a}.
\]
For \(a\le z_m/k\), the numerator is strictly positive; for \(a\ge z_m\) it is strictly negative. Between those endpoints, \(h(ka)\) strictly decreases while \(h(a)\) strictly increases, so precisely one zero \(a_*\) exists and changes sign from positive to negative. Thus the mean exit time, as a function of \(a\), has one strict global maximum; the order-reversing bijection between \(a\) and \(D\) preserves uniqueness. As \(D\downarrow0\), the displayed large-\(z\) expansion gives \(U_1(D)=U_0+\frac{D}{2\kappa^2}(r^{-2}-R^{-2})+O(D^2)>U_0\); as \(D\to\infty\), the small-\(z\) expansion gives \(U_1(D)\to0\). The maximum therefore exceeds the deterministic exit time strictly.

**5. Planar critical layer and limits.** At \(\nu=1\), the kernel simplifies to \(h_1(z)=1-e^{-z}\). Substitution gives the exact planar formula above. For \(b=\kappa r^2/(2D)\to\infty\), substituting \(z=\kappa s^2/(2D)\) reduces its deficit to \((2\kappa)^{-1}\int_b^{kb}z^{-1}e^{-z}\,dz\); one integration by parts yields its stated equivalent \(D(\kappa^2r^2)^{-1}e^{-b}\). The full fixed-dimensional small-noise expansion follows from \(h_\nu(z)=1+(1-\nu)/z+O(z^{-2})\) uniformly for \(s\in[r,R]\), while \(h_\nu(z)=z/\nu+O(z^2)\) gives the large-noise limit.

## Verification

The companion standalone program `verify.py` executes independent evaluations of the radial integral, the special-function kernel, backward-generator residuals, planar exponential-integral identity, root characterization and numerical monotonicity. It is supplementary to the proof, and numerical sampling or finite checks do not certify infinite ranges. With \(\kappa=1\), \(r=1/2\), \(R=1\), the numerical one-dimensional optimum is \(D_*\approx0.102238090533272\) with \(U_1(D_*)\approx0.859277257396038\), compared with deterministic time \(\log2\approx0.693147180559945\).

Reproduction: run `python3 verify.py` with NumPy and SciPy installed. The script uses deterministic integration and root finding; it does not require stochastic simulation.

## Relationship to prior work

Chemnitz, Engel and Koltai (2026), Example 2.1 and Remark 2.4, analyze **exactly the same expanding linear drift and spherical exit domain**. They already derive the small-noise first-order sign \(2-d\), the presence of stochastic inertia for one dimension, and absence in higher dimensions at sufficiently small noise; their discussion says separately that further analysis excludes two-dimensional stochastic inertia. Their reported theorem does **not** establish the full positive-noise strict monotonicity for dimensions at least two, the unique global optimizing noise in one dimension, or the exact exponentially small planar deficit. Their results are not redescribed here as new.

Kersting, Orvieto, Proske and Lucchi (2022), Theorem 4, give the general radial Ornstein–Uhlenbeck ball mean-exit integral for all real restoring-drift coefficients, including its repulsive specialization after a change of sign. That formula already appears in earlier work by Grebenkov and, in narrower parameter settings, by Graczyk and Jakubowski. Their investigated quantity is also the mean exit time, but the inspected paper derives dimension-growth estimates, not the global diffusion-amplitude phase classification proved here. The exact radial integral and its parameter substitution are prior knowledge, not the claimed new theorem.

Related metastable-state work on colored noise addresses a different stochastic dynamical system. The current result requires an **outward linear state drift with additive white Brownian noise**, fixed nonzero starting radius and spherical exit boundary.

## Limitations

The theorem concerns expectations, not the whole first-exit distribution, and only isotropic constant diffusion in a centered sphere. The diffusion intensity is normalized through \(\sqrt{2D}\); changing normalization changes the numerical optimum. The origin \(r=0\), nonspherical domains and anisotropic drift are excluded. The global phase proof depends on exact radial solvability. An independent originality assessment has not been performed, and additional older work may contain equivalent comparisons derived from known exit-time special functions.

## References

1. R. Chemnitz, M. Engel and P. Koltai, *Characterizing stochastic inertia: when does noise increase escape times?* arXiv:2610.08685 (first public 2026-10-06), especially Example 2.1 and Remark 2.4. https://arxiv.org/abs/2610.08685
2. H. Kersting, A. Orvieto, F. Proske and A. Lucchi, *Mean first exit times of Ornstein–Uhlenbeck processes in high-dimensional spaces*, arXiv:2208.04029 (2022), Theorem 4 and discussion of prior formulas. https://arxiv.org/abs/2208.04029
3. D. S. Grebenkov, *First exit times of harmonically trapped particles: a didactic review* (2014), formula reported as Eq. (75) in reference 2.
4. P. Graczyk and T. Jakubowski, *Exit times and Poisson kernels of the Ornstein–Uhlenbeck diffusion* (2008), Theorem 2.2 as described in reference 2.
