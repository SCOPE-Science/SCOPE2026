# Inactive-scenario obstruction and automatic model-decrement bounds in robust steepest descent
## Finding

Consider a robust counterpart with one decision variable, one objective, and two uncertainty scenarios. For any
\[
M>0,
\]
define
\[
f_1(x)=x,
\qquad
f_2(x)=-(M+2)-Mx,
\]
and
\[
\Phi(x)=\max\{f_1(x),f_2(x)\}.
\]

At
\[
x=0,
\]
only the first scenario is active because
\[
f_1(0)=0,
\qquad
f_2(0)=-(M+2)<0.
\]

The steepest-descent subproblem used in the source is
\[
\min_{v\in\mathbb R}
\left\{
\max\left(v,-(M+2)-Mv\right)
+\frac12v^2
\right\}.
\]
Its unique minimizer is
\[
v=-1,
\]
with optimal value
\[
\theta=-\frac12.
\]
The robust directional derivative is
\[
\Phi'(0;-1)=-1<0.
\]

However, the two raw scenario-gradient products are
\[
\nabla f_1(0)^{\mathsf T}v=-1,
\qquad
\nabla f_2(0)^{\mathsf T}v=M,
\]
so
\[
\max_i \nabla f_i(0)^{\mathsf T}v=M>0.
\]
Thus no positive constant \(c\) can make
\[
\max_i \nabla f_i(0)^{\mathsf T}v
\le
-c|\theta|
\]
hold. The violation can be arbitrarily large as \(M\) grows.

Therefore the all-scenario raw-gradient condition in Assumption 4.1(15) is not an automatic consequence of solving the exact steepest-descent subproblem, and the corresponding Step 2 prescription is not universally executable on the stated finite-uncertainty problem class.

The exact subproblem nevertheless provides intrinsic bounds that use the correct max-model. For the general source model, define
\[
\Phi_j^*(x,v)
=
\max_i\left\{
f_j(x,\xi_i)+\nabla f_j(x,\xi_i)^{\mathsf T}v
\right\}
-\Phi_j(x)
\]
and
\[
\Psi_x(v)=\max_j\Phi_j^*(x,v).
\]
If \(v\) is the exact minimizer of
\[
\Psi_x(v)+\frac12\|v\|^2
\]
at a noncritical point, with optimal value
\[
\theta<0,
\]
then
\[
\Phi_j^*(x,v)\le-|\theta|
\]
for every objective \(j\), and
\[
\|v\|^2\le2|\theta|.
\]
For every active scenario \(i\in J_j(x)\), this implies
\[
\nabla f_j(x,\xi_i)^{\mathsf T}v
\le
-|\theta|
<
0.
\]

## Assumptions and scope

The two scenario functions in the counterexample are affine, hence convex, continuously differentiable, and upper uniformly differentiable. The uncertainty set is finite. The robust objective is convex and bounded below.

The finding concerns the all-scenario raw-gradient inequality in Assumption 4.1(15). It does not depend on the separate norm display in that assumption.

The source convergence theorem is conditional on Assumption 4.1. The result does not contradict a theorem once the assumption is imposed. It shows that the exact subproblem direction need not satisfy the assumption, even on an elementary admissible problem.

The replacement bounds are proved for exact subproblem minimizers. No claim is made for inexact subproblem solves or for a complete revised convergence theorem.

## Proof

Let
\[
a=-\frac{M+2}{M+1}.
\]
Then
\[
a=-1-\frac1{M+1}<-1.
\]
The two affine branches in the max-model intersect at \(v=a\).

For
\[
v\ge a,
\]
the first branch dominates and the subproblem objective equals
\[
F(v)=v+\frac12v^2.
\]
Its unique minimizer is
\[
v=-1,
\]
which lies in this branch, with value
\[
F(-1)=-\frac12.
\]

For
\[
v\le a,
\]
the second branch dominates and
\[
F(v)=-(M+2)-Mv+\frac12v^2.
\]
Its derivative is
\[
F'(v)=v-M<0
\]
on that half-line, so the minimum there is attained at the right endpoint \(a\). At the intersection,
\[
F(a)-F(-1)
=
\frac12(a+1)^2
=
\frac{1}{2(M+1)^2}
>
0.
\]
Hence the global minimizer is uniquely \(v=-1\) and \(\theta=-1/2\).

At \(x=0\), only \(f_1\) is active, so
\[
\Phi'(0;v)=\nabla f_1(0)^{\mathsf T}v=v.
\]
Thus
\[
\Phi'(0;-1)=-1<0.
\]
But
\[
\nabla f_1(0)=1,
\qquad
\nabla f_2(0)=-M,
\]
and therefore
\[
\max_i\nabla f_i(0)^{\mathsf T}(-1)
=
\max\{-1,M\}
=
M>0.
\]
This cannot be bounded above by a negative multiple of \(|\theta|\).

