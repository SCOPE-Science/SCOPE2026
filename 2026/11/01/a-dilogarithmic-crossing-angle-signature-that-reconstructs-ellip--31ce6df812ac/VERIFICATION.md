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

# Reproducibility of the conditional crossing-angle identity

Run `python3 checker.py` from this package's directory using Python 3 standard library. The deterministic checker calculates the first eight circular-gap cosine coefficients using independent Simpson integration, compares the dilogarithm formula with a separate Beta–Poisson integral at eight aspect ratios, numerically checks strict order and the inverse range, and simulates the original four endpoint labels at four ellipse aspect ratios. Monte Carlo rejects all nonalternating endpoint patterns before computing the Euclidean determinant-to-norm squared-sine angle; it also verifies the crossing frequency near one third. The deterministic output ends in `ALL_CHECKS_PASSED`.

The analytic proof, including the exact probability, the global derivative inequality, the unique inversion, and both endpoint asymptotics, is in `RESULT.md`. Finite quadrature and random sampling are corroborative, not proof of an infinite-dimensional or universal identity. The code does not produce an independent audit, certify publication priority, or provide finite-sample error guarantees.
