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

The derivation is deterministic and does not depend on probabilistic simulations. For every linearly independent snapshot pair, strict Cauchy–Schwarz for each snapshot stiffness matrix proves both Gram cofactors are strictly positive, and the two-by-two inverse yields the exact sign formulas. This argument applies simultaneously to every finite ambient dimension with the stated hypotheses; finite computations alone do not establish this universal claim.

Run `python verify.py` with Python 3.10 or later; it uses only the Python standard library. The file performs exact rational elimination for the stated diagonal three-dimensional counterexample, including the first reduced coordinate, the full-order comparison, the reduced determinant and both reduced coefficients. It then performs 9,250 exact rational coefficient-identity, sign and reduced-residual orthogonality checks on 250 reproducibly generated diagonal SPD families of dimensions 3–5 and parameters inside and outside the two sample points. The result observed was:

```
PASS: exact 3D counterexample; 9250 exact rational Galerkin/sign identities
```

The 2011 reduced-basis review and the 2026 motivating paper were inspected for the specific sign statement. The 2002 comparison remains abstract-only, so a claim of exhaustive priority verification is not made. Independent audit has not been performed.
