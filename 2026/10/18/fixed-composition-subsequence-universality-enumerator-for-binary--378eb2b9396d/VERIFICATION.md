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

The mathematical finding is an identity of formal generating functions. Its proof is the exhaustive symbolic decomposition of a palindrome into a half-word's greedy complete-alphabet arches, a constant rest, and optionally a middle letter, with all three statistics tracked.

To reproduce the finite checks with Python 3 standard library only, run `python3 VERIFY.py`. It compares exact integer coefficients of the claimed generating function with complete enumeration of all binary palindromes of lengths 0 through 20, retaining every length/weight/universality triple. For lengths 0 through 12 it also tests the index via all binary subsequences rather than via the arch count. The successful run ends with `VERIFY_OK_GF_ALL_COMPOSITION_LENGTHS_0_20_SUBSEQ_INDEPENDENT_0_12`.

The checks do not establish the infinite rational identity by themselves. The result uses the established per-word palindrome arch rule, and the composition refinement is proved by symbolic weighted enumeration. The independent scientific audit has not been performed.
