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
# Verification record

The theoretical certificate is the finite-dimensional real discrete Fourier block diagonalization in `RESULT.md`: it computes the two-by-two Hermitian blocks for every paired harmonic and the additional real self-conjugate block when the arc count is even. Normalization is checked against unnormalized Parseval, so the stated real singular values follow for every integer arc count, rather than from finite enumeration.

Run `python verify_jacobian.py` (Python 3 with NumPy and SciPy). The program independently differentiates the arc Fourier integrals, orthogonally projects onto the exact fixed-length and rotation-gauge tangent, and compares singular values with the two-band formula for all arc counts from \(2\) through \(10\) and duty fractions \(0.13,0.28,0.50,0.74,0.93\). The observed result was `PASS: 45 Fourier-Jacobian spectra, zero moments, and finite differences.` It also checks reference Fourier zeros by explicit integration and direct finite-difference derivatives. Such tests cannot certify the arbitrary-size statement by themselves; the analytic proof supplies that step.

The only asserted stability is an asymptotic local estimate, with an explicitly fixed Euclidean endpoint metric and the normalized positive-frequency Fourier metric. The global inverse condition and the possibility of earlier equivalent results have not been externally certified.
