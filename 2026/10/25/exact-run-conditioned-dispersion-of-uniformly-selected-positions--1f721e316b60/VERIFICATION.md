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

The standalone program `VERIFY.py` uses only the Python standard library; execute `python3 VERIFY.py`. Its printed check counts, as reproduced from the packaged program, are:

`{"conditional_groups_checked": 239, "exhaustive_covariance_checks": 78, "gap_moment_checks": 45020, "marginal_checks": 78, "pair_overlap_checks": 7137, "samples_enumerated": 16278, "strict_monotonicity_checks": 41860}`

The verifier performs exact-rational exhaustive subset enumeration for all \(N\le13\), independent exact overlapping-edge moment checks for \(N\le120\), and all possible run-count weak-composition moment checks for \(N\le80\). It confirms the displayed formulas and every covered boundary case. The verifier is not an exhaustive check of infinitely many sizes and does not establish the theorem without the analytic proof in `RESULT.md`. No independent audit has been conducted.
