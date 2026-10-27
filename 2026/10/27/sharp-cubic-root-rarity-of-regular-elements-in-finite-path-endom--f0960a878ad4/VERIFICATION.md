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

# Verification

Run `python3 verify.py` with Python 3 and its standard library. It constructs all nearest-neighbor maps on small paths, checks the recognized monotone-run characterization and, for small orders, the direct existence of a semigroup inverse witness. It then checks the explicit finite upper and lower spectral bounds and the finite variational approximation to the asymptotic rate.

Expected terminal line: `ALL_REGULAR_PATH_CHECKS_PASSED`.

Only complete finite configurations are called exhaustive. No finite execution can certify the asymptotic theorem or its novelty: these follow respectively from the proof and the literature comparison, with priority risks noted in the accompanying assessment. Independent audit is not performed.
