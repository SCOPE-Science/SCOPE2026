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

## Analytical verification

The exact constrained minimizer is found from the first derivative of the unweighted strictly convex least-squares objective. An integral representation proves strict monotonicity and the range of its normalized coefficient. Explicit integration of the plant and normalized error gives two quadratic threshold equations. Differentiation shows the negative-error boundary has exactly one maximum and the positive-error boundary is strictly decreasing, giving a complete first-contact classification, including equality at grazing. Monotonicity of those roots proves the strict, unattained fitting-horizon supremum. The error-before-contact bound gives exact state contraction at each reset. All-parameter asymptotics follow from expansion of the critical radical and the positive-root equation.

## Reproduction

Run the standalone standard-library program `python3 verify.py`. It tests the defining equations, first-contact state sign and trigger equality, root ordering, 143100 strict pre-contact sample inequalities, and the critical parameter and one-sided jump at the source-compatible choice \(\sigma=1/2\), \(\theta=1/2\). The terminal marker begins `VERIFY_OK:`.

## Limits of verification

Finite grids only corroborate, and cannot establish, universal inequalities. The true infinite-quantifier conclusions rest on the preceding calculus and algebra. The computations do not validate event-detector implementations, floating-point grazing in hardware, discounted fitting, or mathematical originality against every unpublished or inaccessible source. No independent examination has been performed.
