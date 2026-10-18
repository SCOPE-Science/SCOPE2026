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
# Verification

The analytic proof in `RESULT.md` supplies the quantified claims. From the source directory, run `python3 verify.py` using the Python standard library. It verifies the characteristic identity with rational arithmetic, the Perron transition/stationary identities, the low-temperature spectral coefficient, the golden-ratio stationary weights, binary matrix rigidity, and representative rescaled transition probabilities.

Finite experiments do not establish the infinite-temperature limit, the universal binary theorem, or novelty; these depend on the derivation and literature comparisons in `RESULT.md` and `REVIEW.md`. The zero-temperature construction is a full three-symbol shift with a one-step cost potential, not a higher-memory or infinite-alphabet model. The selection coefficients are known in a different nonlocally constant setting.
