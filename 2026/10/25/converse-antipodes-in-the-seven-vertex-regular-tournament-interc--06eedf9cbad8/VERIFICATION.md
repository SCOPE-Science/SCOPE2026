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

# Reproducibility

Run `python3 verify_bitmask.py` and `python3 verify_recursive.py` using standard Python 3.10+ from the same directory. Both source files are embedded and standalone, with no external dependencies or data files. Their actual execution outputs are provided beside them; the final line of each is `PASS`.

The bit-mask checker deterministically tests all \(2^{21}\) possible orientations of the 21 edges, checks all outdegree constraints, then tests all \(\binom73=35\) cyclic triangles per regular tournament, explicitly computes all 5040 relabelings of each representative, and runs exact BFS for the three resulting orbits. It checks that the 2640 masks and 18480 exchange edges are complete and symmetric. It checks all distance histograms and all four-subset cyclic-triangle histograms, as well as each class's exact converse distance and farthest-count. Canonical vertex SHA-256: `4c059786ba7d81ff979b14ada49f93a75947da7d31f3f9b61acdcf10c54ff7d8`. Canonical undirected edge SHA-256: `8f7a44ae81aa3923c15e2f60be0241d5a97f568a0d1d531140aedd5f4c4f2755`.

The independent row-recursion checker directly constructs all balanced adjacency matrices, reverses directed cycles by manipulating row bits, then performs BFS from **every** one of the 2640 roots. It confirms exactly 360 undirected distance-nine pairs and checks every such pair is a converse pair. Its three shell classes agree with the first program.

Exact coverage is finite only: the checkers do not establish an n-dependent general theorem for arbitrary odd tournament order. The closest classical interchange results supply connectivity and bounds, not these exact recorded finite metrics. Independent external validation has not been performed.
