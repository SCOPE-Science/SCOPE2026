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

# Verification and limits

The independent literal generator in `verify.py` enumerates all valid short expansions of each positive integer at most 1024, counting 29,525 distinct representations. It compares the unweighted count to the Stern recurrence and the sign-weighted difference to the last-digit recurrence. It then checks every positive integer below 131072 against the regular language and checks the Fibonacci shell and cumulative counts for binary lengths 1 through 17. Finally it checks the projective state transition rule through 131070.

Run `python3 verify.py` using Python 3 and the standard library only. Expected final messages begin with `PASS:` and end with the sequence `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]`.

No finite test proves the statement for all positive integers. The full proof is in `RESULT.md`, and the exact signed-digit definition and the exclusion of the empty/boundary case are essential. Independent audit has not been performed.
