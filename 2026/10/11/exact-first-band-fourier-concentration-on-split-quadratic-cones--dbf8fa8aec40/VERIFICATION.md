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
# Reproducibility and limits

Execute `python3 CHECK.py` with Python standard library to reproduce exact rational matrix-block identities, invariant eigenvector relations, characteristic polynomials and direct Fourier Gram calculations in eight prime-field cases.

Expected summary: `VERIFY_OK prime_field_cases=8 Fourier_matrix_entries=1880 complete_block_decompositions=8 max_error=2.997e-16`.

The independent direct discrete Fourier calculations are finite checks; the character-sum derivation and invariant decomposition in `RESULT.md` establish all odd prime-power cases. This record contains no independent mathematical audit or external certification.
