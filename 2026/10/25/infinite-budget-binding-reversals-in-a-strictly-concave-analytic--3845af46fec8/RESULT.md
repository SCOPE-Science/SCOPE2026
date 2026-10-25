# Infinite budget-binding reversals in a strictly concave analytic electricity market

## Finding
Consider a single price-taking electricity consumer with a unit spending budget and real-analytic utility
\[
u(x)=\log(1+x)+\frac14\bigl(1-\cos(\log(1+x))\bigr),\qquad x\ge0,
\]
served by a producer with quadratic cost \(C_\theta(y)=\theta y^2/2\), \(\theta>0\). At a price \(\lambda>0\), the consumer maximizes \(u(x)-\lambda x\) subject to \(x\ge0\) and \(\lambda x\le1\); the producer maximizes \(\lambda y-C_\theta(y)\) over \(y\ge0\). The market-clearing price and allocation are unique for each \(\theta>0\).

**Theorem.** As the production-cost coefficient \(\theta\) decreases to zero, the unique equilibrium undergoes *infinitely many alternating open intervals* of strictly binding and slack consumer budgets. Put \(t=\log(1+x_0)\), where \(x_0\) is the unconstrained demand at equilibrium price. For each integer \(k\ge1\), there are precisely two threshold numbers \(t_{2k}\) and \(t_{2k+1}\) in the interval \((2k\pi,(2k+1)\pi)\), determined by
\[
\sin t=\frac4{e^t-1},\qquad 2k\pi<t_{2k}<2k\pi+\frac\pi2<t_{2k+1}<(2k+1)\pi.
\]
The spending cap binds strictly when \(t_{2k}<t<t_{2k+1}\), and is slack on the intervening intervals, including the negative-sine half-periods. At the corresponding cost thresholds, denoted in decreasing order by \(\theta_m\),
\[
\theta_m=\frac1{(e^{t_m}-1)^2},\qquad
 t_m=m\pi+(-1)^m4e^{-m\pi}+o(e^{-m\pi}),
\]
for \(m\ge2\), and
\[
\theta_m\sim e^{-2m\pi},\qquad
\lim_{m\to\infty}\frac{\theta_{m+1}}{\theta_m}=e^{-2\pi}.
\]
Thus finite crossover complexity cannot be inferred from increasing real-analytic, strictly concave utility and quadratic, strictly convex production cost alone. The theorem asserts no globally uniform perturbation robustness of infinitely many switches.

## Assumptions and scope
The consumer has one commodity, budget \(b=1\), and is price-taking. The cost coefficient \(\theta\) varies while the single utility and the budget stay fixed. The interaction is the standard Walrasian single-commodity competitive equilibrium \(x=y\). The profit-maximizing supply is \(y=\lambda/\theta\); the consumer's budget constraint is on *spending*, not on a price-independent quantity. All functions are defined for nonnegative quantities and real positive prices; \(\log\) is natural logarithm. The claimed threshold asymptotic concerns indices \(m\to\infty\), not any fixed finite range.

