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

# Reproducibility and scope

Run `python3 verify.py` with Python 3.9 or later and no nonstandard dependencies. It prints the nine low-half fixed-magnetization optima and exact multiplicities for each graph, followed by `VERIFY_OK`. The associated `verification_output.txt` records the execution of the included program.

The implementation checks 65,536 configurations for each of the two 16-site labelled graphs through two independent combinatorial descriptions. The first performs single-vertex Gray-code flips with exact incremental cut updates; the second calculates the same coefficients by enumerating all ordered four-row assignments with explicit within-row and between-row edge formulas. The entire bivariate cut-size versus negative-spin-count tables agree, not only their maxima. Exact strong regularity and ten construction masks are checked separately. The analytic Rayleigh-quotient lower bound and the row-column counting obstruction in `RESULT.md` establish the extremal profiles without relying on random testing.

No infinite system, thermal behavior, transverse-field spectrum, or independent scientific validation is claimed.
