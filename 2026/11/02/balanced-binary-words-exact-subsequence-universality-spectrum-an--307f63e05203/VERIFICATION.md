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

# Verifiable calculations and limits

`verify.py` runs on Python 3 with no third-party packages. From the squared generating-function equation, it constructs all bivariate coefficient polynomials through semilength eight by integer polynomial recurrence. Separately, it enumerates all balanced binary words up to length sixteen, computes each word's universality index via greedy arch factorization, and checks every enumerated coefficient and the central-binomial totals. It also computes the index independently by testing every possible short binary subsequence for all source words through length ten.

Actual replay: `VERIFY_OK total_balanced_words=17577; all_words_upto_length=10`.

These finite tests do not certify coefficients for all lengths or the limit theorem. The all-length result depends on the exact arch factorization, formal constant-term identity, and analytic square-root singularity argument written in RESULT.md. The infinite claims are proved by those steps, not by extending finite computational observations. An independent scientific audit has not been performed.
