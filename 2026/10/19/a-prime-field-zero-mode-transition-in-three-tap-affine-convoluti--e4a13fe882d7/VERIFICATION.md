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

The theorem is proved by the complete irreducible decomposition of the affine group, one cyclic-permutation-plus-diagonal determinant, and an exact count of additive-character values. The multiplication and representation normalization are stated in RESULT.md. One-dimensional character values have modulus-based nonvanishing, and in the only singular regime the cyclic recurrence bounds the nonlinear kernel dimension by one.

The self-contained `CHECK.py` was run as `python3 CHECK.py` from its actual source path. It printed `PASS: 42 checks on q = 3,4,5,7,8,9,11.` It constructs finite-field arithmetic from irreducible polynomials, verifies affine-line permutation determinants with fraction-free exact arithmetic, verifies full regular matrices directly where feasible, compares larger regular determinants modulo distinct primes, and checks modular nullity ranks. The latter are finite corroborations, not certificates covering arbitrary fields.

Scientific limits: this is a specified-support three-tap theorem, not a general classification for all three-point supports. The research comparison does not establish publication priority, and no independent mathematical audit has occurred.
