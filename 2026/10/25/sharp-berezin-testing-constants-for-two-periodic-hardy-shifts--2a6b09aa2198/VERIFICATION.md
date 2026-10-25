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

# Verification and limits

Run `python verify.py` with Python 3 from the extracted package directory. The program passed 4,588 supplementary finite checks and exact symbolic checks in the quadratic field \(\mathbb Q(\sqrt2)\). These checks cover the algebraic identities \(h^2+2h=1\), \(c=h^2\), \(t_*=1-2c\), the extremal critical point, the two extremal responses, a finite grid of complex coefficients, and deterministic pseudorandom complex coefficients.

The infinite-dimensional assertions are proved in the accompanying text by explicit Hardy-kernel summation, a Jacobi matrix norm argument, and two radial witnesses. A finite grid is not exhaustive over complex coefficients; no infinite operator is numerically certified. The norm and numerical-radius comparisons do not depend on the machine checks. Publication priority and independent scientific audit have not been established.
