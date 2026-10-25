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

The exact proof is in `RESULT.md`. The accompanying `verify.py` implements finite-field arithmetic in a polynomial basis, verifies every nonzero field element has an inverse, and exhaustively computes the number of solutions to each of the three coordinate-square equations over all \(q+1\) projective base points for \(q=3,9,27,81\). It also enumerates points in the full projective ambient space over \(\mathbb F_3\) and \(\mathbb F_9\) independently of the base-fiber method.

Actual executed command: `python3 verify.py`.

Actual outputs:
```
field_order= 3 curve_points= 4 elliptic_quotients= (4, 4, 4) genus_two_quotient= 4
field_order= 9 curve_points= 24 elliptic_quotients= (16, 16, 16) genus_two_quotient= 6
field_order= 27 curve_points= 28 elliptic_quotients= (28, 28, 28) genus_two_quotient= 28
field_order= 81 curve_points= 56 elliptic_quotients= (64, 64, 64) genus_two_quotient= 110
VERIFY_OK
```

These are finite exact checks of identified fields and models, not a finite enumeration of all extensions. Geometric smoothness, genus, finite-field zeta for all extensions, the group-theoretic prime-to-three isogeny, the ordinary factor, and the irreducibility claim depend on the arguments in `RESULT.md`. The same mathematical work was checked internally; independent audit and independent validation have not been performed.
