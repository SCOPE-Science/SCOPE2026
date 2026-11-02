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

# Verification and scope

The spectral proof in `RESULT.md` establishes the full parameter range. Its critical identities are the point–block incidence Gram matrices, the complete zero-sum spectral decomposition, two exact strictly negative endpoint evaluations for the constant-contrast sector, and the mean-value inequalities separating the critical eigenmodes. It does not rely on numerical sampling to infer a universal assertion.

`check_affine_incidence_negative_type.py` constructs point–hyperplane incidence matrices directly over prime fields; its test geometries are \(\operatorname{AG}(2,3)\), \(\operatorname{AG}(3,3)\), \(\operatorname{AG}(4,3)\), \(\operatorname{AG}(2,5)\), and \(\operatorname{AG}(3,5)\). The checker verifies incidence Gram relations; breadth-first-search shortest paths in all but the largest-four-dimensional case; and the *complete* compression-to-zero-sum eigenvalue multiset for five choices of exponent per geometry. The comparison has numerical tolerance \(2\cdot10^{-9}\) and includes values on either side of the exact threshold. It also confirms the expected endpoint nullity by parameter counting.

Reproduce with `python check_affine_incidence_negative_type.py` after installing NumPy in a Python 3 environment. The actual run printed `AFFINE_RESOLVABLE_NEGATIVE_TYPE_SPECTRUM_OK`. It is a finite crosscheck rather than an external or independent proof certificate; independent validation remains unperformed.
