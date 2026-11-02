# Fractional grazing onset and vanishing Floquet contraction in a three-zone Liénard flow

## Finding
Let \(b>0\) be fixed. Define the continuous odd, piecewise-linear function
\[
H(x)=\operatorname{sgn}(x)\max\{|x|-1,0\},\qquad H(0)=0.
\]
Consider the planar differential equation
\[
\dot x=y+\lambda x-bH(x),\qquad \dot y=-x,\qquad\lambda>0.
\]
This is a three-zone continuous Liénard field with two fold lines at \(x=\pm1\). At \(\lambda=0\), its punctured interior disk \(0<x^2+y^2\leq1\) is a period annulus of the harmonic oscillator and its boundary is a grazing periodic orbit.

**Theorem (fractional onset and contraction).** For any \(b>0\) and all sufficiently small \(\lambda>0\), there is an attracting hyperbolic limit cycle \(\Gamma_\lambda\). Its intersection with the positive \(y\)-axis is \((0,R_\lambda)\), and it is the only limit cycle in a sufficiently small fixed neighborhood of the grazing unit circle. With
\[
C_b=\left(\frac{3\pi}{8\sqrt2\,b}\right)^{2/3},
\]
one has
\[
R_\lambda=1+C_b\lambda^{2/3}+o(\lambda^{2/3}),\qquad
\max_{\Gamma_\lambda}|x|=1+C_b\lambda^{2/3}+o(\lambda^{2/3}).
\]
Its nontrivial real Floquet multiplier \(m_\lambda>0\) obeys
\[
\log m_\lambda=-4\sqrt2\,b\sqrt{C_b}\,\lambda^{1/3}+o(\lambda^{1/3}).
\]
Thus the finite-radius onset has exponent \(2/3\), but the contraction exponent tends to zero with exponent \(1/3\). For section values \(r=1+s\lambda^{2/3}\), where \(s\) ranges over any compact subset of \((0,\infty)\), the first-return displacement has the uniform normal form
\[
P_\lambda(r)-r=\lambda\left[\pi-\frac{8\sqrt2}{3}b s^{3/2}+o(1)\right].
\]
The periodic orbit is not claimed to be unique among all parameter-independent remote regions; the theorem's uniqueness is local to the grazing circle.

## Assumptions and scope
The parameter \(b\) is any fixed positive real number, and the limit is \(\lambda\downarrow0\) with \(b\) fixed. Solutions are classical solutions of a globally Lipschitz continuous vector field. The section \(\Sigma=\{(0,r):r>0\}\) is taken in the positive crossing direction, where \(\dot x=r\). The first-return map \(P_\lambda\) is defined on a neighborhood of \(r=1\) for sufficiently small positive \(\lambda\). All asymptotic small-o statements are at fixed \(b\), and the normal-form remainder is uniform on compact positive ranges of the scaled section coordinate \(s\). The nontrivial Floquet multiplier refers to the planar return direction (the other multiplier is 1 for the autonomous time shift).

## Proof
**1. Energy balance and the grazing geometry.** Set \(E=(x^2+y^2)/2\). Along every trajectory,
\[
\dot E=\lambda x^2-b|x|(|x|-1)_+.
\]
At the limiting value \(\lambda=0\), all circles of radius at most 1 are harmonic periodic trajectories. A trajectory of radius just greater than 1 encounters damping only in two short intervals around its right and left turning points.

Fix positive constants \(s_-<s_+\), put \(r=1+s\lambda^{2/3}\) with \(s\in[s_-,s_+]\), and set \(\delta=r-1\). The harmonic comparison orbit from \((0,r)\) is \((r\sin t,r\cos t)\). A finite-time variation-of-constants estimate gives, uniformly until the next positive \(y\)-axis crossing,
\[
(x(t),y(t))=(r\sin t,r\cos t)+O(\lambda+\delta^{3/2})
=(r\sin t,r\cos t)+O(\lambda).
\]
Here is the relevant bootstrap: if the state difference is bounded by \(K\lambda\), then the overshoot forcing \(H(x(t))\) has size \(O(\delta)\) and is supported on two intervals of total duration \(O(\sqrt\delta)\), because \(\lambda=o(\delta)\) in this regime. Its time integral is \(O(\delta^{3/2})=O(\lambda)\), whereas the \(\lambda x\) forcing has integrated size \(O(\lambda)\). Variation of constants for the harmonic fundamental matrix closes the bound by selecting \(K\) sufficiently large. The resulting return time is \(T_\lambda(r)=2\pi+O(\lambda)\).

