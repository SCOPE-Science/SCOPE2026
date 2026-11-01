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

The proof derives the exact periodic Fourier coefficients of the width function, the frequency selection at the least common multiple, and strict monotonicity of the resulting normalized autocorrelation from the strict decrease of \(\sin z/z\). For the closed-form covariance endpoints, a separate symbolic derivative simplification confirmed the displayed formula; direct quadrature agreed with it.

Run `python CHECK.py` using Python 3 standard library. The test enumerates regular-polygon vertices rather than reusing the folded-cosine representation for the geometric width calculations. It checks eight polygon pairs in both arithmetic-parity classes at endpoint and interior relative phases, and verifies the sharp endpoint formulas and fourth-order asymptotics. Its run in this package reported `ALL_CHECKS_PASSED`.

These are finite reproducibility checks only; no claim of exhaustive numerical verification of continuous angles or arbitrary polygon sizes is made. The analytic argument supplies the universal proof. The source comparison is not a certification of global historical novelty. No independent audit has been performed.
