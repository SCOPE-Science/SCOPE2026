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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. No third-party libraries, network access, random seeds, or precomputed tables are needed. The script builds multiplication and addition tables for prime fields and quadratic extensions using an explicit nonsquare polynomial, computes every input value for each selected coefficient configuration, and compares exact integer totals with the rational formulas.

Observed completion:

```text
PASS field 7 cases 7 nonsquare 3
PASS field 11 cases 11 nonsquare 2
PASS field 13 cases 13 nonsquare 2
PASS field 17 cases 17 nonsquare 3
PASS field 19 cases 19 nonsquare 2
PASS field 23 cases 23 nonsquare 5
PASS field 29 cases 29 nonsquare 2
PASS field 31 cases 31 nonsquare 3
PASS field 49 cases 49 nonsquare 8
PASS field 121 cases 3 nonsquare 12
PASS all original leading-coefficient pairs over GF(7)
PASS all original leading-coefficient pairs over GF(11)
PASS interpolation subsets 7
PASS interpolation subsets 11
PASS interpolation subsets 13
PASS interpolation subsets 17
VERIFY_OK configurations= 372 input_evaluations= 13427430 subset_tests= 11418
```

The last four subset checks use a separate combination-based count of the four- and five-point interpolation constraints; they do not evaluate the quintic maps. The verifier also tests translation normalization by enumerating all original fixed leading-coefficient pairs over two fields. This finite test suite does not prove the statement for arbitrary prime powers. The general proof uses root factorization, partition Möbius inversion, nondegenerate quadratic-form representation counts and elementary character algebra.
