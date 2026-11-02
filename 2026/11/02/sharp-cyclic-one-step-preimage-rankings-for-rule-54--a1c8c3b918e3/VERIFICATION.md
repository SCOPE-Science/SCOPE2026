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

## Reproduction
From this directory run `python3 verify.py`; it must exit successfully and print `VERIFY_OK`. The checker uses only Python's standard library and exact integer arithmetic.

## Certificate scope
The checker computes the pair-state transfer matrices, validates the polynomial matrix identities and finite induction seeds, and directly enumerates complete fiber distributions on all cyclic binary input rings of sizes eight to sixteen. The proof in RESULT.md is needed to extend these finite checks to every length at least eight. Output equality classification is not independently audited.
