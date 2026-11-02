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

# Verification record

The full proof has no nonstandard computational lemma and is reconstructed in `RESULT.md`. Specifically: singleton image rigidity follows from back to two disjoint target singleton worlds and forth on their preimages; equality with the direct image follows from forth and back; back against the full target world forces surjectivity; a surjective inverse-image choice supplies the converse back witness.

`checker.py` enumerates **all** functions from source worlds to target worlds (for carrier size pairs \((1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2)\)); it evaluates every forth and back clause directly. Counts: 1, 0, 1, 2, 0, 1, 6. It separately checks 2,676 surjection-induced examples at sizes up to six/four. The checker output ends with `ALL_CHECKS_OK`.

Computational limits: a finite check does not certify an arbitrary-set theorem or originality. Its role is to test the definitions and the finite surjection enumeration; universal correctness is supplied by the written proof. Independent verification has not been performed.
