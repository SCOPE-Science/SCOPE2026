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

The symbolic construction and proof are given in RESULT.md. Execute `python3 verify_optimal_fibres.py` in a Python 3 environment using only the standard library to reproduce the finite recurrence, oddness, certificate-majority, explicit low-degree cases and rational normalization. The output contains `VERIFY_OK`; it also contains `NORMALIZATION_OK`.

The finite checks do not prove measurable nonexistence or infinite divergence. Those rely, respectively, on parity rigidity and a Bernoulli cylinder approximation argument, and on the explicitly divergent geometric-scale degree lower bound in RESULT.md. The checker's finite truncations are not claims of exhaustive verification of infinite graphs. Independent audit is not yet performed.
