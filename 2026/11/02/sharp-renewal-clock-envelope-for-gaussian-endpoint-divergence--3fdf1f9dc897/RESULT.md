# Sharp renewal-clock envelope for Gaussian endpoint divergence

## Finding

For a one-dimensional Ornstein–Uhlenbeck particle refreshed from a fixed nondegenerate Gaussian after independently chosen renewal intervals, the maximum **endpoint symmetrized Kullback–Leibler divergence per unit time** at a prescribed mean interval has an exact two-regime form. A single critical interval separates a burst-like supremizing renewal law from the unique deterministic optimizer. The critical interval has an exact square-root scaling as the reset variance approaches zero.

Write \(\lambda,D>0\), \(0<c<1\), and let the equilibrium variance be \(D/\lambda\). At each renewal, the particle is independently redrawn from \(P_0=\mathcal N(0,cD/\lambda)\). Between renewals it follows
\[
\mathrm dX_t=-\lambda X_t\,\mathrm dt+\sqrt{2D}\,\mathrm dB_t.
\]
The cycle-end law after duration \(t\) is \(P_t=\mathcal N(0,(D/\lambda)u_c(2\lambda t))\), where
\[
u_c(x)=1-(1-c)e^{-x},\qquad
F_c(x)=\frac{(u_c(x)-c)^2}{u_c(x)},\qquad x\ge0.
\]
Its symmetrized endpoint divergence (Jeffreys divergence) is precisely
\[
\mathsf J_c(x)=D_{\mathrm{KL}}(P_t\Vert P_0)+D_{\mathrm{KL}}(P_0\Vert P_t)=\frac{F_c(x)}{2c},\qquad x=2\lambda t.
\]
There exists exactly one \(z_c>0\) solving
\[
 z_c(1-u_c(z_c))(u_c(z_c)+c)=u_c(z_c)(u_c(z_c)-c).
\]
Put \(t_c=z_c/(2\lambda)\). For every prescribed mean interarrival time \(\mu>0\), the sharp endpoint-divergence rate is
\[
\boxed{\displaystyle
\sup_{\substack{W>0\ \mathrm{a.s.}\\\mathbb EW=\mu}}
\frac{\mathbb E\,\mathsf J_c(2\lambda W)}{\mu}
=\begin{cases}
\displaystyle \frac{2\lambda\,\mathsf J_c(z_c)}{z_c},&0<\mu\le t_c,\\[5pt]
\displaystyle \frac{\mathsf J_c(2\lambda\mu)}{\mu},&\mu\ge t_c.
\end{cases}}
\]
For \(\mu\ge t_c\) the **unique** maximizing positive waiting-time law is deterministic, \(W=\mu\). For \(0<\mu<t_c\) the supremum is not attained among strictly positive laws; it is approached by two-point laws supported at \(\{\varepsilon,t_c\}\) as \(\varepsilon\downarrow0\), with limiting masses \(1-\mu/t_c\) and \(\mu/t_c\). If zero-time renewals are allowed, this limiting two-point law attains the maximum. The optimal expected divergence as a function of the fixed mean is continuously differentiable but has a strictly negative jump in second derivative at \(t_c\) (when expressed in the dimensionless mean); this is a sharp change of optimal protocol type.

In the narrow-reset limit \(c\downarrow0\),
\[
\boxed{\displaystyle
z_c=\sqrt{2c}-\frac c3+O(c^{3/2}),\qquad
\frac{2\lambda\,\mathsf J_c(z_c)}{z_c}
=\lambda\left(\frac1c-\sqrt{\frac2c}-\frac16+O(\sqrt c)\right).}
\]
Thus the critical mean time is \(t_c\sim\sqrt{c/2}/\lambda\), and its reciprocal grows at rate \(\sqrt2\lambda/\sqrt c\). In the opposite limit \(c\uparrow1\), \(z_c\to z_\mathrm{w}=1.256431208626\ldots\), where \(z_\mathrm{w}>0\) uniquely satisfies \(e^{z_\mathrm{w}}=2z_\mathrm{w}+1\).

