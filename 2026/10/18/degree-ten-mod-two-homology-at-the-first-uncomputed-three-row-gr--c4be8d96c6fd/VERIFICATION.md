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

# Verification of the mod-two chain calculation

Both complete certificates were actually regenerated from the grid-edge enumeration and compared byte-for-byte against their embedded files. The increasing-order complex has exactly \(393\) dimension-nine and \(122\) dimension-ten critical cells; the decreasing-order complex has \(301\) and \(30\), respectively. No other critical dimensions remain. The exact mod-two differential matrices have ranks \(120\) and \(28\) as independently verified by `verify_matrices.py`.

Compile `verify_grid10.cpp` with `g++ -std=c++17 -O3 verify_grid10.cpp -o checker`. Execute `./checker ascending ascending_replay.txt` and `./checker descending descending_replay.txt`; compare the replay files with `certificates/ascending_mod2.txt` and `certificates/descending_mod2.txt` respectively. Execute `python3 verify_matrices.py` from the package root. The C++ program exhaustively enumerates the faces, constructs the acyclic matching, and derives the Morse matrices from the original simplicial boundary. The Python program independently computes their exact rank using integer bitsets.

The proof depends on a finite exhaustive calculation, not on random sampling. The computation uses about one gigabyte peak RAM. This package does not compute integral torsion or provide an independently performed external audit.
