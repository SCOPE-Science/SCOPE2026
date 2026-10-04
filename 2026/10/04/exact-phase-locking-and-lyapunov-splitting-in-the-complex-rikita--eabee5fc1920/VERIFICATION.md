---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Starting from the published complex equations, expand \(x=x_1+ix_2\) and \(y=x_3+ix_4\). The relative-phase defect is
\[
J=x_1x_4-x_2x_3.
\]
Substitution of the five real differential equations into \(\dot J\) cancels all \(z\)- and \(\alpha\)-terms and leaves exactly
\[
\dot J=-2\beta J.
\]
This algebraic identity is the only nontrivial calculation needed for the phase-locking theorem.

For a bounded complete solution, \(J(t_0)\ne0\) would imply exponential growth as \(t\to-\infty\), so \(J\equiv0\). If \(x=y=0\) at any time, uniqueness forces the complex coordinates to remain zero while \(z\) evolves linearly, contradicting bounded completeness. Hence a fixed common phase is well-defined modulo \(\pi\) and is preserved by uniqueness.

On the corresponding real slice, normal perturbations satisfy
\[
\dot u=-\beta u+Zv,\qquad
\dot v=(Z-\alpha)u-\beta v.
\]
The symmetry mode \((u,v)=(X,Y)\) is an exact solution. Compact recurrence keeps its norm between positive finite bounds, so its Lyapunov exponent is \(0\). The normal trace is \(-2\beta\); Liouville's determinant formula therefore fixes the other exponent at \(-2\beta\).

The published parameter value \(\beta=2\) gives exact normal exponents \(0\) and \(-4\). The displayed initial condition gives \(J(0)=-17\), hence \(J(t)=-17e^{-4t}\). These substitutions are exact and are not evidence for the general theorem; they are checks of its specialization.

Limits: no claim is made that a generic forward transient with nonzero \(J(0)\) reaches a real slice at finite time. The Lyapunov-spectrum conclusion is scoped to compactly supported ergodic invariant measures so that the cocycle hypotheses and the bounded-away-from-zero symmetry mode are explicit.
