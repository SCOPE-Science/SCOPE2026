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

The embedded `verify.py` needs only Python 3 standard-library modules. Run `python3 verify.py`. It enumerates all smooth ordered parameters over fields with \(5\), \(25\), and \(125\) elements, independently evaluates the \(2\times2\) Hasse determinant, checks the parametrizing equation, and tests the nilpotence of the rational exceptional matrix.

Observed output:

```
F_5: smooth parameters=13, nonordinary=1, prediction=1
F_25: smooth parameters=553, nonordinary=19, prediction=19
F_125: smooth parameters=15253, nonordinary=121, prediction=121
VERIFY_OK
```

The code is a finite consistency check, not a proof of the all-characteristics statement. The general characteristic-five formula is established by the symbolic determinant, reciprocal-quartic squarefreeness criterion, and isomorphism of the divisor with a punctured rational line. This file makes no independent-validation claim.
