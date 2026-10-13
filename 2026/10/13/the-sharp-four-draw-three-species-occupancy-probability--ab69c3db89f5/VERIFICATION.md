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

# Reproducible checks

Run `python verify.py` with Python 3 standard library. The check prints `VERIFY_OK compositions=126 pair_split=36 m_uniform=100 max=72/125` after verifying exact rational event enumerations, two-mass split identities, and the sharp uniform support-size arithmetic. The analytic argument, not these finite checks, proves the result for arbitrary distributions and infinite exchangeable sequences. An independent audit has not been performed.
