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

The proof establishes an exact identity between normalized projection moments and moments of weighted independent half-normal variables, proves that all orders of the requisite cumulants are nonzero using the transcendence of \(\pi\), reconstructs the positive facet-area multiset via Newton identities, proves generic lower-data nonidentifiability by a constant-term perturbation, and derives sharp \(1/d\)-Hölder instability at cubes.

The bundled standard-library script `verify.py` performs deterministic finite checks of normalized Gaussian moment-to-cumulant inversion in several dimensions, the critical cumulant nonvanishing for tested finite orders, spherical integration and projected-vertex convex hulls in dimension three, and constructed equal-lower-moment witnesses. These computations supplement the analytic argument and do not establish nonvanishing for arbitrary orders or exhaustive novelty. No independent audit or external certification has taken place.
