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

Run `python3 verify_successor.py` with Python 3.9 or later and no third-party dependencies. Expected output starts with `PASS endpoint multisets 494 unrealizable 130 brute labelled-type sequences 1364`; it also reports the total labelled-component permutations checked by dynamic programming.

The checker independently compares the closed endpoint criterion with exact permutation search over four abstract component endpoint types. It does not enumerate infinite graphs or certify the mathematical universal quantifiers. Those follow from the convex-block and endpoint-boundary arguments in `RESULT.md`. The proof and checker use the same explicit definitions of component types.
