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

The exact package checker `verify.py` uses standard-library rational arithmetic. It substitutes the standard Lorenz parameters \(\sigma=10\), \(\beta=8/3\) into the center-manifold graph, checks the invariance equations through the required orders, and checks the derived coefficients \(2c=15/22\) and \(-q/c=609/1936\). The recorded output is `VERIFY_OK`.

The infinite-time asymptotic is not inferred from a finite trajectory. Analytically, \(W=\xi^{-2}\) satisfies \(\dot W=2c-2q/W+O(W^{-2})\); after \(W=2ct+O(\log t)\), the derivative remainder in \(W-2ct+(q/c)\log t\) is \(O((\log t)/t^2)\), which is integrable.

Limits: the verification is local at \(\rho=1\), assumes a sufficiently smooth center manifold, and does not certify a global basin or an entrance-time estimate.
