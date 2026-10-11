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

The symbolic verifier `verify_yang_chen.py` was executed from the packaged source directory and returned `VERIFY_OK`.

It checks the exact Lie derivatives
\[
L_F(x^2/2)=a(xy-x^2),\quad L_F z=xy-bz,
\]
\[
L_F(y^2/2)=cxy-xyz,\quad L_F(z^2/2)=xyz-bz^2,
\]
eliminates the stationary moments, verifies \(\int z^2\,d\mu=c\bar z\), and factors the variance as \(\bar z(c-\bar z)\). It also checks the algebraic outer-equilibrium condition \(x=y\), \(z=c\), \(x^2=bc\).

The verifier does not certify existence, ergodicity, physicality, or stability of any attractor. Those are outside the claim.
