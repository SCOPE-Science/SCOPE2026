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

# Computational verification

The complete mathematical proof appears in `RESULT.md`; a finite computation is not used as an infinite proof.

Compile and run `gp_subdivision_verifier.cpp` with a C++17 compiler, for example `c++ -O3 -std=c++17 gp_subdivision_verifier.cpp -o verifier && ./verifier`. This program reconstructs the graph, obtains all-pairs shortest-path distances by breadth-first search, identifies forbidden geodesic triples, checks every vertex subset against an independent edge-subgraph characterization, and compares the exact maximum coefficients and extremal counts for \(3\le n\le6\). It inspected exactly 2,131,008 subsets. The recorded output is `gp_subdivision_verification_output.txt`.

Run `python gp_subdivision_series_check.py` with Python 3 and its standard library to calculate the labeled-component coefficient recurrence independently, compare with the exhaustive graph coefficients through \(n=6\), and check the maximum count for each \(3\le n\le9\). Its recorded output is `gp_subdivision_series_output.txt`.

Both checks were run from the packaged source files before packaging; the results correspond to the named files. Exhaustion through six ground vertices does not certify any further orders. Full priority and independent mathematical validation were not performed.
