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

# Mathematical verification notes

The proof uses only conditional first and cross-edge second moments and the shoelace identity. The off-diagonal cyclic correlations obey a tridiagonal closed recurrence; imaginary diagonal correlations are identically zero. The complete Fourier product is derived algebraically from the deterministic mean evolution.

The included `verify_polygon_area.py` checks an exact 512-path enumeration with pairwise-independent but not jointly independent splits, a heterogeneous four-step Monte Carlo experiment, finite regular-polygon and arbitrary-polygon spectral identities, and the fully correlated counterexample. Run with `python verify_polygon_area.py` using Python 3 and NumPy.

These checks are finite corroborations. All times and polygon orders are handled by the analytic recurrence; no external independent audit or historic novelty certification is asserted.
