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

# Verification of the Fourier threshold

The analytic proof uses two endpoint-integral recurrences, explicit formulas for the first three odd Fourier integrals, and a two-step inequality to certify all later odd harmonics. For exponents above the critical value, a negative fifth or fourth Fourier coefficient is an exact obstruction, not a conclusion drawn from a finite computation. Positivity at the endpoint does not require the fifth Fourier coefficient to be positive, because all frequencies greater than five have positive coefficients and determine a nonsingular consecutive-frequency Vandermonde system on every finite collection of distinct circle points.

The independently runnable `CHECK.py` checks symbolic identities and the critical polynomial. Six exponent samples and 64 positive frequencies per sample give 384 direct quadrature comparisons to the recurrence; the maximum observed absolute error was \(4.744\times10^{-14}\). For exponent \(1.7\), a 32-point uniform grid exhibits a strictly negative discrete frequency-five eigenvalue of approximately \(-0.0510351363091\). Numerical tests are finite checks only; the proof supplies the general conclusion.

Literature searches found Gneiting's published family and relevant positivity criteria, but cannot certify the absence of every equivalent publication. Independent audit and mathematical validation have not been performed.
