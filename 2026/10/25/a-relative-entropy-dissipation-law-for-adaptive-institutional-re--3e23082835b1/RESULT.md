# A relative-entropy dissipation law for adaptive institutional rewards

## Finding

In the adaptive institutional-reward public-goods system introduced by Hua and Liu [1], an interior cooperation/reward equilibrium is **globally asymptotically stable among strictly interior states for every positive adjustment-speed parameter**, not merely locally stable or numerically stable at selected speeds. An explicit weighted sum of two Bernoulli relative entropies is a proper Lyapunov function. Its dissipation gives an exact integral identity and a finite budget on squared cooperation deviation.

Write \(S_N(x)=\sum_{k=0}^{N-1}(1-x)^k\) and \(d=c(1-r/N)\). Set
\[
 x_* = \frac{u}{1+u},\qquad
 a_* = \frac{d}{\delta S_N(x_*)}.
\]
Under the hypotheses below, \(\alpha<a_*<\beta\). Define \(y=(a-\alpha)/(\beta-\alpha)\) and \(y_*=(a_*-\alpha)/(\beta-\alpha)\), and the Bernoulli relative entropy
\[
 H(p\Vert q)=p\log\frac p q+(1-p)\log\frac{1-p}{1-q}.
\]
Then
\[
 V(x,a)=H(x_*\Vert x)+\frac{\delta S_N(x_*)}{\epsilon(1+u)}H(y_*\Vert y)
\]
is positive except at \((x_*,a_*)\), diverges at the boundary of the open state rectangle, and obeys the **exact dissipation identity**
\[
 \boxed{\dot V=-\frac{\delta a}{\epsilon}(x-x_*)\big[S_N(x_*)-S_N(x)\big]
 \le -\frac{\delta\alpha}{\epsilon}(x-x_*)^2.}
\]
For every strictly interior starting state, \((x(t),a(t))\to(x_*,a_*)\). Furthermore,
\[
 \boxed{\int_0^\infty a(t)(x(t)-x_*)[S_N(x_*)-S_N(x(t))]dt
 =\frac{\epsilon}{\delta}V(x(0),a(0)),}
\]
and
\[
 \boxed{\int_0^\infty (x(t)-x_*)^2dt\le\frac{\epsilon}{\delta\alpha}V(x(0),a(0)).}
\]
Consequently no nonconstant periodic or recurrent orbit exists entirely in the interior, and changing the positive relative adjustment speed cannot destabilize the interior attractor.

## Assumptions and scope

Fix an integer \(N\ge2\), positive parameters \(c,\delta,u,\epsilon\), a public-goods multiplier \(1<r<N\), and reward bounds \(0<\alpha<\beta\). Use the continuous-time deterministic, well-mixed, infinitely large population model [1]:
\[
 \begin{aligned}
 \epsilon\dot x&=x(1-x)\left[-d+a\delta S_N(x)\right],\\
 \dot a&=(a-\alpha)(\beta-a)\left[u(1-x)-x\right],\\
 d&=c\left(1-\frac r N\right),\qquad S_N(x)=\sum_{k=0}^{N-1}(1-x)^k.
 \end{aligned}
\]
Here \(x\in(0,1)\) is the cooperator fraction and \(a\in(\alpha,\beta)\) is adaptive reward intensity. The theorem assumes the genuinely interior coexistence condition
\[
 \boxed{\alpha<\frac{c(1-r/N)}{\delta S_N(u/(1+u))}<\beta.}
\]
The quantifiers are: for **every** admissible parameter tuple and **every** initial state \((x(0),a(0))\in(0,1)\times(\alpha,\beta)\), the stated conclusions hold for all forward time. No smallness assumption on \(\epsilon\) is made. No claim is made for initial states on the invariant boundary or when the strict coexistence condition fails.

## Proof

**Existence, uniqueness, and invariance.** Every face of the closed rectangle \([0,1]\times[\alpha,\beta]\) is invariant under the polynomial vector field. A strictly interior solution remains strictly interior at every finite time by uniqueness of solutions; its forward existence follows from boundedness of the closed rectangle. At an interior equilibrium, the second equation forces \(u(1-x)-x=0\), hence \(x=x_*\). The first equation then forces \(a=a_*\). The strict coexistence condition puts \((x_*,a_*)\) in the interior, so it is the unique interior equilibrium.

**Entropy derivative.** For fixed \(p\in(0,1)\), direct differentiation gives
\[
 \frac{d}{dq}H(p\Vert q)=\frac{q-p}{q(1-q)}.
\]
Because \(y=(a-\alpha)/(\beta-\alpha)\), the chain rule gives
\[
 \frac{d}{da}H(y_*\Vert y)=\frac{a-a_*}{(a-\alpha)(\beta-a)}.
\]
Consequently, for every interior trajectory,
\[
 \begin{aligned}
 \dot V&=\frac{x-x_*}{x(1-x)}\dot x+
 \frac{\delta S_N(x_*)}{\epsilon(1+u)}
 \frac{a-a_*}{(a-\alpha)(\beta-a)}\dot a\\
 &=\frac{\delta}{\epsilon}(x-x_*)\left[aS_N(x)-a_*S_N(x_*)-S_N(x_*)(a-a_*)\right]\\
 &=\frac{\delta a}{\epsilon}(x-x_*)[S_N(x)-S_N(x_*)].
 \end{aligned}
\]
The middle step uses \(d=\delta a_*S_N(x_*)\) and \(u(1-x)-x=-(1+u)(x-x_*)\). There is no approximation or averaging.

