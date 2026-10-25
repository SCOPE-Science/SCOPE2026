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

Run `python verify.py` under Python 3 without third-party packages. The program numerically solves the unique monotone root for selected link counts; reconstructs consecutive tangent-line intersections independently of the objective formula; confirms that the disk lies inside their tangent half-planes; checks actual polyline length, the radical special cases for two and three links, angle normalization and stationarity; and samples the scaled excess against \(\pi^3/12\). Outputs are finite sanity checks, not exhaustive search or proofs of uniqueness/for-all-\(k\) or an infinite limit. Those follow from the analytic derivation in RESULT.md. The exact comparison with all related literature remains subject to the access limitation described in REVIEW.md. No independent audit has been performed.
