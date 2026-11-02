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

# Verification

The exact claimed object is the spectral Schur multiplier induced by a one-entry unit-phase modification of a finite unnormalized complex Hadamard matrix. The proof verifies all-order correctness by trace duality, a matrix fidelity variational identity, simplex stationarity, a two-dimensional singular-value calculation, and a scalar optimizer equation. The derivation of the phase law is independent of the numerical optimizer.

`check.py` runs 30 Fourier-matrix angle/order cases and nine non-real order-four Hadamard-family cases. Each evaluates the analytic formula and numerically maximizes the unrestricted two-probability-vector dual nuclear norm with three starts. The Fourier cases also compare against an independent one-variable scalar optimization. The final replay reported `PASSED_CASES 30` and `ALL_CHECKS_PASS`, with all 39 cases successful.

The tests are finite floating-point checks, not exact certificates or a substitute for analytic quantifiers. The PDF literature comparisons are not an independent historical audit. There is no claim of independent validation.
