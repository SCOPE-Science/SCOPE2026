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

# Mathematical verification notes

The critical beta-function checks are \(B(\tfrac12,\tfrac32)=\pi/2\), \(M'_{3/2}(1)=\pi\), \(B(\tfrac32,\tfrac12)/(2-3/2)=\pi\), and \(c_{3/2}=2\pi\). The joint limiting normalized profile is \(F(x)=2^{3/2}\pi\sqrt{x}-2\pi x\), uniquely maximized at \(x=\tfrac12\) with value \(\pi\). These identities were verified from analytic formulas and numerical cross-checks; the uniform limit and global localization are proved in RESULT.md, not inferred from finite tests.

Run `python verify_bloch.py` with Python 3 and SciPy for independent computation of the beta identities, numerical radial maxima at several supercritical exponents, and the critical endpoint slope. The direct-integral and derivative calculations have finite numerical errors near the endpoint, so the table is corroboration only. Independent scientific audit and independent formal verification have not been performed.
