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

# Reproducibility and boundaries

Run `python check_sparse_modal_repair.py` with Python 3 standard library. The completed exhaustive run reports `SPARSE_MODAL_REPAIR_FINITE_OK 16656 frame_formulas 264256 valuations 1072 repair_counts`. It checks loop-free directed frames of sizes two to four, four parameter pairs and all valuations, with exhaustive enumeration of deletion sets on the isolated-path cases. It does not calculate infinite probabilities or replace the analytical proof. The asymptotic factorial moments, vanishing overlap and incident-arc bounds, and variance estimates are reconstructed in RESULT.md. No independent scientific audit has been performed.
