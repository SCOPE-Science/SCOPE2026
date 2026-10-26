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

# Reproduction and limits

Run `python verify.py` with standard Python 3. It enumerates all cases described in `RESULT.md` and prints exact `certificate.json` content. Comparisons use rational numbers. Counts checked: 718 model instances, 5,140 threshold comparisons, 850 strict iid checks, and 28 higher-multiplicity counterfamily index pairs. The infinite result follows from the proof in `RESULT.md`, not computation. An external independent mathematical audit has not been performed.
