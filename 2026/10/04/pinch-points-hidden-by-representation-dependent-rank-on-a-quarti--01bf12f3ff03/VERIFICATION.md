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

The exact verifier `verify.py` reconstructs both symmetric matrices and checks determinant equality, the gradient factorizations used for singular-locus exhaustion, projective Hessian rank \(3\) at the four isolated nodes, transverse Hessian rank drops at \(t^2+1=0\), the two pinch-point discriminant identities, the line-intersection discriminant identity, and the \(3\times3\)-minor rank behavior for both representations. It terminates with `VERIFY_OK` when all assertions pass.

The calculation is specific to this quartic over \(\mathbb C\); it does not classify all rational quartic symmetroids with double curves.
