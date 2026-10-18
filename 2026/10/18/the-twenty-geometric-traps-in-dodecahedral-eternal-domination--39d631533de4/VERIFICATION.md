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

# Reproducibility record

The labelled graph has vertices \(0,\ldots,19\), three edge families specified in `RESULT.md`, and exactly thirty undirected edges. In `certificate.json`, a vertex subset is an integer whose bit \(i\) marks the presence of vertex \(i\).

The Python file `generate_certificate.py` performs exhaustive dominating-set tests and explores every collision-free simultaneous guard motion. It lists all ten size-six dominating masks and all \(780\) size-seven dominating masks, flags immediate fatal attacks, and produces one surviving destination for every attack against each of the \(760\) winning placements. The resulting certificate has \(117503\) bytes and SHA-256 `8ce3213814565ac2cf419def755809fb0d6915876e4c17262214d7a84ae9f162`.

The separate C++17 file `matching_recompute.cpp` enumerates all candidate masks independently, checks all potential ordered pairs of equal-sized dominating configurations, and decides legal moves using augmenting-path bipartite matching rather than the Python move-generation recursion. It checks complete sets of possible responses, including negative cases, as well as the twenty exact distance-sphere witnesses and the lower bound \(26\) on the number of winning responses. The file `matching_recompute_output.txt` records the actual recomputed results.

The file `check_certificate.py` checks that the two output data sets coincide exactly, recomputes the graph adjacency and distance spheres, and verifies each of the \(9880\) response witnesses by an additional subset-based matching dynamic program. Its recorded output is in `certificate_check_output.txt`.

Reproduce with `python3 generate_certificate.py certificate.json`, `g++ -std=c++17 -O2 -Wall -Wextra -pedantic matching_recompute.cpp -o matching_recompute`, `./matching_recompute > matching_recompute_output.txt`, and `python3 check_certificate.py certificate.json matching_recompute_output.txt`. The generation and checking scripts use standard-library modules only. All checks are finite, and none is evidence for an infinite-family theorem or an independent external audit.
