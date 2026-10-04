# Epsilon sets a sharp first-step stability frontier in practical MADGRAD
## Finding

MADGRAD uses a cube-root adaptive denominator and an explicit numerical regularizer. On a smooth quadratic, the first practical update has an exact stability boundary controlled by that regularizer.

Consider Algorithm 1 of MADGRAD with zero initial accumulators,
\[
s_0=0,
\qquad
\nu_0=0,
\]
first learning-rate value
\[
\gamma>0,
\]
first averaging coefficient
\[
0<c\le1,
\]
and denominator regularizer
\[
\varepsilon>0.
\]
Let the objective be the axis-aligned positive-definite quadratic
\[
f(x)
=
\frac12
\sum_{i=1}^d
h_i x_i^2,
\qquad
0<h_i\le L.
\]

The first MADGRAD weight is
\[
\lambda_0=\gamma.
\]
Since
\[
g_{0,i}=h_i x_{0,i},
\]
the first accumulators are
\[
s_{1,i}
=
\gamma h_i x_{0,i},
\]
and
\[
\nu_{1,i}
=
\gamma h_i^2 x_{0,i}^2.
\]
The dual-averaging point is therefore
\[
z_{1,i}
=
x_{0,i}
-
\frac{
\gamma h_i x_{0,i}
}{
\gamma^{1/3}h_i^{2/3}|x_{0,i}|^{2/3}
+
\varepsilon
}.
\]
After MADGRAD's inline averaging,
\[
x_{1,i}
=
(1-c)x_{0,i}
+
c z_{1,i},
\]
so
\[
x_{1,i}
=
\left(
1-q_i(x_{0,i})
\right)x_{0,i},
\]
where
\[
q_i(u)
=
\frac{
c\gamma h_i
}{
\gamma^{1/3}h_i^{2/3}|u|^{2/3}
+
\varepsilon
}.
\]

For every finite nonzero \(u\),
\[
0<q_i(u)<\frac{c\gamma h_i}{\varepsilon},
\]
and
\[
\lim_{u\to0}q_i(u)
=
\frac{c\gamma h_i}{\varepsilon}.
\]

It follows that the exact uniform first-step objective-monotonicity frontier is
\[
c\gamma L
\le
2\varepsilon.
\]

If this inequality holds, then
\[
0<q_i(x_{0,i})<2
\]
for every active coordinate, so
\[
|x_{1,i}|<|x_{0,i}|
\]
and hence
\[
f(x_1)<f(x_0)
\]
for every nonzero initialization.

If
\[
c\gamma L>2\varepsilon,
\]
choose a coordinate with curvature \(L\). Along that coordinate, the first step increases the objective exactly when
\[
q(u)>2.
\]
Equivalently,
\[
0<|u|<r_\star,
\]
where
\[
r_\star
=
\left[
\frac{
c\gamma L/2-\varepsilon
}{
\gamma^{1/3}L^{2/3}
}
\right]^{3/2}.
\]
Thus the unstable set is not a large-gradient phenomenon. It is a punctured neighborhood of the minimizer.

The scalar objective ratio is
\[
\frac{f(x_1)}{f(x_0)}
=
\left(
1-q(x_0)
\right)^2.
\]
Therefore
\[
\lim_{x_0\to0}
\frac{f(x_1)}{f(x_0)}
=
\left(
\frac{c\gamma L}{\varepsilon}-1
\right)^2.
\]
Across all nonzero initializations and all coordinates, the exact supremal first-step factor is
\[
\sup_{x_0\ne0}
\frac{f(x_1)}{f(x_0)}
=
\max
\left\{
1,
\left(
\frac{c\gamma L}{\varepsilon}-1
\right)^2
\right\}.
\]

Equivalently, the practical first-step map has one-sided local derivative at the minimizer
\[
1-\frac{c\gamma h_i}{\varepsilon}
\]
in coordinate \(i\). The minimizer is first-step locally contractive in every coordinate exactly when
\[
c\gamma L<2\varepsilon.
\]

The important structural point is that the adaptive cube-root term does not furnish a nonzero startup stability scale near the minimizer:
\[
\nu_{1,i}^{1/3}
=
\gamma^{1/3}h_i^{2/3}|x_{0,i}|^{2/3}
\longrightarrow0
\]
as
\[
x_{0,i}\to0.
\]
At the first practical update, the only nonvanishing denominator scale is therefore
\[
\varepsilon.
\]

## Assumptions and scope

The calculation uses the practical Algorithm 1 recurrence in the defining MADGRAD paper:
\[
\lambda_k
=
\gamma_k\sqrt{k+1},
\]
\[
s_{k+1}
=
s_k+\lambda_k g_k,
\]
\[
\nu_{k+1}
=
\nu_k+\lambda_k(g_k\odot g_k),
\]
\[
z_{k+1}
=
x_0
-
\frac{s_{k+1}}
{\nu_{k+1}^{1/3}+\varepsilon},
\]
and
\[
x_{k+1}
=
(1-c_{k+1})x_k
+
c_{k+1}z_{k+1}.
\]

Only the first update is classified. Later iterations retain nonzero accumulated state and need not obey the same local formula.

The quadratic is diagonal in the optimizer coordinate system. This makes the first update separable and gives a sharp if-and-only-if objective frontier.

Weight decay and stochastic gradient noise are excluded.

The defining paper's convergence theorem analyzes a variant whose denominator includes an additional gradient-bound term. The paper explicitly says that term is omitted from the practical algorithm because its magnitude quickly diminishes. The theorem here concerns the practical recurrence without that extra term.

## Proof

