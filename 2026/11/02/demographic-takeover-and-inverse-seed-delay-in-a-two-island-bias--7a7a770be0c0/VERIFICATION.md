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

# Verification notes

The self-contained Python 3 standard-library checker `check.py` is the only executable dependency. Execute `python3 check.py` inside the extracted package directory. The expected terminal line is `VERIFY_OK assertions= 1172`. It verifies exact fractions for initial drift thresholds, the one-island corner map and reciprocal time increments, plus deterministic trajectory tests of the critical inverse-seed coefficient.

The mathematical proof is independent of finite testing. Its essential equalities are the exact drift sign \(\mathcal B(z,s)-z=z(1-z)(2s-1)/[zs+(1-z)(1-s)]\) and the reciprocal critical increment \(1/v_t-1/v_{t+1}=2(1-v_t)(v_t-e_t)/[v_t(1-e_t+v_t)]\). These yield, respectively, the endpoint-including consensus cases and the logarithmically controlled correction to inverse-seed critical waiting time.

The theorem proves existence of a polarized basin in the middle ratio interval, not that every initially opposed state polarizes there. It assumes strictly interior initial opinions, equal bias exponent one, two internally homogeneous islands, and positive fixed mixing coefficients. It makes no independence, third-party certification, or empirical performance claim.
