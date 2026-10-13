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

The exact verifier `verify.py` uses symbolic polynomial arithmetic over the rationals.

It checks:

- the homogeneous quartic specializes to the source equation on \(Z=1\);
- the two affine projective patches are nonsingular, while the only point omitted by those patches is not on the quartic;
- \(X\mapsto-X\) preserves the quartic;
- with \(Y=X^2+T^2+1\), the quotient equation is \(Y^2=-T(T+1)(T+2)\);
- after \(s=T+1\), the quotient is the \(j=1728\) elliptic curve;
- the fixed-point polynomial has degree four and discriminant \(4257\neq0\);
- coefficient comparison for a general projective transformation fixing \(p=[1:0:0]\) forces away all \(X\)-shears;
- the residual binary-form symmetry equations have Gröbner basis \(u-s,v,w,s^2-1\), leaving exactly two marked projective symmetries.

A fresh replay from the packaged file prints `VERIFY_OK`. Finite computation is used only to certify explicit polynomial identities and the zero-dimensional stabilizer equations; the deduction from those identities to the stated global marked stabilizer is algebraic and exhaustive.
