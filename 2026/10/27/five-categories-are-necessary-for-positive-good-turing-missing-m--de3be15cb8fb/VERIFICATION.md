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

The independent sample calculation is exact: sum over all ordered pairs of labels using their product probabilities, compute the realized unseen mass and the binary singleton estimate, and subtract the product of the means. The provided `check.py` uses only Python's standard-library `fractions.Fraction`, and checks its direct enumeration against the power-sum formula, including 2,444 exact-rational comparisons.

The infinite family of four-or-fewer-category laws is established analytically by the coordinate Cauchy–Schwarz bound, its cubic envelope, and a negative polynomial factor. The checker does **not** claim to exhaust arbitrary real probability vectors; it also does not independently verify historical priority. No independent audit has been performed.
