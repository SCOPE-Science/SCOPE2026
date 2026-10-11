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

# Reproducibility and mathematical limits

Invoke `python3 dihedral_cycle_verify.py` from a directory containing the embedded program. The program uses only the Python 3 standard library and requires no data files. It enumerates every independent face for each cycle of sizes 3 through 18, all reflections and rotations, and the induced orientation signs on fixed simplices. It compares the augmented Lefschetz sums against the stated character formulas for all 336 group elements. For sizes 3 through 15, it also performs exact binary Gaussian elimination on every augmented boundary matrix and checks all mod-two Betti numbers.

The observed exit was `VERIFY_OK signed-traces= 336 GF2-homology= 13`. The checks are exact but finite; they cannot establish the all-parameter assertion without the proof of orbit decomposition and the cited homology concentration theorem. No integral homology module, fixed-point space, or independent human audit is asserted.
