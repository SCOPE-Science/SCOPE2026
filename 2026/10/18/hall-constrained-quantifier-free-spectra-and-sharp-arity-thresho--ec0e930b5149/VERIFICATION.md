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

## Reproducible computations

Run `python3 verify_qf_types.py` with a standard Python 3 interpreter. The verification uses `fractions.Fraction`, exact Stirling recurrences, integer factorials, and independently enumerated equality partitions of tuple terms and their images.

Successful output includes `VERIFY_OK instances= 197 evaluated_tuple_assignments= 21570` and `SHARP_THRESHOLD_OK pairs= 2249`. Enumerated instances include all root-capacity partitions with total carrier size at most seven at the prescribed arity cutoffs and a further five examples. The threshold check covers nested capacity profiles with up to four roots and capacities at most four.

These finite calculations do not prove the arbitrary-size theorem. The proof is the algebraic partition-bijection, sorted-demand matching equivalence, and explicit threshold witness in `RESULT.md`. No independent external review or formal proof-assistant certification has been carried out.
