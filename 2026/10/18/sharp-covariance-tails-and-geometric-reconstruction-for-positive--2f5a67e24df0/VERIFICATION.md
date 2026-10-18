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

Run `python verify.py` with Python 3 and its standard library. The program checks 88 finite numerical and combinatorial identities from the stated family: four admissible parameter examples, exact finite-sign covariance enumeration, weighted-sum identities, finite Fourier logarithm inversion, and convergence of the stated two-term asymptotic. The reported output is `VERIFY_OK 88 diagnostics (finite cases only)`.

The universal identities are proved by summable Bernoulli-coordinate expansions, elementary generating-function manipulations, Euler–Maclaurin summation with exponentially weighted tail control, and a zero-free analytic spectral factor. No finite collection of numerical tests establishes universal formulas or bibliographic originality. Independent audit: not performed.
