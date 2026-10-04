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
# Verification

The exact symbolic checker `verify.py` works over the polynomial ring \(\mathbb Q[a,b,c,d,e,f]\), which is valid for the displayed identities and for the characteristic-zero representative of the characteristic-not-two proof.

It checks:

1. the determinant of the zero-diagonal symmetric \(4\times4\) matrix equals the stated quartic \(F\);
2. all six partial derivatives have the three claimed factors;
3. each of the eight coordinate planes annihilates \(F\) and all six partial derivatives;
4. each of the three quadric ideals reduces all six partial derivatives to zero;
5. the normal Hessian determinant along the representative plane \(V(f,e,d)\) equals \(-32a^2b^2c^2\), hence is nonzero generically when \(\operatorname{char}(k)\neq2\);
6. the exact identity \(F=(af-be-cd)^2-4be\,cd\) used for the representative quadric local normal form;
7. the simultaneous equations \(af-be-cd=af-be+cd=af+be-cd=0\) force \(af=be=cd=0\) when \(2\) is invertible.

A successful run prints `VERIFY_OK`. The global component count is not inferred from sampling: the proof exhausts projective singular points by which of the three opposite coordinate pairs are zero. The checker does not attempt to determine embedded components of the Jacobian scheme or local analytic types at intersections of singular components, and the claim makes neither assertion.
