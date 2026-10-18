# Gaussian invariant-measure resonance and time-average penalty for two stochastic Runge–Kutta samplers

## Finding
For the two Langevin stochastic Runge–Kutta schemes SRK-I and SRK-II defined below, **every real quadratic potential produces exactly the same random trajectory in both schemes** when the Brownian increments and integrals are shared. On a strictly convex Gaussian target, the common scheme admits a unique invariant probability law precisely under the sharp step-size condition \(0<h\lambda_{\max}(K)<2\). Its invariant covariance has an explicit spectral formula and coincides with the correct target covariance in every direction at a positive step size **if and only if** \(K=\lambda I\) and \(h=4/(3\lambda)\). At that exceptional step, the invariant law is exactly correct, but the stationary physical-time mean-square variance coefficient for a linear observable is \(7/3\) times the corresponding coefficient of the continuous Ornstein–Uhlenbeck diffusion.

## Assumptions and scope
Let \(d\ge1\), let \(K\in\mathbb R^{d\times d}\) be symmetric positive definite, let \(m\in\mathbb R^d\), and define the quadratic potential \(U(x)=\frac12(x-m)^\mathsf{T}K(x-m)\). Consider the overdamped Langevin equation
\[
\mathrm dX_t=-K(X_t-m)\,\mathrm dt+\sqrt2\,\mathrm dB_t,
\]
with standard \(d\)-dimensional Brownian motion, whose target law is \(\pi=\mathcal N(m,K^{-1})\). Fix \(h>0\). At step \(k\), define the **jointly sampled** Brownian increment and Brownian time integral
\[
\Delta B_k=B_{(k+1)h}-B_{kh},\qquad J_k=\int_{kh}^{(k+1)h}(B_s-B_{kh})\,\mathrm ds.
\]
The pairs \((\Delta B_k,J_k)\) are independent across steps, with within-step covariance \(\operatorname{Cov}(\Delta B_k)=hI\), \(\operatorname{Cov}(J_k)=h^3I/3\), and \(\operatorname{Cov}(\Delta B_k,J_k)=h^2I/2\). Both schemes use the same pair at each step.

SRK-I (two gradient evaluations) uses
\[
Y_k=Z_k-\frac{3h}{4}\nabla U(Z_k)+\frac{3\sqrt2}{2h}J_k,
\qquad
Z_{k+1}=Z_k-\frac h3\nabla U(Z_k)-\frac{2h}{3}\nabla U(Y_k)+\sqrt2\Delta B_k.
\]
SRK-II (three gradient evaluations) uses
\[
Y_k^\pm=Z_k-\frac h2\nabla U(Z_k)+\frac{\sqrt2}{h}\left(1\pm\frac1{\sqrt2}\right)J_k,
\qquad
Z_{k+1}=Z_k-\frac h2\bigl(\nabla U(Y_k^+)+\nabla U(Y_k^-)\bigr)+\sqrt2\Delta B_k.
\]
These are the integrators displayed in [1, Section 2.2, equations (2.1) and (2.2)] and the two-stage construction in [2, equations (15)–(16)]. Neither result is claimed for the distinct 2019 SRK-LD method [3], nonlinear potentials, approximate Brownian-integral sampling, or Metropolis-corrected schemes.

## Proof
**Step 1: identical pathwise affine maps.** Since \(\nabla U(x)=K(x-m)\), substituting the SRK-I stage and collecting terms yields, for \(e_k=Z_k-m\),
\[
e_{k+1}=R_h e_k+\sqrt2(\Delta B_k-KJ_k),\qquad R_h=I-hK+\frac{h^2}{2}K^2.
\]
For SRK-II, the average of the two intermediate stages equals \(Z_k-\frac h2K e_k+\frac{\sqrt2}{h}J_k\). Substitution gives the identical map, for every realization and every initial state. This proves pathwise equality by induction when driving pairs are coupled.

**Step 2: covariance and exact stability.** Brownian covariance identities give the one-step innovation covariance
\[
Q_h=2h\left(I-hK+\frac{h^2}{3}K^2\right).
\]
For an eigenvalue \(\lambda>0\) of \(K\), write \(z=h\lambda\), \(r(z)=1-z+z^2/2\), and \(q(z)=2h(1-z+z^2/3)\). The quadratic \(1-z+z^2/3\) is strictly positive for real \(z\). Furthermore \(r(z)=\frac12+\frac12(z-1)^2>0\), and \(r(z)<1\) holds exactly for \(0<z<2\). Thus all modes are contractive exactly when \(h\lambda_{\max}(K)<2\). In this case the affine Gaussian autoregression has a unique invariant law \(\mathcal N(m,\Sigma_h)\), reached in distribution from any deterministic starting point. If any mode has \(r\ge1\), its nondegenerate Gaussian innovation makes the stationary characteristic-function relation impossible: iterating \(\phi(t)=\phi(rt)\exp(-q t^2/2)\) forces \(\phi(t)=0\) for every \(t\ne0\), contradicting continuity at zero. Hence no invariant probability measure exists then.

