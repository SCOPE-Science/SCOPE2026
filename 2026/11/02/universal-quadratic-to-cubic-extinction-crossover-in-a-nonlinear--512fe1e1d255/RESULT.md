# Universal quadratic-to-cubic extinction crossover in a nonlinear-dispersal two-patch Allee model

## Finding

For a continuous-time two-patch Allee population model at its critical invasion condition, loss of quadratic dissipation creates a cubic extinction bottleneck. Near the degeneracy, the transition between the two decay laws is not merely qualitative: it has an explicit **universal singular crossover profile**. Put \(B=s\delta/(s+\delta)\), \(H=h+B\), and \(\sigma=H-1/m\). With the assumptions below, on the critical invasion slice \(e=B\), every trajectory in a specified open near-extinction region obeys
\[
\lim_{t\to\infty}t u(t)^2=\frac{1}{2H^2}\quad(\sigma=0),\qquad
\lim_{t\to\infty}t u(t)=\frac1\sigma\quad(\sigma>0).
\]
More strongly, fixing any sufficiently small initial first-patch density \(u_0>0\) and setting the second patch initially to its instantaneous nullcline, as \(\sigma\downarrow0\) the normalized family satisfies, locally uniformly for \(\tau>0\),
\[
\frac{H^2}{\sigma}u_\sigma\!\left(\frac{H^2\tau}{\sigma^2}\right)\longrightarrow U(\tau),\qquad
\tau=\frac1{U}+\log\frac{U}{1+U}.
\]
There is exactly one positive \(U\) for each positive \(\tau\). Its two asymptotic limits are \(U(\tau)\sim(2\tau)^{-1/2}\) as \(\tau\downarrow0\), and \(U(\tau)\sim\tau^{-1}\) as \(\tau\to\infty\). Thus extinction exhibits a density transition at order \(\sigma/H^2\) and a time transition at order \(H^2/\sigma^2\).

## Assumptions and scope

Consider
\[
\begin{aligned}
\dot u&=u\left(\frac{u}{m+u}-e-hu\right)+\delta u(v-u),\\
\dot v&=v\left(s(1-v)+\delta(u-v)\right),
\end{aligned}
\]
for \(u,v\ge0\), \(s,\delta,h,m>0\), and \(0<e<1\). Fix \(s,\delta,h\) with \(B=s\delta/(s+\delta)<1\), choose \(e=B\), set \(H=h+B\), and vary \(m=1/(H-\sigma)\) with \(0\le\sigma\le\sigma_*<H\). Define \(a=\delta/(s+\delta)\), \(v_0=s/(s+\delta)\), \(z=v-v_0-au\), and \(F_\sigma(u)=\sigma u^2+u^3/[m(m+u)]\). There exist \(u_*,\sigma_*,C>0\), depending only on the fixed parameters, such that \(C>4a/s\), the set \(0<u\le u_*\), \(|z|\le C F_\sigma(u)\) is forward invariant, and all solutions therein converge to \((0,v_0)\). The decay assertions hold for every such solution. For the crossover assertion, take \(u(0)=u_0\in(0,u_*]\) independently of \(\sigma\) and \(z(0)=0\). More generally it holds for any choices \(|z(0)|\le C F_\sigma(u_0)\), with the same positive \(u_0\). At \(\sigma=0\), the first patch approaches zero cubically slowly; at \(\sigma>0\), quadratically slowly. The theorem is local near the extinction state, not a global basin theorem.

## Proof

**Exact reduction.** The logistic second-patch nullcline is \(v=v_0+au\), and direct substitution, without a center-manifold approximation, yields
\[
\dot u=-F_\sigma(u)+\delta u z,\qquad
\dot z=-(s+\delta)v z-a\dot u,\qquad
F_\sigma(u)=\sigma u^2+\frac{u^3}{m(m+u)}.
\]
Indeed \(1/m-H=-\sigma\) and \(u/(m+u)-u/m=-u^2/[m(m+u)]\), so the displayed sign and normalization hold exactly. All coefficients depend continuously on \(\sigma\) near zero.

