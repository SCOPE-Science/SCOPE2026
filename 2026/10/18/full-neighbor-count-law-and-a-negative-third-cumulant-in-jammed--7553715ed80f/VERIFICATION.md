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
# Reproducibility and verification

The exact analytic proof is in `RESULT.md`. Run `python verification.py` after installing the versions in `requirements.txt`. The script verifies symbolic covariance/cumulant and inequality identities, an exact cubic generating polynomial, several degree-wise numerical quadratures, finite-tree greedy adsorption simulations with fixed random seeds, and the high-degree logarithmic ratio.

The infinite-volume construction uses finite dependence cones; no finite sample or symbolic check of one degree is substituted for the all-degree proof. A finite-depth tree is only a boundary-affected approximation of the infinite regular tree. The verification does not certify priority uniqueness, independent review, robustness to nonregular graphs, or long-time physical kinetics beyond the defined one-shot arrival model.
