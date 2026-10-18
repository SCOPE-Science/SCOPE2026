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

# Reproducibility and limits

The embedded `check.py` uses a deterministic normal-coordinate quadrature to rederive cap-incidence probabilities from interval overlaps rather than from the arctangent formula alone. Cases include disks, ellipses, rectangles and triangles at three heights each. Other checks independently test Cauchy's mean width identity for polygons, positive Jensen deficit, rigorous curvature sandwich (via numerical evaluation), the local derivative formula, and the global one-dimensional optimization.

Run `python check.py` with Python 3, NumPy and SciPy installed. The checker prints the comparisons and ends in `PASS`. The exact universal statements are proved symbolically in RESULT.md and cannot be certified by finite numerical tests. Earlier circular-cylinder equations are prior results of Cruz-Orive (2026). The novelty comparison depends on the two inspected primary articles and published research summaries; absolute priority and independent mathematical evaluation remain open.
