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

# Reproducibility and verification

Run `python3 check_circle.py` with Python 3 and NumPy. It checks the rational equivalence of the conditional-probability and polynomial covariance formulas across a grid, checks the rational sign classification on another grid, verifies three exact boundary zeros, and independently compares direct simulated circle graphs with the formula. The tested direct-coordinate simulation uses a fixed deterministic seed and does not assume conditional independence beyond the sampled point coordinates.

Observed successful replay: `EXACT_TESTS 15252`; five simulation comparisons for sample sizes 6 and 9; final line `ALL_CHECKS_PASS`. The tests provide finite corroboration only. The universal finite-sample formulas, the uniqueness of both sign thresholds, the minimal size six, and the sparse limit rely on the complete analytic proof in `RESULT.md`. No independent audit is claimed.
