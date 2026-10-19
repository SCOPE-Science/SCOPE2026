# A unique thermal-noise-induced kurtosis optimum under complete resetting of an active Ornstein–Uhlenbeck particle

## Finding

For a one-dimensional overdamped particle driven by a Gaussian active Ornstein–Uhlenbeck force and independent thermal noise, suppose a rate-\(r\) Poisson clock resets **both** position and active force to zero. Let \(\tau\) be the active-force correlation time, \(f\) its unreset stationary standard deviation, \(\gamma\) the friction, and \(D\) the translational thermal diffusivity. Define the dimensionless reset rate and thermal-to-active ratio
\[
k=r\tau>0,\qquad h=\frac{2D\gamma^2}{f^2\tau}\geq0.
\]
The stationary positional **excess kurtosis**, \(K_h(k)=\mathbb E[X^4]/\mathbb E[X^2]^2-3\), obeys the exact law
\[
\boxed{K_h(k)=3+\frac{24k(2hk^3+17hk^2+45hk+36h+36k+72)}{(k+3)(k+4)[h(k+1)(k+2)+4]^2}.}
\]
For **every \(h>0\)** there is **exactly one** \(k_*(h)>0\) at which \(K_h\) is globally maximized; the function strictly increases before and strictly decreases after that point, and tends to \(3\) at both endpoints \(k\downarrow0\) and \(k\to\infty\). In contrast, for **\(h=0\)** the function strictly increases from \(3\) to \(57\) and has no finite maximizer. Thus any positive thermal noise qualitatively changes the reset-frequency optimization of standardized rare displacement fluctuations. The maximum height is strictly decreasing as \(h\) increases.

## Assumptions and scope

Take independent standard Brownian motions \(B,W\), and strictly positive constants \(\gamma,\tau,f,r\), with \(D\geq0\). Between Poisson reset times, set
\[
dX_t=\frac{F_t}{\gamma}\,dt+\sqrt{2D}\,dB_t,\qquad
dF_t=-\frac{F_t}{\tau}\,dt+\sqrt{\frac{2f^2}{\tau}}\,dW_t.
\]
At each Poisson event, \((X,F)\mapsto(0,0)\) instantaneously, independently of the Brownian motions. The process is observed in its unique regenerative stationary distribution. In particular, the active force is restarted at zero, **not** sampled from its unreset stationary law, and thermal noise and active noise are independent. Kurtosis is one-dimensional Pearson fourth-moment excess (Gaussian baseline \(0\)); the value \(3\) at a limit is excess kurtosis, not total kurtosis. No confinement, inertia, viscoelastic memory, or position-only resetting is assumed.

## Proof

**Regenerative Gaussian mixture.** The backward time \(T\) to the last complete Poisson reset has density \(r e^{-rt}\), independent of Brownian increments after that reset. Conditional on \(T=t\), the position has mean zero and is Gaussian. Solving the linear active-force equation with \(F_0=0\) and integrating it gives the active contribution
\[
\int_0^t F_s\,ds=\sqrt{2f^2\tau}\int_0^t\big(1-e^{-(t-s)/\tau}\big)\,dW_s.
\]
Consequently, setting \(u=t/\tau\) and \(C=f^2\tau^2/\gamma^2>0\), the conditional positional variance is exactly
\[
V(t)=C\big(hu+g(u)\big),\qquad
g(u)=2u-3+4e^{-u}-e^{-2u}.
\]
The function \(g\) is nonnegative because it equals twice the integral of \((1-e^{-v})^2\) from \(0\) to \(u\). Let \(U\) be exponential with rate \(k\). Thus the stationary distribution is a zero-mean Gaussian scale mixture with conditional variance \(C[hU+g(U)]\). All required moments exist because \(g(u)\leq2u\) and \(U\) has every finite moment.

**Exact second and fourth moments.** Write \(M_1=\mathbb E[hU+g(U)]\) and \(M_2=\mathbb E[(hU+g(U))^2]\). Exponential integration, using \(\mathbb E[U^n e^{-jU}]=k n!/(k+j)^{n+1}\), gives
\[
\begin{aligned}
\mathbb E[g(U)]&=\frac{4}{k(k+1)(k+2)},\\
\mathbb E[g(U)^2]&=\frac{32(10k^2+25k+12)}{k^2(k+1)^2(k+2)^2(k+3)(k+4)},\\
\mathbb E[Ug(U)]&=\frac{4(4k^2+9k+4)}{k^2(k+1)^2(k+2)^2},\\
M_1&=\frac{h}{k}+\mathbb E[g(U)],\\
M_2&=\frac{2h^2}{k^2}+2h\mathbb E[Ug(U)]+\mathbb E[g(U)^2].
\end{aligned}
\]
Since \(X\mid U\) is centered Gaussian, \(\mathbb E[X^2]=CM_1\) and \(\mathbb E[X^4]=3C^2M_2\). Therefore \(K_h=3M_2/M_1^2-3\), which factors to the displayed exact formula. Its added rational term has strictly positive numerator and denominator for every \(k>0\), \(h\geq0\), hence \(K_h(k)>3\).

