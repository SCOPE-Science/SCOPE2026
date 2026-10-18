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
The theorem is checked analytically by factoring the gamma moment matrix as a Hilbert–Schmidt Gram operator, rescaling its companion operator exactly, and controlling the trace-norm Bochner quadrature error. The crucial uniform inequality is \( |qD_q(v)-\gamma|\le4e^{-qv} \), derived from harmonic-number integral comparisons, not from truncated spectra.

`check_numeric.py` (Python with mpmath) independently evaluates the exact scalar trace integral at beta equal to 1.5 and 2 and q equal to 10, 20 and 50. The observed residuals after subtracting the two leading terms are on the quadratic inverse-q scale, as predicted. These computations do not establish trace-norm convergence or any infinite-dimensional assertion; both are supplied by the proof.

No independent audit has been performed.
