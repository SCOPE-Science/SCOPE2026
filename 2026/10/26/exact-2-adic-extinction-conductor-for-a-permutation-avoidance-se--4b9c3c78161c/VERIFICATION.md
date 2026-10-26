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

# Computational checks and limits

The standalone `verify.py` uses integer arithmetic and no third-party packages. It checks the exact Catalan extraction against an independently generated quadratic recurrence to index 229, the terminal zero congruences and immediately preceding nonzero witness for each dyadic exponent 1 through 64, and the classification of all indices at which the lower valuation bound is met in that range. Algebraic support and Catalan parity prove the infinite claim; these finite tests are corroboration only. Independent mathematical audit is not performed.
