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

# Mathematical verification

The reproducible symbolic script `verify.py` confirms the polynomial identity for \(\dot Q\), the Jacobian characteristic polynomial, the cubic center-manifold invariance equations, and the logarithmic drift coefficient \(2/b\). Its outputs are exact symbolic algebra, not a finite numerical approximation.

The global no-bounded-orbit assertion for \(\Delta<0\) follows analytically from monotonic \(Q\). At the boundary, the bounded-orbit convergence and compact two-sided invariant-set rigidity are established using square integrability, bounded derivatives and two-sided monotonicity. The cubic reduced dynamics and standard stable-foliation theorem together supply the asymptotic classification. A symbolic check alone does not certify the center-manifold theorem, the global convergence proof, or originality. Independent assessment has not been performed.
