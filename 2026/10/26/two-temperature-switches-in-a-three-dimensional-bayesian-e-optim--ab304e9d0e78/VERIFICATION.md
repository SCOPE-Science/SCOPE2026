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

# Reproducibility notes

Run `python verify.py` using Python 3 and only its standard library. It reports `CHECKS_OK` and the two numerical smoothing thresholds. The script checks the two symbolic characteristic polynomials from the explicitly given matrices, exact factorization of the exponential-comparison polynomial, three rational signs that force root existence, and the two sign changes that bound root count. The root locations are then obtained by bisection. The script separately samples thousands of two-dimensional spectral pairs to guard against accidental sign mistakes in the general statement.

The universal existence, uniqueness, root-simplicity, and minimal-dimension assertions follow from exact algebra plus Descartes' sign rule, the intermediate-value theorem, and a decreasing-integrand comparison—not from numerical sampling. The approximate decimal thresholds are not used to establish the signs or root count. The scientific review describes literature-comparison risks; independent external validation has not been performed.
