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

# Reproducibility and verification scope

The source polynomial is the fourth elementary symmetric polynomial in six variables restricted to their sum-zero hyperplane in characteristic three. The proof uses the quotient by the all-ones vector to describe a quartic cone, then the singular scheme of its quartic base.

With Python 3 and the dependency in `requirements.txt`, run `python CHECK.py`. The exact computation checked the translation identity, obtained the displayed reduced Gröbner basis, counted the nine standard monomials, verified all nine affine singular points and nonzero Hessian determinants, enumerated the fifteen distinct pair-difference classes, and checked their affine-chart correspondence. As a diagnostic rather than a proof of geometric completeness, it also enumerated 76 rational points of the threefold over the prime field.

The leap from a finite chart computation to all algebraically closed extensions uses the exact zero-dimensional quotient length and the permutation cover of projective coordinate charts; the explicit points account for the complete length. The classification of the singular locus of the cone and normality then follow from the geometric arguments in `RESULT.md`. Finite-field enumeration alone does not imply these assertions.

There is no claim to have computed the full (possibly nonreduced) singular scheme at the cone vertex, and no independent external assessment has been performed.
