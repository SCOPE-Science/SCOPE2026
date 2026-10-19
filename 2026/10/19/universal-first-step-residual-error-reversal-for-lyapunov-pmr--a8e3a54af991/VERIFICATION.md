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

# Reproducible checks and their limits

Run `python3 verify.py` with Python 3.10+; the verifier needs only the standard library. Its completed execution printed `PASS: 3695 deterministic exact-rational assertions`. It reconstructs scalar Galerkin, MR, and PMR coefficients, full residual norm squares, Frobenius solution-error squares derived from the closed spectral Gramian, and the two-eigenvalue rational witness. Tests cover multiple diagonal spectra and parameter values; they do not replace the proof for arbitrary real spectra or unbounded parameters.

The universal strict orderings follow analytically from the strict convexity of the residual quadratic, the coefficient ordering, and spectral Jensen inequality. The unbounded-error construction follows from exact rational matrix entries and their \(K\to\infty\) asymptotics. The mathematical comparison is unweighted Frobenius solution error; energy-norm optimality is a separate, previously established result. No independent audit is asserted.
