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

# Reproducibility and limits

Run `python check.py` using a standard Python 3 installation. It enumerates all \(3+16+125+1296+16807=18247\) labeled rooted trees of orders three through seven with root label zero. It checks exact rational contraction/probability formulas, an independently recursive child-weighted leaf-depth expectation, all sharp extremum/equality characterizations, and explicit linear-extension/facet incidences on the designated sample. The observed result is `TOTAL 18247 VERIFY_OK`.

A separate direct Euclidean hull calculation on small instances was used as a sanity check for the square-root-of-two normal metric factor, but no numerical hull test is relied upon for an infinite claim. The proof in `RESULT.md` independently establishes the all-tree identity, all sharp equalities, and the stated limitations. The program is not a substitute for these arguments. The finite checker requires no network connection or additional packages. External independent validation has not been performed.
