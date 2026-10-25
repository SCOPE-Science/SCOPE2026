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

# Reproducible verification

Run `python verify.py` with Python 3.10 or later (no third-party packages). The checker enumerates all labeled connected simple graphs on four, five and six vertices and every nontrivial particle count. It compares the exact constant-boundary condition against the claimed graph classes. It also independently constructs nine configuration-space generators, solves their Poisson equations in exact rational arithmetic and confirms the strict/non-strict Fano classification.

The observed exact Fano values include \(1\), \(26/25\), \(7/6\), \(19/15\), \(53/50\), and \(22/15\), with each graph and occupancy printed by the script. These tests provide finite corroboration, not an all-graph proof. The published proof is the tilted-generator perturbation and the adjacency-row rigidity argument in RESULT.md. No independent scientific review or proof certification has been conducted.
