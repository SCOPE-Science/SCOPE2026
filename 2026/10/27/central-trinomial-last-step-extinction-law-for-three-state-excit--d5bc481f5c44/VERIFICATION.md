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
Run `python verify.py` with standard Python 3; no external packages are required. The direct simulator enumerates all initial words for 2 through 11 vertices, independently checks the last-step count and time bound, and the strict-ballot and power-series routines compare the proposed closed form for every size 2 through 42. Expected success marker: `PATH_GHM_FOUR_WAY_VERIFY_OK`.

The infinite-family assertion is established by the mathematical proof, not by finite simulation. No independent external audit has been performed.
