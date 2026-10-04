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

The exact verifier reconstructs the defining polynomial over \(\mathbb Q(\sqrt5)\) from rational pairs, verifies that the conic matrix has determinant \(-32\), checks the three perfect-square restrictions to the coordinate lines, checks the three conic incidences and six avoidances used in the singularity census, and constructs the Jacobian partial derivatives.

For degree-four syzygies it builds the exact coefficient map \(S_4^3\to S_{11}\). The matrix has \(78\) rows and \(45\) columns and exact rank \(42\), so its kernel has dimension \(3\). This proves the upper bound \(\operatorname{mdr}(F)\le4\). The matching lower bound \(\operatorname{mdr}(F)\ge4\) is external mathematical input from Gałecka Proposition 4.1 and is not claimed to be reproved computationally.

The script also checks \(\tau=36\) from the singularity counts and the identity \(4^2-4\cdot7+7^2=37=\tau+1\). The geometric argument that these are all singularities uses the explicit line-incidence list, smoothness of the conic, transverse/simple restrictions on the noncoordinate lines, and Bézout.
