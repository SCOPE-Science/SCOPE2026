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

# Verification and reproducibility

Execute the standalone Python 3 file `check_signed_words.py`. Successful completed run emits `SIGNED_COPY_REVERSE_EXACT_OK 548 endpoint_and_local_tests`. It checks exact endpoint distributions against sign templates, injectivity of seed encoding and deliberately constructed interior-saturated examples at finite sizes.

The checker does not enumerate all natural numbers or prove general Hanf locality. The infinite result depends on the precise probability calculation and the exponential binomial bound for independent disjoint seed windows, together with the standard finite-degree effective Hanf theorem. It is important that the checker only supports finite premises of the proof, and there has been no independent verification.
