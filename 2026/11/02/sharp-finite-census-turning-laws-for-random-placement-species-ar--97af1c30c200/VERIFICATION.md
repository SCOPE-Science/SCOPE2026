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

The derivation is reproduced in `RESULT.md`. The attached `verify_species_area.py` is standard-library-only and was run with Python 3. It checks the exact quotient derivative polynomial for \(2\le n\le150\), a terminal differential identity for 19,607 finite abundance vectors, root and sign predictions for \(3\le n\le250\), the exact \((1,3)\) radical and the census-three partition obstruction. It checks arithmetic independently of the displayed formula in several tests. The all-integer result rests on the coefficient-sign/Descartes proof, not on the finite checks.

Limitations: numerical root checks do not independently prove uniqueness for unbounded species counts, and this package contains no empirical validation or independent mathematical audit. The original Coleman 1981 full text was not accessible for complete priority analysis; qualitative species–area curvature is prior knowledge.
