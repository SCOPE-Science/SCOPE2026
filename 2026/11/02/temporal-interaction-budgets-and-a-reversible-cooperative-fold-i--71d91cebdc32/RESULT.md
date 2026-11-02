# Temporal interaction budgets and a reversible cooperative fold in a higher-order Prisoner's Dilemma

## Finding

In the well-mixed two-/three-person Prisoner's Dilemma mean-field replicator of Civilini et al. [1], fix its game parameters at \(T=3/2\), \(S=-1/2\), and \(a=2(G-W)=5\). Extend the fraction \(\delta\) of three-person interactions from a constant to an exogenous positive periodic function of time. The cooperator frequency \(x\in(0,1)\) then solves
\[
\dot x=x(1-x)\bigl[6\delta(t)x(1-x)-1/2\bigr]. \tag{1}
\]

**Exact temporal budget.** If \(\delta\) is a positive continuous function of period \(P\) and \(x(t)\in(0,1)\) is a \(P\)-periodic solution, then
\[
\boxed{\langle\delta\rangle-\frac13
=\left\langle\delta(t)(2x(t)-1)^2\right\rangle.} \tag{2}
\]
Here \(\langle h\rangle=P^{-1}\int_0^P h(t)\,dt\). In particular, a nonconstant periodic interaction share requires \(\langle\delta\rangle>1/3\) for any interior periodic cooperative state. If \(\langle\delta\rangle<1/3\), every interior orbit converges to full defection. The same global extinction holds at equality when \(\delta\) is nonconstant. For the exceptional constant critical schedule \(\delta\equiv1/3\), \(x\equiv1/2\) is semistable: initial states above \(1/2\) approach \(1/2\), and those below approach \(0\).

**Sharp small-amplitude periodic fold.** Fix any \(\omega>0\) and set
\[
\delta(t)=\frac13+\mu+\eta\cos(\omega t),\qquad P=\frac{2\pi}{\omega},
\tag{3}
\]
with \(\lvert\mu\rvert+\lvert\eta\rvert\) sufficiently small so \(0<\delta(t)<1\). There exist \(\eta_0>0\) and a neighborhood of \(\mu=0\) such that, for each \(0<\lvert\eta\rvert<\eta_0\), an analytic sharp threshold \(\mu_*(\eta,\omega)>0\) has the expansion
\[
\boxed{\mu_*(\eta,\omega)=\frac{3\eta^2}{32\omega^2}+O_\omega(\eta^4).} \tag{4}
\]
Within this parameter neighborhood there are no interior \(P\)-periodic solutions for \(\mu<\mu_*\), one nonhyperbolic interior periodic solution for \(\mu=\mu_*\), and exactly two for \(\mu>\mu_*\). The upper one is attracting and the lower one repelling, where *upper/lower* means their values at phase \(t=0\). At \(\mu<\mu_*\) all interior states converge to full defection; above the fold, the repelling orbit separates the basin of the attracting periodic orbit from the extinction basin. At equality, the nonhyperbolic orbit attracts initial states above it and repels those below it.

The critical orbit passes through \(x(0)=1/2\), and the threshold is equivalently the unique nearby value of \(\mu\) at which the solution launched from \(x(0)=1/2\) satisfies \(x(P/2)=1/2\). The two noncritical periodic solutions are related by
\[
\boxed{x_-(t)=1-x_+(P-t),\qquad \Lambda_-\Lambda_+=1,} \tag{5}
\]
where \(\Lambda_\pm>0\) are their period Floquet multipliers. Both relations hold exactly, not just asymptotically.

## Assumptions and scope

The claims concern the deterministic, infinite-population, one-dimensional *well-mixed mean-field* replicator equation (1), with the displayed fixed Prisoner's Dilemma payoffs. The time-dependent share \(\delta(t)\) is imposed externally; equation (1) is a mathematical extension of the constant-share equation in [1], not a derivation of a time-dependent random-hypergraph limit. Positive periodicity means \(\delta(t)>0\) throughout the period; for the sinusoidal conclusion \(0<\delta(t)<1\) throughout. All initial conditions are strictly interior \(0<x(0)<1\); the absorbing boundary solutions \(x\equiv0\) and \(x\equiv1\) are excluded from the global convergence statement. Constants implicit in \(O_\omega\) can depend on the fixed frequency, and no uniform claim is made as \(\omega\downarrow0\). The fold statement applies only for sufficiently small modulation and for means in a suitably small neighborhood of the unforced threshold.

The primary source [1] gives the well-mixed payoff difference \(\pi_C-\pi_D=-c\delta x^2+(c\delta-b-2S)x+S\), with \(b=T-S-1\), \(c=a+b\), and \(a=2(G-W)\). At the parameters above, \(b=1\), \(c=6\), and the difference reduces exactly to \(6\delta x(1-x)-1/2\). For constant \(\delta\), the equilibrium saddle-node lies at \(\delta=1/3\). Formulae (2)--(5) instead concern genuinely time-varying interactions.

