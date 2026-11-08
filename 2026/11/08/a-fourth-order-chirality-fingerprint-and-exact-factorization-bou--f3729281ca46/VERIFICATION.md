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

# Verification details

The supplied `check.py` solves the four-by-four generator moment stationarity equations up to total degree four using a standalone Gaussian-elimination implementation (Python 3 standard library only), not by replaying the complex-number calculation in the proof. It checks 64 combinations of positive trap strength, propulsion speed and turn-rate pairs, two signed fourth-moment identities, second-moment isotropy, a zero mixed second moment, the exact square covariance, and invariance under three thermal-noise intensities. The program reports `PASS 1024 independent deterministic moment checks` when run successfully.

All tested parameters lie inside the theorem's admissible domain. This finite grid is not exhaustive and does not establish the infinite-parameter theorem or literature priority. The stated infinite-domain results follow from the generator equations and the exact rational simplifications in `RESULT.md`.