**Step 3: invariant covariance and its unique resonance.** The scalar invariant variance is \(q(z)/(1-r(z)^2)\). Using
\[
1-r(z)^2=2z\left(1-z+\frac{z^2}{2}-\frac{z^3}{8}\right),
\]
we obtain, by spectral functional calculus,
\[
\boxed{\Sigma_h=K^{-1}f(hK)},\qquad
f(z)=\frac{1-z+z^2/3}{1-z+z^2/2-z^3/8}.
\]
The denominator is positive throughout \(0<z<2\), and subtraction of one gives the exact defect
\[
\boxed{f(z)-1=\frac{z^2(3z-4)}{24\left(1-z+z^2/2-z^3/8\right)}}.
\]
Thus every spectral direction has variance below, equal to, or above its target variance according as \(h\lambda<4/3\), \(h\lambda=4/3\), or \(h\lambda>4/3\). The equality condition in all eigendirections is precisely \(h\lambda_i=4/3\) for every eigenvalue, equivalent to \(K=\lambda I\) and \(h=4/(3\lambda)\). The positive resonance is unique within the stable region.

**Step 4: a correct invariant law still incurs a time-average variance penalty.** Take the scalar case \(d=1\), \(K=[\lambda]\), and stationarily initialize at the resonant step \(h=4/(3\lambda)\). Then \(r(4/3)=5/9\), \(\operatorname{Var}(Z_k)=1/\lambda\), and \(\operatorname{Cov}(Z_0,Z_j)=r(4/3)^j/\lambda\). Consequently, for \(\overline Z_N=N^{-1}\sum_{k=0}^{N-1}Z_k\),
\[
\lim_{N\to\infty}N\operatorname{Var}(\overline Z_N)
=\frac1\lambda\left(1+2\sum_{j\ge1}(5/9)^j\right)
=\frac7{2\lambda}.
\]
Writing physical observation time \(T=Nh\) gives
\[
\boxed{\lim_{N\to\infty}T\operatorname{Var}(\overline Z_N)=\frac{14}{3\lambda^2}}.
\]
For the stationarily initialized exact Ornstein–Uhlenbeck diffusion and its continuous-time average \(T^{-1}\int_0^T X_t\,\mathrm dt\), its covariance function is \(\lambda^{-1}e^{-\lambda|t-s|}\). Direct integration yields
\[
\lim_{T\to\infty}T\operatorname{Var}\left(\frac1T\int_0^T X_t\,\mathrm dt\right)=\frac2{\lambda^2}.
\]
The ratio is therefore exactly \(\boxed{7/3}\). In an isotropic multivariate target this is the same factor for any nonzero linear observable. This comparison concerns a discrete sample average at mesh times versus a continuously observed physical-time average; it is not a comparison at equal computational cost.

## Verification
The standalone `verify.py` (requires SymPy) reconstructs both stage formulas independently, checks the universal polynomial identities and resonance, and compares exact-rational stage updates on 450 separately chosen input/step combinations. It also checks exact stationary and finite-horizon covariance identities at several rational dimensionless steps. The recorded run passed 483 exact algebraic and rational comparisons. The proof above, not finite testing, establishes the all-dimensional and all-step claims.

## Relationship to prior work
Yang–Wang [2] introduce the two-gradient method and analyze Wasserstein convergence. Ye [1] gives both stage formulas and a general time-average mean-square error bound of \(O((Nh)^{-1}+h^4)\) for small steps, but the inspected methods and main results do not state the exact Gaussian stationary-covariance resonance or its physical-time averaging penalty. Li–Wu–Mackey–Erdogdu [3] analyze a different, earlier stochastic Runge–Kutta sampler, with global sampling error guarantees rather than the invariant law of this specific pair of algorithms. Earlier work on underdamped UBU integrators addresses a different update and is not an implication for these two algorithms. Standard Gaussian autoregression formulas are not claimed as new; the contribution is their exact application to the recently defined scheme pair, yielding the unique nonzero exact-invariance step, anisotropic obstruction, and quantitative time-average mismatch. The finite positive resonance may still have appeared in another unindexed stochastic-integrator study.

## Limitations
The scope is exact, jointly sampled Brownian increments and integrals; strict positive definiteness; constant step size; and the published schemes' precise coefficients. Quadratic potentials are essential to pathwise coincidence. The exact resonance is not a generic property of stochastic Runge–Kutta methods and is outside the small-step asymptotic premise of general convergence theorems. Invariant correctness is a statement about the marginal stationary law, not transition-kernel exactness or optimal sample efficiency. No assertion is made about nonquadratic invariant laws, finite-time estimator bias, or uninspected literature.

## References
[1] Xuda Ye, *Mean Square Error Analysis of Stochastic Runge–Kutta Integrators*, arXiv:2609.11528, first posted 2026-09-10. https://arxiv.org/abs/2609.11528

[2] Bin Yang and Xiaojie Wang, *Accelerating Langevin Monte Carlo via Efficient Stochastic Runge–Kutta Methods beyond Log-Concavity*, arXiv:2605.07939, first posted 2026-05-08. https://arxiv.org/abs/2605.07939

[3] Xuechen Li, Denny Wu, Lester Mackey, and Murat A. Erdogdu, *Stochastic Runge–Kutta Accelerates Langevin Monte Carlo and Beyond*, NeurIPS 2019; arXiv:1906.07868. https://arxiv.org/abs/1906.07868
