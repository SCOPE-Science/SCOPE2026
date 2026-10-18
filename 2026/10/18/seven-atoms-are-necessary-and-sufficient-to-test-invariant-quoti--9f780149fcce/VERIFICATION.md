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

Run `python3 verify.py` in the extracted directory. The checker enumerates all ordered triples on six labels to verify the complement-pair equivalence; groups seven-label triples by all five equality patterns and verifies graph connectivity for all 25 ordered type pairs; then checks an explicit nontransitive configuration on seven labels.

The checker is finite corroboration only. Universal validity for infinite atom sets and the all-arity upper and lower bounds come from the proof in RESULT.md. No independent scientific audit has been performed.
