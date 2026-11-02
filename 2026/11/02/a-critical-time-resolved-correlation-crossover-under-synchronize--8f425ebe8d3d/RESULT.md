# A critical time-resolved correlation crossover under synchronized weak resetting

## Finding

A common-noise Gaussian diffusion approximation can reproduce the **entire transient particle variance** of a synchronized proportional-reset process while misrepresenting its **time-resolved interparticle squared-energy covariance** on a sharp, nontrivial time scale. The exact process relaxes to a finite covariance on that scale, whereas the Gaussian replacement develops exponentially increasing covariance. The difference is quantified by two explicit critical scaling functions and a strict finite-time comparison valid for every time and every admissible reset strength.

Fix \(D,\lambda>0\), \(0<s<1\), an integer \(N\ge2\), and real \(\gamma\). Let \(q=1-s\), \(R=\lambda/s\). Starting at \(X_i(0)=Y_i(0)=0\), the common-reset model has independent Brownian motions between simultaneous rate-\(R\) Poisson events,
\[
 dX_i(t)=\gamma X_i(t)\,dt+\sqrt{2D}\,dB_i(t),\qquad X_i(t)=qX_i(t-)\ \text{at each event},
\]
while its standard weak-reset Itô replacement is
\[
 dY_i(t)=(\gamma-\lambda)Y_i(t)\,dt+\sqrt{\lambda s}\,Y_i(t)\,dW(t)+\sqrt{2D}\,dB_i(t).
\]
The \(B_i\) are independent and independent of the common Poisson clock and the common Brownian motion \(W\). Define
\[
 V(t)=\mathbb EX_1(t)^2=\mathbb EY_1(t)^2,\quad C_P(t)=\operatorname{Cov}(X_1(t)^2,X_2(t)^2),\quad C_G(t)=\operatorname{Cov}(Y_1(t)^2,Y_2(t)^2).
\]
Write
\[
 a_1=2(\lambda-\gamma)-\lambda s,\quad
 a_2^P=(\lambda/s)[1-(1-s)^4]-4\gamma,\quad
 a_2^G=4(\lambda-\gamma)-6\lambda s.
\]
At **every** \(s\in(0,1)\) and \(t>0\), for all real \(\gamma\), the transient moments are finite, \(V(t)=2D(1-e^{-a_1t})/a_1\) (continuous extension at \(a_1=0\)), and
\[
 \boxed{\quad 0<C_P(t)<C_G(t).\quad} \tag{1}
\]

In particular, fix \(0<\theta<1\) and approach the fourth-moment instability along the physically natural parameter curve
\[
 \gamma_s=\lambda\bigl(1-3s/2+\theta s^2\bigr),
 \qquad t_s(u)=\frac{u}{\lambda s^2},\quad u\ge0.
\]
For all sufficiently small \(s>0\), both processes have stationary distributions and finite stationary second moments; the original Poisson system has a finite stationary fourth moment while its Gaussian surrogate has an infinite stationary fourth moment. Yet at finite times all displayed covariances exist, and the following limits hold **uniformly for \(u\) in each compact subset of \([0,\infty)\)**:
\[
 \boxed{\quad\lim_{s\downarrow0}\frac{\lambda^2s^3}{D^2}C_P(t_s(u))
 =\frac{1-e^{-4(1-\theta)u}}{1-\theta},\qquad
 \lim_{s\downarrow0}\frac{\lambda^2s^3}{D^2}C_G(t_s(u))
 =\frac{e^{4\theta u}-1}{\theta}.\quad} \tag{2}
\]
These are different functions at every \(u>0\). In particular, the Gaussian-to-Poisson relative bias tends to
\[
 \boxed{\quad \mathcal R_\theta(u)=
 \frac{(1-\theta)(e^{4\theta u}-1)}{\theta(1-e^{-4(1-\theta)u})}>1,\qquad u>0.\quad} \tag{3}
\]
The limiting covariance difference starts with the **parameter-independent** short-rescaled-time law
\[
 \frac{e^{4\theta u}-1}{\theta}-\frac{1-e^{-4(1-\theta)u}}{1-\theta}
 =8u^2+O_\theta(u^3)\quad(u\downarrow0).
\]
Thus a Gaussian approximation which is exactly correct for the full two-point variance curve can first fail in the time-resolved four-point sector at the much longer \(s^{-2}\) time scale.

## Assumptions and scope

The theorem concerns independent scalar Brownian particle noises, deterministic synchronous contraction by \(1-s\), the exact common-noise Itô approximation above, zero initial positions, and **equal** drift and diffusion parameters across particles. Covariance means equal-time squared-position cross-covariance, not temporal autocorrelation or a time-integrated current. The scaling result keeps \(\theta\in(0,1)\) fixed as \(s\downarrow0\). For the qualitative stationary comparison it is enough that \(s<\min(1/2,4(1-\theta))\), ensuring \(\gamma_s>0\), \(a_1>0\), \(a_2^P>0>a_2^G\) and negative almost-sure growth of both stationary propagators.

## Proof

**Step 1 (conditional independence and common variance).** Condition on the entire common Poisson history. The \(X_i(t)\) are independent centered Gaussians with a common random conditional variance \(Z_P(t)\); conditional on \(W\), the same statement holds for \(Y_i(t)\) with random variance \(Z_G(t)\). Therefore \(C_P(t)=\operatorname{Var}(Z_P(t))\) and \(C_G(t)=\operatorname{Var}(Z_G(t))\). All moments are finite for finite \(t\), by bounded-time Poisson exponential moments and Gaussian exponential moments.

