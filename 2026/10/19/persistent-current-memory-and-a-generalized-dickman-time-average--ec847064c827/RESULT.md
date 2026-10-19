# Persistent current memory and a generalized Dickman time average in a resetting Brownian gas

## Finding

Consider the stationary independent-resetting Brownian gas specified below. Set \(\alpha=\sqrt{r/D}\), \(\theta=\rho/\alpha\), \(u=rt\), and
\[
F(u)=e^u\operatorname{erfc}(\sqrt u),\qquad
h(u)=(3-2u)F(u)+2\sqrt{u/\pi}.
\]
Writing \(Q_t\) for the number of particles on the positive half-line, the *annealed* and *mean conditional (quenched)* stationary lag covariances satisfy, for every \(t\geq0\),
\[
\boxed{C_{\mathrm{an}}(t)=\operatorname{Cov}(Q_0,Q_t)=\frac{\theta}{8}\left(1+e^{-rt}h(rt)\right),}
\]
\[
\boxed{C_{\mathrm{qu}}(t)=\mathbb E_{\Pi}\!\left[\operatorname{Cov}(Q_0,Q_t\mid\Pi)\right]
=\frac{\theta}{8}e^{-rt}h(rt).}
\]
Thus \(C_{\mathrm{qu}}(t)>0\) is strictly decreasing to zero; the annealed covariance decreases to the strictly positive plateau \(\theta/8\). Its equal-time value is \(\theta/2\), so the normalized infinite-lag annealed correlation is exactly \(1/4\). More sharply,
\[
C_{\mathrm{qu}}(t)\sim\frac{\theta}{2\sqrt{\pi rt}}e^{-rt}
\quad(t\to\infty).
\]
For each fixed \(t\), the *one-time* annealed law \(Q_t\sim\operatorname{Poisson}(\theta/2)\) is already known; it is not the novelty claimed here. The exact stationary two-time law is the bivariate-Poisson generating function
\[
\mathbb E[s^{Q_0}v^{Q_t}]
=\exp\left[\frac{\theta}{2}(s-1)+\frac{\theta}{2}(v-1)
+C_{\mathrm{an}}(t)(s-1)(v-1)\right],\qquad 0\leq s,v\leq1.
\]
The general bivariate-Poisson structure is also known; the evaluated resetting-specific coefficient is the contribution.

