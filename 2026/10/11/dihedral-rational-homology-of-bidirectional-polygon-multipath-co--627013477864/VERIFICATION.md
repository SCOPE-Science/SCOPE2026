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

Run `python3 verify_dihedral_multipath.py` with a standard Python 3 interpreter; there are no nonstandard dependencies. The script derives the face set directly from local in/out constraints and excludes reverse-arrow pairs and full directed cycles. It forms unsigned mod-two boundary matrices and computes exact ranks by bitwise elimination, then separately computes oriented simplicial Lefschetz traces using permutation inversion signs.

The script checked all 1,954 permitted faces across polygon lengths from 3 to 8, all 66 dihedral automorphism traces in these cases, and mod-two Betti ranks. A second orbit-orientation method tested all 176 dihedral elements of lengths from 3 to 13. An algebraic check compared graded traces with the indicated representation matrices for every length from 3 to 80. The run exited successfully with `DIRECT_OK`, `ORBIT_OK`, `CHARACTER_OK`, and `VERIFY_OK`.

The finite checks are bounded spot-checks; they are not exhaustive in the polygon parameter. The mathematical proof uses the exact orbit-complex identifications, explicit top cycles, and the previously established homology concentration. It does not compute integral group-module extension data.