For coordinate \(i\),
\[
g_{0,i}
=
h_i x_{0,i}.
\]
At
\[
k=0,
\]
MADGRAD has
\[
\lambda_0
=
\gamma\sqrt1
=
\gamma.
\]
Therefore
\[
s_{1,i}
=
\gamma h_i x_{0,i},
\]
and
\[
\nu_{1,i}
=
\gamma h_i^2x_{0,i}^2.
\]
Taking the real cube root of the nonnegative second-moment accumulator gives
\[
\nu_{1,i}^{1/3}
=
\gamma^{1/3}h_i^{2/3}|x_{0,i}|^{2/3}.
\]

Substitution into the practical dual point yields
\[
z_{1,i}
=
x_{0,i}
-
\frac{
\gamma h_i x_{0,i}
}{
\gamma^{1/3}h_i^{2/3}|x_{0,i}|^{2/3}
+
\varepsilon
}.
\]
The inline average then gives
\[
x_{1,i}
=
x_{0,i}
-
c
\frac{
\gamma h_i x_{0,i}
}{
\gamma^{1/3}h_i^{2/3}|x_{0,i}|^{2/3}
+
\varepsilon
},
\]
which is the displayed multiplier formula.

Because
\[
f(x)
=
\frac12\sum_i h_i x_i^2,
\]
uniform objective nonincrease is equivalent to requiring
\[
|1-q_i(u)|
\le1
\]
for every coordinate and every \(u\). Since \(q_i(u)>0\), this is equivalent to
\[
q_i(u)\le2.
\]
The function \(q_i(u)\) is strictly decreasing in \(|u|\) and has supremum
\[
\frac{c\gamma h_i}{\varepsilon}
\]
as \(u\to0\). Hence
\[
q_i(u)\le2
\]
for every coordinate and every initialization if and only if
\[
c\gamma h_i\le2\varepsilon
\]
for every \(i\), which is equivalent to
\[
c\gamma L\le2\varepsilon.
\]

When
\[
c\gamma L>2\varepsilon,
\]
the inequality
\[
q(u)>2
\]
is equivalent to
\[
\gamma^{1/3}L^{2/3}|u|^{2/3}
+
\varepsilon
<
\frac{c\gamma L}{2}.
\]
Solving gives the stated radius
\[
r_\star.
\]

Finally,
\[
(1-q)^2
\]
is a convex quadratic in \(q\). As \(|u|\) ranges from zero to infinity, \(q(u)\) ranges continuously from its limiting upper endpoint
\[
c\gamma h_i/\varepsilon
\]
down to zero. Hence the supremum of the objective ratio on coordinate \(i\) is
\[
\max
\left\{
1,
\left(
\frac{c\gamma h_i}{\varepsilon}-1
\right)^2
\right\}.
\]
This quantity is maximized at
\[
h_i=L,
\]
which proves the exact global first-step factor.

## Verification

The accompanying `verify.py` reconstructs Algorithm 1's first update directly and compares it with the closed form over randomized diagonal quadratics and parameter values.

It verifies the if-and-only-if frontier
\[
c\gamma L\le2\varepsilon,
\]
checks the exact spike radius when the frontier is violated, and confirms the limiting amplification factor numerically.

The finite calculations are transcription guards. The frontier, spike interval, and supremal factor are proved algebraically above.

## Relationship to prior work

Defazio and Jelassi introduced MADGRAD as a momentumized adaptive dual-averaging method. Their practical algorithm uses a cube-root accumulated squared-gradient denominator plus
\[
\varepsilon.
\]
The paper explains that the cube root is chosen to maintain the desired effective step-size scaling and recommends a constant averaging coefficient for nonconvex problems.

For the convergence proof, the same paper analyzes a modified denominator containing an additional gradient-bound term. It states that this extra term is important in the theory but is omitted from Algorithm 1 because its magnitude quickly diminishes in practice.

The defining paper proves convex convergence guarantees and discusses practical adaptivity, but it does not state the sharp first-step quadratic frontier
\[
c\gamma L=2\varepsilon,
\]
the exact near-minimizer spike radius, or the exact worst first-step amplification factor.

A later broad empirical study of first-order optimizers reports that MADGRAD can display mixed behavior with periodic loss explosions on Rosenbrock-type problems and high sensitivity to hyperparameter choice. That observation is not an implication-equivalent result: it concerns longer nonlinear trajectories, while the present theorem isolates a separate exact startup mechanism on a diagonal quadratic.

Focused published-record searches for MADGRAD quadratic startup stability, epsilon-controlled local Jacobians, cube-root-denominator overshoot, and equivalent first-step frontiers did not locate a stronger or equivalent statement.

## Limitations

The theorem concerns one update, not asymptotic convergence.

The exact multidimensional if-and-only-if statement assumes that the Hessian is diagonal in the optimizer coordinate system.

The instability mechanism is deterministic and does not model stochastic gradient noise.

The theoretical MADGRAD variant with the extra gradient-bound denominator term has a different startup scale and is not covered by the practical-algorithm formula here.

A first-step objective increase does not imply eventual divergence. It is a sharp local stability diagnostic for the practical update.

## References

1. Aaron Defazio and Samy Jelassi, “Adaptivity without Compromise: A Momentumized, Adaptive, Dual Averaged Gradient Method for Stochastic Optimization,” arXiv:2101.11075v1, 2021; Journal of Machine Learning Research 23(144), 2022.
2. “First-order optimization algorithms: state of the art, classification, and performance: a practitioner’s guide,” Neural Computing and Applications, 2026, DOI 10.1007/s00521-026-12014-1.