**Sharp sign and compact sublevels.** Differentiating the finite sum gives
\[
 S_N'(x)=-\sum_{k=1}^{N-1}k(1-x)^{k-1}\le-1
 \qquad (0\le x\le1),
\]
where the \(k=1\) term ensures the bound. By the mean-value theorem,
\[
 (x-x_*)[S_N(x_*)-S_N(x)]\ge(x-x_*)^2.
\]
The relative entropies are nonnegative and vanish precisely at their matching arguments. As either coordinate approaches an endpoint, at least one entropy diverges to infinity because both target arguments are strictly between zero and one. Thus every finite sublevel of \(V\) is a compact subset of the **open** rectangle, and solutions remain in their initial sublevel.

**Global attraction.** The displayed dissipation identity implies \(\dot V\le0\), with equality only on the vertical line \(x=x_*\). On this line,
\[
 \dot x=\frac{x_*(1-x_*)\delta S_N(x_*)}{\epsilon}(a-a_*),
\]
so the only invariant subset of the zero-dissipation locus is the single point \((x_*,a_*)\). Applying the standard invariance principle on the compact, forward-invariant initial sublevel yields convergence of every interior trajectory to that point. The same argument gives Lyapunov stability. In particular, no interior nonconstant periodic orbit or other nontrivial compact recurrent trajectory is possible.

**Integrated quantitative bound.** Integrate the exact derivative from zero to \(T\). The just-proved convergence implies \(V(T)\to0\), so taking \(T\to\infty\) gives the equality for total dissipation. Since \(a(t)\ge\alpha\) and \(S_N'\le-1\), the integrand dominates \(\alpha(x-x_*)^2\), giving the claimed squared-error bound. The Jacobian at \((x_*,a_*)\) has negative trace \(x_*(1-x_*)\delta a_*S'_N(x_*)/\epsilon\) and positive determinant \(x_*(1-x_*)\delta S_N(x_*)(a_*-\alpha)(\beta-a_*)(1+u)/\epsilon\); hence the equilibrium is additionally a hyperbolic sink for every \(\epsilon>0\).

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It exhausts 6,048 rational parameter/state configurations, directly checks the unreduced chain-rule derivative against the compact dissipation formula, checks \(S_N'\le-1\), and checks the squared-deviation domination. It is a finite algebraic regression test, not a substitute for the general proof.

For the motivating parameters \(N=5\), \(r=3\), \(c=1\), \(u=2\), \(\alpha=1/2\), \(\beta=3\), and \(\delta=1/5\), the equilibrium is exactly
\[
 (x_*,a_*)=\left(\frac23,\frac{162}{121}\right),
\]
strictly inside the admissible rectangle. The theorem applies to these parameters for **every** \(\epsilon>0\), including speeds beyond the finite set of values explored in [1]. Reproduction: save `verify.py` next to this file and run `python verify.py` with Python 3. No numerical ODE solver, external data, or third-party library is required.

## Relationship to prior work

Hua and Liu [1, Eq. (6); Sec. 4; Appendix] introduced the exact model, its interior equilibrium, and local Jacobian stability, and illustrated convergence for selected parameter choices and selected adjustment speeds. Those are prerequisites, not claimed as new here. The contribution is the **global, all-positive-speed** stability statement on the full interior coexistence parameter region together with a proper closed-form entropy Lyapunov function and exact integrated transient bound. The source's finite phase portraits and its local Jacobian cannot by themselves establish the all-initial-state theorem.

Liu, Chen, and Szolnoki [2, Eq. (5), Appendix 1] studied a related two-way-feedback collective-risk game. Its cooperation payoff contains a binomial risk factor with a generally nonmonotone dependence on cooperation, and stable cycles can arise. That model does not imply convergence for the strictly decreasing reward kernel used here. The different sign of the payoff derivative is the structural distinction that makes the exact dissipation work.

Classical relative-entropy Lyapunov arguments in evolutionary dynamics provide methodological context; the present proof is a direct calculation for the specified two-variable payoff/feedback equations. Identical or stronger prior results in less immediately indexed mathematical literature remain a publication-priority risk; no claim of exhaustive uniqueness is made.

## Limitations

The result assumes homogeneous well-mixed public-goods sampling, a deterministic infinite-population replicator model, strictly positive lower and upper reward bounds, linear strategy-to-reward feedback, the source's declining per-cooperator reward kernel, and the strict interior coexistence condition. It does **not** classify attraction on parameter boundaries, prove global attraction when the interior equilibrium is absent, describe stochastic finite-population behavior, or extend to nonmonotone incentive kernels. The squared-error estimate controls time-integrated cooperation deviation but does not give a single parameter-uniform convergence rate for all initial conditions.

## References

[1] Shijia Hua and Linjie Liu, “Coevolutionary dynamics of population and institutional rewards in public goods games,” arXiv:2308.09530v1, first posted 2023-08-18. https://arxiv.org/abs/2308.09530 . Model Eq. (6), Secs. 3–5, and Appendix.

[2] Linjie Liu, Xiaojie Chen, and Attila Szolnoki, “Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game,” eLife 12:e82954 (2023), https://doi.org/10.7554/eLife.82954 . Full text at https://journal-symfony7.elifesciences.org/articles/82954 . Equation (5), Results, and Appendix 1.
