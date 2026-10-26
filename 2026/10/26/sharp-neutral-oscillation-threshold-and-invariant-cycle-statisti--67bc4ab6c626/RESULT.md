# Sharp neutral-oscillation threshold and invariant cycle statistics in a two-person public-goods model

## Finding
Consider the nonlinear public-goods replicator/environment system defined below with group size \(N=2\), including distinct synergy and discounting coefficients. For every allowed positive parameter choice, the open state square has a nonconstant periodic trajectory **if and only if** the public-goods multiplication factor equals \(r=2\). At that critical factor, every interior trajectory other than one equilibrium is periodic and belongs to a smooth family of nonisolated closed curves. Off the factor \(r=2\), no interior periodic trajectory exists.

At \(r=2\), every periodic orbit, regardless of amplitude, has exact physical-time means and mixed moment
\[
\overline x=\frac1{1+\theta},\qquad
\overline p=\frac{\delta_s}{\delta_s+\delta_d},\qquad
\overline{xp}=\frac{\delta_s}{(1+\theta)(\delta_s+\delta_d)}.
\]
In particular, the period-wise temporal covariance is exactly \(\overline{xp}-\overline x\,\overline p=0\), although both coordinates oscillate nontrivially.

## Assumptions and scope
Let \(r>0\), \(\epsilon>0\), \(\theta>0\), and \(0<\delta_s,\delta_d<1\). Here \(x\in(0,1)\) is the fraction of cooperators, and \(p\in(0,1)\) is the probability of the discounting game. The model is the \(N=2\) specialization of the asymmetric nonlinear feedback model of Jiang and coauthors [1, equation (11)]:
\[
\begin{aligned}
\dot x&=x(1-x)\left\{\frac r2\left[(1-p)(1+\delta_s x)+p(1-\delta_d x)\right]-1\right\}\\
&=x(1-x)\left[\frac r2-1+\frac r2x\left(\delta_s-(\delta_s+\delta_d)p\right)\right],\\
\dot p&=\epsilon p(1-p)\left[(\theta+1)x-1\right].
\end{aligned}
\]
All statements concern classical solutions with initial conditions in the open square, which is forward invariant. A nonconstant periodic orbit means a periodic classical solution entirely inside that square. The moment \(\overline f\) denotes the integral of \(f(x(t),p(t))\) divided by the orbit's positive period. The symmetric case is obtained by \(\delta_s=\delta_d\).

## Proof
Set \(q(p)=\delta_s-(\delta_s+\delta_d)p\), \(a=r/2-1\), and denote the two vector-field components by \(F\) and \(G\). On the simply connected open square use the positive \(C^1\) Dulac density
\[
B(x,p)=\frac1{x^2(1-x)p(1-p)}.
\]
Direct differentiation, using \(BF=a/[xp(1-p)]+(r/2)q(p)/[p(1-p)]\) and \(BG=\epsilon[(\theta+1)x-1]/[x^2(1-x)]\), gives
\[
\frac{\partial(BF)}{\partial x}+\frac{\partial(BG)}{\partial p}
=-\frac{r/2-1}{x^2p(1-p)}.
\]
For every \(r\ne2\) this divergence is strictly of one sign throughout the domain. The Bendixson–Dulac criterion excludes all nonconstant interior periodic trajectories.

At \(r=2\), the equations become \(\dot x=x^2(1-x)q(p)\) and \(\dot p=\epsilon p(1-p)[(\theta+1)x-1]\). Define
\[
\mathcal H(x,p)=\delta_s\log p+\delta_d\log(1-p)
-\epsilon\left[\theta\log\left(\frac{x}{1-x}\right)+\frac1x\right].
\]
The two partial derivatives are
\[
\mathcal H_p=\frac{q(p)}{p(1-p)},\qquad
\mathcal H_x=-\epsilon\frac{(\theta+1)x-1}{x^2(1-x)}.
\]
Thus \(\dot x=B^{-1}\mathcal H_p\), \(\dot p=-B^{-1}\mathcal H_x\), and \(d\mathcal H/dt=0\) exactly. This representation also shows the weighted area form \(B(x,p)\,dx\wedge dp\) is invariant at the critical factor.

