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

Use Python 3 with dependencies in `requirements.txt`, then run `python verify.py`. In the checked environment it returned `VERIFY_OK checks=32, exact Smith, modular images and a direct quantum spectrum`.

The program performs six exact Boolean-zeta factorizations (through binary dimension six), two complete rectangular integer Smith-form checks, ten modular Smith-image predictions, nine independent single-context modular image enumerations with constant-intersection checks, six direct cut-image enumerations, and one normalized Hilbert-space density-spectrum calculation. The suite is a finite diagnostic for the analytical proof, not an exhaustive proof of arbitrary dimension or modulus. For composite local dimensions the character-sum derivation—not a prime-field rank shortcut—controls the spectrum.

No independent validation, external certification or expert review has been performed.
