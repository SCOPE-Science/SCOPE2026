# Sharp fixed-radius phase transition for composite trust-region gradient descent
## Finding

Let
\[
\phi(x)=\frac a2x^2+\lambda|x|,
\qquad
a>0,\quad \lambda>0,
\]
and consider the exact Euclidean trust-region gradient update
\[
x_{k+1}\in
\arg\min_{|z-x_k|\le\eta}
\left\{a x_k z+\lambda|z|\right\},
\qquad
\eta>0.
\]
This is the deterministic one-dimensional composite specialization of the trust-region gradient method that minimizes the linearization of the smooth term plus the unchanged convex regularizer over a ball.

Set
\[
\theta=\frac{\lambda}{a}.
\]
Then the following phase transition is sharp.

If
\[
0<\eta<2\theta,
\]
every admissible trajectory, including every possible choice at a set-valued subproblem, reaches the unique minimizer \(0\) after finitely many steps and stays there.

At the critical radius
\[
\eta=2\theta,
\]
global selection-robust finite termination fails: the admissible choices
\[
\theta\mapsto-\theta\mapsto\theta
\]
form an exact two-cycle.

For every supercritical radius
\[
\eta>2\theta,
\]
there is an open interval of unique two-cycles. Specifically, every
\[
c\in(\theta,\eta-\theta)
\]
satisfies
\[
c\mapsto c-\eta\mapsto c,
\]
and both subproblems on this cycle have unique minimizers.

Hence
\[
\eta<\frac{2\lambda}{a}
\]
is exactly the selection-robust global finite-termination region for this canonical strongly convex composite model.

## Assumptions and scope

The smooth part is
\[
f(x)=\frac a2x^2,
\]
the regularizer is
\[
r(x)=\lambda|x|,
\]
and \(\phi=f+r\) is \(a\)-strongly convex with unique minimizer \(0\). The update is solved exactly with a constant Euclidean trust radius. No stochastic error, momentum, changing radius, or approximate subproblem solve is present.

The statement concerns the linearized-ball trust-region gradient method, not the full-objective ball-proximal oracle. The distinction is essential because the latter minimizes \(\phi\) itself over each ball, whereas the method here minimizes only
\[
f(x_k)+f'(x_k)(z-x_k)+r(z),
\]
up to an irrelevant constant.

## Proof

Dividing the subproblem objective by the positive number \(a\), define
\[
T_\eta(x)
=
\arg\min_{|z-x|\le\eta}
\left\{xz+\theta|z|\right\}.
\]
The objective is piecewise linear in \(z\). On \(z<0\) its slope is \(x-\theta\), and on \(z>0\) its slope is \(x+\theta\).

If \(x>\theta\), both slopes are positive, so the unique minimizer is the left endpoint:
\[
T_\eta(x)=\{x-\eta\}.
\]
If \(x<-\theta\), both slopes are negative, so the unique minimizer is the right endpoint:
\[
T_\eta(x)=\{x+\eta\}.
\]

If \(|x|<\theta\), the slopes have opposite signs and the unconstrained minimizer is \(0\). Therefore
\[
T_\eta(x)=
\begin{cases}
\{0\}, & |x|\le\eta,\\
\{x-\eta\,\operatorname{sgn}(x)\}, & |x|>\eta.
\end{cases}
\]

At the two threshold points, direct slope inspection gives
\[
T_\eta(\theta)=
\begin{cases}
\{\theta-\eta\}, & \eta\le\theta,\\
[\theta-\eta,0], & \eta>\theta,
\end{cases}
\]
and symmetrically
\[
T_\eta(-\theta)=
\begin{cases}
\{-\theta+\eta\}, & \eta\le\theta,\\
[0,-\theta+\eta], & \eta>\theta.
\end{cases}
\]

Now suppose \(0<\eta<2\theta\). Starting from \(x>\theta\), repeated unique updates subtract \(\eta\) until the first iterate enters
\[
(\theta-\eta,\theta].
\]
Because \(\eta<2\theta\),
\[
\theta-\eta>-\theta,
\]
so this first crossing lies in \((-\theta,\theta]\). The same argument holds symmetrically from \(x<-\theta\).

