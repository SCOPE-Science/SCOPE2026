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

# Verification of the endpoint law

The analytic proof uses a parameter-uniform change of variables in the published exact continuum-plus-edge formula. The transformed densities were checked against the original printed equation (67), including the sign of the even density near its gap edge. The error terms are bounded by integrable \(\operatorname{sech}^3y\) moments times \(\lambda^4[1+\log(1/\lambda)]\), and the special integrals follow by differentiating a convergent beta integral. This establishes the asymptotic claims; numerical quadrature alone would not.

A reproducible optional numerical test is supplied in `verify.py` using `mpmath` at 45-digit precision. It compares both exact integral expressions with their proposed leading terms for several positive transmissions. These checks do not certify all parameters or independently validate the argument. The published spectral formula and any numerical values need independent scientific verification before broader reliance.
