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

# Reproducibility and proof boundaries

Run `python verify.py` with the Python standard library. The script independently constructs the vertices of each regular polygon, computes intersections with a central line, resolves the two boundary arcs, and checks the exact analytic formula for integers \(3\leq n\leq37\) at eleven interior sample angles. It also checks exact-rational samples of the rational identity connecting edge-intersection parameters with the tangent-product expression, and the equilateral-triangle coefficient \(4/9\).

The complete proof for all \(n\) does **not** rely on a finite search: its indispensable steps are reduction to the fundamental angular sector, exact edge-intersection expressions, equality of the rational expression with \(\tan\alpha\tan(\pi/n-\alpha)/2\), and the strictly increasing cosine quotient. The checks do not independently certify novelty or any manuscript beyond these included files.
