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

# Verification details

Run `python checks/checker.py` using a Python 3 standard-library interpreter. The exact reference stdout is stored in `checks/verification_output.txt`.

The checker enumerates complete random-to-top selection histories and the independently specified selected-set/uniform-prefix representation for small deck sizes. It compares the resulting joint distributions of moved-card count, total and prefix fixed-point count, unmoved suffix, internal descents and total descents. It also verifies hypergeometric formulas, exact geometric-suffix probabilities, Eulerian descent invariance for arbitrary selected sets, the conditional fixed-point/descent covariance, and the exceptional boundary probability.

The checks use exact integers and rational arithmetic, not statistical tests. They verify finite equations and expose implementation mistakes but do not prove the asymptotic joint limit, its independence structure, or the unscaled covariance limit. Those follow from the factorial-moment/deletion proof, the occupancy central limit theorem, and the covariance Taylor expansion in RESULT.md. The broader historical originality assertion is not independently certified.
