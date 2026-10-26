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

# Mathematical verification

The standalone artifact `check_wiman.py` (Python 3 standard library only) checks coefficient equality between the integral sextic reduced modulo five and \(x^2y^2z^2+2(x^2+y^2+z^2)^3\), via exact coefficient dictionaries. It then enumerates every projective point over \(\mathbb F_5\) and over the explicit quadratic field \(\mathbb F_5[t]/(t^2-2)\), checking that the respective curve counts are \(10\) and \(22\). It explicitly verifies the ten \(\mathbb F_5\)-rational gradient-zero points, confirms that the node tangent discriminant is the nonsquare \(3\), and verifies the local coordinate change to \(U^2+2V^3\) at the cusps has nonzero Jacobian determinant \(3\).

Run from the unpacked finding directory:

```sh
python3 check_wiman.py
```

A successful run ends in `CHECK_OK`. Finite enumeration cannot establish irreducibility or exclude singular points over algebraic closures; those are proved by the Kummer independence and geometric Jacobian arguments in `RESULT.md`. The normalization and zeta conclusions rely on the algebraic delta and Frobenius-branch argument, not on an extrapolation from the two enumerated fields.

No independent audit has been performed.
