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

# Finite verification

Execute `python3 verify_click_petersen.py` (Python 3 standard library). Its observed final output was `VERIFY_OK`.

The program constructs the ten two-subsets of a five-set and all fifteen disjointness edges; it then enumerates exactly all 32768 orientation bit masks. Topological peeling and an independently coded directed DFS agree on acyclicity for all masks; exactly 16680 pass. The known chromatic polynomial agrees at minus one, and exactly 704 acyclic orientations have a designated vertex as their unique source.

For every admitted mask, all legal three-edge source/sink toggles are generated; every result is checked for acyclicity and every adjacency for symmetry. The 16680-state graph has exactly 704 connected components, with component-size histogram \(\{12:120,16:120,21:120,22:120,28:120,38:60,50:24,66:20\}\). BFS from every state computes all component eccentricities and pair distances; independently every reachable *ordered pair* is checked by the known integer-potential median distance formula. The 235080 unordered-pair total is verified from component sizes.

Every one of the 120 permutations of the five underlying symbols is applied as a Petersen automorphism to each component representative. Exactly nine component orbits arise. The separate published count of 168 orbits on *individual orientations* is reproduced as an independent action check. Complementing all fifteen orientation bits exchanges exactly two of the nine component orbits, both of size 21, and leaves the other seven orbit types invariant.

This is a mathematically exhaustive finite check for this ten-vertex graph, not a proof of a general family theorem. The general potential-median formula is credited to previously published research; the package computes explicit values from it and independently from BFS. No independent audit or external certification is asserted.
