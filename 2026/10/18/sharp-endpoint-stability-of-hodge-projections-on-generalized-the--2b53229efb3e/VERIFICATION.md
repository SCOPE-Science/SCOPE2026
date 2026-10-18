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

The analytic proof reduces the circulation subspace to branchwise constants with one balancing constraint, derives every projection matrix row, and proves that a shortest branch maximizes the absolute gradient-row sum on a simple generalized-theta graph. The proof covers all integer path lengths with at most one unit-length arm and every number of arms \(r\ge2\).

Reproduction: run `python verify_theta.py` in the directory containing this file (NumPy and SymPy required). This checks 64 exact-rational incidence-matrix projections, 150 further numerical incidence-matrix projections, 1,064 exact equal-length specializations, and 84 high-contrast bound calculations. The finite calculations do not constitute a proof over infinite families. Literature priority remains provisional and a separate independent audit has not been performed.
