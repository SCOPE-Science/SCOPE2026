# Sharp finite-variance horizon for the Riccati coding-tree Monte Carlo integrator

## Finding

Let \(a>0\) and let \(H_{\mathrm{Id}}(t)\) be the positive weighted coding-tree estimator of Penent and Privault for the scalar initial-value problem \(y'(t)=y(t)^2\), \(y(0)=a\). Every particle has a fresh independent exponential lifetime of rate \(\lambda>0\). Under the precise derivative-code mechanism below, its second moment is finite **if and only if** \(0\le t<t_2(\lambda)\), where

\[
\kappa=\frac{\log(3+2\sqrt2)}{2\sqrt2},\qquad
 t_2(\lambda)=\frac1\lambda\log\left(1+\kappa\frac{\lambda^2}{a^2}\right).
\]

It diverges at the sharp boundary as

\[
\mathbb E[H_{\mathrm{Id}}(t)^2]\sim
\frac{\lambda}{2\exp(\lambda t_2(\lambda))\,[t_2(\lambda)-t]}
\quad(t\uparrow t_2(\lambda)).
\]

The unique rate maximizing this horizon is

\[
\lambda_*=a\sqrt{\frac{z_*-1}{\kappa}},\qquad
2\left(1-\frac1{z_*}\right)=\log z_*,\quad z_*>2,
\]

and the maximal horizon is

\[
\sup_{\lambda>0}t_2(\lambda)
=\frac{\sqrt\kappa}{a}\frac{\log z_*}{\sqrt{z_*-1}}
=\frac{0.635300752421607\ldots}{a}.
\]

Here \(z_*=4.9215536345675\ldots\) and \(\lambda_*/a=2.50845643416216\ldots\). Consequently, for every \(t\) in \([0.635300752421607\ldots/a,1/a)\), the estimator has its correct finite mean \(a/(1-at)\), but **no constant exponential branching rate makes its second moment finite**. In particular, for \(a=\lambda=1\) the second moment is already infinite at \(t=1/2\) because \(t_2(1)=0.484415059026754\ldots\).

## Assumptions and scope

Work on a scalar autonomous ordinary differential equation with \(f(u)=u^2\), \(a>0\), and \(0\le t<1/a\). Codes are \(\mathrm{Id},f,f',f'',0\), with terminal labels at \(a\) respectively \(a,a^2,2a,2,0\). At its independent lifetime \(\tau\sim\mathrm{Exp}(\lambda)\), a live particle with remaining time \(s\) contributes its terminal label divided by \(e^{-\lambda s}\) when \(\tau\ge s\); otherwise it contributes \(1/(\lambda e^{-\lambda\tau})\), times the independent subtrees with remaining time \(s-\tau\). The branching rules, each deterministic in this one-dimensional setting, are \(\mathrm{Id}\mapsto(f)\), \(f\mapsto(f,f')\), \(f'\mapsto(f,f'')\), \(f''\mapsto(f,0)\), and \(0\mapsto(f,0)\). This is the scalar specialization of the coding-tree mechanism; no importance-sampling mixture, truncation, or adaptive branching intensity is used. All random lifetimes are independent. A subtree whose label is zero contributes zero, and all weights are nonnegative.

The claim optimizes only over **constant** rate \(\lambda\) in this fixed exponential-clock estimator; it does not cover all branching estimators or time-dependent clock laws.

## Proof

**1. First moments and exact second-moment recursion.** Conditioning on the first exponential lifetime gives, for any code \(c\) with terminal label \(g_c\) and offspring \(d_1,\ldots,d_k\),

\[
 M_c(t):=\mathbb E[H_c(t)^2]
 =g_c^2e^{\lambda t}
 +\frac1\lambda\int_0^t e^{\lambda(t-s)}\prod_{j=1}^k M_{d_j}(s)\,ds.
\]

This identity holds as an equality in nonnegative extended reals by Tonelli's theorem. Its minimal nonnegative solution is obtained by iterating the integral equations from the first no-branch contribution, equivalently by finite-generation truncation with nonnegative terms. The zero-coded estimator is identically zero. Writing \(I=M_{\mathrm{Id}}\), \(F=M_f\), \(C=M_{f'}\), and \(B=M_{f''}\), the last code yields \(B(t)=4e^{\lambda t}\), and finite-valued branches solve

\[
 I'=\lambda I+\frac F\lambda,\quad
 F'=\lambda F+\frac{FC}{\lambda},\quad
 C'=\lambda C+\frac{4e^{\lambda t}F}{\lambda},
\]

with \(I(0)=a^2\), \(F(0)=a^4\), \(C(0)=4a^2\). These equations are not an assumed moment closure: they follow exactly from independent offspring products and positive weights. The analogous *first*-moment renewal system has the solution

