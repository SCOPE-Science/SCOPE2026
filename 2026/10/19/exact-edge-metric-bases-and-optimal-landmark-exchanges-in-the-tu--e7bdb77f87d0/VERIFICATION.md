---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and evidence

Construct the graph from its 15 duads and 15 synthemes. A candidate landmark set resolves the edges exactly when it separates all 990 unordered edge pairs. `python3 verify_python.py` regenerates the complete list of optimum bases, the exchange edges and the distance-seven pairs. Independently compile `c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp` and run `./verify_cpp` for the minimum and exchange statistics using edge signature uniqueness rather than pair masks. The expected marginal and scalar summaries are in `verify_python_output.txt` and `verify_cpp_output.txt`.

The certificate files `basis_states.txt`, `exchange_edges.txt` and `distance_7_pairs.txt` retain their original ordering and contents. In a directory containing those files, run `python3 verify_joint.py` (or supply the certificate directory as the first argument). This script reconstructs the exchange edges from the four-subset buckets of the bases and compares the whole edge list, recomputes every eccentricity and the complete distance-seven list, and tallies degree with eccentricity on the same source. The joint output is in `verify_joint_output.txt`. In particular the marginal counts from the original programs do not establish which vertices contribute to both bins, and the new check reports that pairing explicitly. Each check is a finite exact calculation for this graph and adjacency rule.
