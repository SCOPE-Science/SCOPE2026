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

The characterization and orbit formula have all-parameter combinatorial proofs in `RESULT.md`. The scripts give finite, independently implemented stress tests, not certification for infinite parameters.

`python3 artifacts/verify_bruteforce.py` exhausts all source level compositions through a total of five points and target compositions through four points (with target size at most source size), checking successor images against the full Kripke relation for every onto function. It compares 395 composition pairs, 1,550 valid maps, and the 247 resulting orbit profiles to two formulas.

`python3 artifacts/verify_group_actions.py` constructs actual source and target within-cluster transposition generators, closes each orbit on the set of bounded morphisms, and independently verifies map and orbit counts in 22 selected boundary and mixed-size cases.

Recorded console outputs are in `artifacts/verification_brute.log` and `artifacts/verification_group.log`. Python 3 standard library suffices. The verification does not address literature completeness, categorical interpretations beyond the stated frame class, or independently audited publication priority.
