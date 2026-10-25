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

## Mathematical checks

The support function is obtained exactly from the vertex set:
\[
H(\phi)=\max\{0,2\cos\phi,\cos\phi+\sin\phi,\sin\phi\}.
\]
The edge support numbers are \(0,\sqrt2,1,0\). The nonnegative-dependence cone of the four edge normals has the two extreme generators \(n_b+n_t=0\) and \(n_b+\sqrt2n_r+n_\ell=0\), which yield the exact containment thresholds \(W(t)\) and \(Q(t)\).

The width branches are checked on the full angular domain modulo \(\pi\). The set on which \(W(t)<3/\sqrt5\) is covered by the three stated intervals; on each, \(Q(t)\geq3/\sqrt5\). At \(t=2\pi-\arctan(1/2)\), both thresholds equal \(3/\sqrt5\). The other boundary points have a strictly larger \(Q\), establishing uniqueness of the minimizing axis.

No numerical sampling is used to prove the infinite family of orientation inequalities. The conclusion is limited to the specified trapezoid. Independent audit and independent validation remain unperformed.
