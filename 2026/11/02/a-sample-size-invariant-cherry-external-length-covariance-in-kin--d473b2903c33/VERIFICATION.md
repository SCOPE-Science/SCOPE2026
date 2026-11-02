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

Run `python3 verify.py` using only Python 3 standard libraries. This checks exact probability moments and all levelwise formulas for sample sizes 3 through 100, plus exhaustive ranked-history enumeration for sizes 3 through 7. The exhaustive enumeration has 59,601 histories in total and checks the expected cherry count, each stage covariance, and the external-length covariance under independent mean holding times. The analytic proof in RESULT.md, rather than finite verification, establishes every sample size. No independent audit has been performed.
