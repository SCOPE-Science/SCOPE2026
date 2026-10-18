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
# Reproducibility and checks

Run `python3 verify.py` from the folder containing the reproduced files. The program uses only Python 3 standard-library modules. It evaluates two exact symbolic polynomial identities that serve as finite certificates for the full three-state first moment and nine-state second moment. It also enumerates all binary words through length 11 and checks fixed-composition rational-function coefficients, independently constructs all distinct scattered subsequences through length 9, and checks iid exact moment identities through length 31.

Expected final output:

```
VERIFY_OK: full word-set comparison n<=9; exact composition moments n<=11; iid formulas n<=31
SYMBOLIC_OK: exact 3-state and 9-state polynomial certificates
```

The exact polynomial identities are proved by substitution in a finite ring and imply the full formal-series theorem. Bounded enumeration corroborates the construction but is not itself an infinite proof. Source comparison gives qualified originality support, not independent validation or a universal literature completeness certificate. An independent audit has not been performed.
