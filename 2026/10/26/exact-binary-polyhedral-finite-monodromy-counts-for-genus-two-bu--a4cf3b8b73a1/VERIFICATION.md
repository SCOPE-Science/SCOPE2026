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

## Executed checks

From the final embedded `verify_finite_monodromy.py`, invoke `python3 verify_finite_monodromy.py` using Python 3 standard library. The verifier builds the two finite groups, validates order and center, closes and enumerates all subgroups, counts commutators on each, evaluates the exact recursive epimorphism formula and independently evaluates subgroup Möbius inversion. The whole-group homomorphism totals are checked a second way using the Frobenius–Mednykh character-degree formula. Expected successful marker: `VERIFY_OK two_exact_finite_group_models_subgroup_mobius_frobenius_genus2_bundle_counts`.

The mathematical reduction to stable bundles and the self-normalizing-subgroup statement are proved in `RESULT.md`, not delegated to a finite-group program. There are no randomized trials or heuristic rounding steps. This arithmetic replay is not an independent external audit.
