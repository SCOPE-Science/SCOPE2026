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

Run `python3 verify_wheel_character.py` using a standard Python 3 installation. The program has no optional dependencies, enumerates exact dihedral actions and orbit graphs, and uses integer fraction-free elimination. It checks the determinant formulas for all \(136\) group elements for \(5\le k\le12\). It also computes direct equivariant-forest sums where feasible. At \(k=5,6,7\), it separately enumerates all simplices, including the empty simplex, and reconstructs the signed reduced Lefschetz trace, not just determinant values. The complete face totals are \(2527\), \(10800\), and \(45369\). The expected terminal output is `VERIFY_OK`.

These finite calculations check definitions, boundary signs, group actions, and small cases. The proof for every integer \(k\ge5\) is a mathematical argument using complete-source shellability, the forest determinant identity, and explicit quotient determinants; computational tests cannot establish the infinite family by themselves. The rational group-module identification uses character theory and is not an integral lattice classification.
