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

Run `python verify.py` under Python 3. This is a standalone standard-library program and uses no downloaded data. It returns PASS after 16,663 exact-rational, algebraic-sign and geometry checks. The analytic proof in RESULT.md establishes the positive-parameter claims; numerical and finite checks do not constitute an exhaustive proof of infinite parameter ranges.

The verification code checks exact factorization, exact site-capture gaps at prescribed investment levels, 6,000 seeded rational parameter configurations, and squared-distance identities. It also confirms the midpoint/incumbent normalization at high precision. No automated independent validation has been performed.
