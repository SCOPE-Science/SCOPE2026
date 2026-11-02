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

The proof consists of rank normalization, the four exact matrix-block equations, a count of square-zero square blocks by image/kernel flags, a rank stratification of the projected off-diagonal block, and a final quotient-space count of the remaining off-diagonal block. The proof does not infer an infinite statement from finite samples.

`verify.py` is self-contained Python 3 and evaluates the original triple matrix product entrywise. It checks 16 canonical matrix sizes/ranks/fields, plus three noncanonical rank-one sandwich matrices, and four independent rank-one inclusion-exclusion identities. The full output marker is `SANDWICH_SQUARE_ZERO_OK 19 exhaustive matrix cases; 4 component counts`.

Explicit cases include \((m,n,r,q)=(3,3,2,2)\), with exactly \(44\) square-zero elements, and \((2,2,1,4)\), with exactly \(28\). For arithmetic in the four-element field the checker uses \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\); it does not confuse this field with \(\mathbb Z/4\mathbb Z\).

Limitations: the tests are finite, the theorem counts labelled elements rather than isomorphism/orbit classes, only square-zero is treated, and the rank-one geometry is reduced. No independent audit has been performed.
