# A horizon-dependent log-error floor for positive exponential approximations of a Gaussian survival kernel

## Finding

For the Gaussian droplet-survival kernel \(\phi_b(t)=\exp(-\pi t^2/(4b^2))\), with \(b>0\), let \(g(t)=\sum_{j=1}^{m} a_j e^{-\lambda_j t}\) be any finite positive exponential mixture with \(a_j>0\), \(\lambda_j\ge0\), and \(\sum_{j=1}^{m}a_j=1\). For every \(T>0\), its uniform log-error \(E_T(g)=\sup_{0\le t\le T}|\log(g(t)/\phi_b(t))|\) obeys \[E_T(g)\ge \frac{\pi T^2}{24b^2}.\] Consequently, \(\sup_{0\le t\le T}|g(t)/\phi_b(t)-1|\ge 1-\exp(-\pi T^2/(24b^2))\). The bound is independent of the number and rates of the exponential terms; it concerns uniform relative/log accuracy, not absolute error or general state-space realizations.

## Assumptions and scope

The parameter \(b\) is positive, \(T\) is any positive finite horizon, and the approximant is a finite sum with positive weights normalized to \(g(0)=1\). The rates \(\lambda_j\) are nonnegative. No assumption is made about the number of terms or their spacing. The claim is a uniform log-error bound, with a corollary for uniform relative error. It is not a lower bound in absolute error.

The motivating physical model uses \(\phi_b(t)=\exp(-\pi t^2/(4b^2))\) as a droplet-survival kernel in a memory integral. The result applies when that kernel is replaced by a positive parallel sum of exponential decays.

## Proof

Set \(c=\pi/(4b^2)\) and \(F(t)=\log g(t)\). Define the probability weights \(p_j(t)=a_j e^{-\lambda_j t}/g(t)\). Differentiating the finite log-sum gives

\[
F''(t)=\sum_j p_j(t)\lambda_j^2-\left(\sum_jp_j(t)\lambda_j\right)^2
=\operatorname{Var}_{p(t)}(\lambda_j)\ge0.
\]

Thus \(F\) is convex, and \(F(0)=0\). Write \(E=E_T(g)\). Since \(\log\phi_b(t)=-ct^2\), the definition of \(E\) implies

\[
F(T)\le -cT^2+E,
\qquad
F(T/2)\ge -cT^2/4-E.
\]

Convexity at the midpoint also gives

\[
F(T/2)\le \frac{F(0)+F(T)}2\le -cT^2/2+E/2.
\]

Combining the last two inequalities yields \(cT^2/4\le3E/2\), hence \(E\ge cT^2/6=\pi T^2/(24b^2)\). If a positive ratio has log-distance at least \(\delta\) from zero, its relative error is at least \(1-e^{-\delta}\); applying this with \(\delta=\pi T^2/(24b^2)\) proves the stated relative-error bound.

## Verification

The proof is analytic and uses only differentiation of a finite positive sum, convexity, and a midpoint inequality. It establishes the infinite family of rates and all finite term counts directly; no numerical enumeration is used as a substitute for proof. The coefficient is a valid universal lower-bound constant; optimality of that constant is not claimed.

## Relationship to prior work

The motivating atmospheric-convection preprint specifies the Gaussian survival kernel in its memory term and identifies \(b\) through the integral of that survival function. Its inspected model equations do not state an approximation-error theorem for positive exponential mixtures. published-finding corpus searches for equivalent formulations and exact lower bounds returned, among the closest indexed results, a uniform-convexity classification for a different function class and a transform-gap result for Gamma-sum approximation; neither implies the bound above. This comparison is limited to the actually retrieved statements and does not certify absolute novelty.

## Limitations

The result does not cover signed exponential sums, arbitrary finite-dimensional state-space realizations, phase-type survival laws outside the positive-mixture class, or absolute-error approximation. It does not by itself prove that a particular atmospheric simulation's oscillations change under a given approximation. A sharper minimax constant may be possible. Classical convex-approximation literature may contain related bounds that were not fully inspected in this run.

## References

1. Dalila Remaoun Bourega, “Stationary Solutions and Oscillatory Dynamics in a Mathematical Model of a Saturated Moist Atmosphere,” EGUsphere preprint, discussion started 2026-05-22, DOI: 10.5194/egusphere-2026-2648. The inspected material includes the Gaussian survival kernel and its use in the droplet-memory integral.
