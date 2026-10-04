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

The bundled `verify.py` reconstructs the three quartics printed in Example 21 using sparse integer polynomial dictionaries and no third-party packages. It checks:

- \(F_0=X_1dq\) and \(F_2=d^2q\);
- \(F_1|_{d=0}=-2X_0X_1^3\);
- the Segre parametrization lies on \(q=0\);
- \(F_1\circ\psi=16s^3(u^2+2v^2)(2suv-tu^2-4tv^2)\);
- the three source quadrics for \(\mathcal C\) pull back to \(-2sh,-2th,0\);
- after \(X_3=X_0-d\), all three quartics have \((X_1,d)\)-order at least three and the minimum order is exactly three.

The reduced-support conclusion then follows from the two exhaustive factors \(d=0\) or \(q=0\), together with the displayed factorizations. The statement that \(M_\pm\) have no real points is the elementary consequence that \(u^2+2v^2=0\) has no nonzero real solution.

Limits: this verification does not compute a primary decomposition, embedded components, scheme multiplicities, a blowup, or a resolution of the rational map.
