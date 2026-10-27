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

# Reproducibility checks

The file `artifacts/verify.py` uses only the standard Python library. From the directory containing the unpacked seven-file package, execute `python3 artifacts/verify.py`. The expected successful terminal line begins `CHECKS_OK` and reports `total= 283216` exact assertion units.

The program constructs every graph on three, four, five, and six labeled vertices, groups by exact number of edges, and separately tallies the moments of isolated-vertex count, degree-one count, and their product. It compares these with closed finite-hypergeometric moments and covariance signs. It checks the independent-edge formula by weighting all enumerated graphs with three rational probabilities. A second set of checks uses exact rational arithmetic for \(4\le n\le84\) and every admissible edge count, verifies the sign and the strict consecutive-ratio inequality, and checks the independent-edge identity for five rational probabilities.

These checks were executed successfully in the packaged source form. Exhaustive testing ends at six vertices, and no finite computation proves the universal inequality or asymptotic theorem: those use the symbolic arguments in `RESULT.md`. No independent audit was carried out.
