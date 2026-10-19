# An exponential homoclinic pulse and reflected Riccati continuation at a chemical exchange boundary

## Finding

In the three-reaction quadratic mass-action flow
\[
\dot X=aX^2-(a+\delta)XY,\qquad
\dot Y=(a+\delta)XY-aY^2,
\]
with \(a>0\), \(\delta>0\), and \(X(0),Y(0)>0\), every trajectory in the open positive quadrant is a nonstationary, globally defined homoclinic orbit to the origin. Nevertheless, when \(\delta\downarrow0\), the transient concentration pulse becomes exponentially large for any fixed initial imbalance \(X(0)>Y(0)\). The pulse develops a universal profile governed by the inverse of the imaginary error function, and the solution on opposite sides of its limiting blow-up time approaches two distinct Riccati arcs related by exchanging species.

Write
\[
u_0=X(0)+Y(0),\qquad q_0=\frac{X(0)-Y(0)}{u_0},\qquad k=\frac{a}{\delta}.
\]
For every \(\delta>0\), the total concentration \(u=X+Y\) has a unique maximum on the complete orbit. Its exact value \(C_\delta\), attained at a unique time \(t_\delta\), is
\[
C_\delta=u_0(1-q_0^2)^{-a/\delta},\qquad
\delta\log\frac{C_\delta}{u_0}=a\log\frac{1}{1-q_0^2}.
\]
If \(0<q_0<1\) is held fixed as \(\delta\downarrow0\), let
\[
t_*:=\frac{1}{a u_0 q_0}.
\]
The peak time satisfies the two-term, original-physical-time asymptotic law
\[
\boxed{t_\delta=t_*+\frac{\delta(1-q_0^2)}{2a^2u_0q_0^3}+O_{a,u_0,q_0}(\delta^2).}
\]
For each fixed real \(t\ne t_*\), the positive-parameter trajectories have the pointwise singular limit
\[
\boxed{\begin{aligned}
\lim_{\delta\downarrow0}u_\delta(t)&=\frac{1}{a q_0|t-t_*|},\\
\lim_{\delta\downarrow0}q_\delta(t)&=
\begin{cases}q_0,&t<t_*,\\-q_0,&t>t_*.
\end{cases}
\end{aligned}}
\]
Thus the limiting continuation after the would-be explosion exchanges the two species; it is **not** a classical continuation of the \(\delta=0\) initial-value solution through infinity.

The pulse has a universal scaled shape for **every** fixed \(-1<q_0<1\), including balanced initial data. Define
\[
\sigma=\frac{C_\delta\sqrt{a\delta}}{2}(t-t_\delta),\qquad
W_\delta=\frac{2}{C_\delta\sqrt{a\delta}}.
\]
There is a unique continuous odd function \(Z:\mathbb R\to\mathbb R\) determined by
\[
\sigma=-\int_0^{Z(\sigma)}e^{v^2}\,dv.
\]
For every fixed finite \(L>0\), uniformly in \(|\sigma|\le L\),
\[
\boxed{\frac{u_\delta(t_\delta+W_\delta\sigma)}{C_\delta}
\longrightarrow e^{-Z(\sigma)^2}.}
\]
For fixed \(q_0>0\), the physical pulse-width scale \(W_\delta\) is exponentially small (times \(\delta^{-1/2}\)). For balanced initial data \(q_0=0\), by contrast, \(C_\delta=u_0\), \(t_\delta=0\), and \(W_\delta=2/(u_0\sqrt{a\delta})\) diverges: the same normalized profile appears on an expanding time scale.

## Assumptions and scope

The network consists of \(2X\to3X\) at rate \(a\), \(X+Y\to2Y\) at rate \(a+\delta\), and \(2Y\to Y\) at rate \(a\). The theorem uses deterministic mass-action kinetics with strictly positive fixed \(a\) and strictly positive initial concentrations. The singular limit fixes \(a,u_0,q_0\) while \(\delta\downarrow0\). The two-term peak-time expansion and the post-explosion reflected limit require fixed \(0<q_0<1\); no uniformity as \(q_0\to0\) is claimed. The universal centered pulse profile applies to fixed \(-1<q_0<1\). All time statements use the actual ODE time, not an orbitally reparameterized clock.

