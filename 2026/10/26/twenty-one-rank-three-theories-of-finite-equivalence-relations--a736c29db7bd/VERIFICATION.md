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

The files `verification/census.py`, `verification/game_crosscheck.py`, and `verification/rank3_classes.csv` form a self-contained Python 3 standard-library certificate. From their containing package directory, run `python verification/census.py` and `python verification/game_crosscheck.py`.

The census checked 63 reduced profiles, found exactly 21 distinct depth-three first-order types, verified all 63 CSV entries, and found a maximum minimum representative order of 9. The independent minimax solver checked all 63 claimed same-type memberships and all 210 distinct-type separations. Both commands completed successfully.

The proof that every arbitrary nonempty finite equivalence structure reduces to these 63 profiles uses a mathematical three-round game argument, not the scripts. Sharpness at nine elements follows from the two explicit rank-three sentences in RESULT.md. The statements make no claim about higher quantifier ranks, extra predicates, or total quantifier counts. Independent audit has not been performed.