**Step 2 (closed transient moment equations).** Between Poisson events, the conditional variance obeys \(\dot Z_P=2\gamma Z_P+2D\); each common reset sends \(Z_P\mapsto q^2Z_P\). Thus its first and second moments \(m_1(t)=\mathbb EZ_P(t)\), \(m_2^P(t)=\mathbb EZ_P(t)^2\) satisfy
\[
 m_1'=-a_1m_1+2D,\qquad (m_2^P)'=-a_2^P m_2^P+4Dm_1,
\]
with zero initial conditions. For the Gaussian approximation, the stochastic multiplier gives \(dZ_G=[(2\gamma-2\lambda+\lambda s)Z_G+2D]dt+2\sqrt{\lambda s}\,Z_GdW\) (this is **not** the pathwise squared position). Itô's formula yields exactly the same \(m_1\) equation and \((m_2^G)'=-a_2^G m_2^G+4Dm_1\). Hence
\[
 m_1(t)=\frac{2D}{a_1}(1-e^{-a_1t}),\qquad
 m_2^Q(t)=4D\int_0^t e^{-a_2^Q(t-v)}m_1(v)\,dv\quad(Q=P,G).
\]
These are valid also for negative and zero coefficients, using the continuous integral definition. Since \(a_2^P-a_2^G=\lambda s^2(4-s)>0\) and \(m_1(v)>0\) for \(v>0\), the integrand for \(m_2^P\) is strictly smaller than for \(m_2^G\) at every \(t>0\). Subtract the identical \(m_1(t)^2\). Moreover, for every \(t>0\), the Poisson clock has positive probabilities of both no resets and at least one reset, and the resulting conditional variance differs on events of positive probability because \(q<1\) and \(D>0\); thus \(\operatorname{Var}(Z_P(t))>0\). This proves (1).

**Step 3 (critical time).** On the specified curve,
\[
 a_1=2\lambda s(1-\theta s),\quad a_2^G=-4\lambda\theta s^2,\quad
 a_2^P=\lambda s^2[4(1-\theta)-s].
\]
Put \(v=w/(\lambda s^2)\). The exact convolution becomes
\[
 \frac{\lambda^2s^3}{D^2}m_2^Q(t_s(u))
 =4\int_0^u e^{-[a_2^Q/(\lambda s^2)](u-w)}
 \frac{\lambda s}{D}m_1(t_s(w))\,dw.
\]
For every \(w>0\), \((\lambda s/D)m_1(t_s(w))=[1-e^{-2(1-\theta s)w/s}]/(1-\theta s)\to1\); it is uniformly bounded by \((1-\theta s)^{-1}\). The exponential kernels converge uniformly on bounded \((u,w)\) triangles. Dominated convergence, with a uniform integral estimate, therefore yields compact-uniform convergence to \(4\int_0^u e^{-4(1-\theta)(u-w)}dw\) in the Poisson case and \(4\int_0^u e^{4\theta(u-w)}dw\) in the Gaussian case. The scaled mean-square subtraction \((\lambda^2s^3/D^2)m_1(t_s(u))^2\) is bounded by \(s/(1-\theta s)^2\to0\) uniformly. This proves (2). Elementary comparison of integrands proves (3); Taylor expansion gives \(8u^2\).

**Step 4 (stationary boundary consistency).** Along this curve \(a_1>0\), \(a_2^P>0>a_2^G\) for small \(s\). Conditional Gaussian fourth moments equal three times the second moments of the conditional variance, so the Poisson fourth stationary moment is finite while the Gaussian fourth stationary moment diverges. Negative almost-sure Lyapunov exponents of the respective propagators follow from \(\gamma_s<-(\lambda/s)\log(1-s)\) and \(\gamma_s<\lambda(1+s/2)\). These stationary facts justify the physical choice of the critical curve; (2) is proved directly from finite-time equations and does not assume stationary limits commute with \(s\downarrow0\).

## Verification

The accompanying `verify.py` independently solves both first-/second-conditional-variance moment equations in closed form and checks them against direct numerical quadrature and differential equations at multiple positive rational parameters. It checks exact symbolic gap identities and the exact critical-time limits at successively smaller reset strengths, plus strict finite-time covariance ordering. These finite checks are not proofs of uniform asymptotics; the latter follow from the dominating bound in Step 3.

## Relationship to prior work

Galla (2026) provides the weak-reset approximation and its **stationary** Gaussian interparticle squared-position covariance. Earlier partial resetting and Gaussian stochastic dynamics work establish the underlying Gaussian-mixture and moment methods. Prior exact stationary moment cutoff comparisons for Poisson versus Gaussian weak resets are **not** claimed as new. The result here is instead the **critical transient correlation scaling law (2)–(3)**, including the entire \(u\)-dependent finite-time profile, the sharper \(s^{-2}\) time-scale separation from variance relaxation, and the universal initial \(8u^2\) profile difference. A stationary denominator comparison does not imply the transient profiles without controlling the joint noncommuting time/reset limit. No equivalent or stronger time-resolved result was identified in the inspected primary material or accessible research records; broader semigroup comparison theory is a residual priority risk.

## Limitations

The model is linear and its exact moment closure is special. No result is stated about nonlinear drift, non-Poisson or asynchronous resets, arbitrary initial laws, temporal autocorrelation, higher spatial dimensions with correlated Brownian drivers, or relative errors for all times at fixed \(s\). A small-reset critical scaling is not a uniform finite-\(s\) approximation. Scientific priority remains best-knowledge; independent review is not performed.

## References

- Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1, first publicly submitted February 25, 2026, https://arxiv.org/html/2602.21635 .
- J. Kevin Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1, https://arxiv.org/html/2204.07215v1 .
- Marco Biroli, Yannick Feld, Alexander K. Hartmann, Satya N. Majumdar, and Gregory Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1, https://arxiv.org/html/2406.08387v1 .
