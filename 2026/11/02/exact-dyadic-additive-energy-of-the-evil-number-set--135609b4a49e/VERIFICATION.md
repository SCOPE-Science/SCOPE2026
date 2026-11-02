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

The proof is mathematical rather than a claim of exhaustive computational certification. Run `python3 artifacts/verify.py` using the standard library. The script constructs every carry transition directly from sixteen digit quadruples, checks sixteen exact terms of each rational-recurrence identity for all six mask representatives and confirms their multiplicities among all sixteen masks, checks the full algebraic formula across seventeen scales, and separately enumerates ordinary integer sum-pair convolutions at eleven scales.

The output `VERIFY_OK` is supporting evidence for concrete tests and algebraic identities; the unbounded theorem follows from the exact digit-carry bijection and finite-dimensional rational matrix resolvent. The 2018 signed-moment full text was inaccessible, so bibliographic completeness is not certified. Independent audit and validation were not performed.
