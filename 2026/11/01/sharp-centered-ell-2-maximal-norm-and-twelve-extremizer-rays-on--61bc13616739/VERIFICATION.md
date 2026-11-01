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

# Exact verification

Run `python verify_c6.py` from the directory containing this document. The checker uses Python 3 standard-library integer and rational arithmetic only, and regenerates every ball, matrix, exact spectral test and active-selection comparison from the mathematical definitions. It requires no hidden data, downloaded resources or packages.

The completed checker produced:

`CERTIFICATE_OK selections=4096 strict=4084 exceptional=12 characteristic_quintic=exact root_isolation=exact eigenvector=exact active_selection_tests=18`

Specifically, its 4096 cases exhaust all four centered-ball choices at each of six vertices. All 4084 strict cases satisfy the exact positive-definiteness test, and the other 12 equal the one dihedral orbit. The exceptional Gram characteristic polynomial, unique isolated root above the gap threshold, positive eigenvector identity, and 18 strict active-ball differences are checked algebraically using exact rational bounds. The script is an executable finite mathematical certificate; its output log alone is not an independent proof without the checked source and mathematical reduction in `RESULT.md`.

Limits: only the unweighted six-cycle, counting measure and centered graph-ball operator on real \(\ell^2\) are certified. The mathematical priority assessment is qualified, and independent scientific auditing has not been performed.
