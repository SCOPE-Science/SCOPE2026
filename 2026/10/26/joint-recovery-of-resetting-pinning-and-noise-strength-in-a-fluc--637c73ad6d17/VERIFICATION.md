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

# Computational and analytic verification

The proof of strict invertibility is the one-variable derivative calculation in `RESULT.md`; no finite numerical test substitutes for that argument. The explicit covariance is checked from the heat-kernel integral, while the excess kurtosis is checked from the independent conditional Gaussian age-mixture quadratures.

With SciPy installed, run `python3 verify.py` in the extracted package. The checker asserts agreement of the closed-form variance, normalized spatial covariance and excess kurtosis with numerical quadratures for five positive parameter tuples, then solves the inverse scalar problem and verifies recovery of all three parameters. All five checks passed in this package. No Monte Carlo results or external data are required.

Boundaries \(r=0\), \(\mu=0\), and vanishing spatial separation are deliberately excluded from the strict inverse theorem. The script is supporting evidence, not a certificate for arbitrary floating-point data or statistical measurements.
