# Travel-time variability shortens optimal residence under background mortality

## Finding

Consider sequential exploitation of identical renewable patches with a fresh strictly decreasing marginal gain rate \(g\), random independent transit durations \(T\), and independent background mortality at hazard \(\mu>0\). The reward objective is the expected total benefit earned before death, not a finite-horizon reward or the mortality-free gain rate. For this model, the optimal patch residence time is a *unique deterministic stationary threshold*, even when the policy is allowed to adapt to all previous transit observations.

The law of \(T\) affects the optimal threshold and the maximum expected lifetime reward **only through** its mortality Laplace factor \(A_\mu=\mathbb E[e^{-\mu T}]\). If two transit laws have the same finite mean and one is strictly larger in convex order, its optimal residence time is strictly **shorter**, and its optimal lifetime benefit is strictly **greater**. This distributional sensitivity is absent from the standard mortality-free marginal-value criterion.

More precisely, define
\[
G_\mu(t)=\int_0^t e^{-\mu u}g(u)\,du,\qquad
H_\mu(t)=e^{-\mu t}g(t)+\mu G_\mu(t).
\]
For \(A_\mu\in(0,1)\), the unique optimal threshold \(t_\mu^*>0\) is characterized by
\[
A_\mu=\frac{g(t_\mu^*)}{H_\mu(t_\mu^*)}.
\]
If \(T_1\le_{\mathrm{cx}}T_2\) with equal positive finite means and different laws, then
\[
t_{\mu,2}^*<t_{\mu,1}^*,\qquad
J_\mu^*(T_2)>J_\mu^*(T_1),
\]
where \(J_\mu^*\) is optimal expected lifetime reward starting before an initial transit.

