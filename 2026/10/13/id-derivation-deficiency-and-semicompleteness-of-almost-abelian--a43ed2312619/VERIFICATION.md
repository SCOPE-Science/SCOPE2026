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
# Reproducibility and boundaries

Run `python3 verify.py` from a directory containing the standalone program. It uses Python's standard library only. Successful output includes `ALL_BINARY_ENDOMORPHISMS_DIMENSIONS_AND_SEMICOMPLETE_BOUNDARY_OK`, `PRIMARY_COMPONENT_DIMENSION_EXAMPLES_OK`, and `VERIFY_OK`.

The script solves the commuting and image equations directly by modular Gaussian elimination; the exhaustive binary cases comprise all matrices of orders one, two, and three. Characteristic-three and specific higher-dimensional binary examples are independently tested. These finite checks are not proofs for general fields or dimensions. The general result follows from the symbolic derivation-identity argument, the elementary-divisor Hom formula, and the three-case semicompleteness proof in `RESULT.md`.

The 2026 motivating source's complete text could not be inspected through the available public access route. An independent originality audit has not been performed.
