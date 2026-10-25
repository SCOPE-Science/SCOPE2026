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

Run `python verify.py` from the package root. This checks direct solution/recursion agreement and the first-order pair formula for several deterministic jump configurations, including negative drift, signs and multiple jumps. The proof of stable convergence is the density/Fourier averaging argument in RESULT.md, not a finite simulation.

The archive makes no claim of independent audit or general MLMC validity.