There is also an explicit near-zero-mortality boundary. Let \(m=\mathbb E[T_i]>0\), let \(t_0\) be the unique classical marginal-value threshold satisfying
\[
(m+t_0)g(t_0)=\int_0^{t_0}g(u)\,du,
\]
and assume both transit laws have finite third moments and \(g\) is twice continuously differentiable near \(t_0\). Then
\[
t_{\mu,2}^*-t_{\mu,1}^*
=\frac{\mu g(t_0)}{2g'(t_0)(m+t_0)}
\left(\operatorname{Var}T_2-\operatorname{Var}T_1\right)+O(\mu^2)
\quad(\mu\downarrow0).
\]
The coefficient is strictly negative when the variance increases.

**Exact witness.** Take \(g(u)=e^{-u}\), \(\mu=1\) and either \(T_1=\log2\) surely or \(T_2\in\{0,2\log2\}\) with probability one-half each. Both transit means are \(\log2\), but
\[
(A_{\mu,1},A_{\mu,2})=(1/2,5/8),\qquad
(t_{\mu,1}^*,t_{\mu,2}^*)=(\operatorname{arcosh}2,\operatorname{arcosh}(8/5)).
\]
The corresponding maximal expected lifetime gains before initial transit are \(2-\sqrt3\) and \((8-\sqrt{39})/5\), respectively, with the latter strictly greater.

## Assumptions and scope

Fix \(\mu>0\). A forager encounters infinitely many identical, independent, initially unexploited patches. A patch reached alive yields deterministic instantaneous benefit \(g(u)\) at time \(u\ge0\) since entry. Assume \(g:[0,\infty)\to(0,\infty)\) is continuously differentiable, \(g'(u)<0\) for every finite \(u\), and \(g(u)\to0\). Benefit earned up to the moment of death is retained. There is no reward during transit, no penalty for moving beyond elapsed exposure, no within-patch random information, and no replenishment within one visit. A fresh independent transit of nonnegative length \(T\) precedes every patch, including the first. Its law is fixed, \(0<\mathbb E[T]<\infty\), and transit durations are independent of one another, of gain, and of the exponential lifetime clock. The mortality hazard \(\mu\) applies uniformly in transit and in patches.

Policies may choose nonnegative dwell times based on previously observed transits and elapsed times; they cannot foresee a future transit or death time. Waiting indefinitely in a patch is permitted. Statements concern maximizing expected cumulative *pre-death* reward, not realized gain per unit time, population fitness, energy budgets, state-dependent predation, adaptive habitat choice, or noisy empirical estimation. The small-hazard expansion assumes \(\mathbb E[T_i^3]<\infty\) and local \(C^2\) regularity of \(g\) at \(t_0\). Convex order means comparison of expectations for all convex functions for which those expectations exist.

## Proof

**1. Exact renewal reward and global control optimality.** Let \(A=A_\mu=\mathbb E[e^{-\mu T}]\in(0,1)\). From entry into a patch, a fixed residence time \(t\) yields expected pre-death reward \(G_\mu(t)\). Reaching the next patch alive has conditional discount factor \(A e^{-\mu t}\). Therefore the patch-entry value under repeated residence time \(t\) is
\[
V_t=G_\mu(t)\sum_{j\ge0}(A e^{-\mu t})^j
=\frac{G_\mu(t)}{1-Ae^{-\mu t}},
\qquad J_t=A V_t.
\]
A history-dependent strategy starting alive at a patch entrance has Bellman operator
\[
(\mathcal Bv)=\sup_{t\in[0,\infty]}\bigl\{G_\mu(t)+A e^{-\mu t}v\bigr\}.
\]
It is an \(A\)-contraction, so its bounded fixed point is the optimal value. Put \(V_*=\sup_t V_t\). By \(G_\mu(t)\le (1-A e^{-\mu t})V_*\) for every \(t\), \(\mathcal B(V_*)\le V_*\), with equality at any maximizer of \(V_t\). Continuity and the limiting value at infinite residence ensure a maximizer exists. Hence \(V_*\) is the optimal fixed point, realized by a repeated deterministic threshold. No past-dependent or randomized policy improves it. Multiplication by \(A\) converts the patch-entry value into the before-first-transit value.

**2. Strictly unique optimum.** Differentiation gives
\[
V_t'=\frac{e^{-\mu t}\{g(t)-A H_\mu(t)\}}{(1-Ae^{-\mu t})^2},\quad
H_\mu'(t)=e^{-\mu t}g'(t).
\]
For \(F_\mu(t)=g(t)/H_\mu(t)\), direct cancellation yields
\[
F_\mu'(t)=\frac{\mu G_\mu(t)g'(t)}{H_\mu(t)^2}<0\quad(t>0).
\]
Moreover \(F_\mu(0)=1\) and \(\lim_{t\to\infty}F_\mu(t)=0\), since \(H_\mu(t)\to\mu G_\mu(\infty)>0\) while \(g(t)\to0\). Thus \(F_\mu(t)=A\in(0,1)\) has exactly one positive solution. The derivative of \(V_t\) is positive before it and negative after it. The solution is the unique global optimum, including against never leaving.

**3. Convex-order response and identifiability.** By the strictly convex function \(x\mapsto e^{-\mu x}\), if \(T_1\le_{\mathrm{cx}}T_2\) and the laws differ, then \(A_{\mu,1}<A_{\mu,2}\); strictness follows from a martingale coupling and strict Jensen inequality. As \(F_\mu\) strictly decreases, larger \(A\) forces strictly smaller optimal \(t\). At each fixed positive \(t\), \(J_t=A G_\mu(t)/(1-Ae^{-\mu t})\) is strictly increasing in \(A\). Evaluating the second model at the first model's optimum proves a strict increase in the maximum. Conversely, two travel laws with identical Laplace factors have identical \(J_t\) for every policy's fixed residence choice and hence identical optimal threshold and value. Since \(t^*\) maps bijectively to \(A\) through \(F_\mu\), equality of optimal thresholds is also sufficient for equality of Laplace factors.

**4. Classical limit and first variance-sensitive term.** Let \(G_0(t)=\int_0^t g(u)\,du\), \(m=\mathbb E[T]\) and \(m_2=\mathbb E[T^2]\). For fixed \(t\),
\[
A_\mu=1-\mu m+\frac{\mu^2m_2}{2}+O(\mu^3),
\quad \mu J_t\to \frac{G_0(t)}{m+t}.
\]
The classical rate has unique interior maximizer \(t_0\), since its derivative numerator \(K_0(t)=(m+t)g(t)-G_0(t)\) decreases strictly from \(mg(0)>0\) to a negative value, with \(K_0'(t)=(m+t)g'(t)<0\). Write the mortality first-order condition divided by \(\mu\) as
\[
\frac{g(t)-A_\mu H_\mu(t)}{\mu}
=K_0(t)+\mu\left[-g(t)\left(\frac{m_2}{2}+mt+\frac{t^2}{2}\right)+\int_0^t u g(u)\,du+mG_0(t)\right]+O(\mu^2).
\]
This expansion is uniform for \(t\) in a fixed neighborhood of \(t_0\); finite third moments provide the stated remainder. Uniqueness and signs near \(t_0\) show \(t_\mu^*\to t_0\). The implicit-function expansion is valid because \(K_0'(t_0)\ne0\). For equal-mean laws the only difference in the \(\mu\)-coefficient comes from \(-g(t_0)m_2/2\), while \(m_2=m^2+\operatorname{Var}T\). Subtracting the two expansions gives the displayed first-order variance effect, with \(O(\mu^2)\) remainder.

**5. Exact two-law check.** For \(g(u)=e^{-u}\), \(\mu=1\),
\[
G_1(t)=\frac{1-e^{-2t}}2,\qquad F_1(t)=\frac1{\cosh t}.
\]
The two travel Laplace factors are \(1/2\) and \((1+1/4)/2=5/8\), giving the asserted unique thresholds. At either optimum \(J_t=e^{-t}\), yielding \(2-\sqrt3\) and \((8-\sqrt{39})/5\). These inequalities are exact, not simulation-based.

## Verification

Run `python3 verification/check.py` with Python 3 standard library from the package root. The checker exercises the exact example, the unimodality and comparative statics across finite grids of admissible exponential-gain parameters and mean-preserving travel spreads, a distinct non-exponential gain curve, and numerical convergence to the first-order small-hazard variance coefficient. It reports 2,311 successful assertions. These checks are consistency tests; all infinite-law and arbitrary-gain conclusions follow from the algebraic proof above, not finite enumeration. No stochastic simulations or external solvers are required.

## Relationship to prior work

Charnov's 1976 marginal-value theorem and Calcagno, Mailleret, Wajnberg and Grognard's 2013 reanalysis determine optimal residence times from long-run gain divided by mean travel-plus-foraging time. Their ordinary homogeneous objective depends on mean transit but not equal-mean transit variability. Newman (1991) incorporates predation hazard and refuge/stored-energy decisions with fixed transit durations and obtains numerical dynamic-programming predictions. Wajnberg, Bernhard, Hamelin and Boivin (2006) allow random travel times under a deterministic finite-life horizon and numerically compare unequal-mean uniform and triangular transit laws. Those models establish important context but do not yield the present full class of decreasing gain rates, the strict *equal-mean convex-order comparison*, or the universal first-order variance coefficient under exponential lifetime mortality. The 2025 risk-marginal-value theory of Calcagno and collaborators also studies mortality, primarily with specified transit duration, but provides a different general risk framework and is not claimed here.

This result uses classical renewal reward, Bellman contraction, Laplace transforms, convex-order Jensen inequalities and the implicit-function theorem. Originality attaches only to their indicated joint ecological residence-time classification in the stated model, not to these mathematical techniques or the older models themselves.

## Limitations

The claim is a theorem for an idealized homogeneous sequential-patch model with an exogenous exponential death clock, deterministic declining within-patch gain, and no extra state information. It does not address time-dependent hazards, stochastic patch contents, heterogeneity of habitat types, prey learning, nonexponential lifetime, losses of accumulated reward at death, competing survival objectives, or data estimation. Strict ordering may fail for travel laws not ordered in convex order, even if one has larger variance. The small-hazard expansion is only a local result and needs finite third moments. The exact novelty comparison is based on accessible scholarly literature and database searches, not an independent exhaustive historical audit.

## References

1. E. L. Charnov (1976), *Optimal foraging, the marginal value theorem*, Theoretical Population Biology 9(2), 129–136. DOI: https://doi.org/10.1016/0040-5809(76)90040-X
2. V. Calcagno, L. Mailleret, É. Wajnberg and F. Grognard (first publicly released 2013-10-26), *How optimal foragers should respond to habitat changes: a reanalysis of the Marginal Value Theorem*, Journal of Mathematical Biology 69, 1237–1265. https://doi.org/10.1007/s00285-013-0734-y
3. J. A. Newman (1991), *Patch use under predation hazard: foraging behavior in a simple stochastic environment*, Oikos 61, 29–44. https://doi.org/10.2307/3545404
4. É. Wajnberg, P. Bernhard, F. Hamelin and G. Boivin (first publicly released 2006-01-14), *Optimal patch time allocation for time-limited foragers*, Behavioral Ecology and Sociobiology 60, 1–10. https://doi.org/10.1007/s00265-005-0131-7
5. V. Calcagno, F. Grognard, F. M. Hamelin and L. Mailleret (2025), *Taking fear back into the marginal value theorem: the rMVT and optimal boldness*, Evolution 79, 1742–1755. https://doi.org/10.1093/evolut/qpaf100
