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

Run `python3 verify.py` with Python 3 standard library only. The verifier independently constructs the idempotent transformations, composes every relevant ordered pair literally, forms their commutation graph, and finds all inclusion-maximal cliques using Bron–Kerbosch. For each integer from 2 to 7 it compares the **sets** of cliques to families generated from binary search trees, including complete cardinality profiles; for 8 and 9 it checks recursive uniqueness, Catalan total and minimum-size counts. The expected terminal line is `VERIFY_OK_CATALAN_MAXIMAL_IDEMPOTENT_CLIQUES`.

Finite computations do not prove the all-dimension claim: proof is given in RESULT.md. This package does not contain independent human verification or certify literature priority.
