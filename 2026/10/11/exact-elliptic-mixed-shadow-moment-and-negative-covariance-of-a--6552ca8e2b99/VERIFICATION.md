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

# Reproducible verification
Run `python3 verify.py` in the directory containing that file. It uses only the Python standard library. The certificate constructs rational intervals for square roots, both trigonometric constants, \(\pi\), and a finite alternating binomial sum, enclosing the integral with an analytic remainder. The resulting rational interval for covariance lies strictly between \(-0.0004\) and \(-0.0003\); no floating-point result is trusted for the sign.

The script separately computes 400 planar convex hulls from projected tetrahedron vertices and compares direct shoelace area and edge perimeter with the normal/edge formulas. It also approximates the final one-dimensional integral using 200,000 midpoint nodes as a diagnostic. Random samples and quadrature alone cannot establish an all-directions identity or certify a sign; those conclusions depend on the analytic derivation and rational bounds. The numerical sample is deterministic by fixed pseudorandom seed, not a probabilistic confidence claim. No independent external audit was performed.
