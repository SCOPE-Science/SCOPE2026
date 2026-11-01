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

Run the Python 3 standard-library script `python verify.py` from its directory. The script enumerates exact rational moment-solving triples and compares these to the convex-hull product criterion for 4,800 sampled rational configurations, checks four symbolic \(n=3,4\) probability identities at rational \(q\), and computes the exact rational-plus-log finite-sample coefficients through \(n=12\). The observed result is `CHECKS_OK`. Its finite checks are supplementary and are not certificates of the all-\(n\), continuous-\(q\), or exponential-limit claims, which are derived in the mathematical proof. The probability is for unconstrained positive weights; not for numerical conditioning or any prescribed relative weight interval.
