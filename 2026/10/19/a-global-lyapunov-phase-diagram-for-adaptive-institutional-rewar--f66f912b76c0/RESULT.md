# A global Lyapunov phase diagram for adaptive institutional rewards

## Finding

For the exact institutional-reward public-goods replicator of Hua and Liu (2023), all strictly interior initial states converge to **one and the same selected equilibrium**, for **every** positive relative timescale \(\varepsilon\). Four ordered, explicit incentive thresholds divide the positive incentive axis into exactly five regimes, including all degenerate threshold equalities. A separable strict Lyapunov argument proves the global statement; local stability of the equilibria alone would not imply it.

Let
\[
 k=c\left(1-\frac rN\right),\qquad
 S_N(x)=\sum_{j=0}^{N-1}(1-x)^j,\qquad
 h=\frac{u}{1+u},\qquad
 A_\delta(x)=\frac{k}{\delta S_N(x)}.
\]
Set
\[
 \delta_0=\frac{k}{N\beta},\qquad
 \delta_1=\frac{k}{\beta S_N(h)},\qquad
 \delta_2=\frac{k}{\alpha S_N(h)},\qquad
 \delta_3=\frac{k}{\alpha}.
\]
These satisfy \(0<\delta_0<\delta_1<\delta_2<\delta_3\). For each \(\delta>0\), the limit \((x_\infty,a_\infty)\) of **every** solution with \((x(0),a(0))\in(0,1)\times(\alpha,\beta)\) is
\[
(x_\infty,a_\infty)=
\begin{cases}
(0,\beta),&0<\delta\le\delta_0,\\
(\xi_\beta(\delta),\beta),&\delta_0<\delta<\delta_1,\\
(h,A_\delta(h)),&\delta_1\le\delta\le\delta_2,\\
(\xi_\alpha(\delta),\alpha),&\delta_2<\delta<\delta_3,\\
(1,\alpha),&\delta\ge\delta_3.
\end{cases}
\]
Here \(\xi_\beta(\delta)\) is the **unique** root of \(A_\delta(x)=\beta\) in \((0,h)\), and \(\xi_\alpha(\delta)\) is the **unique** root of \(A_\delta(x)=\alpha\) in \((h,1)\). This includes the four threshold cases and all parameters satisfying the assumptions, rather than merely five chosen numerical scenarios. The autonomous planar flow admits **no nonconstant periodic orbit wholly inside the open rectangle**. Along the stable branch, \(x_\infty\) varies continuously and nondecreasingly with \(\delta\), whereas \(a_\infty\) varies continuously and nonincreasingly; the increasing portions of \(x_\infty\) are precisely regimes two and four, and the decreasing portion of \(a_\infty\) is precisely regime three.

## Assumptions and scope

The model is the following **specific** two-equation autonomous ODE, equation (6) of the original preprint:
\[
\begin{aligned}
\varepsilon\dot x&=x(1-x)\big[-k+a\delta S_N(x)\big],\\
\dot a&=(a-\alpha)(\beta-a)\,[u(1-x)-x].
\end{aligned}
\]
Assume \(N\in\{2,3,\ldots\}\), \(c>0\), \(1<r<N\), \(\delta>0\), \(u>0\), \(\varepsilon>0\), and \(0<\alpha<\beta\). The cooperation fraction is \(0\le x\le1\); reward strength lies in \(\alpha\le a\le\beta\). Claims of convergence apply **only to strictly interior initial data**, not to all the other invariant boundary faces and corner states. The parameters are fixed during each trajectory. No stochastic, spatial, or delayed feedback is considered.

## Proof