## Proof

**1. Logit variable and the temporal-budget identity.** Put \(y=\log(x/(1-x))\). On the interior, equation (1) becomes
\[
\dot y=\frac32\delta(t)\operatorname{sech}^2(y/2)-\frac12
=\frac32\delta(t)[1-(2x-1)^2]-\frac12. \tag{6}
\]
The average of the left side vanishes over any interior periodic solution, immediately giving (2). Since \(\delta(t)>0\), the right side of (2) is zero only if \(x\equiv1/2\), which solves (1) only when \(\delta\equiv1/3\). Thus a nonconstant schedule supporting a periodic interior state has mean strictly greater than \(1/3\).

For \(\langle\delta\rangle<1/3\), (6) implies \(\dot y\le(3/2)\delta(t)-1/2\). Integrating over complete periods yields \(y(nP)\le y(0)+nP[(3/2)\langle\delta\rangle-1/2]\to-\infty\). The derivative of \(y\) is uniformly bounded for bounded periodic \(\delta\), hence \(y(t)\to-\infty\) also between sampling times and \(x(t)\to0\). At equality, the period return map \(F(y_0)=y(P;y_0)\) satisfies \(F(y_0)\le y_0\), strictly unless the corresponding trajectory is constant \(x\equiv1/2\) with \(\delta\equiv1/3\). For a nonconstant critical schedule, \(F(y)<y\) for every finite \(y\). Its increasing, strictly decreasing iterates cannot converge to a finite fixed point, so tend to \(-\infty\); bounded interperiod drift again gives extinction. For constant \(\delta\equiv1/3\), (6) reads \(\dot y=-\tfrac12\tanh^2(y/2)\): positive \(y\) tends to zero while negative \(y\) tends to \(-\infty\).

**2. Reflection and exact multiplier reciprocity.** For the sinusoidal schedule, let \(A(t)=\tfrac12+\tfrac32\mu+\tfrac32\eta\cos(\omega t)\). Then
\[
\dot y=f(t,y)=A(t)\operatorname{sech}^2(y/2)-1/2,
\qquad A(P-t)=A(t),\quad f(t,-y)=f(t,y). \tag{7}
\]
If \(y(t)\) is \(P\)-periodic, \(\widetilde y(t)=-y(P-t)\) also solves (7) and is periodic. Its phase-zero value is \(-y(0)\). The first-variation multiplier is \(\Lambda=\exp\int_0^P f_y(t,y(t))\,dt\). As \(f_y(t,-y)=-f_y(t,y)\), the reflected orbit has reciprocal multiplier, proving (5) after reverting to \(x\).

Let \(F_{\mu,\eta}(s)=y(P;s,\mu,\eta)\) be the return map. A self-reflected periodic solution necessarily starts at \(s=0\); it is nonhyperbolic by multiplier reciprocity. A trajectory started at \(s=0\) returns to zero at \(P\) if and only if it returns to zero at \(P/2\): one direction follows by uniqueness under time reflection, and the other by reflecting the first half of the trajectory. Its period multiplier is then exactly one.

**3. Local saddle-node and expansion.** Set \(D(s,\mu,\eta)=F_{\mu,\eta}(s)-s\). Standard smooth dependence of ODE solutions makes \(D\) analytic for parameters near \((0,0,0)\). At zero forcing and zero mean excess, the solution starting at zero is identically zero. Direct differentiation of (7), or a second-order Taylor expansion, gives
\[
D(0,0,0)=D_s(0,0,0)=0,\quad
D_\mu(0,0,0)=\frac{3P}{2},\quad
D_{ss}(0,0,0)=-\frac P4. \tag{8}
\]
The two equations \(D=0\), \(D_s=0\) define a unique analytic nearby fold curve by the implicit-function theorem, because their Jacobian in \((\mu,s)\) is nonsingular at the origin. Reflection maps any zero at phase \(s\) to a zero at phase \(-s\); uniqueness of the double zero forces its phase to be exactly \(s=0\). Consequently, the fold is determined equivalently by the half-period shooting equation.

For the coefficient, at \(s=\mu=0\), solve (7) perturbatively as \(y(t)=\eta u(t)+\eta^2v(t)+O_\omega(\eta^3)\) with \(y(0)=0\). Then
\[
u'(t)=\frac32\cos(\omega t),\quad
u(t)=\frac{3}{2\omega}\sin(\omega t),\quad
v'(t)=-\frac18u(t)^2.
\]
Hence
\[
D(0,0,\eta)=\eta^2v(P)+O_\omega(\eta^3)
=-\frac{9P}{64\omega^2}\eta^2+O_\omega(\eta^3). \tag{9}
\]
Using \(D_\mu=3P/2\) yields \(\mu_*=3\eta^2/(32\omega^2)+O_\omega(\eta^3)\). Replacing \(\eta\) by \(-\eta\) shifts the forcing by half a period, which conjugates the return maps and preserves their fold parameter. Analyticity therefore makes \(\mu_*\) even, sharpening the remainder to \(O_\omega(\eta^4)\). Positivity follows from its leading coefficient.

