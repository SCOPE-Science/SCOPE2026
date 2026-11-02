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

Run `python verify_coverage_variance.py` with Python 3.10+, `scipy`, and `mpmath`. This executes numeric comparisons of (i) the Gaussian rectangle's conditional-normal integral with the correlation-based variance, (ii) the correlation-derivative formula with its Laplace-support form, and (iii) two independent quadrature implementations at high precision. Its deterministic result is stored in `verification_output.txt`.

The analytical argument (Gaussian correlation derivative, positive-kernel transforms, strict Laplace-ratio monotonicity, endpoint Laplace estimate) is the proof for every real \(z>0\). Finite-precision numerical checks cannot establish that continuum uniqueness or rigorously certify the last displayed decimal digits. An independent review has not been performed.