Let \(x_*=1/(1+\theta)\) and \(p_*=\delta_s/(\delta_s+\delta_d)\). The function \(\delta_s\log p+\delta_d\log(1-p)\) is strictly increasing before \(p_*\), strictly decreasing after it, and tends to \(-\infty\) at both endpoints. The function
\[
Q(x)=\theta\log\left(\frac{x}{1-x}\right)+\frac1x
\]
has derivative \(Q'(x)=[(\theta+1)x-1]/[x^2(1-x)]\), so it strictly decreases on \((0,x_*)\), strictly increases on \((x_*,1)\), and tends to \(+\infty\) at both endpoints. Hence \(\mathcal H\) has a unique strict global maximum at \((x_*,p_*)\). For every level below that maximum, its equation can be solved in two \(p\)-branches over one closed \(x\)-interval; the branches meet smoothly at its endpoints, making exactly one compact smooth simple closed curve. The vector field vanishes only at \((x_*,p_*)\) in the open square, so it is nowhere zero on the curve. A nonvanishing smooth tangent vector field traverses that compact circle periodically. Consequently every other interior trajectory is a nonisolated periodic orbit. None is an isolated attracting limit cycle.

For exact cycle statistics, integrate three total derivatives over an arbitrary period \(T>0\). First,
\[
\frac{d}{dt}\log\frac p{1-p}=\epsilon[(\theta+1)x-1]
\]
gives \(\overline x=x_*\). Second, writing \(K(x)=\log[x/(1-x)]-1/x\), the identity \(K'(x)=1/[x^2(1-x)]\) yields
\[
\frac{dK(x(t))}{dt}=q(p(t)),
\]
so \(\overline p=p_*\). Third,
\[
\frac{d}{dt}\log\frac x{1-x}=x(t)q(p(t))
\]
gives \((\delta_s+\delta_d)\overline{xp}=\delta_s\overline x\), proving the mixed moment and zero temporal covariance. The integrations require no small-amplitude approximation.

## Verification
The reproducible script `checker.py` independently checks the polynomial vector field, the critical conserved quantity, the full off-critical Dulac identity, and all three differentiated averaging identities symbolically in SymPy. It also reconstructs three complete asymmetric or symmetric periodic trajectories numerically, locates their return times, integrates along them by Gaussian quadrature, and compares both coordinate means and the covariance with the exact formulas. In one asymmetric example with \((\delta_s,\delta_d,\epsilon,\theta)=(3/4,1/4,3/10,2)\), the computed period is approximately \(58.048664815\), with means \((\overline x,\overline p,\overline{xp})=(1/3,3/4,1/4)\). Finite numerical experiments are corroboration only; the global existence/nonexistence and means are analytical.

To reproduce from a directory containing the attached files, run `python checker.py` with the Python packages SymPy, NumPy, and SciPy installed. The checker does not use outside data.

## Relationship to prior work
Jiang et al. [1] introduce the symmetric and asymmetric feedback nonlinear public-goods model and derive local stability regions and an attracting-cycle regime (illustrated for \(N=5\)). Their strict cycle interval \(N<r<r_*\) becomes empty at \(N=2\), since the given formula gives \(r_*=2\). That interval statement does not resolve the equality \(r=N=2\), a full interior continuum of neutral cycles, or exact temporal moments.

Weitz et al. [2] prove periodicity and a conserved quantity for a feedback-evolving two-strategy payoff family with a nonzero baseline cooperation advantage against a defector; the printed separable formula divides by that positive baseline. The present critical specialization has **zero** such baseline and an additional \(x\)-factor in the selection gradient; it requires its own singular-limit calculation. The present asymmetric environment probability \(p_*=\delta_s/(\delta_s+\delta_d)\) is not fixed at one-half. Ito and Yamamichi [3] classify neutral oscillations for several strict pairwise-game types, providing general context but not the degenerate two-person nonlinear public-goods equality or its joint statistical identities. Neither comparison implies the exact three moment laws or the parameter-wide Bendixson exclusion in this model. A separate complete 2026 mathematical finding on classical Lotka–Volterra flow establishes mutual mean-independence and zero covariance for its distinct two-species equations; its generic stationary-generator technique parallels the present averaging argument, but its hypotheses do not cover the public-goods vector field or its sharp critical boundary.

## Limitations
This theorem is specific to group size \(N=2\), deterministic infinite-population replicator/environment dynamics, strictly positive feedback rate and nonlinear coefficients, and the open state square. It does not say all off-critical solutions converge to the same equilibrium, nor classify all boundary equilibria. It does not exclude cycles for \(N\ge3\), analyze finite stochastic populations, or claim incentive or welfare guarantees. Existing general theory of two-strategy environmental feedback contains related center phenomena; publication priority for this exact model and moment triple is not independently established.

## References
[1] Y. Jiang, X. Wang, W. Zhu, M. Wei, L. Liu, S. Tang, and H. Zheng, *Nonlinear Public Goods Game in Dynamical Environments*, arXiv:2510.10259, first public October 11, 2025, equation (11), sections 3.2–3.3 and appendices B–C. https://arxiv.org/abs/2510.10259

[2] J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, and W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, PNAS 113 (2016), E7518–E7525, equation (17), supplemental appendix A. https://doi.org/10.1073/pnas.1604096113

[3] H. Ito and M. Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus 3 (2024), pgae455, methods and results on strict pairwise-game configurations. https://doi.org/10.1093/pnasnexus/pgae455
