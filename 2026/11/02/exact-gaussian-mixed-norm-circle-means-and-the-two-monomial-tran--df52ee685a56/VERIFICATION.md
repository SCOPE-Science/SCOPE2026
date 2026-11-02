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

# Verification and limits

The exact-rational checker was executed from its delivered package path with Python 3. It uses `fractions.Fraction`, `factorial`, and seeded finite test coefficient sequences. The execution returned PASS for 560 inequalities, 56 closed-form identities, 80 coefficient-support moment equalities, 16 endpoint identities, and the origin check. The experiment probes only finitely many degree configurations. The global proof rests on exact moment integration, strictly increasing successive ratios from strict log-convexity of positive moment sequences, positivity of all coefficients, and Cauchy--Schwarz.

The norm uses `4 * alpha` in the original radial integral and `2` in the transformed exponential moment integral; this normalization is essential. The result is proved only for angular exponent two and radial exponent four, for all positive Gaussian parameters and all radii. No external independent mathematical audit or certification has occurred.
