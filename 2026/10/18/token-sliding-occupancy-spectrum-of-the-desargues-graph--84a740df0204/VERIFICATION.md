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

# Reproduction instructions

Run `python3 verify.py` under Python 3 with its standard library and no additional input files. The program reconstructs the original 20-vertex graph from the disjoint-pair model and maps it to the canonical generalized Petersen \(GP(10,3)\) adjacency list by a fixed bijection. It generates all independent vertex subsets using two different algorithms, tests sliding edges by two independent definitions, computes connected components with breadth-first search and union–find, checks frozen-star and small-component geometries, and performs exhaustive breadth-first shortest-path searches from each nonisolated state.

The expected completion marker is `ALL_CHECKS_OK`, printed only after all census and distance assertions succeed. The certificate proves exact properties of this one finite graph, not a family-level statement. Published independent-set face counts provide an additional consistency check but do not themselves determine any token-sliding component. No independent external verification is represented in the status front matter.
