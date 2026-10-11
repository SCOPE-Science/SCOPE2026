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

Run `python verify.py` with a standard Python 3 interpreter. The script uses only the standard library. It reconstructs the graph from duads and synthemes rather than loading a stored adjacency list.

The exact checks are: \(30\) graph vertices, \(45\) graph edges, cubic degree sequence, girth \(8\); complete independent-face enumeration; the full face vector and Euler characteristic; every discrete-Morse pair as a one-vertex Hasse cover; exactly \(238{,}088\) matched pairs; critical-cell dimensions \(0\) and \(8\) with multiplicities \(1\) and \(9\); all \(3{,}461{,}400\) nonempty-face Hasse covers; and acyclicity of the entire Morse orientation by topological sorting.

The computation is finite and exhaustive for the stated graph. It does not prove a corresponding formula for a larger family. The expected final markers are `ACYCLIC_MATCHING_OK` and `VERIFY_OK`.
