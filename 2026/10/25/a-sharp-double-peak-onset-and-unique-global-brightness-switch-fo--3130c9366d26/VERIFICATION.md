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

# Reproduction and verification

Run `python3 verify_lambert.py` with a standard Python 3 interpreter. The script performs 4,500 reproducible derivative comparisons, 513 complete numerical phase-angle grids with 3,201 points each, checks extrema ordering across both transitions, and checks the strictly positive analytic envelope derivative at several eccentricities. The script reports the fold and global-switch eccentricities plus peak angles and intensities. The analytic proof, rather than any finite grid, establishes the global quantifiers and the uniqueness of the crossover. No measurement data or empirical parameter validation are claimed.

Boundary coverage in the mathematical proof includes \(e=0\), the fold \(e=e_{\mathrm f}\), the exact global tie \(e=e_{\mathrm s}\), the degenerate apastron transition \(e=1/3\), and every \(1/3<e<1\). The discontinuous location of the global maximizer is a statement about the ideal noiseless function, not an observed physical discontinuity.
