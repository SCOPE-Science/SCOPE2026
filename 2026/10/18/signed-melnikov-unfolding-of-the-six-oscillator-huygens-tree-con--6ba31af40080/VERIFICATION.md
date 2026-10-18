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

# Verification notes

Run `python3 verify.py` from the directory containing this file. The verifier is self-contained, uses only standard Python, and checks exact edge-matrix reduction relations and numerical scalar-orbit Green-series implementations at three independent fixed step sizes. The proof in `RESULT.md` is the basis for the infinite, parameter-uniform theorem. Truncated series and floating-point checks do not certify the infinite statement.

The critical independent analytic checks are: endpoint multipliers \(1+2h,1-h\) and \(1-2h,1+h\); cancellation of the longitudinal variation in the normal recursion; geometric convergence of the positive series; smooth dependence of the stable/unstable intersections on central weight; and nonzero positive first-order separation. Limitations include lack of a globally uniform detuning radius and no full-dimensional transversality conclusion.
