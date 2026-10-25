# Sharp finite-horizon excursion tails under stationary velocity resetting

## Finding

A randomly accelerated particle has a stationary *velocity* but no stationary position when only its velocity is reset. Surprisingly, for any fixed observation duration \(T>0\), its position increment has a sharp, ordinary exponential far tail even though its long-time variance is diffusive.

Fix a Poisson reset rate \(r>0\) and acceleration-noise diffusivity \(D>0\). Set \(\kappa=\sqrt{r/D}\). Let \(V\) be the stationary continuous-time process satisfying \(dV_t=\sqrt{2D}\,dW_t\) between independent rate-\(r\) resets \(V\mapsto0\). The position itself is never reset. Observe the increment \(X_T=\int_0^T V_s\,ds\), and write \(N_T\) for the number of velocity resets during \((0,T)\).

**Theorem (exact fixed-time extreme-excursion law).** For every \(r,D,T>0\),
\[
\lim_{x\to\infty}e^{\kappa x/T}\Pr(X_T>x)
=\frac12e^{-2rT/3},\qquad
\Pr(N_T=0\mid X_T>x)\longrightarrow1.
\]
The same asymptotic holds for \(\Pr(X_T<-x)\). Thus a sufficiently extreme displacement diagnoses the absence of a velocity reset *during the observation window*, even though earlier velocity-resetting events generate the stationary initial velocity.

The moment-generating function has the **exact finite-horizon domain**
\[
\mathbb E e^{\theta X_T}<\infty
\quad\Longleftrightarrow\quad
|\theta|<\kappa/T.
\]
Its leading boundary singularity satisfies
\[
\lim_{\theta\uparrow\kappa/T}
\left(1-\frac{D\theta^2T^2}{r}\right)
\mathbb E e^{\theta X_T}=e^{-2rT/3}.
\]
By contrast, the entire second-order increment law is governed by
\[
\operatorname{Var}(X_T)=
\frac{4D}{r^3}\left(rT-1+e^{-rT}\right)
\sim\frac{4D}{r^2}T\qquad(T\to\infty).
\]
These are separate, non-uniform limits: the far-tail statements fix \(T\) and let \(x\to\infty\), whereas the variance asymptotic lets \(T\to\infty\).

## Assumptions and scope

The velocity-reset events form a homogeneous Poisson process of rate \(r\), independent of a two-sided standard Brownian motion. At each event velocity becomes exactly zero, while position remains continuous. For the stationary velocity initialization at time zero, the Poisson process is constructed on the entire past and future real line. The sample-path integral defining \(X_T\) is ordinary, and \(T\) is finite and strictly positive. No viscosity, drag, restoring force, position reset, or refractory period is included. All probability statements concern the one-dimensional process and its unconditional stationary-velocity initialization, not a trajectory initialized by resetting velocity to zero at time zero.

## Proof

**1. Stationary initial velocity.** Let \(A\) be the time since the most recent reset before time zero. By Poisson memorylessness \(A\sim\operatorname{Exp}(r)\); given \(A=a\), the stationary velocity \(V_0\) is centered normal with variance \(2Da\). Hence
\[
\mathbb E e^{iuV_0}=\mathbb E e^{-Du^2A}=
\frac{r}{r+Du^2}=\frac{\kappa^2}{\kappa^2+u^2}.
\]
Therefore \(V_0\) has the centered Laplace density \(\frac\kappa2e^{-\kappa|v|}\). Crucially, \(V_0\) is independent of all Poisson events and Brownian increments after time zero.

**2. Exact conditional Gaussian mixture.** Fix the future Poisson times inside \((0,T)\). They partition the interval into lengths \(\ell_1,\ldots,\ell_{m+1}>0\) summing to \(T\). Set \(L=\ell_1\) and \(S=\sum_{j=1}^{m+1}\ell_j^3\). Additivity of the velocity integral across reset intervals gives exactly
\[
X_T\ \stackrel{d}{=}\ LV_0+G,\qquad
G\mid(\ell_j)\sim N\left(0,\frac{2D}{3}S\right),
\]
with \(V_0\) and \(G\) conditionally independent. Indeed, the integrated Brownian increments on disjoint intervals have variances \(2D\ell_j^3/3\). Since all lengths are nonnegative and sum to \(T\), \(S\le T^3\). On \(\{N_T=0\}\), \(L=T\) and \(S=T^3\); otherwise \(L<T\) almost surely.

**3. Uniform exponential-tail control.** Put \(c=\kappa/T\). The Laplace positive tail obeys, for all real \(u\) and all \(0<L\le T\),
\[
e^{cu}\Pr(LV_0>u)\le1.
\]
For \(u\ge0\), this follows from \(\Pr(LV_0>u)=\frac12e^{-\kappa u/L}\) and \(\kappa/L\ge c\); for \(u<0\), use \(\Pr(LV_0>u)\le1\le e^{-cu}\). Therefore, conditioning on the future reset times,
\[
e^{cx}\Pr(X_T>x\mid(\ell_j))
\le\mathbb E(e^{cG}\mid(\ell_j))
=\exp(Dc^2S/3)\le e^{rT/3}.
\]
For any fixed partition with \(L<T\), the strict inequality \(\kappa/L>c\) implies \(e^{cx}\Pr(LV_0+G>x)\to0\) by conditioning on \(G\) and dominated convergence. If \(L=T\), the same argument gives
\[
\lim_{x\to\infty}e^{cx}\Pr(TV_0+G>x)
=\frac12\mathbb E e^{cG}
=\frac12e^{rT/3}.
\]
The uniform bound permits dominated convergence over the random partition. The probability of no future resets is \(e^{-rT}\), so the total tail limit is \(\frac12e^{-rT}e^{rT/3}=\frac12e^{-2rT/3}\). All reset-containing histories contribute \(o(e^{-cx})\), which also proves the conditional no-reset probability tends to one. Reflection symmetry gives the negative tail.

