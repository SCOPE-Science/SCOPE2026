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

# Numerical checks and analytical limits

Run `python verify.py` with the packages specified in `requirements.txt`. The standalone checker computes matrix exponentials of the symmetric two-state telegraph generator, the normalized Choi matrix and its partial transpose, and numerical maximizers of the lobe critical-rate functions. It then checks the theorem's closed formulas on finite parameter sets.

Recorded result for the packaged checker:

`VERIFY_OK telegraph_expm=40 choi_ppt=84 threshold_bounds=144 weak_noise_counts=4 static_counts=3 lobe_grids=56 max_telegraph_error=6.66e-16`

The checker does not evaluate an infinite number of oscillation lobes and cannot certify all-rate monotonicity or the asymptotic remainder. Those results rely on the explicit inequalities and log-concavity argument in `RESULT.md`. The finite grid checks near a lobe threshold omit inconclusive numerically tiny intervals; they cannot prove an interval absent by themselves. The Bell-state partial-transpose calculation checks a physical consequence of the full channel characterization but is not an independent audit.
