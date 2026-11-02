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

# Reproducibility and limits

Running `python3 check_entropy.py` with the Python standard library passed 5633 deterministic assertions. These include direct finite-state transition-matrix and stationary-law comparisons against the compact formula over many \(m,n,r\), checks of endpoint normalization, asymptotic optimizer-rate and gain diagnostics for fixed opposite part, corresponding diagnostics for proportional parts, and independent comparison rates.

The actual proof is in `RESULT.md`. In particular, global optimization requires the proved envelope bound and localization: finite numerical scans alone cannot establish an all-size or an asymptotic uniqueness statement. The result does not assert finite-size optimizer uniqueness. The comparisons with older literature are qualified, and an independent mathematical audit has not been performed.
