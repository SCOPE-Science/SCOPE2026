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

## Reproducible checks

`python3 verify.py` uses only the Python standard library and checks numerical quadrature of the positive two-arc leakage against its Fourier form and the sharp local quadratic coefficient. These finite-precision tests confirm the algebraic normalization and symmetry at specified sample parameters; they do not establish the universal theorem.

The universal proof is analytical: the cross-arc integral, differentiation, strict Poisson positivity, Parseval with explicit Fourier coefficients, and a one-dimensional Abelian asymptotic. All endpoints and the case \(\rho=0\) are covered by the written argument. No independent audit or independent validation has been performed.
