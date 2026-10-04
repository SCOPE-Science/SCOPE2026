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

The proof is algebraic and asymptotic. `verify.py` uses exact symbolic algebra to substitute the claimed center-manifold jet into the five source equations at \(r=1\). It checks the coefficient equations that determine the cubic and quintic terms, the identity \(q=\sigma B\), and the rational specialization \(2c=15/22\), \(-q/c=9393/36784\) for \(\sigma=10\), \(b=8/3\), \(d=19/3\).

The checker does not prove existence of a center manifold; that is the standard finite-dimensional center-manifold theorem under the smooth polynomial vector field. It also does not certify a global rate. The long-time formula is proved analytically from the reduced scalar equation by setting \(W=\xi^{-2}\), obtaining \(\dot W=2c-2q/W+O(W^{-2})\), and integrating the resulting integrable remainder after the logarithmic counterterm.
