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

The primary open-access article was inspected directly for the exact vector field, equilibrium formulas, the parameter range of the numerical study, and the published classification at \\(a=3\\).

`artifacts/verify_hopf.py` symbolically verifies the equilibrium substitutions, both characteristic polynomials, the Hopf factorization, the exact real-part crossing speed \\(6/13\\), the cubic discriminant, the standard first Lyapunov coefficient \\(-2\\sqrt3/3\\), and the scalar filter identity for \\(z-1\\).

The checker is an algebra replay only. The Routh-Hurwitz sign argument, application of the nondegenerate Hopf theorem, bounded-complete variation-of-constants limit, and originality/value judgments are supplied analytically in the accompanying files. No finite-time numerical experiment is used as proof.
