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

The exact checker `artifacts/verify.py` uses symbolic arithmetic over \(\mathbb Z[\lambda_1,\lambda_2,\lambda_3,\lambda_4]\). It verifies:

- the determinant condition for \(P\cap SP\ne0\) in Plücker coordinates;
- the three singular parameters of the pencil of quadrics and the factorization separating those parameters;
- the six affine quadratic normal forms through nonvanishing Hessian determinants, uniformly under pairwise distinct eigenvalues;
- the anticanonical weight identity \(\xi_h=2\varpi_1+\varpi_2\);
- the localization consistency check \((-K_X)^4=192\).

The saved output `artifacts/verify.out` ends with `VERIFY_OK`. The checker establishes the exact algebraic identities used in the proof. The birational statements additionally use the incidence argument, normal/Gorenstein properties of a nodal complete intersection and its projective-line bundle, and the absence of exceptional divisors for a small resolution. Literature originality is assessed separately and is not certified by the checker.
