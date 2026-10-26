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

# Reproducible checks

Run `python matching_biclique_checker.py` with Python 3's standard library. The program reconstructs the weighted grounded-Laplacian inverse using exact fractions instead of the analytic spectral decomposition, checking all source-edge projection columns for six rational conductance-square-root values at each of four graph sizes, 516 columns in total. Its successful output is `MATCHED_BICLIQUE_EXACT_OK graphs=24 columns=516`. The checker also checks the projection-column energy identity for each source. Symbolic steps needed beyond these samples, particularly all-parameter sign control and uniform asymptotic maximization, are proved in RESULT.md; no infinite extrapolation is made from finite tests.

No independent mathematical verification has been performed.
