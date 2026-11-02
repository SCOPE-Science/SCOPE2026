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

# Reproduction and boundaries

From a folder containing `checker.py`, run `python3 checker.py`. A normal completion prints `VERIFY_OK`; failed assertions show the first tested counterexample. The checker uses only integer operations and Python's standard library.

Checks include all binary source words of lengths 3 through 7 (where each tested triple fits), substitution orders 1 through 4, multipliers 1 through 3, all valid starts and offsets; plus dyadic Thue–Morse starts 0 through 255, orders 1 through 5 and exponents up to 8. Short window profiles are also cross-checked against independent direct scattered-subsequence enumeration.

The full universal theorem is established in `RESULT.md` by the free-algebra proof, not by these finite checks. All computations concern the same coefficient normalization: a pattern occurs once per increasing index tuple. The fixed-point corollary is supported by the established Thue–Morse length-three nonconstant property. Independent validation and exhaustive historical priority checks are not performed.
