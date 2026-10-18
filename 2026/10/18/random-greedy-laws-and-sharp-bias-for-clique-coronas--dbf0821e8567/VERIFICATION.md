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

Run `python verify_corona_greedy.py` with Python 3 and no third-party packages. The verifier constructs the stated graphs and enumerates literal vertex permutations independently of the analytic proof; all probability comparisons are exact rational arithmetic. Current output: PASS, 24 graph/size cases and 1,418,450 complete vertex permutations.

The unrestricted classification, candidate-coupling law, asymptotic coefficient, and unequal-block obstruction are proved symbolically in `RESULT.md`. Enumerations are finite cross-checks only. Independent audit has not been performed.
