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

Run `OPENBLAS_NUM_THREADS=1 python check.py` with NumPy and SciPy installed. The checker assembles the weighted-path Green inertia and independently diagonalizes long finite free-ended chains, tests the analytic contiguous ceiling across 60 configurations, and verifies spectral count monotonicity for 28 parameter modifications. At packaging time its output was `PASS: 104 independent count/formula/monotonicity checks`. The source code is embedded separately.

The full theorem concerns the infinite chain: finite windows alone cannot exclude eigenmodes arbitrarily near the acoustic band. The strictly monotone Birman--Schwinger proof and the band-edge pseudoinverse reduction establish the infinite statement and threshold equalities. No independent audit has been performed.
