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

The exact finite-field checker `verify.py` was run from the delivered package source. Its result was:

```
m,q,projective_points,singular_points = (3, 5, 3906, 121)
m,q,projective_points,singular_points = (4, 3, 3280, 652)
m,q,projective_points,singular_points = (5, 2, 1023, 671)
VERIFY_OK
```

The checker compares each projective point against the Jacobian and the independently evaluated set-membership criterion; it also checks Euler identities and two Hessian determinants. The characteristic-zero, all-parameter theorem is established by the symbolic stratification proof, not by extrapolation from finite fields. The reduced components are proven using irreducibility and generic-point arguments. The reduced singular locus is not asserted to equal the Jacobian scheme scheme-theoretically; no claim is made about embedded components or all nongeneric singularity types.