**Invariant tube.** Fix \(C>4a/s\). For uniformly small \(u_*,\sigma_*\), within the tube \(|z|\le C F_\sigma(u)\) we have \(v\ge v_0/2\), \(\delta C u_*<1/2\), \(\sup_{0<u\le u_*}|F_\sigma'(u)|\) as small as required. Hence
\[
-F_\sigma(u)(1+\delta Cu)\le\dot u\le-F_\sigma(u)(1-\delta Cu)<0.
\]
At the upper face \(z=C F_\sigma(u)\), direct differentiation gives
\[
\frac{d}{dt}[z-C F_\sigma(u)]
=F_\sigma(u)\{-C(s+\delta)v+(a+C F_\sigma'(u))(1-\delta Cu)\}<0.
\]
At the lower face \(z=-C F_\sigma(u)\),
\[
\frac{d}{dt}[z+C F_\sigma(u)]
=F_\sigma(u)\{C(s+\delta)v+(a-C F_\sigma'(u))(1+\delta Cu)\}>0.
\]
The choices above make both inequalities uniform in \(\sigma\); the tube is forward invariant, and \(u\) decreases to zero (a positive limit would contradict the uniform strict derivative bound). Then \(z\to0\), \(v\to v_0\). In particular,
\[
\dot u=-F_\sigma(u)[1+O(u)],
\]
with a uniform \(O(u)\) bound over the tube and the specified \(\sigma\)-interval.

**Fixed-parameter decay laws.** At \(\sigma=0\), \(F_0(u)=H^2u^3/[1+Hu]\), giving \(d(u^{-2})/dt=2H^2+o(1)\). Thus \(t u(t)^2\to(2H^2)^{-1}\). For each fixed \(\sigma>0\), \(F_\sigma(u)=\sigma u^2[1+o(1)]\), so \(d(u^{-1})/dt=\sigma+o(1)\), yielding \(tu(t)\to1/\sigma\).

**Singular two-scale limit.** Let \(T_\sigma(w)\) be the unique time at which \(u=w\), for \(0<w<u_0\). Because \(\dot u=-F_\sigma(u)[1+O(u)]\), uniformly,
\[
T_\sigma(w)=\int_w^{u_0}\frac{1+O(\xi)}{\sigma\xi^2+q_\sigma(\xi)\xi^3}\,d\xi,
\quad q_\sigma(\xi)=\frac{(H-\sigma)^2}{1+(H-\sigma)\xi}.
\]
(The \(O(\xi)\) factor has a uniform bound, and need not be the same function along different trajectories.) Set \(w=\sigma V/H^2\), and substitute \(\xi=\sigma y/H^2\). For each fixed \(V>0\), dominated convergence gives
\[
\lim_{\sigma\downarrow0}\frac{\sigma^2}{H^2}
T_\sigma\left(\frac{\sigma V}{H^2}\right)
=\int_V^\infty\frac{dy}{y^2(1+y)}
=\frac1V+\log\frac{V}{1+V}=:\Theta(V).
\]
For domination, use \(q_\sigma(\xi)\ge c>0\) for \(0\le\xi\le u_0\) and small \(\sigma\); the transformed integrand is bounded by \(K/[y^2(1+cy/H^2)]\) for \(y\ge V\), an integrable majorant, and converges pointwise to the stated integrand. The limit \(\Theta\) is continuous, strictly decreasing from infinity to zero. Monotonicity of \(T_\sigma\), plus convergence at every \(V\), implies locally uniform convergence of the inverse rescaled trajectory on every compact subinterval of \((0,\infty)\). Finally expand \(\Theta(V)\) as \(V\to\infty\) and \(V\downarrow0\) to obtain the two endpoint asymptotics. These are limits of the universal profile and do not claim a joint uniform asymptotic all the way to \(\tau=0\) or infinity.

## Verification

`verification/check.py` executes exact symbolic reductions (including the cubic critical coefficient) and integrates one admissible parameter slice. For \(s=\delta=1\), \(h=e=1/2\), \(H=1\), and \(u_0=0.1\), it compares the rescaled numerical trajectories at decreasing positive \(\sigma\) with the unique root of the implicit profile equation; it also checks the critical decay coefficient numerically. These finite computations corroborate but do not establish the infinite-time or singular limits. The proof above supplies those limits.

## Relationship to prior work

Xia, Chen, Srivastava and Parshad (2023, arXiv:2310.10558) introduced the two-patch continuous model, identified the nonlinear-dispersal critical parameter plane and studied equilibrium and local bifurcation structure, including a higher-order center-manifold degeneracy. The present contribution is a **trajectory-level singular limit**: rigorous uniform trapping and the explicit universal crossover clock, scale, and implicit profile linking the quadratic and cubic extinction regimes. The general cubic normal form alone is not claimed as new. Chen, Liu and Chen's related additive-Allee two-patch study concerns a different dispersal mechanism. Gao, Chen and Chen's discrete two-patch model does not yield this continuous-time profile by implication.

## Limitations

This is a local theorem for strictly positive first-patch populations in an explicitly controlled near-extinction tube; it does not show all trajectories enter the tube, prove a global basin statement or address stochastic demographic extinction. The rescaled profile convergence is on compact positive time intervals, not the whole half-line; the initial positive density is held fixed as the parameter degenerates. The analytical proof is provided here; independent audit and validation have not been performed. Priority over every unindexed or inaccessible source is not asserted.

## References

1. Y. Xia, L. Chen, V. Srivastava and R. D. Parshad, *Stability and bifurcation analysis of a two-patch model with Allee effect and dispersal*, arXiv:2310.10558v1 (first posted 2023-10-16), https://arxiv.org/abs/2310.10558; *Mathematical Biosciences and Engineering* (2023), DOI:10.3934/mbe.2023876.
2. L. Chen, B. Liu and L. Chen, *Stability and bifurcation in a two-patch model with additive Allee effect*, *AIMS Mathematics* (2022), DOI:10.3934/math.2022034, https://aimspress.com/article/doi/10.3934/math.2022034.
3. Z. Gao, L. Chen and L. Chen, *Dynamical analysis of a discrete two-patch model with Allee effect and nonlinear dispersal* (2024), https://www.aimspress.com/.
