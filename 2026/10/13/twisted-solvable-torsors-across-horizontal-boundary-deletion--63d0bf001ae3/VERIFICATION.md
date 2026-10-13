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

The geometric premise was checked in N. Yamaguchi, arXiv:2610.02948v1, Theorem 2.5: under condition \((\dagger)\), the natural surjection from the étale fundamental group of the divisor complement to that of the ambient scheme has topologically perfect kernel.

The coefficient dictionary was checked in the Stacks Project, Tag 0DV4: finite locally constant sheaves on a connected scheme correspond to finite continuous fundamental-group actions. The torsor interpretation was checked against Tags 03AG and 03AJ.

For a cocycle \(z:G\to A\), the kernel \(K\) acts trivially on \(A\), so \(z|_K\) is a homomorphism. Its finite image is perfect because it is a quotient of the topologically perfect group \(K\), and solvable because it lies in the solvable coefficient group \(A\). Therefore the image is trivial. The cocycle descends uniquely to \(G/K\), and the same elementwise coboundary relation descends, proving bijectivity on torsor classes.

Limits checked: no higher-degree cohomology statement is inferred; no nonsolvable fiber is admitted; no coefficient sheaf defined solely on the complement is claimed to extend.
