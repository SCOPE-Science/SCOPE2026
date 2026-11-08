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

The all-length proof is in `RESULT.md`, with the exact quotient-shell restrictions, explicit forbidden sets, integer shell cardinalities, and a uniform asymptotic counting argument. `CHECK.py` uses Python 3 standard-library arithmetic to test all ordered pairs among 255 binary antipalindromes of length at most 16, and to verify the first eight shell-boundary counts. The actual output is `CHECK_OUTPUT.txt`. The finite checks do not prove the all-length statement; no independent audit has been performed.