## Proof

**Exact reduction and complete trajectories.** Put \(u=X+Y\), \(q=(X-Y)/u\); then \(X=u(1+q)/2\), \(Y=u(1-q)/2\). Direct differentiation gives
\[
\dot u=a u^2q,\qquad
\dot q=-\frac{\delta}{2}u(1-q^2).
\]
These identities also give the first integral
\[
H_\delta(X,Y)=\frac{XY}{(X+Y)^{2+\delta/a}}
=\frac{1-q^2}{4u^{\delta/a}}.
\]
For \(\delta>0\), eliminating time and using the initial condition yields
\[
\frac{d\log u}{dq}=-\frac{2a q}{\delta(1-q^2)},\qquad
u=C_\delta(1-q^2)^{a/\delta},\qquad
\dot q=-\frac{\delta C_\delta}{2}(1-q^2)^{1+a/\delta}.
\]
The associated exact time quadrature, with \(t_\delta\) defined by \(q(t_\delta)=0\), is
\[
\boxed{t-t_\delta=-\frac{2}{\delta C_\delta}
\int_0^{q(t)}(1-v^2)^{-1-a/\delta}\,dv.}
\]
The last integral diverges at both endpoints \(q=\pm1\), since \(a/\delta>0\). Hence \(q\) passes monotonically through every value in \((-1,1)\) exactly once over \(t\in\mathbb R\), while \(u\to0\) at both infinite-time ends; \(X,Y\) remain positive and finite at every finite time. Because \(\dot u\) has the sign of \(q\), \(t_\delta\) is the unique global maximum of \(u\), with the asserted height. The evenness of the integrand proves the exact reflection identities
\[
q(t_\delta+s)=-q(t_\delta-s),\qquad
u(t_\delta+s)=u(t_\delta-s).
\]
Equivalently, \(X(t_\delta+s)=Y(t_\delta-s)\) and \(Y(t_\delta+s)=X(t_\delta-s)\).

**Sharp peak-time clock.** When \(q_0>0\), the time quadrature gives
\[
t_\delta=\frac{2(1-q_0^2)^k}{\delta u_0}
\int_0^{q_0}(1-v^2)^{-k-1}\,dv,
\qquad k=a/\delta.
\]
Set \(r=1-q_0^2\), \(f(v)=-\log(1-v^2)\), and \(g(v)=1/(1-v^2)\). The endpoint \(v=q_0\) is the strict maximum of \(f\) on \([0,q_0]\), with \(f'(q_0)>0\). Splitting at \(q_0/2\), the first part is exponentially smaller after factoring out \(e^{kf(q_0)}\); on the remainder, two integrations by parts using \(f'>0\) give
\[
e^{-kf(q_0)}\int_0^{q_0}e^{kf(v)}g(v)\,dv
=\frac{1}{2q_0k}+\frac{r}{4q_0^3k^2}+O(k^{-3}).
\]
Here \(g/f'=1/(2v)\) and \(-((g/f')')/f'=r/(4v^3)\) at the endpoint; a third bounded integration-by-parts remainder gives the displayed error for fixed \(q_0>0\). Multiplying by \(2/(\delta u_0)\) and substituting \(k=a/\delta\) proves the two-term peak-time expansion.

**Reflected singular continuation.** At exactly \(\delta=0\), the reduced angle \(q\) is constant. With fixed \(q_0>0\), the maximal initial-value solution is
\[
q_0(t)=q_0,\qquad
u_0(t)=\frac{u_0}{1-a u_0q_0t}
=\frac{1}{a q_0(t_*-t)},\qquad t<t_*.
\]
For any fixed \(t<t_*\), standard continuous dependence on the polynomial vector field gives \((u_\delta(t),q_\delta(t))\to(u_0(t),q_0)\). For any fixed \(t>t_*\), the reflected time \(2t_\delta-t\) approaches \(2t_*-t<t_*\). Apply the exact reflection identities to the same compact-time continuous-dependence argument at that reflected time. The result is \(u_\delta(t)\to1/[a q_0(t-t_*)]\) and \(q_\delta(t)\to-q_0\), proving the two-sided statement without assigning a solution value at \(t=t_*\).