## Proof
**1. Strict utility regularity.** Set \(t=\log(1+x)\). Differentiation yields
\[
u'(x)=\frac{1+\frac14\sin t}{1+x}>0,
\quad
u''(x)=\frac{-1+\frac14(\cos t-\sin t)}{(1+x)^2}<0.
\]
The strict last inequality follows from \(\cos t-\sin t\le\sqrt2<4\). Hence \(u\) is increasing, strictly concave and real analytic, with \(u'(0)=1\) and \(u'(x)\downarrow0\) at infinity. Its unconstrained demand \(D(\lambda)\) is therefore the unique solution \(u'(D)=\lambda\) for \(0<\lambda<1\).

**2. Market existence and parameterization.** At any \(0<\lambda<1\), budget-constrained demand is
\[
d(\lambda)=\min\{D(\lambda),1/\lambda\}.
\]
Both \(D(\lambda)\) and \(1/\lambda\) decrease strictly with \(\lambda\), so \(d\) does as well. Supply \(\lambda/\theta\) strictly increases with \(\lambda\); demand diverges as \(\lambda\downarrow0\), while supply tends to zero, and demand tends to zero as \(\lambda\uparrow1\). There is therefore one and only one market-clearing price for every \(\theta>0\). Parameterize that equilibrium with the hypothetical unconstrained demand \(x_0=e^t-1\):
\[
\lambda(t)=e^{-t}\left(1+\tfrac14\sin t\right),\quad
 d_t=\min\{e^t-1,1/\lambda(t)\},\quad
 \Theta(t)=\lambda(t)/d_t.
\]
The function \(\lambda(t)\) decreases strictly, \(d_t\) increases strictly, and \(\Theta(t)\) is continuous and strictly decreasing from infinity to zero. Thus \(t\in(0,\infty)\) parametrizes all distinct production-cost coefficients \(\theta\in(0,\infty)\) exactly once.

**3. Switch equation and root count.** The consumer is budget-constrained, strictly, exactly when its *unconstrained* expenditure exceeds one:
\[
\lambda(t)(e^t-1)=(1-e^{-t})\left(1+\tfrac14\sin t\right)>1.
\]
Rearrangement gives \(\sin t>4/(e^t-1)\). On every negative-sine half-period this fails. On the positive-sine half-period \(I_k=(2k\pi,(2k+1)\pi)\), \(k\ge1\), define
\[
h(t)=\sin t-\frac4{e^t-1}.
\]
At both endpoints \(h<0\), and at the midpoint \(h>0\), because \(e^{2k\pi+\pi/2}-1>4\). Moreover
\[
h''(t)=-\sin t-\frac{4e^t(e^t+1)}{(e^t-1)^3}<0
\]
throughout \(I_k\). Therefore \(h\) is strictly concave, has exactly two simple zeros in \(I_k\), and is positive precisely between them. This gives exactly one strictly binding interval within each \(I_k\), separated by nonempty slack intervals. Monotonicity of \(\Theta\) transfers this alternating structure to the market's cost coefficient.

**4. Sharp accumulation law.** Let \(a=2k\pi\), \(b=(2k+1)\pi\), and denote the left and right zeros by \(t_{2k}=a+\delta_k\), \(t_{2k+1}=b-\eta_k\). Their defining equation gives, by \(\sin\delta\sim\delta\) and \((e^t-1)^{-1}\sim e^{-t}\),
\[
\delta_k\sim4e^{-a},\qquad \eta_k\sim4e^{-b}.
\]
These expansions are justified by bracketing each zero between \(a+2e^{-a}\) and \(a+8e^{-a}\), or respectively between \(b-8e^{-b}\) and \(b-2e^{-b}\), for sufficiently large \(k\); uniqueness from Step 3 then identifies the relevant zero. On a crossover, unconstrained spending equals one, hence \(\lambda=1/(e^t-1)\), and the market-clearing equilibrium has \(d_t=e^t-1\). As \(\theta=\lambda/d_t\), the crossover cost equals exactly \((e^t-1)^{-2}\). The asymptotic expansions of the two roots therefore imply \(\theta_m\sim e^{-2m\pi}\) and the claimed ratio limit. This concludes the proof.

## Verification
The standalone `verify.py` probes the exact market equations at representative points, bisects six distinct crossover points with standard floating-point arithmetic, checks numerical feasibility and budget switching on three positive-sine periods, and checks the geometric cost scaling. It also tests the strict-concavity derivative inequality. Its finite computations are corroboration only: root uniqueness, infinitely many intervals, and the asymptotic ratio are proved analytically in Steps 1–4. The code intentionally avoids extrapolating double-precision bisection to thresholds too small for its resolution.

## Relationship to prior work
Perkins and Zhang, *Resource Allocation in Electricity Markets with Budget Constrained Customers* (2026), establish existence/uniqueness of competitive equilibrium under strictly concave utilities and strictly convex costs, and introduce a logarithmically modified utility via crossover points. Their explicit quadratic and square-root utility examples have two and one crossover points, respectively; the analyzed main text does not construct infinitely many crossings or their asymptotic spacing. The present result retains the same one-commodity equilibrium and budget semantics but gives a globally increasing, analytic, strictly concave utility with infinitely many *endogenous-price* budget transitions as the cost coefficient varies. It does not claim the general demand-clipping formula, uniqueness principle or the modified-utility method as new. Classical comparative statics provides the monotone clearing-price principle; strict concavity alone does not bound the number of intersections of the unconstrained expenditure \(x u'(x)\) with a fixed budget.

## Limitations
The oscillatory logarithmic utility is an explicit mathematical example, not an empirically estimated household utility. The conclusion uses a parameter interval accumulating at zero production cost; it does not imply infinitely many switches within a compact coefficient interval bounded away from zero. The result establishes equilibrium allocations and the active-set pattern, not convergence of a fixed-stepsize price iteration. This is an originality assessment based on identified accessible primary sources, not a guarantee of absolute historical priority.

## References
1. L. Perkins and B. Zhang, *Resource Allocation in Electricity Markets with Budget Constrained Customers*, arXiv:2603.20277v1, first submitted 17 March 2026, https://arxiv.org/html/2603.20277v1. In particular, §§ II–IV and the quadratic and square-root crossover examples.
2. Standard elementary calculus and monotone one-dimensional market-clearing arguments, proved explicitly above; no external technical lemma is required.
