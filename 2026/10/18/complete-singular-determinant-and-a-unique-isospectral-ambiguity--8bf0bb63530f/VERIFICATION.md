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

# Verification and limitations

Run `python verify_reflection.py` with the NumPy version range in `requirements.txt`. The independent finite-section, rational coefficient and scalar-root checks completed **472 assertions**. The finite integration matrices represent midpoint quadrature and are not claimed to be exact infinite-dimensional models. The proof in `RESULT.md` independently establishes the singular determinant, root location and multiplicity, complete isospectral classification, the asymptotic coefficient and its Schatten consequences. Bibliographic priority and independent formal validation remain unperformed.
