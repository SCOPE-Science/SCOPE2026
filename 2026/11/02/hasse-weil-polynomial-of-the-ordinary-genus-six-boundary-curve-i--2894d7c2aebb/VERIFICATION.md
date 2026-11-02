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
Run `python3 verify.py` from this package. The program requires only standard Python 3, uses explicit irreducible field moduli and polynomial arithmetic over \(\mathbb F_3\), checks every modulus by trial division, and traverses every finite-field element in the nine point counts. It independently counts solutions using the image of \(y\mapsto y^3-y\) and the trace criterion; it additionally repeats the degree-three and degree-six calculations over alternate field presentations.

Observed output includes:

```
COUNTS {1: 4, 2: 10, 3: 76, 4: 82, 5: 244, 6: 670, 7: 2188, 8: 6562, 9: 18868}
WEIL_COEFFICIENTS [1, 0, 0, 16, 0, 0, 118, 0, 0, 432, 0, 0, 729]
FACTOR_E [1, -1, 3] FACTOR_A2 [1, 1, -2, 3, 9]
JAC_F3 1296
VERIFY_OK
```

The general proof supplies the smooth genus, ramification contribution, degree-twelve Weil functional equation, quartic irreducibility and the translation-orbit argument. The enumerations certify the finitely many coefficients needed to reconstruct the exact polynomial. They do not purport to enumerate all extension fields, all possible twists, or all earlier publications.