**Uniqueness of the finite optimum.** Direct differentiation yields
\[
\frac{dK_h}{dk}=-\frac{24P_h(k)}{(k+3)^2(k+4)^2[h(k+1)(k+2)+4]^3},
\]
with the polynomial
\[
\begin{aligned}
P_h(k)={}&h^2(4k^7+65k^6+419k^5+1337k^4+2077k^3+1026k^2-864k-864)\\
&+h(128k^5+1096k^4+2948k^3+1692k^2-3456k-3456)\\
&-720k^2-3456k-3456.
\end{aligned}
\]
For each \(h>0\), the coefficients of degrees \(7,6,5,4,3\) are strictly positive, that of degree \(2\) has either sign, and those of degrees \(1,0\) are strictly negative. Reading coefficients in descending degree and deleting any zero coefficient gives **exactly one sign change**. Descartes' rule gives at most one positive real zero. Since \(P_h(0)=-864(h+2)^2<0\) while its leading coefficient is \(4h^2>0\), continuity gives at least one. Thus there is exactly one positive root, with \(K_h'\) positive before and negative after. The limits \(K_h(k)\to3\) at \(k\downarrow0\) and \(k\to\infty\), together with strict positivity above \(3\), show this root is the unique global maximizer.

At \(h=0\), instead,
\[
\frac{dK_0}{dk}=\frac{54(5k^2+24k+24)}{(k+3)^2(k+4)^2}>0,
\]
while \(K_0(k)\to3\) as \(k\downarrow0\) and \(K_0(k)\to57\) as \(k\to\infty\). Hence no finite maximizer exists without thermal noise.

**Thermal-noise dependence.** Differentiating at fixed \(k>0\) gives
\[
\frac{\partial K_h}{\partial h}=-\frac{24k[2hk^5+23hk^4+100hk^3+205hk^2+198hk+72h+64k^3+292k^2+396k+144]}{(k+3)(k+4)[h(k+1)(k+2)+4]^3}<0.
\]
The optimized peak is therefore strictly decreasing with \(h\): for two positive noise ratios, compare the larger-noise optimum with the smaller-noise function at that same strictly positive reset rate.

A further sharp weak-thermal-noise consequence follows by dividing the critical polynomial by its dominant scale at \(k\asymp h^{-1/3}\): the unique optimum obeys \(k_*(h)\sim(45/(8h))^{1/3}\) as \(h\downarrow0\), and the peak tends to the \(h=0\) supremum \(57\). This is a sequential limit of stationary distributions; there is no stationary law at \(r=0\).

## Verification

The included `verify.py` reconstructs Gaussian age-mixture moments from elementary exponential integrals, verifies the displayed rational kurtosis and derivative polynomial in exact symbolic arithmetic, checks the sign-change certificate, compares to **20 independent high-accuracy numerical quadratures** at varying reset and noise ratios, locates six unique positive derivative roots, and corroborates three representative cases with seeded Gaussian age-mixture simulations of 1,500,000 draws each. It reports `PASS` when its assertions hold. The script is reproducible using Python, SymPy, SciPy and NumPy; it does not require remote data. Quadrature and finite sampling are checks on, not replacements for, the infinite-domain Gaussian-mixture proof and Descartes argument.

For example, at \(h=1\), the optimal dimensionless reset rate is \(k_*=1.1739006879\ldots\), and the maximum stationary excess kurtosis is \(5.5229089372\ldots\).

## Relationship to prior work

Shankari and Sahoo (2025) develop renewal-propagator and mean-square-displacement formulas for an active Ornstein–Uhlenbeck particle subject to full stochastic resetting, including the overdamped thermal-noise model. Their Gaussian no-reset propagator and complete-reset renewal equation provide the natural starting point. The present result is not a new renewal formula: it identifies and proves a complete global-reset-frequency classification of the **stationary standardized fourth moment**, including its exact rational law, unique finite optimum for any positive thermal noise, and qualitatively different zero-thermal-noise endpoint.

Patel and Shee (2026) analyze fourth moments and non-Gaussianity under complete resetting of a **two-dimensional inertial active Brownian particle driven by a fixed-speed rotating orientation**. Their reset-driven kurtosis behavior makes the observable important but their force and inertia dynamics are not the one-dimensional, Gaussian active-force process specified here. Related viscoelastic-bath studies reset a probe while retaining bath memory; that protocol does not restart the active force at zero. The general facts that reset stationary laws are renewal mixtures and that centered Gaussian mixtures have excess kurtosis governed by variance mixing are standard; originality is claimed only for the specific exact law and sharp whole-parameter classification.

## Limitations

The theorem applies only to the free overdamped **complete-reset** process with a Gaussian active-force OU component and independent thermal Brownian noise. It does not concern force-only resetting, position-only resetting with persistent active-force memory, bounded domains, harmonic traps, inertial motion, viscoelastic baths, or non-Poisson resetting. Kurtosis is a standardized fourth moment and does not determine tail asymptotics, mean first-passage times, or operational optimality in any other objective. A more general renewal-based fourth-moment theorem could reproduce this particular algebraic specialization; such implicit coverage is a residual priority risk.

## References

1. U. Shankari and M. Sahoo, *Active Ornstein-Uhlenbeck particle under stochastic resetting*, arXiv:2509.18515v1, first posted 23 September 2025, https://arxiv.org/abs/2509.18515 .
2. M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134v1, 24 February 2026, https://arxiv.org/abs/2602.21134 .
3. D. K. Georgiou, P. C. Bressloff, and T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein--Uhlenbeck particle*, arXiv:2609.21124, 17 September 2026, https://arxiv.org/abs/2609.21124 (abstract-level topical check; not a full-text originality exclusion).
