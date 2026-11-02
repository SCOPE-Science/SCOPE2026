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

# Reproducibility and proof boundary
Execute `python3 verify.py` with standard Python 3. The checker enumerates the reciprocal image sets and tests their equivalence to the proposed discriminant indicator, computes every Gram entry in each tested field, and checks the multiplicative-character Fourier diagonalization by direct matrix multiplication. It uses explicit irreducible field polynomials for nonprime fields and tests sixteen fields including orders \(9\), \(25\), \(27\), and \(49\).

The observed execution is:

```text
VERIFY_OK finite_fields= 16 individual_columns= 181 incidence_entries= 5112 square_character_spectra=validated
FIELDS 3,5,7,11,13,17,19,23,29,31,37,41,9,25,27,49
```

All general claims are proved algebraically in `RESULT.md`; exhaustive finite enumeration does not prove arbitrary prime-power cases. The complex arithmetic used for tested character eigenvectors is numerical, whereas the symbolic proof uses exact character orthogonality and Jacobi sums. Independent review has not been performed.
