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

# Verification record

Run `python3 verification/check_bk_optimizer.py` from a Python 3 environment. This standalone program needs only the Python standard library. Its output is recorded in `verification/check_output.txt`.

The integer-arithmetic assertions check, for every integer \(1\le n\le1100\), the exact scaled BK-gap values, uniqueness of the proposed maximizing threshold, every adjacent first-difference identity and its predicted sign; they also test the strict ratio bound. For each \(1\le m\le150\), a second exact calculation checks the three-coin coupling equation and its positivity. A few floating checks compare large finite tails with the announced entropy exponent. The checker prints 1,311,695 assertions passed.

These finite tests do not establish the theorem for all \(n\). The analytic argument appears in RESULT.md, notably the unconditional difference identity, the monotonicity of the three-coin coupling, the strict factorial-ratio recurrence, and the classical large-deviation exponent. This is a self-review only; no independent audit was performed.
