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

The checker enumerates the cyclic gap tuples of lengths 2 through 8 over gap alphabet {1,2}, discarding tuples with adjacent short gaps including wraparound. It enumerates every marked rotation and independently computes shortest missing scattered-subsequence length and count by a next-occurrence dynamic program and direct enumeration of all length-\(r+1\) binary candidates. Both methods agree for 119 legal tuples and 2146 cuts, and each complete histogram matches the stated frequencies. The program additionally checks an excluded boundary tuple (1,1,2) that gives a fourth count value. Run `python3 verify.py`. These finite tests do not establish the infinite theorem: that is proved in RESULT.md. No independent scientific audit has been performed.
