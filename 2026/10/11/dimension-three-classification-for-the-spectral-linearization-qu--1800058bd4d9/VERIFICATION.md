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
The theorem is proved analytically in `RESULT.md`. The accompanying `verify.py` is a finite algebraic replay, not a substitute for the arbitrary-matrix proof.

It checks:
- exact expansion of the sum of cubes of the six permutation pairings and factorization of the coefficient of \(\operatorname{tr}(A^3)\);
- the characteristic polynomial and discriminant formula for a zero-diagonal symmetric \(3\times3\) matrix;
- exact rational test cases for the explicit repeated-coordinate block construction.

The proof step that excludes the normalized distinct weight \(a=(1,0,-1)\) uses the symbolic fact that \(4(x^2+y^2)^3\) is not a square polynomial over \(\mathbb R[x,y]\), because \(x^2+y^2\) is irreducible and has odd exponent. The checker confirms the displayed discriminant identity but does not attempt to mechanize unique factorization.

No claim is made for dimensions \(d\ge4\).
