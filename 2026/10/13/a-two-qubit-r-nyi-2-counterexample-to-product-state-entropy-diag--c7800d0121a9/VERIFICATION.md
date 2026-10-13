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

The proof has two independent components.

First, for a one-qubit Bloch vector \(r=(x,y,z)\), direct measurement gives \(C_Z=(1+z^2)/2\) and \(C_X=(1+x^2)/2\). The Bloch-ball condition \(x^2+z^2\leq1\), together with \(x^2z^2\leq(x^2+z^2)^2/4\), yields \(C_ZC_X\leq9/16\). This is a symbolic universal argument, not an enumeration. Tensor factorization then gives the two-qubit product-state ceiling \(81/256\).

Second, the accompanying exact-arithmetic verifier starts from the integer amplitude vector \((3,-1,-1,1)\), applies the Walsh matrix corresponding to \(H\otimes H\), and obtains \((1,1,1,3)\). It checks both collision probabilities \(7/12\), the nonzero product-state coefficient determinant, and the strict inequality \(49/144>81/256\).

No claim is made that this determines the full Rényi-2 entropy diagram. The independent audit channel has not been performed.
