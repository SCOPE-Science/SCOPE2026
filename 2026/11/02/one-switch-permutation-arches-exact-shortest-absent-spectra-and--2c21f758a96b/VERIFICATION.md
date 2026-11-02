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

Run `python verify.py` using Python 3 and the standard library. Expected output:

`VERIFY_OK candidate_cases=768 candidate_patterns=1245538 independent_set_cases=56 strict_extrema_cases=12 balancing_cases=441`

The verifier checks q-ary pattern absence directly by leftmost subsequence matching and compares it with the closed condition and binomial count. For 56 small cases it constructs literal sets of all length-specific subsequences in a separate dynamic-programming implementation. It also exhausts order choices for selected parameters and tests the balanced maximum over 441 further parameters. No hidden data, third-party packages, external credentials or compilation steps are required.

These finite computations do not establish an infinite theorem. The full proof is in `RESULT.md`. The verification concerns correctness of these statements and code output only. Independent scientific audit has not been performed.
