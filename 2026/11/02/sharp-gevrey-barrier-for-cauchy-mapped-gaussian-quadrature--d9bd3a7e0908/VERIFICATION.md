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

Run `python3 verify.py` using only the Python standard library. The supplied verifier reports 218 passed finite checks: pointwise equality of the importance transform with its original density ratio, even symmetry, normalization against the closed-form Gaussian exponential moment, discrete Fourier coefficients, and alias-variance comparisons against direct integration over uniform shifts at six sample sizes. The numerical tests use a finite discretization and ordinary floating-point arithmetic.

The all-parameter, all-order Gevrey claim and sharp impossibility of any faster uniform-in-sample-size exponent are established by the analytic complex-derivative and Fourier-converse proofs in RESULT.md; finite calculations cannot certify those infinite assertions. No independently performed scientific audit or general-purpose formal proof certificate is asserted.
