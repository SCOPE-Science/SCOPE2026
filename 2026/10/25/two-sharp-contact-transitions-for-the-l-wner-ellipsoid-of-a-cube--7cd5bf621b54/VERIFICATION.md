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

The script `verify.py` is a standalone standard-library implementation. Run `python3 verify.py` from the directory containing it. The actual run returned:

`PASS exact rational configurations 50022 regime_counts [43083, 5543, 1396] random_vertex_checks 4200`

For each exact case the script tests the three ellipsoid parameters, exact apex and cube-vertex orbit inequalities, equality classifications, admissible design weights, exact mean and covariance identities, and positivity. The additional vertex checks use seeded pseudorandom cube vertices. These are finite diagnostics only. Global optimality for arbitrary ellipsoids is established by the analytic trace–determinant proof, not by finite experimentation. The literature-priority comparison is not an independent validation.
