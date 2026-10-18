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
# Reproducible mathematical checks

Run `python verify.py` using a Python 3 standard library installation. The checker evaluates the frustum coefficient identities exactly over 1,050 dimension/index/ratio combinations, then reconstructs planar Minkowski-sum hulls by an independent monotone-chain algorithm and integrates their quadratic section areas using rational Simpson quadrature in 36 configurations. Its expected terminal marker is `VERIFY_OK`.

A separate development-time check constructed three-dimensional convex hulls of every pairwise vertex difference for the same 36 triangular, square, and pentagonal-base frusta. They matched the formula numerically to absolute error below \(10^{-8}\). This optional independent geometric test uses numerical hull software and is not required by the standalone checker.

The proof for arbitrary dimensions and arbitrary convex bases is analytical. Exact finite tests do not certify the global statement, and neither computation nor the self-review supplies independent external audit. The residual scientific uncertainty is bibliographic priority, particularly older mixed-volume literature and recent primary-source full texts that were not retrievable here.
