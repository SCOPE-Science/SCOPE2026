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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 with no external dependencies. The program implements exact polynomial Euclidean arithmetic over \(\mathbb F_5\), constructs irreducible field models of degrees one through four, checks the displayed factorization of \(h(s)\), verifies polynomial coprimalities and factor irreducibility, and uses a separately expanded \(f_1f_2\) square to reconstruct the Cartier--Manin entries. It checks all geometric root representatives over the degree-three and degree-four extensions, and exhaustively counts valid coefficient triples over \(\mathbb F_5\) and \(\mathbb F_{25}\).

Observed standard output:

```
full_coefficient_census F_5=4
full_coefficient_census F_25=24
normalized_nonzero_shift_roots [(5, 0), (25, 0), (125, 6), (625, 4)]
factorization_and_smoothness OK
VERIFY_OK
```

The script's finite enumerations do not prove statements in arbitrary extension degree by themselves; the symbolic Cartier elimination, coprimality and polynomial irreducibility in `RESULT.md` establish those assertions. Counts distinguish coordinate-marked triples, not isomorphism classes. No independent validation is represented by these checks.
