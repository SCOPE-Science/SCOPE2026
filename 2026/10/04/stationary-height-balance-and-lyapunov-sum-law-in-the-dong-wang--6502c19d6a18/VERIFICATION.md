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
The core polynomial identity was replayed exactly from the displayed vector field by the included dependency-free checker. The checker differentiates the polynomial observable \(Q=y^2+z^2\), forms its Lie derivative, and verifies coefficient equality with \(-2cy^2-2bz\). It also verifies the divergence \(-a-c+kz\) and the exact source-parameter arithmetic.

The invariant-measure step uses only the standard identity \(\int Lf\,d\mu=0\) for smooth \(f\) on compact support. The half-space obstruction uses the standard existence of an invariant probability measure on a compact invariant set. The Lyapunov-sum step uses Liouville's determinant identity and ergodicity; compact support supplies the needed integrability.

The source's finite numerical Lyapunov values are not used to prove any infinite-time statement. Their sum is reported only as a consistency illustration conditional on their asymptotic interpretation.
