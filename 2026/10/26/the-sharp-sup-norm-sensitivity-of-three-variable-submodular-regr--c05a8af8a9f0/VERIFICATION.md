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
# Verification record

The embedded `check.py` uses only Python standard-library rational arithmetic. It was executed from its packaged source path and reported success. It constructs the six elementary constraints, verifies rank four and the two exact row relations, checks twenty-two feasible equality patterns among sixty-four candidates, computes all their exact Gram-matrix row projectors, and confirms all seven class-table cases and exactly five norms equal to \(7/4\). It separately checks an attainable extremizing face and the two-element norm \(3/2\).

The complete mathematical claim also depends on a standard piecewise-affine nearest-point projection theorem and the explicit constructive classification of active faces, each explained in `RESULT.md`. The code does not constitute an independent audit or a proof for any larger ground set. Source priority remains provisional.
