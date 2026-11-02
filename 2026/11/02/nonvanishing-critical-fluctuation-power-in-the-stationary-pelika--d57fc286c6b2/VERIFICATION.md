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

Run `python verify.py` with Python 3 and the standard library. Seven rational probabilities strictly between \(1/2\) and \(1\) are checked. For each, the two tilted transition operators are iterated exactly through lag 12 and compared against independently generated coefficients of the closed resolvent. The checker also computes the stationary one-time variance and two independent expressions for the Green–Kubo variance, one from Poisson solutions and one from the rational formula. Endpoint substitutions check the formal limits at \(p=1/2\) and \(p=1\).

The finite checks cannot establish the all-time statements. These rely on independent fair binary digits, the reversible Jacobi spectral gaps for \(p>1/2\), exact Poisson equations, geometric-series moments, and rational limits as given in `RESULT.md`. No independent scientific audit has been performed.
