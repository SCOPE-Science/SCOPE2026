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

# Verification

Execute `python3 check.py` from this directory. The program requires only the Python standard library and uses exact rational arithmetic for full finite-state edge-coverage probabilities. A completed run prints `OK: 864 exact-rational checks`.

The checked graphs include several complete bipartite graphs and odd cycles of lengths seven through thirteen. The checks cover the exact Stirling-number first-passage formula, sharpness of matching-based sampling, the minimum-edge-cover count, strict early reversal and later uniform dominance, and the odd-cycle marginal characterization. The sample of distributions and time horizons is finite and cannot establish the infinite theorem; that is proved by the symbolic argument in RESULT.md. No independent mathematical audit or external certification is claimed.
