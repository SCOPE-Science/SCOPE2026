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

The accompanying `verify.py` uses exact symbolic arithmetic. It reconstructs the printed cubic as \(F=A+B\), forms both branch discriminants as adjugate quadratic-form expressions, and checks that both have degree six. It then computes projective Gröbner bases for the derivative ideals: the first branch sextic has no projective singularity, while the second has the unique singular point \([0:1:0]\). The degree-two local term at that point has nonzero determinant, so the branch singularity is an ordinary node. Direct substitution checks that the fiber there is the stated projective line, and the multidegree coefficients give \((H_1+H_2)^2=14\).

The verifier is finite and exact; it does not certify general statements about all cubic fourfolds or all degree-14 K3 surfaces. Smoothness of the specific K3 is also reported in the source, and a separate nine-chart Jacobian computation from the displayed equations found no singular point.
