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

The analytical proof establishes all dimensions and parameters by finite simplex and pyramid volume integrations followed by a strict monotonicity calculation and factorial induction. The executable `verify.py` uses only Python's standard library and checks exact rational instances, dimension-dependent endpoint inequalities, and exhaustive cross-polytope facet visibility in dimensions three through nine. It does not certify the infinitely many dimensions or continuum of cut depths by enumeration; those are proved in `RESULT.md`.

A separate numerical geometry check computed convex hulls of the \(2d+2\) polar candidate vertices in dimensions three, four, and five, at truncation depths \(0.37\), \(1\), \(1.83\), and \(2\), and agreed with the analytic polar volume to displayed numerical precision. No independent scientific audit has been performed.
