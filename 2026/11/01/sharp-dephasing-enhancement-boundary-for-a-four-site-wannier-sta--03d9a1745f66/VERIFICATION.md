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

The self-contained `checker.py` computes the full four-site stationary moment system and an independent Hermitian-correlation representation. It checks exact identities using symbolic polynomial division, tests the strictly positive coefficients of the two derivative-certificate numerators (85 and 224 monomials), verifies the exact onset polynomial, and compares 150 independent parameter combinations.

The exact coefficient checks prove finite polynomial identities over the integers; the numerical comparisons are corroboration and are not used as a substitute for the global proof. The theorem applies to the specified four-site Lindblad model and not to chains of arbitrary length, non-linear potentials, or interacting extensions. Independent scientific audit has not yet been performed.
