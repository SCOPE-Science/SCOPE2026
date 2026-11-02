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

# Reproduction

Run `python verify_binary_sums.py` using Python 3's standard library. The program constructs degree-two through degree-eight binary finite fields from independently tested irreducible polynomial moduli, evaluates \(f_a(x)=x^5+ax^3\), enumerates all ordered pairs of graph points for every input difference, builds complete target multiplicity tables, and compares them with the stated formulas.

The executed check produced:

```
FIELD_OK m=2 q=4 modulus=0x7 coefficients=4
FIELD_OK m=3 q=8 modulus=0xb coefficients=8
FIELD_OK m=4 q=16 modulus=0x13 coefficients=16
FIELD_OK m=5 q=32 modulus=0x25 coefficients=32
FIELD_OK m=6 q=64 modulus=0x43 coefficients=64
FIELD_OK m=7 q=128 modulus=0x83 coefficients=8
FIELD_OK m=8 q=256 modulus=0x11b coefficients=8
VERIFY_OK independent_pair_enumeration=True coefficient_cases=140 full_coefficients=124
```

The tests are exact (integer and finite-field arithmetic, not floating-point), but finite. The statement for all extension degrees follows from the displayed linearized factorization and trace count. No external or independent audit is represented by these checks.
