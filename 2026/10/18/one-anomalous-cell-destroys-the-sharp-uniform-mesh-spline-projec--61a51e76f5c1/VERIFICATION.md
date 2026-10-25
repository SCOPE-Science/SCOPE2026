---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every fixed tau>0, the piecewise-linear L² spline mass matrix gives Jacobi Q=6M with diagonal 4 except nodes 0,1, where it is 2(1+tau), and off-diagonal 1 except the exceptional edge tau. Conjugation by alternating signs gives a positive exponentially decaying Green inverse, with r=2-sqrt(3). Independently checked the two explicitly proposed Green rows against the junction equations and their factored absolute-integral identities symbolically in Q(sqrt(3)); direct independent evaluations give L_0(1/2)-2≈0.04824942>0, L_{-1}(2)-2≈0.04514007>0. For 0<tau<1 the former has numerator 3tau(1-tau²); for tau>1 the latter has (tau²-1), with every other factor positive. At tau=1 translation-invariant Green rows yield all knot Lebesgue values 2, and convexity bounds between knots, proving iff. Does NOT claim the exact nonunit global norm or maximizing knot.

## originality

PASS

Nonstandard one-defect infinite cardinal-grid spline projection rigidity and opposite-side explicit witnesses; older Franklin kernel calculations and uniform grid results supply methods but their fixed domains/conclusions do not state or imply the strict arbitrary tau threshold. Search is best-of-knowledge, not priority certificate.

## value

PASS

Local mesh perturbations are a natural stability question for L² spline projection: even one exceptional cell destroys the exact uniform L∞ threshold. Opposite witness locations for shorter vs longer perturbations are a motivated structural boundary rather than a routine uniform-grid substitution; explicit nonstandard Green-row formulas are useful for mesh sensitivity and stability analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
