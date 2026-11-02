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

The analytic endpoint-route decomposition in RESULT.md establishes the universal statement. The two standalone Python 3 programs in `artifacts/` check the decomposition using exact rational arithmetic:

- `python3 artifacts/verify_metric_routes.py`: 266,256 edge-parameter route and detour comparisons on 16 small grids, together with exceptional-event counting and mean-sign checks.
- `python3 artifacts/verify_cdf_integrals.py`: 91 exact comparisons obtained from independent convex-polygon clipping and integration across seven grids (12 CDF thresholds and one mean per grid).

Both programs ran successfully after being written to their packaged paths. The small-grid checks are finite and do not replace the proof. Historical priority was assessed by literature search and source-text inspection, not independently certified. No external or independent mathematical audit has been performed.