## Assumptions and scope

Renewal intervals \(W_1,W_2,\ldots\) are independent and identically distributed, strictly positive almost surely, independent of the Brownian fluctuations and independent Gaussian refresh samples, and have the fixed finite mean \(\mu>0\). Full Gaussian refresh is instantaneous at renewal epochs. The optimized quantity is the *sum of per-cycle endpoint Jeffreys divergences divided by elapsed physical time*, not the full path-space entropy production or the physical work needed to implement a reset. Under the stated renewal assumptions, the renewal-reward theorem identifies its long-time rate with \(\mathbb E\mathsf J_c(2\lambda W)/\mu\). Dimensionless time \(x=2\lambda t\) is used consistently.

## Proof

**Gaussian reduction.** Solving the variance ODE \(v'(t)=-2\lambda v(t)+2D\) with \(v(0)=cD/\lambda\) gives \(v(t)=(D/\lambda)u_c(2\lambda t)\). For positive variances \(a,b\), the sum of the two directed Gaussian divergences equals \((a/b+b/a-2)/2\). This proves the displayed formula for \(\mathsf J_c\). It is nonnegative, bounded, and increases strictly from zero; these properties also ensure integrability of the renewal reward.

**One inflection and one tangent.** Set \(u=u_c(x)\). Differentiation gives
\[
F_c'(x)=(1-u)\left(1-\frac{c^2}{u^2}\right),\qquad
F_c''(x)=\frac{1-u}{u^3}\bigl(2c^2-c^2u-u^3\bigr).
\]
As \(x\) increases, \(u\) increases strictly from \(c\) to \(1\). The cubic \(H_c(u)=2c^2-c^2u-u^3\) decreases strictly; it is positive at \(u=c\) and negative at \(u=1\). Hence \(F_c\) is strictly convex until one inflection point and strictly concave afterwards. Define \(Q_c(x)=xF_c'(x)-F_c(x)\). Then \(Q_c(0)=0\), \(Q_c'(x)=xF_c''(x)\), and \(Q_c(x)\to-(1-c)^2<0\) as \(x\to\infty\). Thus \(Q_c\) has precisely one positive zero \(z_c\), lying strictly after the inflection point. Factoring \(Q_c\) yields
\[
Q_c(x)=\frac{u-c}{u^2}\left[x(1-u)(u+c)-u(u-c)\right].
\]
This proves the stated positive-root equation, strict global maximality of \(F_c(x)/x\) at \(z_c\), and \(F_c''(z_c)<0\).

**Exact global envelope.** The least concave majorant of \(F_c\) on the nonnegative half-line is
\[
\widehat F_c(x)=\begin{cases}
(F_c(z_c)/z_c)x,&0\le x\le z_c,\\
F_c(x),&x\ge z_c.
\end{cases}
\]
Indeed, the line segment dominates \(F_c\) by the established global maximum of \(F_c(x)/x\). At \(z_c\) its slope matches \(F_c'(z_c)\), and the remaining branch is strictly concave; therefore \(\widehat F_c\) is concave. Every other concave majorant must dominate its chord from \(0\) to \(z_c\), proving minimality. For \(X=2\lambda W\) of mean \(m=2\lambda\mu\), two inequalities give
\[
\mathbb E F_c(X)\le\mathbb E\widehat F_c(X)\le\widehat F_c(m).
\]
For \(m\ge z_c\), choosing \(X=m\) attains this bound, and strict concavity together with the unique contact points forces the deterministic law. For \(0<m<z_c\), its only possible equality support in the nonnegative closure is \(\{0,z_c\}\) with masses \(1-m/z_c\), \(m/z_c\); no strictly positive law attains it. Replace zero by \(\varepsilon>0\), keeping the other atom at \(z_c\), and choose masses to preserve mean \(m\): the expectation converges to the bound. Reintroducing \(\mathsf J_c=F_c/(2c)\) and \(m=2\lambda\mu\) proves the rate formula and all equality claims. Since \(F_c''(z_c)<0\), the majorant is \(C^1\), but has a nonzero downward jump of second derivative at \(z_c\).

**Small-width expansion.** Set \(c=\epsilon^2\) and \(x=\epsilon y\) in the tangent equation. Dividing its difference of sides by \(\epsilon^3\), Taylor expansion near the positive root gives
\[
 y-\frac{y^3}{2}+\epsilon\left(\frac{7y^4}{12}-\frac{3y^2}{2}\right)+O(\epsilon^2)=0.
\]
The limiting positive root \(y=\sqrt2\) is simple. The implicit-function theorem and the single-root property show \(y=\sqrt2-\epsilon/3+O(\epsilon^2)\). Substitution into \(F_c(x)/(cx)\) yields
\[
\frac{F_c(z_c)}{cz_c}=\epsilon^{-2}-\sqrt2\,\epsilon^{-1}-\frac16+O(\epsilon).
\]
This establishes both sharp cold-width expansions. For \(c\uparrow1\), divide \(F_c(x)\) by \((1-c)^2\); the quotient converges locally uniformly on positive \(x\) to \((1-e^{-x})^2\). The maximizing tangent points remain in a compact positive interval, and the unique positive critical point of \((1-e^{-x})^2/x\) obeys \(e^x=2x+1\). This gives the warm-width limit.

## Verification

Run `python3 verify.py` from the package directory. It uses only the Python standard library. The program compares direct numerical Gaussian integrals to the endpoint-divergence formula, checks the unique tangent equation and supporting-line inequality across many reset widths, tests Jensen bounds for finite-support renewal laws, checks the sharp two-point approximation, and checks the cold and warm asymptotic formulas. In the saved package the checker passes 7,123 finite assertions. Those finite checks corroborate formulas but do not replace the global analytic proof.

## Relationship to prior work

Farago (arXiv:2605.28445v1) formulates the finite-width Gaussian endpoint-divergence measure for harmonic resetting and compares periodic and Poisson resetting at a given rate, including limiting regimes. The present theorem optimizes the entire class of independent positive renewal waiting-time distributions at *fixed mean*, identifies the exact least concave majorant, classifies equality and nonattainment, and determines the singular protocol-transition scale. General renewal-clock methods appear in Eule and Metzger (2016), while Mori, Olsen, and Krishnamurthy (2023) analyze a different path-level entropy-production model with random reset positions. Olsen, Gupta, Mori, and Krishnamurthy (2024) treat work and fluctuations for finite-time trap switching; their optimality problem concerns trap choices, not this endpoint-KL renewal-clock envelope. These frameworks and classical concavification are acknowledged background; no novelty is claimed for the renewal-reward theorem or the elementary concave-majorant method in isolation.

## Limitations

This is an idealized benchmark concerning independent Gaussian redraws and harmonic relaxation. Zero-time events are used only as a limiting extremizer; positive minimal dwell-time constraints or finite reset implementation duration change the feasible class. The result does **not** identify the full thermodynamic entropy production of any physical reset device, the actual work dissipated, the optimal resetting mechanism, or an extension to anharmonic potentials. More general published variational principles may imply the concave-envelope construction, and literature-wide originality priority remains qualified.

## References

1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445v1 (first submitted 2026-05-27). https://arxiv.org/abs/2605.28445.
2. K. S. Olsen, D. Gupta, F. Mori, and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, Physical Review Research 6, 033343 (2024). https://doi.org/10.1103/PhysRevResearch.6.033343.
3. F. Mori, K. S. Olsen, and S. Krishnamurthy, *Entropy production of resetting processes*, Physical Review Research 5, 023103 (2023), arXiv:2211.15372. https://arxiv.org/abs/2211.15372.
4. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18, 033006 (2016). https://doi.org/10.1088/1367-2630/18/3/033006.
