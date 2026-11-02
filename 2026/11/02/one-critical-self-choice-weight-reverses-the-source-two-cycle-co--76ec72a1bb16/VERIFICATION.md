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

# Verification of the finite claims

The standalone `verify_weighted_mapping.py` enumerates all maps for \(n=3,4,5,6\) at five exact rational self-image weights, computing source and directed-cycle counts from each mapping. Every mapping is weighted by the product of its self-loop weights. Exact-rational covariance values are compared to the analytically derived factorization for every cycle length at the tested parameters; the symbolic sign bracket is also compared. Additional rational sign checks range over higher finite values of \(n\). The checker was run successfully and reported:

`EXACT_TEST_PASS checks= 79610 sample_weighted_map_evaluations= 250320`

These are finite checks of a finite-sample law, not an infinite proof. The unrestricted result follows from the event calculation and strict inequalities in `RESULT.md`. The asymptotic limits follow by elementary expansion of the exact expression and are not inferred from numerical samples.
