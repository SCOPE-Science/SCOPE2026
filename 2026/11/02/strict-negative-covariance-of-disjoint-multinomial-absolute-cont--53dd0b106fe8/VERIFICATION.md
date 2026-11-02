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

# Verification evidence

The standalone `verify_multinomial.py` performed 315 exact-rational assertions. It independently evaluates multinomial outcome sums at small sample sizes for asymmetric rational category masses and tests conditional binomial reduction and the monotone biased-walk auxiliary function. It passed. Run `python3 verify_multinomial.py` to reproduce. Finite checks do not prove the theorem for arbitrary sample size: the complete conditional-regression proof is in RESULT.md. No independent audit has been performed.
