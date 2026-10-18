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

The accompanying `verification.py` is a standalone Python 3 script requiring `sympy`, `numpy`, and `scipy`. Run with `python verification.py`. It performs symbolic cancellation of the drift and harmonic-mean formulas; 1,800 exact-rational substitutions into the actual five-equation differential system; four exact-rational equilibria at resonance; and 303 high-precision integration sample comparisons, including both signs of the drift and resonance.

The general claims are proved algebraically in `RESULT.md`. Finite samples do not establish global absence of invariant sets; the translation-invariant probability-measure argument supplies that step. No external independent validation has been performed.
