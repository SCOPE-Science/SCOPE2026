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

# Verification evidence
Run `python3 verify_etd1_complete_graph.py` using Python 3 standard library. The checker prints `VERIFICATION_OK 32817` on successful completion. It verifies the positive semigroup coefficients, their row sums, maximizing vectors, threshold roots across dimensions and mixing rates, selected global and limiting checks, and comparison with sampled admissible vectors. The exact mathematical statements rely on the analytic proof in `RESULT.md`; this finite checker cannot prove all-parameter uniqueness or asymptotic correctness. No independent scientific audit has been performed.
