# Sharp dual-weight robustness and Gaussian collapse window for aggregated linear constraints

## Finding

There is a bounded linear-programming family on which exact dual-multiplier weights recover the entire disaggregated bound with one surrogate linking constraint, yet an error of Euclidean norm only \(1/\sqrt m\) can cause the surrogate bound to lose its entire unit objective range. The complete deterministic error profile is sharp in both Euclidean and coordinatewise norms. Independent Gaussian errors exhibit an exact dimension-dependent transition, including a normal critical window for complete loss of the bound.

Precisely, let \(m\ge 2\), \(K_m=[-1,1]^m\), \(e_1=(1,0,\ldots,0)^\top\), and consider the full linking formulation
\[
 z_m^{\rm full}=\min\{-x_1:x\in K_m,\ x=0\}=0.
\]
Its unique optimal Lagrangian multiplier for the convention \(\pi^\top(0-x)\) is \(\pi^\star=-e_1\). For any weight \(w\in\mathbb R^m\), let
\[
 z_m^{\rm agg}(w)=\min\{-x_1:x\in K_m,\ w^\top x=0\},\qquad
 D_m(w)=z_m^{\rm full}-z_m^{\rm agg}(w).
\]
Then, defining \(S(w)=\sum_{j=2}^m|w_j|\),
\[
 D_m(w)=\begin{cases}\min\{1,S(w)/|w_1|\},&w_1\ne0,\\1,&w_1=0.\end{cases}
\]
Write \(w=\pi^\star+\varepsilon\). For \(0\le\rho<1\), the exact worst-case loss under an Euclidean error budget is
\[
 \sup_{\|\varepsilon\|_2\le\rho}D_m(\pi^\star+\varepsilon)
 =\min\left\{1,\frac{\rho\sqrt{m-1}}{\sqrt{1-\rho^2}}\right\},
\]
and the supremum equals one for \(\rho\ge1\). For \(0\le\delta<1\), the exact worst loss under a coordinatewise budget is
\[
 \sup_{\|\varepsilon\|_\infty\le\delta}D_m(\pi^\star+\varepsilon)
 =\min\left\{1,\frac{(m-1)\delta}{1-\delta}\right\},
\]
and it is one for \(\delta\ge1\). In particular, the minimum norm of a perturbation causing complete loss is exactly \(1/\sqrt m\) in \(\ell_2\) and \(1/m\) in \(\ell_\infty\).

For independent \(G_1,G_2,\ldots\sim N(0,1)\), set \(w_m=-e_1+(c/m)(G_1,\ldots,G_m)\) for fixed \(c>0\), and let \(\mu_G=\sqrt{2/\pi}\), \(v_G=\sqrt{1-2/\pi}\), and \(c_\star=1/\mu_G\). Under a common infinite Gaussian coupling,
\[
 D_m(w_m)\longrightarrow\min\{1,c\mu_G\}\quad\text{almost surely}.
\]
The probability of complete loss \(D_m(w_m)=1\) converges to zero for \(c<c_\star\), one half for \(c=c_\star\), and one for \(c>c_\star\). More finely, for any fixed \(\tau\in\mathbb R\), replacing \(c/m\) by \(c_\star(1+\tau/\sqrt m)/m\) gives
\[
 \lim_{m\to\infty}\Pr(D_m=1)=\Phi\left(\frac{\tau\mu_G}{v_G}\right),
\]
where \(\Phi\) denotes the standard normal distribution function.

## Assumptions and scope

The feasible box is compact, so it equals the convex hull of its \(2^m\) vertices; it is a valid convexified subproblem in a Dantzig--Wolfe formulation. All linking constraints are equalities, all weights are real (signed weights are permitted), the original linking right-hand side is zero, and objective values are computed exactly. The Gaussian perturbation model is an added diagnostic assumption, not a claim about the noise produced by a particular weight-update implementation. The statements concern one aggregate containing all \(m\) linking equalities; they do not assert identical behavior for arbitrary stochastic mixed-integer instances or multiple groups.

## Proof

**Full bound and optimal multiplier.** For any \(\pi\in\mathbb R^m\),
\[
 \min_{x\in K_m}\bigl[-x_1+\pi^\top(0-x)\bigr]
 =-\|e_1+\pi\|_1.
\]
Its maximum is zero, attained uniquely by \(\pi=-e_1\). The exact full linking equations force \(x=0\), hence \(z_m^{\rm full}=0\). The optimal weights identified by the multiplier-recovery principle therefore aggregate to the single equation \(-x_1=0\), which preserves the full objective bound.

**Exact surrogate gap.** Fix \(t=x_1\in[-1,1]\). The remaining terms \(\sum_{j=2}^m w_jx_j\), with \(|x_j|\le1\), fill exactly the interval \([-S(w),S(w)]\). Therefore some point with first coordinate \(t\) satisfies \(w^\top x=0\) precisely when \(|w_1t|\le S(w)\). Maximizing \(t\) yields the stated formula, including the case \(w_1=0\). No relaxation or inequality is used in this equality.

**Coordinatewise robustness.** If \(\|\varepsilon\|_\infty\le\delta<1\), then \(S(w)\le(m-1)\delta\) and \(|w_1|=|{-1+\varepsilon_1}|\ge1-\delta\). Equality in the uncapped quotient is achieved by \(\varepsilon_j=\delta\) for every coordinate. For \(\delta\ge1\), the smaller error \(\varepsilon=(1/m,\ldots,1/m)\) already produces complete loss. This proves the coordinatewise supremum.

