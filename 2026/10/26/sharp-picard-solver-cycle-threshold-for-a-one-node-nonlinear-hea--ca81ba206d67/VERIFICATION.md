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

The complete proof is in `RESULT.md`. Execute `python verify.py` with SymPy available. Checks include exact symbolic identities for the two-step map, the critical Taylor jet, two-cycle roots and multiplier, and reproducible finite numerical trajectories. Finite trajectory checks illustrate rather than prove the global convergence assertions. The original 2026 manuscript was inspected in full in its arXiv HTML representation, section 4; a rational-map identity with an equivalent statement in other literature cannot be categorically excluded. The verified mathematical scope is a particular one-node centered-flux specialization, not a replication of the source's large-grid solver implementation. Independent audit has not been performed.
