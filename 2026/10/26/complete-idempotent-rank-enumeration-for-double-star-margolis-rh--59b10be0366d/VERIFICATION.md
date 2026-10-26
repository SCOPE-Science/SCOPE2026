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

# Exact checker and limits

Execute `python3 verify.py` from this package. The standalone checker independently constructs the double-star edge set, visits every partial map including the everywhere-undefined map, tests exact idempotence and the full vertex/edge inverse-preimage conditions, and compares each rank coefficient against the symbolic formula. Tested pairs are `(1,1), (1,2), (2,2), (1,3), (2,3)`; the script prints `VERIFY_OK` only after all tests pass. The exhaustive range is finite and does not itself prove the formula for larger branching sizes; that follows from the fixed-target fiber lemma and exhaustive four-case proof in RESULT.md.

No formal proof assistant or independent external audit was used.