**4. Exhausting the nearby phase diagram and basins.** At \((\mu,\eta)=(0,0)\), every nonzero finite \(y\) strictly decreases over a period, since \(\dot y=-\tfrac12\tanh^2(y/2)\). The period displacement is uniformly negative outside a small neighborhood of \(y=0\), including near both infinite ends where \(\dot y\) is uniformly close to \(-1/2\). This remains true for small \(\lvert\mu\rvert+\lvert\eta\rvert\). Inside the small neighborhood, \(D_{ss}<0\) uniformly by (8); therefore its graph is strictly concave and has at most two zeros. The unique local double zero changes sign transversely with \(\mu\), as \(D_\mu>0\). This proves the zero/one/two classification without unexamined periodic orbits elsewhere in the interior. In the two-orbit regime, monotonicity of scalar flows and the sign of the return displacement make the lower orbit repelling and the upper attracting; all trajectories above the lower orbit approach the upper, and all below it approach extinction. The corresponding one-sided conclusions at the fold and the extinction conclusion below it follow from the same return-map signs. The reflecting partner identity and reciprocal multipliers were proved in step 2.

## Verification

The standalone file `verify.py` uses SymPy to confirm the exact substitution into the primary source's payoff polynomial. With SciPy it numerically solves the half-period fold shooting equation at frequencies \(0.7,1,2\) and amplitudes \(0.02,0.05,0.1\), checks the full-period return and unit multiplier, and checks the leading coefficient in (4). At \(\omega=1\), \(\eta=0.05\) it obtains \(\mu_*\approx0.000234283676\), compared with the leading approximation \(0.000234375\). At \(\mu=\mu_*+0.0002\) it identifies two phase-zero logit coordinates about \(-0.04994664034\) and \(+0.04994664034\), with respective multipliers about \(1.07991547\) and \(0.92599840\); the time-average identity (2) is satisfied to numerical accuracy. This is supporting computation, not the proof of the infinite-dimensional parameter statement.

Reproduce with `python verify.py` using the dependency versions specified in `requirements.txt`. The manuscript proof, not numerical sampling, establishes the universal and local bifurcation statements.

## Relationship to prior work

Civilini et al. [1] derive the *autonomous* well-mixed quadratic payoff difference and its constant-share saddle-node. Equations (2), (4), and (5) are about an exogenously time-varying three-person interaction fraction and are not corollaries of the autonomous fixed-point formula. Babajanyan, Lin, and Cheong [2] study rapid oscillation of payoffs in a **two-population pairwise** evolutionary game; their two-dimensional averaged dynamics and coexistence cycles do not give the one-population interaction-budget identity or the fold of (1). He et al. [3] simulate asynchronous participation in spatial **public-goods** games, changing agent participation and updates instead of periodically varying the well-mixed three-game share. The closest accessible related results therefore address different objects and cannot imply (2)--(5) merely by substituting game parameters. Earlier and subsequent unindexed specialist literature could nevertheless affect priority.

## Limitations

This result covers one explicitly motivated payoff slice of a larger four-parameter social-dilemma family, not the general payoff tensor. Equation (1) is a deterministic mean-field model with prescribed time-varying interaction mix and does not assert that a finite evolving hypergraph realizes that mix. It does not quantify finite-population fixation probabilities, stochastic network fluctuations, or arbitrary large-amplitude forcing. The perturbative expansion is for fixed positive frequency; it is not uniform in the slow-forcing limit. Numerical checks support but do not independently certify the proof. No claim is made that a literature search proves global priority.

## References

[1] A. Civilini, O. Sadekar, F. Battiston, J. Gómez-Gardeñes, V. Latora, *Explosive cooperation in social dilemmas on higher-order networks*, arXiv:2303.11475v1, first public 20 March 2023; Phys. Rev. Lett. 132, 167401 (2024), https://arxiv.org/html/2303.11475v1 , https://doi.org/10.1103/PhysRevLett.132.167401 .

[2] S. G. Babajanyan, W. Lin, K. H. Cheong, *Cooperate or Not Cooperate in Predictable but Periodically Varying Situations? Cooperation in Fast Oscillating Environment*, Advanced Science 7, 2001995 (2020), https://doi.org/10.1002/advs.202001995 .

[3] Y. He et al., *Temporal interaction and its role in the evolution of cooperation*, arXiv:2401.11782 (22 January 2024), Phys. Rev. E 110, 024210, https://arxiv.org/abs/2401.11782 , https://doi.org/10.1103/PhysRevE.110.024210 .
