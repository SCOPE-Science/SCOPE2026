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

# Reproducibility and scope

Run `python verification.py` using Python 3's standard library; no external dependencies or input files are required. A completed execution reported: "PASSED: 24 angle-ratio profiles, exact rational case checks, direct clipped-area integration, 72000 independent normal counts and 9 boundary-layer cases".

The checks independently reconstruct the six-normal chamber by clipping the original Cartesian triangle against both projection half-planes; they compare the computed area with the analytic fraction for six angles and four side-ratio pairs, check rational exact arithmetic when \(k=3/5\) and \(b/c=2/3\), and compare the predicted six-normal probability with 72,000 direct sampled point normal counts. They additionally test finite right-angle degenerating sequences and the exact hyperbolic-sine stability identity. The Monte Carlo tolerance is deliberately probabilistic and does not certify exact equalities.

The infinite-family conclusion relies on the analytic proof in RESULT.md and the 2024 source's planar critical-point classification. Independent mathematical validation was not performed.
