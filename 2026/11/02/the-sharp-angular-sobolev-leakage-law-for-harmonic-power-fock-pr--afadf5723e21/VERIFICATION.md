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

The analytic argument requires the orthonormality of the two-sided harmonic radial basis, the exact gamma quotient for angular matrix coefficients, positivity of the projection residual, the trigamma bound \(\psi_1(t)\le t^{-1}+t^{-2}\), and Fourier-series dominated convergence/Fatou arguments. These are written out in `RESULT.md`.

Run `python3 check_harmonic_fock_leakage.py` in the extracted artifact directory; it uses only the Python standard library. The script was executed from its actual package source path and completed 1907 finite assertions covering gamma coefficients, a Gaussian exact harmonic-number identity, signed Fourier symmetry, independent radial quadrature, contraction inequalities and sample high-index behavior.

The numerical tests are finite and do not validate the theorem's arbitrary-\(L^2\) and infinite-\(N\) quantifiers. A research review of the proof and closest identified literature was performed, but independent audit, independent validation, exhaustive literature search, and a computer-proof certificate have not been performed.
