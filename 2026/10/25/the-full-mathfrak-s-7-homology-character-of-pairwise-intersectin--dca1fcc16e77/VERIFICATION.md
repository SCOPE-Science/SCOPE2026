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

# Exact verification

The accompanying `verify.py` runs with Python 3 standard-library facilities only. To check the finite part of the proof, place it in the same directory and run `python3 verify.py`. It enumerates the 35 three-subsets, one representative of each of the fifteen cycle types of \(\mathfrak S_7\), and the admissible triple-orbits; it forms the orbit-disjointness graphs and computes their independence-polynomial values at \(-1\) by an exact deletion-and-closed-neighborhood recurrence.

For the eleven orbit graphs having at most fifteen vertices, it independently enumerates every vertex subset to cross-check the recurrence. It checks the orientation sign of a transposition on the ten antipodal triple-pairs of six points, calculates all Specht characters by Murnaghan–Nakayama, verifies both row and column character orthogonality, and checks all hook-length dimensions and multiplicities. In particular the reproducible 15-class outputs give degrees six and nine with dimensions 29 and 7 and their claimed constituents.

The homological concentration and top-sphere independence used to infer the two graded characters are published theorems [1,2], not re-derived by this finite checker. The calculation is exact for seven ground points and provides no conclusion about integral torsion or all larger cases. No independent audit has been performed.

[1] Z. Feng, arXiv:2610.17394v1 (Theorem 18).  [2] Z. Feng and G. Wang, arXiv:2404.10566v1 (Theorem 10).
