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

# Reproducibility

Run `python3 verify_dfa.py` in a directory containing the supplied script. It reports `FINITE_CHECK_PASS` when its independent saturated-counter DFA minimization agrees with the formula for every integer from 0 through 45; it also checks all 8191 binary words of lengths up to 12 by comparing direct index-pair counts with a streaming count and by checking the prefix/suffix join identity.

The unbounded theorem is established by the quotient proof in `RESULT.md`. The verifier is bounded and makes no claim about untested values. The source-comparison limitations described in `REVIEW.md` remain applicable. Independent audit has not been performed.
