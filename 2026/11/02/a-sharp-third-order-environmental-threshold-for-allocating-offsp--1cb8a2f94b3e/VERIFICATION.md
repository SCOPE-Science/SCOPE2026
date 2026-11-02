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

# Verification of the mathematical statement

The accompanying `checker.py` is a reproducible, standard-library finite checker. It enumerates the 4 even-parity and 4 odd-parity binary environmental states, verifies their one- and two-coordinate moments, calculates exact rational derivatives by direct state sums, and compares these values against the analytic threshold formulas. It also checks negative curvature at a finite rational grid and the explicit \(a=2\), \(b=3/2\), \(t=1/3\) boundary and odd-parity maximizer.

Run with `python3 checker.py`. The script supplies finite cross-checks only. The infinite theorem depends on the moment-fiber enumeration, strict negative Hessian in tangent directions, symmetry of the unique maximizer, and the exact derivative signs as shown in `RESULT.md`. No computer search over finite parameters substitutes for these analytical steps.

The literature comparison establishes compatibility and distinct scope relative to the inspected sources; it is not an independent claim of priority. No external scientific audit or empirical validation is asserted.
