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

`verify_hexagon.py` uses only Python 3 and exact rational arithmetic. It confirms that the six cyclic rays enclose area \(1\), verifies the cone-linear values and gradients of \(q\) and \(f\), checks both convexity inequalities at \(\tau\in\{-1,0,1\}\) and \(\tau=1/2\), rejects the out-of-range values \(\tau=\pm3/2\), checks that the only integer point with \(q(z)<2\) is the origin, and checks the nonplanar equatorial vertex data. The mathematical proof establishes the complete continuous range \(|\tau|\le1\), the projection tiling, and the equality/vertex classification independently of finite tests.

To reproduce: `python3 verify_hexagon.py`. This is a self-review and rational certificate, not an independent audit.
