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
The claim is verified analytically from the source event definition. At \(z=0\), the event has probability exactly \(1/2\). For \(z>0\), division by \(z\) converts the two random inequalities into the interval \(-z\le q^{\xi}\le\rho/z-z\). Strict monotonicity of the standard Gaussian CDF gives the exact least feasible boundary \(g(z)\). Its radial ratio diverges because the inverse-CDF argument tends to one as \(z\downarrow0\). This supplies the required infeasible convex-combination points without numerical approximation.

A decimal illustration in RESULT.md is explicitly non-proof evidence. The mathematical conclusion does not depend on floating-point evaluation, finite enumeration, or an external certificate. The proof does not establish any statement for \(p>1/2\).
