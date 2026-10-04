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

The standalone `verify.py` reconstructs the 13-point poset \(P_2^2\) from the incidence data in the cited source and the four-point circle \(C\) from its four order relations. It exhaustively checks all \(13^4\) set maps and obtains exactly \(853\) order-preserving maps.

It constructs the pointwise order on the full mapping set and verifies exactly two comparability components, of sizes \(721\) and \(132\). It independently constructs the target order complex, verifies \(36\) edges and \(24\) triangles, computes mod-two boundary ranks \(12\) and \(23\), and hence verifies \(\dim H_1(P_2^2;\mathbf F_2)=1\). It then maps the fundamental cycle of the source order complex and verifies that exactly \(132\) maps give the nonzero homology class and that these are precisely the smaller mapping-poset component.

For the larger component, the script carries out \(708\) beat-point deletions while preserving the constants. Before each deletion it checks, in the current induced subposet, the required least strict upper neighbor or greatest strict lower neighbor. The remaining \(13\) points are exactly the constant maps, and their inherited order is checked against \(P_2^2\).

The exact replay output is stored in `verification_output.txt`. The exhaustive computations certify the finite counts and reduction. The implication from comparability components to finite-space homotopy classes, and the fact that beat-point deletion is a strong deformation retraction, are established general results and are not reproved computationally here.
