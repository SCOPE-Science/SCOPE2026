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

The source equation used is the fourth equation of the published dimensionless System (12):
\[
\dot u=\alpha d\left(e^{-u/(2n)}\cosh\!\left(\frac{x}{2n}\right)-1\right).
\]
For \(R=e^{u/(2n)}\), the identity \(e^{-u/(2n)}=R^{-1}\) and the chain rule give
\[
\dot R=\frac{R}{2n}\dot u
=\frac{\alpha d}{2n}\left(\cosh\!\left(\frac{x}{2n}\right)-R\right).
\]
The bundled `verify.py` checks this reduced algebra with exact rational arithmetic for multiple nonzero rational test values and verifies the coefficient \(1/(8n^2)\) in the quadratic lower bound inherited from \(\cosh r\ge1+r^2/2\).

The infinite-past representation and \(u\ge0\) recurrence barrier are proved analytically by variation of constants on bounded complete trajectories. They are not inferred from finite numerical integration. The invariant-measure identity uses stationarity of the smooth observable \(R\) on compact support.

Limits: the check and proof cover the unshifted capacitor-only model with \(n>0\) and \(\alpha d>0\). They do not establish existence of a compact invariant set or boundedness for arbitrary initial data, and they do not cover the source's later offset-boosted variants without re-derivation.