\[
 \mathbb EH_{\mathrm{Id}}(t)=\frac a{1-at},\quad
 \mathbb EH_f(t)=\frac{a^2}{(1-at)^2},\quad
 \mathbb EH_{f'}(t)=\frac{2a}{1-at},\quad
 \mathbb EH_{f''}(t)=2
\]

for \(t<1/a\). Nonnegativity and monotone integral iteration identify these expectations, including beyond the second-moment boundary.

**2. Integrable reduction and exact threshold.** Put

\[
 x=\frac{e^{\lambda t}-1}{\lambda^2},\quad
 F(t)=e^{\lambda t}\widehat F(x),\quad
 C(t)=e^{\lambda t}\widehat C(x).
\]

Then \(\widehat F_x=\widehat F\widehat C\), \(\widehat C_x=4\widehat F\). Their first integral is \(\widehat C^2-8\widehat F=8a^4\). Set \(b=2\sqrt2a^2\), \(q=3-2\sqrt2\) and \(R(x)=q e^{bx}\). Solving the resulting scalar Riccati equation gives

\[
 \widehat C(x)=b\frac{1+R(x)}{1-R(x)},\qquad
 \widehat F(x)=\frac{b^2R(x)}{2(1-R(x))^2}.
\]

Both are finite precisely when \(x<x_*=\kappa/a^2\), and \(\widehat F(x)\sim1/[2(x_*-x)^2]\) as \(x\uparrow x_*\). From the first moment equation for \(I\),

\[
 I(t)=e^{\lambda t}\left[a^2+
 \int_0^{x(t)}\frac{\widehat F(u)}{1+\lambda^2u}\,du\right].
\]

It is finite for \(x(t)<x_*\) and diverges as \(x(t)\uparrow x_*\). At and after the boundary the nonnegative renewal integral diverges; thus there is no second interval of finite moments. Since \(x'(t)=e^{\lambda t}/\lambda\), the displayed double pole for \(\widehat F\) yields \(I(t)\sim\lambda/[2e^{\lambda t_2}(t_2-t)]\), proving both the exact horizon and the sharp one-sided blow-up constant. Every finite \(t\) has finite expected tree population because its branching rate is bounded and offspring count at most two, so infinite variance here does not require infinite expected work.

**3. Rate optimization.** Let \(z=1+\kappa(\lambda/a)^2>1\). Then

\[
 at_2(\lambda)=\sqrt\kappa\frac{\log z}{\sqrt{z-1}}.
\]

The sign of its derivative is the sign of \(2(1-1/z)-\log z\). This expression increases from zero on \((1,2)\), then strictly decreases to minus infinity, and hence has exactly one additional root \(z_*>2\). The function tends to zero at both parameter endpoints \(z\downarrow1\) and \(z\to\infty\), establishing a unique global maximum. Since its value is below \(1\), the finite-mean interval extends strictly beyond the best second-moment interval.

## Verification

The standalone `verify.py` uses only Python's standard library. It evaluates the exact transformed moment formulas and independently integrates the unreduced three-moment differential system by fourth-order Runge–Kutta for 100 parameter/time configurations, checks global-rate maximization and scaling, and directly samples 80,000 independent coding trees in a finite-moment regime. It reports 312 check groups. These finite checks are corroboration only; the global statements and infinite-variance boundary follow from the analytic nonnegative renewal reduction and explicit singularity.

## Relationship to prior work

Penent and Privault [1] introduced the **same** exponential-lifetime derivative-code estimator, established its expectation representation and sufficient integrability conditions, and presented the quadratic Riccati example with exponential rate one and samples through time one-half. Those results are retained as prior work. The additional result here is the exact **second**-moment breakdown time for that estimator, the singularity coefficient, the uniquely optimal constant exponential rate and the impossibility of finite variance beyond the optimized horizon. Its interval is shorter than the source's mean-integrability interval. Huang and Privault [2] analyze a different estimator with randomly chosen Butcher-tree *sizes*, no independent exponential branching-time recursion; their variance bounds and optimal size laws do not imply the clock-specific identity here. Henry-Labordère and colleagues [3] study polynomial branching representations of semilinear PDEs with general integrability restrictions, not this fixed Riccati derivative-code moment system.

## Limitations

The result does not show that all unbiased Monte Carlo representations of the Riccati solution must have infinite variance. The rate-optimal statement ranges only over independent exponential lifetimes with constant positive rate, and its numerical values assume scalar \(f(u)=u^2\) with positive initial condition. The first-moment representation holds only before the Riccati ODE's own blow-up time. Numerical tree samples can miss rare, extremely large weights and cannot certify second-moment integrability. A specialized earlier marked-branching moment calculation could have priority over this closed form; independent literature review and formal audit have not been performed.

## References

[1] G. Penent and N. Privault, *Numerical evaluation of ODE solutions by Monte Carlo enumeration of Butcher series*, arXiv:2201.05998 (first posted January 16, 2022), especially Definition 4.1, Theorem 4.2, Proposition 4.3 and Section 7. https://arxiv.org/abs/2201.05998

[2] Q. Huang and N. Privault, *On the random generation of Butcher trees*, arXiv:2404.05969 (first posted April 9, 2024), especially the tree-size probability law and the second-moment bound in Section 6. https://arxiv.org/abs/2404.05969

[3] P. Henry-Labordère, N. Oudjane, X. Tan, N. Touzi and X. Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, arXiv:1603.01727 (2016). https://arxiv.org/abs/1603.01727
