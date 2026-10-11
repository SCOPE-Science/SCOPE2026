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

The analytic derivation differentiates the unnormalized cyclic autocorrelations of Gaussian chirps. The linearized Fourier multiplier is \(i\gamma_s(e^{-2\pi i a s^2/N}-1)\sqrt N\), and its nonzero squared moduli yield a positive normal Hessian. Zero Fourier frequencies satisfy \(N\mid s^2\), giving exactly the periodic phase tangent space. The family itself has identically vanishing autocorrelation, so continuity of the transverse Hessian proves local exhaustiveness and the stated quadratic bound.

A standard-library verifier, `verify.py`, ran from the extracted package path and reported:

`VERIFY_OK n=2..26 units_checked=211 squareful_cases=66 max_abs_autocorrelation=1.5e-12 max_quadratic_relerr=1.9e-13`

It compares all invertible chirp multipliers at lengths 2 through 26, including nonconstant periodic phases, the explicit Fourier quadratic form, the direct autocorrelation derivative, and finite-difference costs. Absolute error near machine precision is expected from complex exponentials. These finite experiments are not an infinite proof, an independent review, or a test of all possible solutions outside the analytic local neighborhood. The local neighborhood size and globally complete CAZAC classification are not computed.
