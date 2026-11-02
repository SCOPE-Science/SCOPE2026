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

# Finite reproducibility checks and mathematical limits

Run `python verify.py` with Python 3 and no third-party packages. The script independently enumerates simultaneous self-essential inverted-threshold updates on every binary action configuration for all \(19{,}432\) threshold vectors on the complete bipartite graphs \(K_{a,b}\), \(1\le a,b\le3\), with thresholds in the range zero through degree plus one. There are \(1{,}111{,}428\) individual binary configurations examined. It compares the exact equilibrium pairs with the closed-form condition and checks the asserted maxima. It separately checks \(1{,}010\) constructed threshold assignments representing every target equilibrium count for \(1\le a,b\le15\).

These computational checks are finite corroboration; the all-orders upper bound and attainment assertions follow from the local compatibility, two-unit separation and explicit construction in `RESULT.md`. No independent third-party review or infinite computation is claimed.
