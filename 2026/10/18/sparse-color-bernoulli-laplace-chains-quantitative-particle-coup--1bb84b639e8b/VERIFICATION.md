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

# Verification record

Run `python3 verify.py` from the folder containing this file. It uses only `fractions.Fraction` and the Python standard library.

It checks 1,680 exact finite-state parameter/time configurations, including exact hypergeometric transition probabilities, row normalization, the precise binomial proxy, the stationary hypergeometric-to-binomial error, and the stated total-variation difference bound.

The proof's general coupling inequality and the infinite triangular-array Gaussian limit are established analytically in `RESULT.md`; finite checks are supplementary and do not certify these universal claims. The cutoff window is lattice-aware. No independent audit has been performed.
