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

# Reproducibility checks
Execute `python3 verify.py` from this package. It uses only the Python standard library and verifies (in exact rational arithmetic when relevant) the 0–6 innovation moments, the 0–6 stationary moments, the 21 one-lag mixed moments of total degree at most five, twelve finite-time propagation steps, the support-frontier algebra, and the numerical entropy constant.

The result on a singular continuous measure with full support comes from its biased ternary digit representation and the strong law of large numbers. No finite computation or Monte Carlo run could certify that property. The sixth-moment discrepancy follows analytically from the additivity of cumulants. The source comparison and interpretation are separate scientific judgements and have not received independent external validation.
