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

# Reproducibility notes

Run `python verify.py` using Python 3 and the adjacent standalone source file. The program performs all computations with exact Python integers and residues, without dependencies or network access.

It independently verifies the eight exceptional-characteristic polynomial square identities, the three distinct quadratic centers in each example, the integer discriminant \(728^2\) of the relevant cubic, and irreducibility modulo three. For every prime from seventeen through six hundred, it checks that the cubic has either zero or three roots and verifies the four polynomial-square identities for every one of those roots. The observed run output is:

```
VERIFY_OK
exceptional_distinct_center_fields=2 (characteristics 5 and 13)
prime_fields_tested= 103 split= 33 inert= 70
exact_four_square_identities_tested= 396
polynomial_discriminant= 529984
```

The checker is finite and cannot prove the universal characteristic exclusion, finite-extension characterization, irreducibility over rational numbers, or natural density. Those facts are justified by the symbolic coefficient argument, rational root obstruction modulo three, finite-field splitting, and Chebotarev as written in `RESULT.md`. Independent external verification has not been performed.
