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

# Reproducible verification

Run `python verify.py` using Python 3.9 or newer. The verifier is dependency-free and constructs finite exterior algebras using bitmask bases and the actual alternating product (including product signs and repeated-generator annihilation). It enumerates every algebra automorphism of the two-generator exterior algebra over the prime fields of orders three and five, squaring substitutions by explicit composition. For three generators over the three-element field, it separately enumerates all \(3^6\) non-linear automorphism coordinates above a representative linear involution of each negative eigenspace dimension, then composes each and tests for the identity. It also checks closed-form exponents and their leading-degree cancellation for generator numbers two through fourteen.

Expected output includes `N2_EXHAUSTIVE [(3, [1, 36, 9]), (5, [1, 150, 25])]`, `N3_DIAGONAL_LIFTS [1, 27, 81, 27]`, and `VERIFY_OK`. These are exact finite enumerations, not randomized tests. They do not independently prove the full infinite family. The theoretical proof depends on the known automorphism group decomposition and the odd-order conjugacy-of-complements lemma. No independent audit has been performed.