**1. Monotone reward isocline.** For \(0\le x<1\), \(S_N'(x)=-\sum_{j=1}^{N-1}j(1-x)^{j-1}<0\); by continuity the strict monotonicity extends to the closed interval. Moreover \(S_N(0)=N\) and \(S_N(1)=1\). Thus \(A_\delta\) increases strictly from \(k/(N\delta)\) to \(k/\delta\), and \(1<S_N(h)<N\). Because \(0<\alpha<\beta\), the four thresholds are strictly ordered. The five displayed cases follow by comparing \(A_\delta(0)\), \(A_\delta(h)\), \(A_\delta(1)\) with \(\alpha\) and \(\beta\). At the selected point, both ODE right-hand sides vanish, including if a coordinate belongs to the invariant boundary.

**2. A universal nonnegative Lyapunov function.** Put
\[
 P(x)=\frac{\delta}{\varepsilon}x(1-x)S_N(x),\qquad
 Q(a)=(a-\alpha)(\beta-a).
\]
Then
\[
 \dot x=P(x)\,[a-A_\delta(x)],\qquad
 \dot a=(1+u)Q(a)(h-x).
\]
Write \((x_e,a_e)=(x_\infty,a_\infty)\) from the relevant phase. On the open rectangle define
\[
 V(x,a)=(1+u)\int_{x_e}^{x}\frac{s-x_e}{P(s)}\,ds
 +\int_{a_e}^{a}\frac{z-a_e}{Q(z)}\,dz.\tag{1}
\]
When an endpoint is on a boundary, the corresponding integrand has a finite one-sided limit there; interpret that improper endpoint by continuity. Each integral is nonnegative because its integrand has the sign of the displacement from its lower limit, and both vanish together exactly at \((x_e,a_e)\). Differentiating along any interior solution gives the **exact** identity
\[
\begin{aligned}
\dot V/(1+u)
&=(x-x_e)(a-A_\delta(x))+(a-a_e)(h-x)\\
&=(x-x_e)(a_e-A_\delta(x))+(a-a_e)(h-x_e)\\
&=-(x-x_e)[A_\delta(x)-A_\delta(x_e)]\\
&\quad+(x-x_e)[a_e-A_\delta(x_e)]+(a-a_e)(h-x_e).
\end{aligned}\tag{2}
\]
The first term is nonpositive by strict monotonicity. In the central regime \(x_e=h\) and \(a_e=A_\delta(h)\), so the two remaining terms vanish. On the upper-reward boundary branch, \(a_e=A_\delta(x_e)=\beta\), \(x_e<h\), and \(a-\beta<0\), making the last term nonpositive. On the lower-reward boundary branch, \(a_e=A_\delta(x_e)=\alpha\), \(x_e>h\), and \(a-\alpha>0\), again giving a nonpositive last term. At the defection corner, \(x_e=0\), \(a_e=\beta\), \(A_\delta(0)\ge\beta\), so the middle and last terms are nonpositive. At the cooperation corner, \(x_e=1\), \(a_e=\alpha\), \(A_\delta(1)\le\alpha\), and the same holds. **These inequalities include equality at every threshold.** Thus \(\dot V\le0\) throughout the open rectangle for all \(\varepsilon>0\).

**3. Coercivity relative to the allowed boundary.** The vector field is smooth on the invariant compact rectangle \([0,1]\times[\alpha,\beta]\); initial data in its interior stay interior at every finite time, since each face has a multiplicative vanishing factor and uniqueness holds. When \(x_e\) is interior, the first integral in (1) diverges as \(x\to0\) or \(x\to1\). When \(x_e\) is an endpoint, that integral extends finitely **only** to that selected endpoint and diverges at the opposite endpoint. The identical alternative applies to the second integral at \(a_e\). These assertions follow from \(P(x)\asymp x\) near \(0\), \(P(x)\asymp1-x\) near \(1\), \(Q(a)\asymp a-\alpha\) near \(\alpha\), and \(Q(a)\asymp\beta-a\) near \(\beta\): a numerator vanishes exactly at a selected endpoint, removing precisely that logarithmic divergence. Consequently each finite \(V\)-sublevel is compact in the rectangle extended by only the selected coordinate faces. Since \(V\) decreases, its trajectory is precompact within that extended invariant set.

**4. Strict invariance, including nonhyperbolic thresholds.** If \(x\ne x_e\), the first term of (2) is strictly negative because \(A_\delta\) is strictly increasing, while the other terms are nonpositive. Hence \(\dot V=0\) requires \(x=x_e\). When \(x_e=h\), the flow on this vertical line has \(\dot x=P(h)[a-A_\delta(h)]\), which is zero only when \(a=a_e\). When \(x_e\ne h\), the last term in (2) is strictly negative unless \(a=a_e\); this remains true at each corner and boundary branch, including the critical equality values. Thus the largest invariant subset of \(\{\dot V=0\}\) in any bounded \(V\)-sublevel is exactly the singleton \(\{(x_e,a_e)\}\). LaSalle's invariance principle gives convergence to this point for every strictly interior initial state. This proof does not require exponential convergence and covers threshold equilibria with zero eigenvalues.

**5. Absence of interior cycles and threshold continuity.** Strict decrease of \(V\) off the selected point rules out nonconstant interior periodic trajectories. Strict monotonicity of \(A_\delta\) also gives continuity of the roots at each threshold: \(\xi_\beta\to0,h\) at \(\delta_0,\delta_1\), while \(\xi_\alpha\to h,1\) at \(\delta_2,\delta_3\). Since \(A_\delta(x)=k/[\delta S_N(x)]\), an increased \(\delta\) requires increased \(x\) on either root branch. At the interior equilibrium, \(a_e=k/[\delta S_N(h)]\) decreases strictly with \(\delta\). This proves the stated one-sided monotonicity, all continuity statements, and absence of static equilibrium-branch hysteresis.

## Verification

The exact phase thresholds, the derivative identity (2), and every sign used in the proof follow algebraically from the printed ODE. A standalone standard-library Python script, `verify.py`, implements the five-case equilibrium selector, checks all four endpoints, verifies the derivative identity and the nonpositive derivative on a fixed-seed parameter sweep, and checks both monotone response coordinates. Run with `python verify.py`; no external package is required. These computational checks are finite corroboration, **not** a substitute for the analytic proof of arbitrary \(N\), arbitrary positive parameters, or infinite-time convergence.

## Relationship to prior work

Hua and Liu's preprint (2023, equation (6), Section 4 and Appendix) derives the exact coupled model, lists its equilibria, analyzes their linearized stability, and plots five illustrative dynamical scenarios. Those local calculations and illustrations are compatible with the present result. The contribution here is **one explicit Lyapunov function** plus a **complete, sharp ordered four-threshold theorem** guaranteeing a common global limit for every interior initial condition and every \(\varepsilon>0\), including all four equality surfaces, without inferring global behavior merely from local eigenvalues.

Gong and collaborators' 2022 environmental-feedback game analysis studies limit cycles for a different replicator/environment coupling. Liu, Chen and Szolnoki's 2023 collective-risk game includes a nonmonotone binomial threshold factor and may exhibit periodic regimes. Hua, Xu, Liu and Chen's 2024 collective-risk/dilemma-strength model has a different payoff and feedback sign and can be multistable even when institutional incentives are added. These works emphasize that non-oscillation is a **model-specific consequence** of the strictly decreasing marginal incentive \(S_N\) and the negative-feedback structure, rather than a generic property of all coevolutionary games.

## Limitations

The result is about the deterministic, well-mixed, autonomous Hua–Liu equation (6). It neither treats finite-population random games, networks, delays, changes in the incentive parameter during a trajectory, nor asserts uniqueness of equilibria on the *whole closed rectangle* (there are invariant boundary corners and possibly other boundary equilibria). The selected attractor concerns **strictly interior starts** only. Convergence need not be exponential at a threshold. The proof does not establish optimal public policy outcomes, robustness to a changed feedback law, or an independent audit; originality comparison is limited to the inspected primary literature and accessible research records.

## References

1. S. Hua and L. Liu, *Coevolutionary dynamics of population and institutional rewards in public goods games*, arXiv:2308.09530v1, first publicly submitted 2023-08-18; later *Expert Systems with Applications* 237, 121579 (2024), DOI: 10.1016/j.eswa.2023.121579. Full preprint: https://arxiv.org/html/2308.09530v1.
2. Z. Gong et al., *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734v1 (2022), https://arxiv.org/html/2205.10734v1.
3. L. Liu, X. Chen and A. Szolnoki, *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*, arXiv:2305.00253v1 (2023), https://arxiv.org/html/2305.00253v1.
4. S. Hua, M. Xu, L. Liu and X. Chen, *Coevolutionary dynamics of collective cooperation and dilemma strength in a collective-risk game*, *Physical Review Research* 6, 023313 (2024), DOI: 10.1103/PhysRevResearch.6.023313.
