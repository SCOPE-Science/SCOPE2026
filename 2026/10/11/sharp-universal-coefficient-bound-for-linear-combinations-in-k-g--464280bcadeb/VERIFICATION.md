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

The source statement and proof of Huang--Yang Theorem 3.4(1) were checked in the open-access article. The critical published comparison fails already on the one-dimensional choice \(K_1=I\), \(K_2=-I\), \(a_1=1\), and \(a_2=-1\).

For the corrected bound, define the frame energy \(E(f)\) by the coefficient sum in the theorem. Each source lower bound gives \(\|K_i^*f\|\le E(f)^{1/2}/\sqrt{A_i}\). Applying the triangle inequality to \((\sum_i a_iK_i)^*f\) yields the claimed constant directly.

Sharpness was checked symbolically in dimension one: take one identity coefficient map and let \(K_i\) be scalar multiplication by a phase-aligned scalar of modulus \(1/\sqrt{A_i}\). Every individual lower-bound inequality is then an equality, and the combined operator has modulus \(\sum_i|a_i|/\sqrt{A_i}\), forcing the claimed lower bound and ruling out every larger universal constant based only on these parameters.

No finite numerical experiment is used. The result does not assert that the supplied \(A_i\) are optimal for a particular application, nor that the universal constant is the optimal lower bound for every specific operator tuple.
