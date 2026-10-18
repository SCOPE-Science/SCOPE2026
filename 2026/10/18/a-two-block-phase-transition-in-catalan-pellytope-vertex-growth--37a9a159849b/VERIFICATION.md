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

Run `python3 CHECKER.py` with Python 3 standard library. During this review it returned `CHECKER_OK`: 55 exact published-table comparisons, 66 exact independent ordered-composition enumerations, normalized diagonal checks at five depth ratios, and the two-block Riemann-limit diagnostic at three ratios. The proof in RESULT.md establishes the limit for every fixed real depth ratio between zero and one by explicit fixed-block asymptotics, a controlled three-block tail, and a summable geometric domination. The checker is not a proof of infinite limits. No external independent audit, formal proof assistant certification, or general-boundary uniformity test was performed.
