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

Run `python3 check_round45.py` using standard Python. Its integer-square-root arithmetic avoids floating point, and its executable assertions cover every starting lattice point in the centered \(321\times321\) grid and \(20{,}000\) additional large-coordinate lattice points. It checks the functional identity \(R^3(z)=Q R(z)\), the return identities \(R^4(Rz)=-Rz\) and \(R^8(Rz)=Rz\), least periods for nonzero image points, and the sharp example. The run emitted `PASS: 103,041 lattice seeds, 20,000 large exact seeds`.

The proof is independent of the finite tests: the signed diamond inequality establishes the exact identity for arbitrary lattice points; the four translated-diamond overlap areas and two-coordinate Weyl criterion establish the claimed natural densities. No claim is made that the finite enumeration or random seeds independently prove either universal statement. The mathematical novelty comparison is subject to the specific access limitations recorded in the review. Independent audit has not been performed.
