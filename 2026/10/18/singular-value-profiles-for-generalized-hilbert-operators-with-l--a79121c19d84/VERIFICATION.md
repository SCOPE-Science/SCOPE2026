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

The package contains `checks/lacunary_hilbert_checks.py` (Python 3 standard library, no dependencies). Run `python3 checks/lacunary_hilbert_checks.py`. The script validates the exact factorization coefficient identity for four Hadamard-gap degrees and exact positivity of the truncated Cauchy-kernel Gram matrix, both using `fractions.Fraction` arithmetic.

The verifier does not constitute proof of a Riesz basis property, an infinite integral formula, or any Schatten class criterion; those follow from the analytic proof in RESULT.md. No independent audit or external validation has been performed.
