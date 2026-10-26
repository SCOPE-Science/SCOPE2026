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

# Reproducibility

Run `python verify.py` with a modern Python 3 interpreter. The script has no third-party dependencies and runs exact-rational tests for the threshold factorization and derivative, then compares the analytic eigenmode representation with direct recurrence calculations at several positive decay parameters. It checks strict positivity at the threshold for exact exponential starting data and tracks first-negative indices on six nearby supercritical parameters. The observed convergence of the products of distance and first-negative index is consistent with the proved limit.

The exact cubic discriminant, positive-history cone classification, proof that the exact starter excites nonreal modes, and irrational-rotation bounded-waiting argument are established analytically in `RESULT.md`. Finite checks cannot certify all parameters or arbitrarily large indices. No independent audit has been performed.
