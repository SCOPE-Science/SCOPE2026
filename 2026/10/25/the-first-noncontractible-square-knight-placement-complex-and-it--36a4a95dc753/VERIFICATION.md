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

# Reproducibility and scope

Execute `python3 verify_knight4.py` in the same directory; Python 3.9+ standard library is sufficient. The exact replay is provided as `verification_output.txt`.

The verifier reconstructs the ordinary nonperiodic knight adjacency from coordinates, enumerates all independent faces, and constructs precisely the pivot-specified Morse matching. It checks pair disjointness, all directed incidences, complete directed acyclicity, critical-cell counts and faces, separate boundary ranks over \(\mathbb F_2\), and each of the eight signed simplicial Lefschetz sums. The claimed wedge conclusion is a mathematical application of discrete Morse theory to this exhaustively verified matching; finite-field rank checks alone would not establish an integral result.

Actual result: 1,364 nonempty faces, 679 matched pairs, six critical cells in dimensions \((0,3,3,3,3,3)\), 5,772 checked covers, and a full 1,364-vertex acyclic topological ordering. The exact character is \((5,-1,1,-1,3,-1,3,-1)\) in the prescribed dihedral element order. Smaller square boards are contractible because their knight graphs have an isolated vertex.

Limits: no assertion about larger boards, integral representation lattices, or independent audit.
