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

# Reproduction and limits

Execute `python3 verify.py` using Python 3 standard library. It constructs the graph edges explicitly for each listed tuple of cycle lengths, forms the triangle hyperedge set by testing each vertex triple, enumerates every triangle-avoiding subset, and computes every reduced mod-two Betti number by GF(2) boundary rank reduction. The executable contains its expected homology ranks independently from the direct face enumeration. Exactly ten parameter tuples were checked, for a combined 2,784 nonempty faces; the complete stdout is in `verification-output.txt` and ends `ALL_PASS cases 10 faces 2784`.

This is a finite mod-two check only. It does not certify integral torsion-freeness, general parameter ranges, or homotopy type. The general integral homotopy theorem follows instead from the exact face decomposition, nullhomotopies and mapping-cylinder/cofiber proof in `RESULT.md`. An independent audit has not been performed.