Near each of the two harmonic extrema, writing \(t=t_0+u\) gives
\[
|r\sin t|-1=\delta-\frac{u^2}{2}+O(\delta u^2+u^4).
\]
Consequently, for \(r\downarrow1\),
\[
\int_0^{2\pi}|r\sin t|(|r\sin t|-1)_+\,dt
=2\int_{-\sqrt{2\delta}}^{\sqrt{2\delta}}
\left(\delta-\frac{u^2}{2}\right)du+o(\delta^{3/2})
=\frac{8\sqrt2}{3}\delta^{3/2}+o(\delta^{3/2}).
\]
The \(O(\lambda)\) trajectory perturbation alters the two overshoot integrals by \(O(\lambda\sqrt\delta)=o(\lambda)\). Also \(\int_0^{T_\lambda(r)}x(t)^2dt=\pi+o(1)\). Integrating \(\dot E\) across the return yields
\[
\frac{P_\lambda(r)^2-r^2}{2}
=\pi\lambda-\frac{8\sqrt2}{3}b\delta^{3/2}+o(\lambda).
\]
Since \(P_\lambda(r)-r=O(\lambda)\) and \(r\to1\), this proves the asserted uniform scaled return displacement.

**2. Existence and local uniqueness.** The limiting scaled displacement function
\[
D_b(s)=\pi-\frac{8\sqrt2}{3}b s^{3/2}
\]
is continuous, strictly decreasing and has exactly one positive zero \(s=C_b\). Choose fixed \(s_-<C_b<s_+\); for sufficiently small \(\lambda\), the return displacement has opposite signs at \(1+s_-\lambda^{2/3}\) and \(1+s_+\lambda^{2/3}\). Continuity produces a periodic orbit with \(R_\lambda=1+C_b\lambda^{2/3}+o(\lambda^{2/3})\).

For the claimed local uniqueness, first note that periodic orbits wholly inside \(|x|<1\) are impossible when \(\lambda>0\): the divergence is the positive constant \(\lambda\) there, contradicting the planar area integral for a cycle. Moreover, when \(r\) tends to 1, the energy balance forces every fixed point to have \(r-1\asymp\lambda^{2/3}\): if the excursion beyond the folds were \(o(\lambda^{2/3})\), positive interior input of order \(\lambda\) could not be balanced; if it were much larger, the outer loss would dominate. The same comparison argument, using \(\max(r-1,0)+O(\lambda)\) as the effective overshoot, makes these exclusions uniform. For any fixed \(\epsilon>0\), at \(\lambda=0\) every initial section point with \(r\in(1,1+\epsilon]\) loses energy whenever it exits the disk; by continuity, for small \(\lambda\) there are no fixed points with \(r-1\) bounded away from zero. Section values strictly below 1 and bounded away from 1 lie inside the unstable linear core for small \(\lambda\), so cannot be periodic. Thus all possible periodic orbits in a sufficiently small fixed neighborhood of the unit circle lie in a scaled annulus \(r=1+s\lambda^{2/3}\) with \(s\) in a fixed compact positive interval.

