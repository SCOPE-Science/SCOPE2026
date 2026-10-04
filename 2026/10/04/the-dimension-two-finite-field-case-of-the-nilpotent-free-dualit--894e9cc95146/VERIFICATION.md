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

The symbolic verification uses only standard facts about a separable quadratic extension \(K/F\): the nontrivial automorphism \(\sigma\) has order two, multiplication by a nonzero field element is invertible, and Cayley--Hamilton holds in \(\operatorname{End}_F(K)\). These imply \((L_a\sigma)^2=N_{K/F}(a)I\), trace zero for every \(L_a\sigma\), and invertibility for nonzero \(a\). A trace-one matrix then gives a direct one-dimensional complement, and trace eliminates that complement from any nilpotent element.

The standalone checker exhausts the resulting three-dimensional space for \(q=2,3,4,5,7,11,13\). It verifies that the only element with trace and determinant both zero is the zero matrix. For \(2\times2\) matrices, these two equations are exactly the nilpotency condition. The \(q=4\) check uses an explicit model of \(\mathbb F_4\), so the replay is not restricted to prime fields.

Computational verification is finite and supplementary; it is not used to infer the all-finite-field theorem. No claim is made beyond \(n=2\).
