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

# Computational verification and limits

The proof in `RESULT.md` works for every odd prime-power \(q\) and is logically independent of these finite checks. Run the two complete embedded scripts directly (both depend only on Python plus the listed numerical/symbolic library):

```sh
python symbolic_certificate.py
python paraboloid_frame_check.py
```

The symbolic checker verifies exactly, using SymPy, the residual characteristic polynomial identity, the cubic discriminant, the resultant excluding collisions with the two-dimensional block, and the boundary polynomial values. Its observed output was:

```
SYMBOLIC_CERTIFICATE_OK determinant_cubic resultant discriminant boundary substitutions
```

The numerical checker constructs the additive characters and full normalized coefficient Gram directly in the prime fields of orders \(3,5,7,11,13,17,19,23\) and explicitly realized quadratic extension fields of orders \(9,25\). It compares complete multiplicity-expanded spectra and checks nullities in the exceptional small fields. Its observed output was:

```
VERIFY_OK fields= [3, 5, 7, 11, 13, 17, 19, 23, 9, 25] total_columns= 376 max_eigenvalue_deviation= 3.33e-15 small_field_singularities=PASS
```

Numerical floating point accuracy does not certify exact equality, and finite examples are not exhaustive over finite fields; infinite validity relies on the stated character orthogonality and Hermitian block reduction. The proof excludes general mixed frequencies, even-characteristic fields and unrelated quadratic varieties. Independent audit: not performed.