Once \(|x|<\theta\), every nonzero singleton step moves toward \(0\) by exactly \(\eta\), and whenever \(|x|\le\eta\) the next iterate is \(0\). If \(x=\theta\) or \(x=-\theta\), every possible threshold choice under \(\eta<2\theta\) lies strictly inside \((-\theta,\theta)\), except in the subcase \(\eta\le\theta\) where the unique step already moves toward the origin. Hence every admissible trajectory reaches \(0\) in finitely many steps.

At \(\eta=2\theta\),
\[
T_\eta(\theta)=[-\theta,0],
\qquad
T_\eta(-\theta)=[0,\theta].
\]
Choosing the opposite endpoint at each step gives
\[
\theta\mapsto-\theta\mapsto\theta,
\]
so universal finite termination fails exactly at the boundary.

Finally let \(\eta>2\theta\) and choose
\[
c\in(\theta,\eta-\theta).
\]
Since \(c>\theta\), the first subproblem has the unique minimizer
\[
c-\eta.
\]
The upper bound \(c<\eta-\theta\) implies
\[
c-\eta<-\theta,
\]
so the next subproblem also has a unique minimizer and returns
\[
(c-\eta)+\eta=c.
\]
Thus the supercritical regime contains an open band of unique exact two-cycles.

## Verification

The standalone script `artifacts/verify_trgm_l1_phase.py` uses exact rational arithmetic. It checks the complete piecewise minimizer map, exhaustive representative branching at the two set-valued threshold states, finite absorption for several subcritical radii and starts, the critical selector-induced cycle, and supercritical unique cycles.

Those computations are consistency checks only. The quantified all-parameter statement follows from the slope classification and interval argument in the proof.

## Relationship to prior work

The 2026 heavy-tailed min-max paper formulates the same composite trust-region gradient subproblem, proves existence and a normalized-step representation, and notes that nonuniqueness can arise when the linearized composite stationarity condition vanishes at a minimizer. It does not give a constant-radius phase portrait on a strongly convex composite objective.

Kovalev's 2025 trust-region gradient paper introduces the broader composite method and proves a generic best-iterate stationarity bound with an additive term proportional to the fixed radius. It does not state the sharp radius threshold, the critical selector-induced cycle, or the open family of unique supercritical two-cycles above.

The distinction from the ball-proximal method is qualitative. The ball-proximal oracle minimizes the full convex objective over the ball and has finite exact termination for arbitrary positive fixed radii. Here the smooth term is first-order linearized, and that approximation creates the exact boundary
\[
\eta=\frac{2\lambda}{a}
\]
between selection-robust finite termination and possible cycling.

Targeted database searches for composite trust-region gradient descent, the scalar quadratic-plus-absolute-value model, fixed-radius cycling, and the sharp threshold returned no equivalent statement. The closest trust-region record concerns classical Cauchy-point decrease on smooth quadratic models rather than this composite linearized-ball recurrence.

## Limitations

The result is one-dimensional and uses the canonical quadratic-plus-\(\ell_1\) composite objective. It does not classify multidimensional sparse quadratics, non-Euclidean trust regions, stochastic momentum variants, or variable-radius schedules.

At the critical radius the nonconvergence example depends on an admissible tie choice because the subproblem is set-valued. Above the critical radius the displayed two-cycles are stronger: both subproblems are singletons, so no tie-breaking convention can remove those cycles on the stated open interval.

## References

1. T. Zhu, Y. Xu, X. Ji, *The Role of Gradient Modification in Heavy-Tailed Nonconvex Stochastic Min-Max Optimization*, arXiv:2609.06064v1, 2026.
2. D. Kovalev, *Understanding Gradient Orthogonalization for Deep Learning via Non-Euclidean Trust-Region Optimization*, arXiv:2503.12645v2, 2025.
3. K. Gruntkowska, H. Li, A. Rane, P. Richtárik, *The Ball-Proximal Point Method: a New Algorithm, Convergence Theory, and Applications*, arXiv:2502.02002v2, 2025.
