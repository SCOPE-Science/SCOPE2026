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

# Reproduction and proof boundary

The included `verify.py` implements the scalar spectral-root equation and the left Perron-vector recurrence independently of any saved computational logs. It checks normalization, the finite open-Markov eigenrelation, escape mass, the root equation, and the sharp critical harmonic-proxy comparison for a range of fixed parameters and finite truncations. Execute `python3 verify.py` from the directory containing this file. The observed result was `VERIFY_OK`.

The theorem for all cutoffs and for its weak limits is established by the four analytical steps in `RESULT.md`. These tests are finite-dimensional regression checks and do not certify the infinite limits independently.
