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

The associated `verify.py` uses Python's standard library only. It checks the original matrix-projection residual against the derived angular expression, directly scans time grids, performs independently discretized angular CDF/expectation checks, tests unequal partitions against the equal-length optimum, verifies the strictly concave refresh-count optimizer numerically, and checks the exact one-versus-two crossover. Run `python verify.py` after extracting it from this finding's embedded files.

The argument for every angular length and singular-value ratio is analytic, not inferred from a finite mesh. Numerical time scans approximate rather than prove a continuum supremum. Numerical integration tolerances and discrete integer searches cannot exclude all exceptional parameter combinations. This report is a reproducibility check and supplies no external or independent audit.
