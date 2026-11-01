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

# Reproducibility and verification

Run `python verify.py` using a standard Python 3 interpreter. The checker performs exact rational evaluations of the finite Fourier eigenvalue formula and its multiplicity trace, compares selected eigenvalues with direct complex character sums, and tests numerically located scalar roots through dimension 18 and multiple alphabet sizes. The expected successful output begins `CHECK_OK`.

The verification consists of finite self-checks; the complete quantifiers, exact endpoint nullity and exclusion of all intermediate bandwidths are established by the analytical proof in RESULT.md. Numerical root location is **not** used to certify infinite-dimensional statements, and neither independent mathematical validation nor publication priority is claimed.
