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

Run `python3 verify.py` with standard Python 3 and no third-party dependencies. The execution in this record returned:

`VERIFY_OK direct_series_checks=18 tail_asymptotic_checks=12 all_checks=31`

The program compares inverse Laurent-mode norms against the transformed exact positive series for 18 finite parameter pairs, and checks 12 larger-order ratios against the proved leading scale. The final additional check tests the zero-mode normalization. It is not an exhaustive theorem prover and cannot establish an infinite-series identity, the Stein property, or global parameter-space continuity. Those require the written proof in RESULT.md. No independent mathematical audit has been performed.
