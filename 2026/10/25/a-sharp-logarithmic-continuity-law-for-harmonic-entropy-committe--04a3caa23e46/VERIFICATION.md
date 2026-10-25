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

Run `python verify.py` in the package directory using Python 3.10+. The script evaluates the water-filling series exactly for rational inputs by detecting the full-support level and telescoping the infinite tail. It checks the conditional splitting identity on deterministic rational inputs with varying support sizes, all rational two-option splits in a specified range, and exact binary perturbation bounds on rational grids. Result: 4,826 passing exact-rational comparisons.

The independent mathematical justification is in RESULT.md. A finite program cannot certify the limiting modulus over all real inputs; that follows from the analytic total-variation and tail estimates. The manuscript's own concavity and water-filling propositions are cited for the specific lemmas used. The identities only concern the harmonic-entropy voter payment potential. They do not certify optimal committees or establish an independent audit.