For the general replacement, write
\[
G(w)=\Psi_x(w)+\frac12\|w\|^2.
\]
Because every objective has at least one active scenario,
\[
\Psi_x(0)=0.
\]
Let \(v\) minimize \(G\). Convex first-order optimality gives
\[
-v\in\partial\Psi_x(v).
\]
The subgradient inequality between \(v\) and \(0\) gives
\[
0=\Psi_x(0)
\ge
\Psi_x(v)+(-v)^{\mathsf T}(0-v)
=
\Psi_x(v)+\|v\|^2.
\]
Hence
\[
\Psi_x(v)\le-\|v\|^2.
\]
Since
\[
\theta
=
\Psi_x(v)+\frac12\|v\|^2,
\]
we obtain
\[
\theta\le-\frac12\|v\|^2,
\]
and therefore
\[
\|v\|^2\le2|\theta|.
\]

For each objective,
\[
\Phi_j^*(x,v)
\le
\Psi_x(v)
=
\theta-\frac12\|v\|^2
\le
\theta
=
-|\theta|.
\]
If \(i\in J_j(x)\) is active, then
\[
f_j(x,\xi_i)-\Phi_j(x)=0.
\]
The corresponding affine term is bounded above by the maximum defining \(\Phi_j^*(x,v)\), so
\[
\nabla f_j(x,\xi_i)^{\mathsf T}v
\le
\Phi_j^*(x,v)
\le
-|\theta|
<
0.
\]
This proves the replacement.

## Verification

The standalone script `artifacts/verify_inactive_scenario.py` uses symbolic and exact rational arithmetic. It verifies the branch intersection, unique minimizer, exact optimal value, strict active-scenario descent, and positive inactive-scenario raw-gradient obstruction for the parameterized affine family.

The general replacement bounds are proved analytically above from convex subgradient optimality. The computation is supporting evidence only and is not used as an exhaustive proof.

## Relationship to prior work

The 2026 primary source introduces max-type and average-type non-monotone steepest-descent methods for objective-wise worst-case robust counterparts. Its Assumption 4.1 places a negative bound on the maximum of all scenario gradients along the computed direction, and both algorithms ask for the exact subproblem direction satisfying that condition.

The 2024 monotone predecessor uses the same robust max-model subproblem and defines robust descent through active scenarios. It does not state the inactive-scenario obstruction above and does not derive the exact replacement bounds
\[
\Phi_j^*(x,v)\le-|\theta|,
\qquad
\|v\|^2\le2|\theta|.
\]

The 2025 global-convergence follow-up likewise characterizes robust descent through active scenarios, not all scenarios.

A 2026 non-monotone Newton method in the same robust-counterpart setting formulates its auxiliary assumptions directly through a Newton model value rather than an all-scenario raw-gradient maximum. It does not imply this steepest-descent counterexample or the exact steepest max-model inequalities.

Targeted searches using the primary article identifier, the assumption number, active and inactive scenario terminology, model-decrement terminology, and equivalent max-objective formulations did not locate a published correction or an equivalent counterexample.

## Limitations

The counterexample addresses one admissible noncritical point and the exact direction generated by the source subproblem. It does not show that implementations which omit Assumption 4.1 necessarily fail in practice.

The replacement bounds concern exact subproblem minimizers. Extending them with sharp constants to inexact solves requires additional error control.

The result identifies the obstruction and a mathematically natural substitute; it does not provide a complete revised proof of global convergence for both non-monotone algorithms.

## References

1. S. Kumar, M. Pant, *Non-monotone steepest descent algorithms for robust counterparts of uncertain multiobjective problems*, Optimization, published online 29 June 2026. DOI: 10.1080/02331934.2026.2692698.
2. S. Kumar, M. A. T. Ansary, N. K. Mahato, D. Ghosh, *Steepest descent method for uncertain multiobjective optimization problems under finite uncertainty set*, Applicable Analysis 104(7), 1163--1184. DOI: 10.1080/00036811.2024.2426219.
3. S. Kumar, N. K. Mahato, D. Ghosh, *Global Convergence and Rate Analysis of the Steepest Descent Method for Uncertain Multiobjective Optimization via a Robust Optimization Approach*, arXiv:2503.06476v1, 9 March 2025.
4. S. Kumar, *Hybrid Newton's descent method with nonmonotone line search for robust multiobjective problems*, Numerical Algorithms, published online 24 April 2026. DOI: 10.1007/s11075-026-02381-0.
