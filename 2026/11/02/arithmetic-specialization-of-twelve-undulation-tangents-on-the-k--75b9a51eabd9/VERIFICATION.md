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
# Exact mathematical verification

Run `python verify_reduction.py` with Python 3. No packages beyond the standard library are required. The code uses integer pairs to represent Gaussian integers and exact finite-field arithmetic to compute residue sections.

## Actual checks performed

The verifier executed successfully and emitted `KOMIYA_KURIBAYASHI_PRIMITIVE_66_SECTION_ARITHMETIC_AND_HERMITIAN_JUMP_OK` along with the exact norm and weight catalogues:

- Gaussian triple determinant norms: `{4:8, 20:48, 36:24, 40:24, 64:12, 80:48, 100:48, 200:8}`, counting exactly 220 triples.
- Inert prime 3: 30 singleton and 6 six-label primitive pair-section classes.
- Both primes above 5: 12 singleton and 6 nine-label classes, all 18 rational points on the reduced four-line quartic.
- Prime 2: 3 two-label, 3 four-label, and 1 forty-eight-label classes, all 7 support points explicitly checked.
- Every one of the 12 fourth-contact identities and both quartic special-fiber polynomial identities.
- Characteristic-three Hermitian 28-point polar tangent set and inclusion of the 12 specialized lines.

## Proof boundary

The full prime-uniform conclusion is based on the *complete* 220-triple norm factorization and the elementary prime divisibility implication. A single good-characteristic sample would not suffice. The complete characteristic-specific enumeration is finite and exact over the specified residue fields. The number of marked sections and their weights must not be identified with the scheme-theoretic local lengths of a flat limit without additional deformation theory. No independent external mathematical audit has been performed.
