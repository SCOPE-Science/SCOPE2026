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

The model has exactly \(2d+1\) accessible spatial states at the boundary, and the one-step conditional transition laws are rational in the counts. Run `python3 verify.py` to enumerate finite feasible state counts and check both normalization and the exact centered neighbor-ratio drift. The completed run returned `EXACT_CONDITIONAL_IDENTITIES_OK 3990`.

This checks the discrete algebra, not the limiting theorem. The almost-sure statements use the martingale-convergence, telescoping and conditioning arguments in RESULT.md. No independent mathematical audit has been performed.
