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

# Reproducibility

Run `python check_cantor.py`. It checks exact rational strict inequalities underlying the tail and Taylor lower bounds, and separately evaluates Fourier product values for 20,000 integer frequencies as a non-probative check. Its expected success marker is `CANTOR_TWO_TIER_RATIONAL_CERTIFICATE_OK`.

The global classification is proved symbolically in `RESULT.md`: a triple-angle identity and unique leading-scale decomposition cover all arbitrarily large integers, while four finite residue cases are handled analytically. The program's finite sampling does not substitute for the global argument. There is no independent external validation.
