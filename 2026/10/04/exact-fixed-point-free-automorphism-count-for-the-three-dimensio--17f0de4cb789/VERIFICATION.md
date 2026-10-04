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
The proof was checked symbolically from the defining bracket. Every automorphism induces \(A\in\mathrm{GL}_2(\mathbb F_q)\), multiplies the center by \(\det(A)\), and is fixed-point-free exactly when both \(A-I\) and \(\det(A)-1\) are invertible. For each \(\delta\ne1\), the matrices with determinant \(\delta\) and eigenvalue \(1\) form the single conjugacy class of \(\operatorname{diag}(1,\delta)\).

The standalone checker exhaustively enumerates \(\mathrm{GL}_2\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), verifies the group order and admissible quotient-matrix count, and ends with `CHECK_OK`.

The finite computations are only consistency checks; the arbitrary-prime-power theorem rests on the symbolic proof.
