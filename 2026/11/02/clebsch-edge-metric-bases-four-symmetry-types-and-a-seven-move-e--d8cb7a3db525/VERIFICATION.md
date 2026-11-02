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

# Reproduction and limitations

The graph is represented on the integers zero through fifteen, using bitwise XOR with the directions `1,2,4,8,15`. A pair of edges is resolved when the minimum distance to its endpoints differs at some selected vertex. The programs contain every algorithm needed to check the claims; no external data files, graph library, or network access are required.

Execute `python3 verify.py` (Python 3.10+). This implementation enumerates all \(2^{16}=65536\) vertex subsets through a recurrence on 780-bit distinguishing-pair masks, builds every legal one-landmark exchange among all 1,600 minimum bases, runs all-source breadth-first search, then classifies the 1,600 bases under 1,920 explicitly constructed affine automorphisms. The reported orbit representatives, omitted-subgraph degree signatures, vertex degrees and eccentricities check the full stated classification.

Execute `g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. This implementation independently computes vertex shortest paths by graph BFS, examines every subset of size at most nine (50,643 masks), represents the forty edge-distances as ternary signatures, tests all possible one-for-one replacements and computes all source eccentricities. It does not import or use the Python implementation's precomputed basis list.

Observed final messages were `ALL_VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. Both checkers yielded minimum size nine, exactly 1,600 bases, 12,960 exchange edges, one connected component, radius six and diameter seven. The first also verified exactly four affine orbits with sizes 160, 240, 240 and 960. These are finite exhaustive computations; they do not establish generalizations to other graphs or any independent scholarly audit status.
