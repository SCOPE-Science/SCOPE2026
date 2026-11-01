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

Run `python3 verify.py` with Python 3 and its standard library in the same directory. The script exhaustively generates the 131 augmented faces (one empty and 130 nonempty), carries out 63 acyclic pairs, computes signed face Lefschetz traces for the five symmetry classes, and reconstructs the binary chain complex, quotient homology, and the rotation and reflection actions.

It verifies the exact \(\mathbf F_2\) rotation row masks \((28,1,19,11,13)\), diagonal-reflection row masks \((8,11,13,1,19)\), relations \(R^4=D^2=I\) and \(DRD=R^{-1}\), and the ranks \((3,2,1,0)\) of successive powers of \(R-I\). The group-character and nonsplitting deductions are explained in the proof.

The enumeration is exhaustive for this precisely defined finite grid; there is no infinite-family claim. Public-source comparison is not an assertion of absolute uniqueness. Independent mathematical audit has not been performed.
