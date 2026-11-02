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

Exact mixed-volume section integration, Brunn--Minkowski, the published Godbersen inequality and its published equality characterization, and the Aleksandrov--Fenchel log-concavity inequality are the analytic proof inputs.

`python verify.py` uses the Python 3 standard library to check exact rational identities, binomial endpoint constants, variance contraction for coefficient profiles, and limiting ratios. `python check_polytope.py` uses NumPy and SciPy to compare explicit three-dimensional convex-hull difference bodies with the predicted quotients. A finite test cannot prove a statement quantified over arbitrary dimensions or bodies. The general result is proved in `RESULT.md`.

Independent mathematical audit: not performed.
