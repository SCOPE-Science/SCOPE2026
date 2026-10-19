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

# Reproducibility and verification

`checker.py` runs with Python 3 and `mpmath`. It checks exact coefficient telescoping and the derivative-coefficient difference identity for every integer \(1\le n\le150\); it also checks the limiting differential equation at a high-precision computed zero, and evaluates nearby polynomial zeros at five degrees. These finite computations completed successfully.

The proof in `RESULT.md`, not the code, establishes nonvanishing in the left half-plane, existence and simplicity of limiting zeros, vertical-strip exclusion, inverse-degree localization of *all* candidate minimum-modulus polynomial roots, and the \(O(n^{-2})\) global radial remainder. There is no numerical certificate for which limiting zero has minimum real part; the exact theorem does not require identifying that index.

Full-text access to the old Love (1949) paper was not obtained. Scientific historical priority is not exhaustively certified. Independent audit has not been performed.
