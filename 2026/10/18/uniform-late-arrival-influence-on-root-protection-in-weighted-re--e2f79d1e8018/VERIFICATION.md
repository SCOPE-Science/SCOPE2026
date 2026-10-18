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

Run `python verify.py` in an ordinary Python 3 environment. The verifier uses only the standard library. It enumerates all growth-parent choices for 2 through 8 nonroot vertices, at root weights 1/2, 1 and 2. Its expected output is `PASSED: 210 exact conservation, strict sign, and influence-bound assertions`.

It checks the exact Ewens partition probability against a separate associated-Stirling recurrence, each root attachment's Bernoulli marginal, strict negative local covariance, and both analytical influence bounds. Finite enumeration does not prove the asymptotic result or the universal all-real-weight claim; both are proved analytically in RESULT.md.

Independent audit: not performed.
