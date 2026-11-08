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

# Verification record

`verify_graph.py` performs explicit finite-field Gaussian elimination on genuine Hamming-distance-three adjacency matrices. Successful checks for \(3\le n\le11\) include predicted ranks and \(A_n^2\in\{0,I\}\), and for \(n=3,7,11\), the predicted involutive fixed-space dimension.

`verify_algebra.py` uses group-algebra basis changes to check the polynomial multiplier in all four classes for \(3\le n\le11\), as well as twenty reproducible random state updates per dimension, independently comparing group-convolution and squarefree-polynomial multiplication.

`verify_forms.py` computes graded ranks of multiplication by \(e_2\) on \(2\le n\le12\) generators and \(e_3\) on \(3\le n\le12\), comparing the ranks to the symplectic calculation. Captured `.out` files contain successful execution results; they are not independent certificates of the infinite theorem.

**Boundary and limits.** All exact finite checks use \(\mathbb F_2\), and the infinite-field extension to all \(Q=2^f\) follows from field-independent integer-coefficient polynomial identities and elementary dimension arguments. No computation was used as evidence for all \(n\), and no independent audit has been performed.
