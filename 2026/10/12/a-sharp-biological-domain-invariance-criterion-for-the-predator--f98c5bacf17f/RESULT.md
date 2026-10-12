# A sharp biological-domain invariance criterion for the predator-dependent refuge model

## Finding

Consider
\[
\begin{aligned}
N'&=
N\left[
r_1\left(m+\frac{n(1-m)}{n+P}\right)-d-bN
-\frac{a(1-\delta P)P}{c+N(1-\delta P)+eP}
-q_1EN
\right],\\
P'&=
P\left[
r_2\left(1-\frac{eP}{K+N(1-\delta P)}\right)
-q_2EP
\right].
\end{aligned}
\]

The source introduces the refuge amount
\[
\delta NP
\]
and explicitly requires
\[
0\le1-\delta P\le1
\]
so that the remaining vulnerable prey quantity is biologically meaningful. The corresponding natural state domain is
\[
\Omega_\delta
=
\left\{
(N,P):
N\ge0,\ 0\le P\le\frac1\delta
\right\}.
\]

The vector field is not continuously differentiable on the entire nonnegative quadrant, contrary to the proof of the source's positive-invariance theorem. For every
\[
P>\frac1\delta,
\]
the predator denominator
\[
K+N(1-\delta P)
\]
vanishes at
\[
N=\frac{K}{\delta P-1}>0,
\]
and the prey denominator
\[
c+N(1-\delta P)+eP
\]
vanishes at
\[
N=\frac{c+eP}{\delta P-1}>0.
\]

On the biologically meaningful strip, both denominators are strictly positive, and the exact forward-invariance criterion is
\[
\boxed{
\delta
\le
\frac eK+\frac{q_2E}{r_2}
}.
\]
This condition is necessary and sufficient.

For the source's numerical Dataset (24),
\[
\delta=0.05,
\qquad
\frac eK+\frac{q_2E}{r_2}=0.25,
\]
so the baseline numerical parameter set satisfies the repaired condition.

The condition is not automatic under the paper's stated parameter assumptions. For the exact positive parameter choice
\[
r_1=2,\quad
m=\frac12,\quad
n=1,\quad
d=\frac1{20},\quad
b=\frac1{10},\quad
a=\frac34,\quad
c=2,\quad
e=\frac1{10},
\]
\[
\delta=\frac15,\quad
q_1=\frac1{10},\quad
q_2=\frac1{10},\quad
E=\frac1{10},\quad
r_2=1,\quad
K=2,
\]
one has
\[
\frac eK+\frac{q_2E}{r_2}
=
\frac3{50}
<
\frac15
=
\delta.
\]
At
\[
(N,P)=(1,5),
\]
which lies on the intended biological boundary, the denominators remain positive but
\[
P'=\frac72>0.
\]
Hence the vector field points immediately out of the refuge strip.

## Assumptions and scope

All rate and saturation parameters used in denominators are positive, and
\[
0<\delta<1.
\]
The refuge interpretation is the one printed by the source: \(\delta NP\) prey are sheltered, so \(N(1-\delta P)\) prey remain vulnerable.

The criterion concerns the natural refuge-valid strip \(\Omega_\delta\). It does not claim that trajectories which leave this strip must subsequently hit a singular curve.

The finding corrects the state-space and positive-invariance claim. It does not re-evaluate the source's later equilibrium, bifurcation, or global-stability calculations when those calculations remain inside a regular domain.

## Proof

Inside \(\Omega_\delta\),
\[
1-\delta P\ge0.
\]
Therefore
\[
K+N(1-\delta P)\ge K>0
\]
and
\[
c+N(1-\delta P)+eP\ge c>0.
\]
The vector field is consequently continuously differentiable on an open neighborhood of every point of the strip.

