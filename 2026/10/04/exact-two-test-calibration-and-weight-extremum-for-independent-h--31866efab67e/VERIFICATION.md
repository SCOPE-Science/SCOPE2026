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
The analytic verification uses the exact region for \(H_w>h\) and a one-dimensional integral. A standalone numerical checker independently compares the closed form with quadrature at multiple \((h,w)\) pairs, verifies the symmetry \(w\leftrightarrow1-w\), checks strict increase toward \(w=1/2\) at \(h=0.05\), confirms the published equal-weight specialization, and solves the exact \(5\%\) cutoff equation.

The numerical checks are finite corroboration only. The universal statements for all \(0<h<1\) and \(0<w<1\) follow from the symbolic integration and derivative argument in RESULT.md. No computation establishes novelty; that assessment rests on the literature comparisons in REVIEW.md and AUDIT.json.
