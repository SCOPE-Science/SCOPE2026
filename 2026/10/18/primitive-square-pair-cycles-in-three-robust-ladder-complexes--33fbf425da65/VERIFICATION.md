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

# Reproducible checks

Run `python verify_ladder.py` using only the Python standard library, then compare its stdout with `verification_output.txt`. The script reconstructs all graph edges and three-robust simplices from definitions, checks integer boundaries of the wedge-product cycles, identifies a distinct coefficient-one (up to sign) tetrahedron for every cycle, verifies row and column symmetry on each cycle, and computes the complete top mod-two boundary nullity independently. It checks all \(3\le n\le11\), giving 165 independently constructed candidate cycles in total. These finite calculations are not substituted for the proof covering every integer \(n\ge3\).

The all-integer homology basis theorem rests on the explicit wedge-chain argument, unit diagonal coefficient lemma, and published all-grid sphere-wedge rank theorem. No independent audit was performed, and no claim is made about integral quotient-space homology.
