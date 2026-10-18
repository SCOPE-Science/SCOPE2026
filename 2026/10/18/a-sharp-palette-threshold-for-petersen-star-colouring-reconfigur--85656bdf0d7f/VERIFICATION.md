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

The programs `labeled_check.cpp` and `partition_check.py` are complete stand-alone finite checks. Compile and run the C++17 program, then run the Python 3 program as shown in `RESULT.md`. The packaged `labeled_output.txt` and `partition_output.txt` are the corresponding actual console outputs.

The full six-name program exhaustively enumerates every valid map, tests every possible single-vertex recolouring, and traverses all named maps from one representative per orbit under vertex and colour-name symmetries. It checks \(341{,}280\) states, the complete degree census, and eleven full BFS runs. The independent Python program exhaustively evaluates all \(115{,}975\) partitions of the ten vertices, including partitions requiring more than six classes, and reconstructs the five- and six-class distributions, block-exchange counts, named-state degrees, and eleven symmetry orbits.

The BFS distance data are not independently reproduced by the Python program; all BFS computations are fully specified and repeatable from C++ source. No probabilistic sampling, infeasibility inference from a timeout, extrapolation to an infinite graph family, or external scientific validation is claimed.