**4. Exact exponential-moment boundary.** By the conditional mixture, whenever \(|\theta|L<\kappa\),
\[
\mathbb E(e^{\theta X_T}\mid(\ell_j))=
\frac{\kappa^2}{\kappa^2-\theta^2L^2}
\exp(D\theta^2S/3).
\]
When \(|\theta|T<\kappa\), this is uniformly bounded by its version with \(L=T\) and \(S=T^3\), so the unconditional moment is finite. When \(|\theta|T\ge\kappa\), the positive-probability event \(N_T=0\) has infinite conditional exponential moment, proving divergence. As \(\theta\uparrow c\), multiply the conditional formula by \(1-\theta^2T^2/\kappa^2\). The product is at most \(e^{rT/3}\), converges to zero on all partitions having \(L<T\), and converges to \(e^{rT/3}\) on \(N_T=0\). Dominated convergence gives the pole coefficient \(e^{-2rT/3}\).

**5. Diffusive second moment.** By stationary initialization and independence after the first reset,
\[
\mathbb E[V_0V_t]=(2D/r)e^{-rt},\qquad t\ge0.
\]
Integrating this velocity covariance over a square yields
\[
\mathbb E X_T^2=2\int_0^T(T-t)\mathbb E[V_0V_t]dt
=\frac{4D}{r^3}(rT-1+e^{-rT}).
\]
This completes the proof for all positive parameters, without taking limits of finite numerical experiments.

## Verification

The standalone `verify.py` checks 158 deterministic identities and numerical evaluations. It independently integrates the stationary exponential-age Gaussian variance and the velocity-covariance formula; compares the no-reset Laplace-plus-Gaussian convolution with the exact extreme-tail constant at multiple parameters and thresholds; tests the finite exponential-moment expressions in their valid domain; and numerically verifies the suppression of a one-reset trajectory class. Run from a directory containing this file with `python verify.py`. Requires Python 3 and SciPy. The proof of all \(x\to\infty\) assertions is analytic; finite-threshold quadrature is corroborative only.

## Relationship to prior work

Olsen and Löwen (2024, first arXiv version January 23, 2024) analyzed transport when one variable, notably velocity, resets while the observed coordinate does not. They developed transform and moment tools and established diffusive long-time displacement scaling. The present result addresses instead the *fixed-horizon extreme displacement of the stationary-velocity initialized process*, its sharp leading constant, and posterior inference of whether a reset occurred inside the window. Their full manuscript could not be independently inspected in this review; the completeness of priority comparison remains a specific risk.

Singh (2020) treated random acceleration under either joint position-and-velocity resetting or resetting of position alone, rather than the velocity-only resetting considered here; the accessible manuscript's model definitions and conclusions were inspected. Smith and Majumdar (2022) studied large-time anomalous deviations of areas under reset Gaussian processes, typically initialized at the reset point; their results involve a different initial ensemble and limit order from the fixed-time, stationary-velocity far-tail coefficient here. The exact numerical prefactor derived above is not an assertion of an entirely new resetting mechanism; it is a quantitative boundary phenomenon induced by equilibrium initialization.

## Limitations

The asymptotic holds with \(r,D,T\) fixed before sending the positive spatial threshold to infinity; it is not uniform as \(T\to\infty\), \(D\to0\), or \(r\to0\). The model neglects drag and resets velocity precisely to zero. It establishes neither a finite-threshold relative-error bound nor the rate at which \(\Pr(N_T=0\mid X_T>x)\) approaches one. No claims are made for arbitrary reset-time distributions, non-Gaussian driving noise, or higher dimensions. While the mathematical proof is self-contained, the claim's independent scholarly priority has not been established.

## References

1. K. Stølevik Olsen and H. Löwen, “Dynamics of inertial particles under velocity resetting,” *Journal of Statistical Mechanics: Theory and Experiment*, 033210 (2024); arXiv:2401.12685v1 (January 23, 2024). https://arxiv.org/abs/2401.12685
2. P. Singh, “Random acceleration process under stochastic resetting,” *Journal of Physics A* 53, 405005 (2020); arXiv:2007.05576v1 (July 10, 2020). https://arxiv.org/abs/2007.05576
3. N. R. Smith and S. N. Majumdar, “Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting,” *Journal of Statistical Mechanics: Theory and Experiment* 053212 (2022); arXiv:2202.03546v1 (February 7, 2022). https://arxiv.org/abs/2202.03546