**Universal peak profile.** Introduce
\[
z_\delta(\sigma)=\sqrt{\frac{a}{\delta}}\,
q\left(t_\delta+\frac{2\sigma}{C_\delta\sqrt{a\delta}}\right).
\]
The exact quadrature becomes
\[
\sigma=-\int_0^{z_\delta(\sigma)}
\left(1-\frac{\delta}{a}v^2\right)^{-1-a/\delta}\,dv,
\qquad
\frac{u}{C_\delta}=\left(1-\frac{\delta}{a}z_\delta^2\right)^{a/\delta}.
\]
For bounded \(v\), the integrand converges locally uniformly to \(e^{v^2}\). The integrals are strictly monotone from the entire allowed \(z_\delta\)-interval onto \(\mathbb R\). Their inverse functions therefore converge uniformly on compact \(\sigma\)-intervals to the inverse of \(z\mapsto-\int_0^z e^{v^2}dv\), and substitution into the concentration formula yields uniform convergence to \(e^{-Z(\sigma)^2}\). If \(q_0=0\), the exact initial peak occurs at \(t_\delta=0\) with \(C_\delta=u_0\), establishing the contrasting widening clock.

## Verification

The standalone script `verify.py` checks the exact \(u\)- and \(q\)-derivative identities, conservation of \(H_\delta\), the sharp peak-time asymptotics at several positive parameter values, the symmetry of the finite-parameter time quadrature, and numerical convergence toward the universal peak profile. Running `python verify.py` in an environment with `sympy` and `mpmath` produces `22 diagnostic assertions passed; no claim of computer-assisted exhaustive proof`. The universal limits and global-in-time statements follow from the analytical arguments above, not the finite diagnostics.

## Relationship to prior work

Yeung and Erban, arXiv:2610.06130v1, Example 2.1, give the specific rate triple \((1,3,1)\), the first integral \(XY/(X+Y)^4\), and the homoclinic nature of the open-quadrant trajectories. Those are prior facts. The present result varies the exchange rate toward the critical self-reaction rate, retaining physical time and establishing a sharply quantified exponentially tall excursion, its two-term event clock, its reflected singular continuation, and its universal inverse-imaginary-error-function peak profile. None of these parameter-singular time statements is asserted by that fixed-rate example.

Algaba, García and Reyes (arXiv:1805.02873) treat analytic/formal integrability and normal-form equivalence of quadratic Lotka–Volterra perturbations, not this physical-time singular-rate transition; general integrability information by itself does not determine the event clock or profile. Newton's classical classification of homogeneous quadratic phase portraits concerns geometric equivalence, which does not preserve physical-time scaling. Complete access to that older paper was not available, so priority uncertainty remains rather than being silently resolved. Related work on exponential slowing in cubic global centers concerns periodic trajectories of a different vector field and does not imply the displayed quadratic homoclinic pulse law.

## Limitations

The singular limit is pointwise in fixed physical time away from \(t_*\), not a uniform limit through the blow-up instant. The two-term peak-time formula assumes fixed \(q_0>0\) and does not extend uniformly through balanced data. The theorem does not classify the \(\delta<0\) regime, chemical noise, diffusion, higher-order reaction terms, or general nonsymmetric rate triples. It does not claim that the nonanalytic first integral, the fixed-rate homoclinic sector, or generic quadratic phase-portrait classifications are new. Independent bibliographic verification and a complete comparison with some older full texts remain outstanding.

## References

1. N. Yeung and R. Erban, *Classification of strongly non-hyperbolic critical points of planar second-order chemical reaction systems*, arXiv:2610.06130v1, publicly posted 2026-10-05, especially Example 2.1. https://arxiv.org/abs/2610.06130
2. A. Algaba, C. García and M. Reyes, *The analytic integrability problem for perturbations of homogeneous quadratic Lotka–Volterra systems*, arXiv:1805.02873v1 (2018). https://arxiv.org/abs/1805.02873
3. T. A. Newton, *Two Dimensional Homogeneous Quadratic Differential Systems*, SIAM Review **20** (1978), 120–138. https://doi.org/10.1137/1020007
