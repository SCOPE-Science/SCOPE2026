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
# Reproducibility and evidence

The graph is constructed from 15 duads and 15 synthemes on a fixed six-element set; every allowed incidence is derived directly. A landmark resolves an edge pair exactly when the two vertex-to-edge distance values differ. This reduces basis verification to finite 990-pair coverage.

Run `python3 verify_python.py` in this directory to recreate the exhaustive five-element minimum-basis list, the 37320 exchange edges and the 360 diametral pairs. Check its output against `verify_python_output.txt`. Independently compile `c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp` and run `./verify_cpp`; compare its output with `verify_cpp_output.txt`. The C++ code does not load the Python certificates and instead uses uniqueness of edge-distance signature vectors. Both implementations check all subsets below the claimed optimum and all-source exchange distances. The output of each run is deterministic; output files use ASCII and LF.

`basis_states.txt` contains all 4560 lexically ordered five-element bases, one line per basis. `exchange_edges.txt` contains every edge of the reconfiguration graph as an ordered pair of distinct zero-based basis-line indices, with the smaller first. `distance_7_pairs.txt` similarly contains the 360 unordered diametral pairs. A reproduced instance may be compared byte-for-byte with these certificate files. Counts, optimization, distances, and configuration composition are restricted to the exact graph and adjacency rule. The finite scripts and their outputs have been checked together; independent external verification is not performed.
