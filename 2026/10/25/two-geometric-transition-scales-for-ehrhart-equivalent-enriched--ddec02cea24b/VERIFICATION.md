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

# Reproduction and limits

Run `python verify_enriched_metrics.py` with Python 3, NumPy and SciPy. The standalone script recomputes vertices directly from the two-cube construction, checks the complete facet inequalities and affine ranks, convex-hull volume and surface area, inball distances, enclosing-ball contact counts, 518 direct support evaluations and independent numerical asymptotic diagnostics. Its successful run ends with `VERIFY_OK`.

The analytical proofs in `RESULT.md` establish the results for every integer pair of sizes at least two and the stated asymptotic regimes. Enumeration and Monte Carlo comparisons are checks only, not proof of infinite-dimensional limits. No independent mathematical validation has been performed.
