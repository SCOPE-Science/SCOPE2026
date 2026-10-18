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

Run `python3 verify.py` using only the Python standard library. The script enumerates complete stationary path laws with exact rational arithmetic for 224 parameter/horizon configurations, compares all lagged switch covariances, computes means/variances, and checks the strict variance gap against the binomial variance upper bound. It also checks the exact binomial distribution for symmetric transition matrices. The general proof does not rely on extrapolating these finite checks. The available primary source comparisons are summarized in REVIEW.md and AUDIT.json.
