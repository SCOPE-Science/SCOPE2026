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

Run `python verify.py` with a Python environment containing `numpy`, `scipy` and `sympy`. The checker constructs the Bloch characteristic determinants with symbolic Laurent variables and compares them to the Schur formula at resonator path lengths 1–5; it also checks the Chebyshev recursion. For resonator path lengths 1–12 it solves the root Green equation numerically for every interlacing interval, tests two positive hopping profiles and five Bloch momenta, checks that the resulting flat energy is the predicted ordered eigenvalue, and verifies the explicit compact eigenvector residual.

Recorded successful run on the packaged checker:

`VERIFY_OK exact_characteristic_orders= 5 tuning_spectra= 780 motif_lengths=1..12 band_ranks=1..m`

These tests do not exhaust the real symmetric cyclic resonator domain; completeness is supplied by the analytic determinant and monotonicity proof. Numerical tolerances reflect floating-point eigenvalue computation. The checker is ordinary reproducibility code, not an independent audit or certification.
