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

Run `python3 checker.py` from the folder containing the extracted research files (Python 3 standard library only). The program exits nonzero upon any failed assertion. The delivered checker passed 77 assertions, comprising 20 independent exact-state/transfer comparisons over four even cycle sizes, nine independently derived exact expectation comparisons using rational arithmetic, 27 scaled-profile checks at three offsets and three size levels, 18 logarithmic-crossover checks, and three analytical maximum-constant identities.

The finite exact checks compare the circular transfer with direct enumeration of every possible attempted/unattempted edge state. Expectation comparisons use both polynomial time integration and vertex-uncovered-event inclusion-exclusion; they share no transfer-matrix code. Numerical convergence checks are diagnostics, not certificates of asymptotic correctness. The infinite-size results rest on the analytic eigenvalue expansion, explicit far-tail bound, and dominated convergence in the accompanying proof. The 1995 nonidentical circular-runs article was not fully accessible, so historical priority is not externally certified.