**Euclidean robustness.** For \(0\le\rho<1\), put \(t=\varepsilon_1\). Cauchy--Schwarz gives
\[
 \frac{S(w)}{|w_1|}
 \le \frac{\sqrt{m-1}\sqrt{\rho^2-t^2}}{1-t},
 \qquad -\rho\le t\le\rho.
\]
For \(0<\rho<1\), differentiation of the positive ratio shows that its maximum is at \(t=\rho^2\): the sign of its derivative is the sign of \(\rho^2-t\). The maximum equals \(\rho\sqrt{m-1}/\sqrt{1-\rho^2}\). It is attained by \(\varepsilon_1=\rho^2\) and \(\varepsilon_j=\rho\sqrt{1-\rho^2}/\sqrt{m-1}\) for every \(j\ge2\). The case \(\rho=0\) is immediate. Since complete loss is possible with \(\varepsilon=(1/m,\ldots,1/m)\), whose Euclidean norm is \(1/\sqrt m\), the capped bound is attained also beyond that threshold. Alternatively, whenever complete loss occurs there is a feasible \(x\) with \(x_1=1\), forcing \(\varepsilon^\top x=1\); hence \(1\le\|\varepsilon\|_2\|x\|_2\le\sqrt m\|\varepsilon\|_2\), proving sharp minimality of the threshold.

**Gaussian limit and critical window.** Let \(T_m=\sum_{j=2}^m|G_j|\). The exact gap law becomes
\[
 D_m=\min\left\{1,\frac{\sigma_m T_m}{|1-\sigma_m G_1|}\right\}.
\]
The strong law gives \(T_m/m\to\mu_G\) almost surely. With \(\sigma_m=c/m\), the denominator tends to one and the almost-sure limit follows. The event \(\sigma_mG_1\ge1\) has probability tending to zero. Off this negligible event, complete loss is equivalent to
\[
 \sigma_m(T_m+G_1)\ge1.
\]
For \(c\ne c_\star\), the strong law establishes the zero/one limits. At the boundary, the central limit theorem for the independent half-normal variables gives
\[
 \frac{T_m+G_1-m\mu_G}{\sqrt m}\ \Longrightarrow\ N(0,v_G^2).
\]
Indeed, the one normal variable and the fixed missing half-normal mean are negligible on the \(\sqrt m\) scale. With \(\sigma_m=c_\star(1+\tau/\sqrt m)/m\), the preceding event is equivalent, up to an event of vanishing probability, to
\[
 \frac{T_m+G_1-m\mu_G}{\sqrt m}
 \ge-\tau\mu_G+o(1).
\]
Continuity of the Gaussian distribution function yields the stated critical-window probability. Taking \(\tau=0\) gives the critical value one half. All limit claims follow from these probability theorems, not finite sampling.

## Verification

The standalone \`verify.py\` enumerates hypercube vertices and edge intersections independently of the closed-form surrogate formula for many small rational instances, checks exact coordinatewise extremizers, checks Euclidean extremizers against randomized competitors, and runs seeded Gaussian experiments across both sides of the phase boundary and its critical window. In the submitted run, 623 exact rational cases, 3,050 deterministic Euclidean checks, and 14,400 Gaussian trials passed. These finite tests corroborate the algebra and scaling but do not certify universal quantifiers or asymptotics; those are proved above. The program uses only the Python standard library.

## Relationship to prior work

Kothari, Luedtke, and Marshall (2026, arXiv:2610.19181v1), Section 2.2.2 and Theorem 1, prove that suitably chosen optimal dual multipliers recover the full convexified nonanticipativity bound despite grouping constraints into weighted surrogate equations. The present result uses that exact-recovery setting but adds an exact sharp perturbation budget and stochastic collapse law on a bounded explicit linear-programming family. The source's weight-update theorem does not itself assert these error thresholds. Classical surrogate-constraint and duality literature, including Glover (1968) and Rardin--Unger (1976), motivates the strongest surrogate bound; it is not being claimed that optimal-multiplier recovery is new. The specific dimension-calibrated error laws require the box geometry and are the claimed contribution.

## Limitations

The examples describe the worst effect of perturbed surrogate weights, not a failure of the convergent weight-update procedure in the motivating study. They are linear-programming instances; no randomized algorithm or two-stage stochastic recourse distribution is modeled. The radius depends on the scaling of the linking constraints and variables, which is fixed explicitly here; it is not invariant under arbitrary row rescaling. Gaussian errors are exogenous, independent, and unnormalized before forming the surrogate constraint. The extreme-value loss comes from dropping all but one linear equality and must not be conflated with the original integer-feasible objective. Historical-priority assessment is limited by incomplete inspection of older specialized surrogate-duality texts. Independent external mathematical review has not been performed.

## References

1. H. Kothari, J. Luedtke, and L. Marshall, *Aggregated Column Generation for Two-Stage Stochastic Mixed-Integer Programs*, arXiv:2610.19181v1 (first public version: October 13, 2026), https://arxiv.org/abs/2610.19181 .
2. F. Glover, *Surrogate Constraints*, Operations Research 16(4), 741--749 (1968), https://doi.org/10.1287/opre.16.4.741 .
3. R. L. Rardin and V. E. Unger, *Surrogate Constraints and the Strength of Bounds Derived from 0-1 Benders' Partitioning Procedures*, Operations Research 24(6), 1169--1175 (1976), https://doi.org/10.1287/opre.24.6.1169 .
4. J. N. Hooker, *Integer Programming Duality*, background survey, https://johnhooker.tepper.cmu.edu/encyIPdualityRevised.pdf .
