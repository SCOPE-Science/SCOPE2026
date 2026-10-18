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

# Verification record

Analytic proof: the containment inequalities hold for all factor polar directions. A positive transferred John decomposition proves unrestricted ellipsoid optimality in every finite dimension. Contact classification follows by equality in the same support bounds.

Reproducible exact check: `python verify_free_join.py` passed all 360 dimension vectors having 2–5 factors, each of dimension 1–3, using rational arithmetic. It checked covariance positivity margins, the barycentric projection identity, every selected cube-factor contact norm, and full first and second moments without floating-point tolerances.

Limits: finite symbolic tests are supporting evidence, not an exhaustive geometric check. The proof invokes the standard John criterion for arbitrary convex factors. Independent audit is not performed; bibliographic novelty retains the stated residual risk.
