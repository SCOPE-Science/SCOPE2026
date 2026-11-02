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

## Reproducible checks
Run `python3 verify.py` using an unmodified Python 3 interpreter and the standard library. This checks character-orbit counts, all pairwise divisor intersections by exact polynomial elimination over \(\mathbb F_2\), symbolic root transformations and Cartier stable ranks over \(\mathbb F_8\) and \(\mathbb F_{16}\), and all five tangent directions at both \(\mathbb F_4\) special parameters. The expected final line is `VERIFY_OK`.

## Actual results
`INTERSECTIONS_OK`, `CHARACTERS_OK`, `GF(2^3)_OK`, `GF(2^4)_OK`, `TANGENTS_OK`, and `VERIFY_OK` were observed. Over \(\mathbb F_{16}\), 120 ordered parameters have rank \(40\), 60 rank \(38\), and two rank \(30\); no other smooth marked parameters exist in this field.

## Limits
The finite-field tests are consistency checks only, not proofs about all algebraically closed characteristic-two fields. The proof uses tame idempotents, genus-two ordinarity from a published complete type \((3,3)\) computation, symbolic Cartier identities and polynomial elimination for the universal parameter family. Independent audit has not been performed.
