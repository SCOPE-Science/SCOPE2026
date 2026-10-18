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

Execute `python verify.py` from the package directory using standard Python 3. It checks the exact affine-height increment for a finite rectangular set of rational parameters and states; it also checks fixed points below and at the fold, with 498 exact checks total. The test does not use floating point arithmetic or external services. The closed-form proof in RESULT.md is required for the all-parameter and infinite-time statements. No independent mathematical audit has been performed; the status reflects a self-review only.
