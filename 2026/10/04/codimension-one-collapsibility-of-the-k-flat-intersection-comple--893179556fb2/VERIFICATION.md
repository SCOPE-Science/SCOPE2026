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

The theorem was checked by reconstructing every implication in the proof.

1. **Slab classification.** From \(H=a+V\subset F\), the points \(x+v+t(a-x)\) lie in \(F\) for \(t\in(0,1)\); closedness gives \(x+v\in F\). Thus \(F+V=F\). Quotienting by \(V\) identifies \(F\) with a closed interval in one dimension.

2. **Uniqueness of direction.** Invariance under two distinct hyperplane directions would imply invariance under their linear span \(\mathbb R^d\), forcing \(F=\mathbb R^d\).

3. **Face decomposition.** A hyperplane contained in a proper slab must be parallel to the slab. Hence a face cannot use proper vertices from two direction classes. Within one class, faces are exactly intersecting subfamilies of the quotient intervals.

4. **Collapse step.** For an interval \(I\) with minimal finite right endpoint \(r\), every interval meeting \(I\) contains \(r\); therefore \(I\) belongs to a unique maximal face. If every remaining right endpoint is \(+\infty\), the block is a simplex. Universal vertices merely join to that unique maximal face and can be deleted last.

No numerical experiment, software theorem prover, or external certification is needed for the proof. The main limitation is bibliographic rather than mathematical: targeted searches found no prior codimension-one statement, but historical equivalent terminology cannot be ruled out exhaustively.
