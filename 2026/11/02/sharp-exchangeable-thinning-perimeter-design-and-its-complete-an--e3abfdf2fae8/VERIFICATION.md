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
# Reproducibility and limits

Execute `python3 verify.py`. Independent brute-force subset enumeration checks all fixed-cardinality retention probabilities for small polygons and checks Bernoulli expectations against a chord formula and a closed-form regular optimum. A second calculation diagonalizes the exact quadratic form by the discrete Fourier transform and compares it with the real-space formula. Numeric agreement is not a substitute for the analytic proof for arbitrary polygon order and arbitrary exchangeable laws. There is no independent mathematical audit.
