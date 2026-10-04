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

`verify.py` uses only the Python standard library and exact `Fraction` arithmetic. It reconstructs the Gaussian raw-moment polynomials from centered-normal moments, substitutes them into the Taylor polynomial for \(\log\cosh(\theta Z)\), and checks the e-power coefficients through \(\theta^8\). It also verifies the quadratic e-power exactly and checks the claimed reciprocal-series coefficients by multiplication.

The analytic remainder is not inferred from computation: bounded higher derivatives of \(\log\cosh\), together with locally bounded Gaussian moments, give the stated \(O(\theta^{10})\) expectation remainder. The pointwise dominance is likewise analytic, via monotonicity of \(x^2/2-\log\cosh x\) on \([0,\infty)\).

Limit: the verifier certifies the algebraic coefficients, not the completeness of the literature search or any independent review.
