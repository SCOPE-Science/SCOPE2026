# Review of Quadratic onset and quartic gain of anisotropy in sharp harmonic Jacobians

## Correctness

PASS. The source gives the exact smooth one-variable objective
\[
\Psi_n(s,r)=n\log L_{n,r}(e^s)-s
\]
with a unique minimizer.

At the center, the Hessian in the anisotropy variable is
\[
H_n
=
\frac{2(n-1)(n+1)}{n(n+2)}
>0.
\]
A direct second-order expansion of the source's Poisson-gradient formula gives
\[
\partial_s\Psi_n(0,r)
=
\frac{(n-2)(n-1)(3n+2)}
{n^3(n+2)}
r^2
+
O(r^4).
\]
The implicit-function theorem therefore gives the stated coefficient of
\[
q_n(r)-1.
\]

Strict convexity then gives the optimized objective improvement
\[
\frac{A_n^2}{2H_n}r^4+O(r^6),
\]
which simplifies to the claimed positive
\[
\delta_n.
\]

## Originality

PASS. The fresh source introduces
\[
q_n(r)
\]
and proves only the qualitative fact
\[
q_n(r)<1
\]
away from the origin. It does not give a small-radius expansion, a radial/tangential anisotropy coefficient, or the quartic determinant gain relative to the scalar trial.

Searches covering the exact source, the minimizer notation, quadratic anisotropy onset, small-radius Jacobian profile, and quartic isotropic-trial gap returned no implication-equivalent result.

Earlier harmonic Schwarz and planar Jacobian papers have different objects and do not contain the higher-dimensional radius-dependent minimizer introduced by the new paper.

## Value

PASS. Strict anisotropy is one of the main structural conclusions of the source's exact Jacobian theory. The accepted result identifies its local scale and shows a non-obvious separation of orders: the extremal shape becomes anisotropic at order
\[
r^2,
\]
but optimizing that anisotropy changes the determinant only at order
\[
r^4.
\]

This supplies a quantitative local model for the newly discovered extremal geometry and an exact benchmark for numerical or analytic approximations to the source's implicit minimizer.

Same-model review: passed. Independent audit: not yet performed.