On this scaled annulus, the crossings of the fold lines are transverse and the return map is differentiable. Liouville's formula and the section-crossing correction give
\[
P_\lambda'(r)=\frac{r}{P_\lambda(r)}
\exp\left(\lambda T_\lambda(r)-b\,\tau_{\mathrm{out}}(r)\right),
\]
where \(\tau_{\mathrm{out}}(r)\) is the time spent with \(|x|>1\) during that return. The two grazing windows yield
\[
\tau_{\mathrm{out}}(r)=4\sqrt{2(r-1)}+o(\sqrt{r-1}),
\]
uniformly in the scaled annulus. Because \(\lambda=o(\sqrt{r-1})\) and \(r/P_\lambda(r)=1+O(\lambda)\), one has \(P_\lambda'(r)<1\) throughout the annulus. Hence \(P_\lambda(r)-r\) is strictly decreasing there and its zero is unique.

**3. Multiplier and spatial amplitude.** At the fixed point, the section factor \(r/P_\lambda(r)\) is 1. Thus the exact nontrivial Floquet multiplier is
\[
m_\lambda=\exp\left(\lambda T_\lambda(R_\lambda)
-b\tau_{\mathrm{out}}(R_\lambda)\right).
\]
Substituting \(R_\lambda-1=C_b\lambda^{2/3}+o(\lambda^{2/3})\) and the residence-time formula gives
\[
\log m_\lambda=-4\sqrt2\,b\sqrt{C_b}\,\lambda^{1/3}+o(\lambda^{1/3})<0.
\]
This proves hyperbolic attraction. Finally, over a whole circuit the energy changes by at most \(O(\lambda)\) from its positive-section value. At an \(x\)-extremum, \(\dot x=0\) implies \(y=-\lambda x+bH(x)=O(\lambda^{2/3})\); thus the squared \(y\)-term is of smaller order than \(\lambda^{2/3}\). Therefore \(\max|x|=R_\lambda+o(\lambda^{2/3})\), proving the spatial-amplitude law. \(\square\)

## Verification
The leading two-fold integral is exactly \(2\int_{-\sqrt{2\delta}}^{\sqrt{2\delta}}(\delta-u^2/2)du=(8\sqrt2/3)\delta^{3/2}\). The limiting time outside the linear core is exactly \(4\sqrt{2\delta}\) at leading order. The symbolic checker in `checks/grazing_checker.py` evaluates both expressions and their algebraic consequences. It additionally performs numerical finite-parameter Poincaré tests for several small parameter values using adaptive ODE integration, reporting convergence toward the two predicted constants. These numerical calculations are diagnostics, not proofs of the asymptotic statements.

## Relationship to prior work
Cai, Chen, Jin and Lu (arXiv:2610.10050v1, first posted October 7, 2026) study continuous piecewise-linear Liénard systems with arbitrarily many folds. Their main results concern a new lower bound on possible limit-cycle counts and a very large finite upper bound, rather than this quantitative singular transition at a two-fold center boundary. The two-fold classification of Chen, Feng, Jia and Meng (DOI:10.1112/jlms.70430; published January 2026) already proves a sharp maximal count and discusses grazing limit-cycle bifurcations. No global limit-cycle count is attributed to this theorem as a new finding. The distinction claimed here is the exact coupled fractional asymptotic of the orbit location and multiplier for an explicitly specified symmetric two-fold family. General nonsmooth grazing theory includes fractional-power return terms; the present calculation evaluates the coefficient for this Liénard field and propagates it to the spectral exponent.

## Limitations
The asymptotics concern \(\lambda\downarrow0\) with a fixed positive outer slope \(b\); they are not uniform as \(b\downarrow0\) or \(b\to\infty\). The uniqueness argument is local to a neighborhood of the grazing circle and is not presented as a new global uniqueness theorem. The main analytic proof uses a small-parameter crossing argument; numerical data do not certify an infinite limit. Priority remains uncertain because the full text of the closely relevant January 2026 two-fold classification could not be reviewed. This is a self-reviewed mathematical finding, not independently audited.

## References
1. S. Cai, H. Chen, J. Jin, Y. Lu, *Bounds on the maximum number of limit cycles of piecewise linear Liénard systems I. The continuous case*, arXiv:2610.10050v1 (2026), https://arxiv.org/abs/2610.10050.
2. H. Chen, Z. Feng, M. Jia, Y. Meng, *Maximum number of limit cycles of the piecewise linear Liénard system with three zones*, Journal of the London Mathematical Society **113** (2026), e70430, https://doi.org/10.1112/jlms.70430.
3. M. R. Jeffrey, *Modeling with nonsmooth dynamics* (2020), https://research-information.bris.ac.uk/files/216852466/nsmodelfiadsRR.pdf. Relevant background: general near-grazing fractional return laws, not the particular constants claimed here.
