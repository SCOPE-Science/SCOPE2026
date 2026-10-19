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

`verify.py` performs exact-integer checks of 64 explicitly constructed five-site parameter pairs and an exhaustive **bounded** test of all one-to-four-point supports within ten sites, with four allowed nonzero coefficient values. It verifies coordinate magnitudes, aperiodic autocorrelations, and signed-reversal equivalence. The analytic support-size theorem does **not** follow from those finite checks; the general proof is given in `RESULT.md`. No independent scientific audit has been performed.
