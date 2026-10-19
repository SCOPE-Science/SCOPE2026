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

Run `python verify_counts.py` and `python verify_orbits.py` with Python 3 and standard library only. The first enumerates all adjacency-preserving full maps of \(C_n\) directly, applies \(f^2=f\) without assuming an arc classification, and compares their rank counts against two separate exact formulas for \(3\le n\le16\). It prints `CHECKER_OK` after all assertions. The second enumerates complete unit-conjugacy orbits using every rotation and reflection of \(C_n\) independently of the Burnside formula, then tests the walk involution and midpoint formula for \(3\le n\le15\); it prints `SYMMETRY_OK` after all assertions. Both passed in the recorded execution.

Selected expected totals of labeled idempotents: \(9\) for \(C_4\), \(25\) for \(C_6\), \(73\) for \(C_8\), \(221\) for \(C_{10}\), and \(685\) for \(C_{12}\). Expected numbers of dihedral unit-conjugacy classes: \(3,4,8,14,36\), respectively. Odd cycles have only the identity idempotent.

These finite computations are corroborations; the all-size claims require the proof's image-arc bijection, automorphism stabilizer, midpoint count, and determinant identity. No independent audit is asserted.
