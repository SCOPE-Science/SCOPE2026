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

`verify.py` reconstructs the complex from the published formula for \(T_{7,1,2}\). It checks the fourteen faces, complete twenty-one-edge one-skeleton, rank \(13\) of the face-boundary span, and therefore \(\dim H_1(K;\mathbf F_2)=2\). It then reduces every empty triangle boundary modulo global boundaries and exhausts all \(128\) induced vertex sets.

The replay result is:

`VERIFY_OK H1dim=2 empty_triangles=21 classes=7,7,7 layers=0:0x1;1:0x7;2:0x21;3:0x14,1x21;4:1x21,2x14;5:2x21;6:2x7;7:2x1 complement4=face_iff_rank2 threshold=5`

The verification is exhaustive for this finite complex. No claim is made that these mod-two classes determine integral homology classes, nor is any larger torus triangulation tested or covered.
