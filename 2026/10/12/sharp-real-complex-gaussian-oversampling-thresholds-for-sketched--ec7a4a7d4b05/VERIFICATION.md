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

# Reproducibility and boundaries

Run `python verify.py` with Python 3.10+ and NumPy installed per `requirements.txt`. The deterministic test seeds reproduce full-matrix pseudoinverse calculations for dimensions \(m=2,3,4,5\), three sketch sizes per dimension, and real and complex Gaussian inputs. Separately constructed residualized normal-equation coefficients agree with the spectral first block of the sketched matrix. The test also samples both real and complex Student-ratio laws and compares empirical tail frequencies with their exact formulas.

Completed finite checks include 1,560 reconstructed reduced eigenvalue identities, 24 Gaussian tail probability tests, 2,240,000 Gaussian ratio draws, and 24 analytic moment and density normalizations.

No finite experiment certifies a universal law or the failure of an expectation to exist. Those facts follow from the orthogonal Gaussian regression reduction and exact inverse-chi-square/inverse-gamma integrals in `RESULT.md`. The tests do not cover floating-point failure, non-Gaussian sketches, root identification without an invariant basis, or adaptive sketches.
