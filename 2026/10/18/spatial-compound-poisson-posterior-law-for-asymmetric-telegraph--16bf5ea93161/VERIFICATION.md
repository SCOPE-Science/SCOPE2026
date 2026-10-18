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

# Reproducibility and proof boundary

The theorem follows from exact symbolic two-state matrix inversion, spatial partial fractions and the Bessel-Laplace integral identities presented in `RESULT.md`. The proof analytically verifies that the base measure and the compound-Poisson Lévy measure are positive and finite. It proves an infinite family of posterior laws; numerical quadrature alone is not offered as a proof.

Run `python verify.py` with Python 3 and the libraries `numpy` and `scipy` available. The script evaluates the known fixed-time asymmetric telegraph kernel by integration against exponential stopping, including the no-switch ballistic atom, and checks its value against the independently derived spatial resolvent. It also checks the proposed base probability transform, compound-Poisson jump intensity and exponent factorization. The tests cover unequal speeds in both orientations, symmetric speeds as a boundary consistency check, both signs of observed displacement, and several Laplace parameters.

Expected successful output: `256 independent numerical assertions passed`. This output was observed when the embedded program was executed for the present package. The numerical tests sample parameters and do not establish the theorem for untested parameter values. Independent validation has not been performed.
