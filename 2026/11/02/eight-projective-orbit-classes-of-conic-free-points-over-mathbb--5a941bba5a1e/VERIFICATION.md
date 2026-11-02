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

## Reproducible finite checks
Run `python3 verify_f64_conics.py` (Python 3 standard library). It must print `F64_QUADRATIC_ORBIT_CENSUS_PASS`. Every field element is a 6-bit polynomial modulo `0b1000011`. It proves the modulus irreducible via binary polynomial Frobenius and gcd tests; verifies all nonzero elements are invertible; enumerates each of 4096 affine points; cross-checks rank six against direct evaluation of all 63 binary conics; enumerates each of 512 candidate binary projective matrices, retaining 168 invertible ones; classifies all 1344 conic-free points into eight disjoint 168-element orbits; computes the exact Frobenius permutation and its cycle lengths. The witness is additionally verified symbolically in RESULT.md.

## Limits
These are exhaustive finite computations over a specific field, not a proof for other fields or degrees. No independent external audit or certification is represented here.