Despite this stationary Poisson marginal, the long *physical-time average* is nonergodic under the annealed law. Almost surely,
\[
\boxed{\lim_{T\to\infty}\frac1T\int_0^T Q_t\,dt
=M_{\Pi}=\frac12\sum_{z\in\Pi}e^{-\alpha z}.}
\]
The limit depends on the frozen starting positions \(\Pi\). Its Laplace transform and cumulants are
\[
\mathbb E[e^{-sM_{\Pi}}]
=\exp\left[-\theta\int_0^{1/2}\frac{1-e^{-sw}}{w}\,dw\right]
\quad(s\geq0),
\qquad
\kappa_n(M_{\Pi})=\frac{\theta}{n2^n}\quad(n\geq1).
\]
In particular \(\operatorname{Var}(M_{\Pi})=\theta/8>0\). The variable \(2M_{\Pi}\) has the generalized Dickman distribution with parameter \(\theta\), characterized by \(W\stackrel{d}=U^{1/\theta}(1+W')\), where \(U\) is uniform on \((0,1)\) and independent of \(W'\stackrel{d}=W\).

## Assumptions and scope

Fix \(D,r,\rho>0\). Let \(\Pi\) be a homogeneous Poisson process of *anchor distances* \(z>0\) with intensity \(\rho\,dz\), representing particles initially at \(-z\). Conditional on \(\Pi\), each particle has independent displacement \(Y_t^z\), a stationary one-dimensional Brownian motion with generator \(D\partial_y^2\) interrupted at independent rate-\(r\) Poisson times by complete resetting to \(y=0\). The starting law is the stationary Laplace density \(\alpha e^{-\alpha|y|}/2\), independently for different anchors. Anchor positions are frozen; resetting does not resample them. Set
\[
Q_t=\sum_{z\in\Pi}{\bf1}_{\{Y_t^z>z\}}.
\]
This is the standard net integrated crossing count for an initially left-half-line gas, represented as its instantaneous positive-half-line occupancy. For each fixed \(t\), \(Q_t\) is almost surely finite. The covariances above use both thermal/resetting and (where applicable) anchor randomness. No equilibrium detailed-balance assumption is made.

## Proof

**Stationary one-particle law and the one-time baseline.** The stationary reset-renewal identity gives
\[
\mathbb P(Y_t^z\in dy)=\int_0^\infty re^{-ra}\,
(4\pi Da)^{-1/2}e^{-y^2/(4Da)}\,da\,dy
=\frac{\alpha}{2}e^{-\alpha|y|}\,dy.
\]
Consequently \(f(z)=\mathbb P(Y_t^z>z)=\tfrac12e^{-\alpha z}\). Poisson thinning proves the already known \(Q_t\sim\operatorname{Poisson}(\rho\int_0^\infty f(z)dz)=\operatorname{Poisson}(\theta/2)\).

**Two-time reduction.** Let \(Y\) have the stationary Laplace law, independent of \(B_t\sim N(0,2Dt)\). Define
\[
a_t(z)=\mathbb P(Y>z,Y+B_t>z),\quad
b_t(z)=\mathbb P(Y+B_t>z).
\]
An event of no reset between times \(0\) and \(t\) has probability \(e^{-rt}\). On its complement, future motion is independent of the state at time zero. Therefore, for a particle with anchor \(z\),
\[
\mathbb P(Y_0^z>z,Y_t^z>z)
=f(z)^2+e^{-rt}[a_t(z)-f(z)b_t(z)].
\]
Campbell's formula, independent marking, and the law of total covariance yield
\[
C_{\mathrm{an}}(t)=\rho\int_0^\infty
\mathbb P(Y_0^z>z,Y_t^z>z)\,dz,
\qquad
C_{\mathrm{qu}}(t)=\rho e^{-rt}\int_0^\infty[a_t(z)-f(z)b_t(z)]\,dz.
\]
In particular their difference is \(\rho\int_0^\infty f(z)^2dz=\theta/8\), the variance of the random conditional mean \(\sum_{z\in\Pi}f(z)\).

**Exact evaluation.** For \(u=rt>0\), elementary Gaussian and exponential integrations give
\[
\int_0^\infty a_t(z)\,dz=\frac{1+F(u)}{4\alpha},
\]
\[
\int_0^\infty f(z)b_t(z)\,dz
=\frac{2-(1-2u)F(u)-2\sqrt{u/\pi}}{8\alpha}.
\]
For instance, by Tonelli the first integral is \(\tfrac12\int_0^\infty e^{-\alpha x}\Phi(x/\sqrt{2Dt})dx\), with \(\Phi\) the standard-normal cdf; integration by parts gives the first displayed expression. For the second, use the Laplace density of \(Y\), split into positive and negative halves, and integrate the same Gaussian tail. Their difference equals \(h(u)/(8\alpha)\), proving both covariance identities. Continuity gives the \(t=0\) endpoints. The Poisson marking theorem applied to the four joint occupancy types at two times yields three independent Poisson populations, proving the joint generating function; this general structure predates the present evaluation.

**Strict decay and asymptotics.** For \(z>0\) and \(t>0\),
\[
a_t(z)-f(z)b_t(z)
=\operatorname{Cov}\left({\bf1}_{\{Y>z\}},
\Phi\!\left(\frac{Y-z}{\sqrt{2Dt}}\right)\right).
\]
Given one value of \(Y\) above \(z\) and another below, the conditional difference of the two displayed normal cdfs is strictly positive and strictly decreases as \(t\) increases. Conditioning on both sides of the threshold proves that the integrand, and hence its integral, is positive and strictly decreasing in \(t\). Multiplication by \(e^{-rt}\) preserves strict decline. The standard expansion \(e^u\operatorname{erfc}(\sqrt u)= (\pi u)^{-1/2}[1-(2u)^{-1}+3(4u^2)^{-1}+O(u^{-3})]\) yields \(h(u)\sim4/\sqrt{\pi u}\), proving the claimed large-lag behavior.

**Long-time law.** Given \(\Pi\), the countable product of independently reset Brownian processes is stationary and ergodic: finite-cylinder observables are exponentially mixing since each of their finitely many particles resets, and finite cylinders are dense in the product \(L^2\) space. The count \(Q_t\) is integrable because \(\sum_{z\in\Pi}f(z)<\infty\) almost surely. The ergodic theorem therefore gives the almost-sure limit \(\sum_{z\in\Pi}f(z)\). The Poisson Laplace functional, with substitution \(w=e^{-\alpha z}/2\), gives the transform above, and expanding the exponent shows \(\kappa_n(M_{\Pi})=\rho\int_0^\infty f(z)^n dz=\theta/(n2^n)\). To identify the distribution, order the anchors and let \(E\) be their first distance, exponential of rate \(\rho\). Translation invariance and the Poisson memoryless property imply
\[
W=2M_{\Pi}\stackrel d=e^{-\alpha E}(1+W'),
\]
with \(W'\) an independent copy. Since \(e^{-\alpha E}\stackrel d=U^{1/\theta}\), this is the generalized Dickman fixed-point identity.

## Verification

Run `python check.py` after installing packages from `requirements.txt`. The self-contained script performs 145 assertions: the equal-lag marginal and variance limits, all-lag formulas, comparison with independent nested Gaussian-probability quadrature for three different physical parameter triples, strict monotonicity on dense numerical grids, the sharp asymptotic coefficients, and the shot-noise Laplace/cumulant identities. All 145 passed. These checks are supplementary; analytical proofs of every infinite-domain statement are given above. The scripts do not simulate infinite particles or independently establish research priority.

## Relationship to prior work

Di Bello et al. (arXiv:2302.06696, first posted 2023-02-13) introduced the same independent-resetting step-density gas and evaluated its *single-time* annealed and quenched counting distributions, mean current, and stationary variances. In particular the single-time Poisson law and the stationary mean conditional variance \(3\theta/8\) are prior results. The present two-time formula agrees with these at zero lag.

Dean, Majumdar, and Schehr (arXiv:2303.08961, 2023) derived general two-time effusion identities and an annealed bivariate-Poisson structural law for independent particles. Their formulas, in principle, reduce the covariance of any specified dynamics to a one-particle two-time propagator; the structural formula is not new. Their evaluated Gaussian-process examples do not include resetting Brownian particles, whose stationary two-time paths are non-Gaussian. The evaluated resetting-specific complementary-error-function rate, its persistent disorder plateau, and the identified long physical-time generalized Dickman distribution are not stated in those inspected calculations.

The generalized Dickman distribution and its fixed-point description are classical; see Bhattacharjee and Goldstein (arXiv:1706.08192, 2017). The new identification concerns this resetting-current time average, not the distribution itself. Related finite-box effusion calculations without resetting (arXiv:2404.13988) do not determine the frozen-Poisson-anchor long-time law.

## Limitations

The conclusions require independent complete Poisson resets to *fixed* individual initial positions, a stationary initial displacement law, independent particles, a Poisson anchor field, and constant positive parameters. Resetting every particle simultaneously, resampling anchors, non-Poisson anchors, finite boxes, run-and-tumble motion, and physical current-current derivatives are not covered. The nonzero plateau describes the annealed stationary ensemble; at a fixed realization of anchors the connected lag covariance decays. No claim is made that the bivariate-Poisson structure or generalized Dickman distribution is itself newly discovered. The literature comparison does not rule out an unlocated exact equivalent specialization elsewhere.

## References

1. C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso, G. Schehr, *Current fluctuations in stochastically resetting particle systems*, arXiv:2302.06696 (first posted 2023-02-13), https://arxiv.org/abs/2302.06696 .
2. D. S. Dean, S. N. Majumdar, G. Schehr, *Effusion of stochastic processes on a line*, arXiv:2303.08961 (first posted 2023-03-15), https://arxiv.org/abs/2303.08961 .
3. C. Bhattacharjee, L. Goldstein, *Dickman approximation in simulation, summations and perpetuities*, arXiv:1706.08192 (2017), https://arxiv.org/abs/1706.08192 .
4. *Current fluctuations in finite-sized one-dimensional non-interacting passive and active systems* (arXiv:2404.13988, 2024), https://arxiv.org/abs/2404.13988 .