The coordinate axes are invariant because
\[
N'=Nf(N,P),
\qquad
P'=Pg(N,P).
\]
The only nontrivial boundary of the strip is
\[
P=\frac1\delta.
\]
Substitution into the predator equation gives
\[
\begin{aligned}
P'
&=
\frac1\delta
\left[
r_2\left(
1-\frac{e/\delta}{K}
\right)
-\frac{q_2E}{\delta}
\right]\\
&=
\frac{
\delta r_2-r_2e/K-q_2E
}{\delta^2}.
\end{aligned}
\]
Thus the vector field points inward or tangentially at every point of the upper boundary exactly when
\[
\delta r_2
\le
\frac{r_2e}{K}+q_2E,
\]
equivalently
\[
\delta
\le
\frac eK+\frac{q_2E}{r_2}.
\]
Standard uniqueness for locally Lipschitz ordinary differential equations then gives forward invariance. Necessity follows because if the inequality is reversed, every point of the upper boundary has \(P'>0\).

Solutions in the invariant strip are global. The predator coordinate is bounded by \(1/\delta\). Also, since
\[
m+\frac{n(1-m)}{n+P}\le1
\]
and the refuge-dependent predation term is nonnegative on the strip,
\[
N'
\le
N(r_1-bN).
\]
Hence \(N\) has a logistic upper bound and finite-time blow-up is impossible.

The whole nonnegative quadrant cannot be the regular state space of the printed vector field. If
\[
P>\frac1\delta,
\]
then \(1-\delta P<0\). Choosing
\[
N=\frac{K}{\delta P-1}
\]
makes the predator denominator zero, while choosing
\[
N=\frac{c+eP}{\delta P-1}
\]
makes the prey denominator zero. Both values of \(N\) are positive.

For the exact counterexample,
\[
\frac eK+\frac{q_2E}{r_2}
=
\frac1{20}+\frac1{100}
=
\frac3{50}
<
\frac15.
\]
At \(P=5=1/\delta\),
\[
P'
=
5\left(
1-\frac{(1/10)5}{2}
-\frac1{10}\frac1{10}5
\right)
=
\frac72.
\]
Thus the strip fails to be invariant.

## Verification

The bundled `verify.py` checks the boundary derivative, the sharp threshold, the exact counterexample, the source Dataset (24), and explicit singular points using symbolic or rational arithmetic.

For the counterexample it verifies
\[
\delta=\frac15,
\qquad
\frac eK+\frac{q_2E}{r_2}=\frac3{50},
\qquad
P'(1,5)=\frac72.
\]

For Dataset (24) it verifies
\[
\delta=\frac1{20}
<
\frac14
=
\frac eK+\frac{q_2E}{r_2},
\]
and the upper-boundary predator derivative is negative.

It also checks a point with \(P>1/\delta\) at which each printed denominator vanishes exactly.

## Relationship to prior work

Jamil and Naji explicitly motivate the refuge law by requiring
\[
0\le1-\delta P\le1,
\]
but their Theorem 1 then argues positive invariance of the entire nonnegative quadrant from a claim of continuous differentiability and exponential representations. The denominator singularities show that this whole-quadrant argument does not apply.

Earlier nonlinear-refuge literature treats predator-dependent refuge quantities together with explicit conditions such as
\[
0<1-my<1
\]
to keep the available-prey fraction meaningful. Mondal, Samanta, and Nieto discuss this restriction in their survey of predator-dependent refuge formulations before adopting a saturating refuge function.

Later discrete predator-prey work with fear and refuge cites the motivating article but uses a different discrete formulation. The inspected material does not state the sharp continuous-time strip criterion above or repair the motivating paper's Theorem 1.

The new contribution is therefore source-specific: it identifies the singular curves of the printed vector field, derives the exact necessary-and-sufficient refuge-strip invariance condition, and supplies both a failing admissible parameter set and a check that the source's baseline numerical data satisfy the repaired condition.

## Limitations

The repaired strip condition is a state-space result, not a new equilibrium or bifurcation theorem.

Failure of the strip condition proves loss of invariance, but it does not by itself determine the later fate of a trajectory after it exits the biologically meaningful refuge domain.

A non-indexed correction by the authors could exist outside the searched records.

## References

1. A. R. M. Jamil, R. K. Naji, “Modeling and Analysis of the Influence of Fear on the Harvested Modified Leslie–Gower Model Involving Nonlinear Prey Refuge,” Mathematics 10 (2022), 2857. DOI: 10.3390/math10162857.
2. S. Mondal, G. P. Samanta, J. J. Nieto, “Dynamics of a Predator-Prey Population in the Presence of Resource Subsidy under the Influence of Nonlinear Prey Refuge and Fear Effect,” Complexity 2021 (2021), 9963031. DOI: 10.1155/2021/9963031.
3. “Analysis of the Dynamical Properties of Discrete Predator-Prey Systems with Fear Effects and Refuges,” Discrete Dynamics in Nature and Society (2024), 9185585. DOI: 10.1155/2024/9185585.
