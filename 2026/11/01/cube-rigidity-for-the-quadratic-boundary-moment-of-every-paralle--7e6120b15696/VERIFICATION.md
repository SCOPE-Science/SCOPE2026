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

# Reproducibility and limitations

Run `python verify.py` with Python 3 using the standard library. The program performs 11,000 exact integer/rational polynomial checks for the eight relaxed-box vertices and three interior points, verifies the three-pair sum-of-squares identity, and checks 699 geometric cases by direct facet Gaussian quadrature versus the independent integrated-moment expression. Randomized inputs use a fixed seed; the final geometric test is a cube equality example. The analytic proof supplies the universal quantifiers and the equality classification; no finite numerical sweep proves them. Every surface is centered at its central-symmetry point, which is also the Euclidean surface centroid.

Historical priority remains provisional; the earlier cuboid theorem and the current weighted-perimeter paper were both read directly. Independent mathematical audit: not performed.
