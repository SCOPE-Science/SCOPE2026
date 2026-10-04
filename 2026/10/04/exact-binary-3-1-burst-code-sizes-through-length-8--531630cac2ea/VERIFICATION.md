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

The claim is finite: compute the compatibility graph on all binary source words separately for each \(3\le n\le8\), where adjacency means disjoint exact \((3,1)\)-burst balls. A correcting code is a clique.

`verify.py` generates each ball in two independent ways and asserts equality for every source. It then verifies that every ball has \(n-1\) distinct outputs, checks the explicit code in `codes.json`, and computes the graph clique number by exhaustive branch-and-bound. The only pruning rule uses a greedy proper coloring of the current candidate subgraph; if that coloring uses \(k\) colors, no clique in the candidate set can contain more than \(k\) vertices.

The replay gives clique numbers \((1,1,2,2,4,8)\) for lengths \(3\) through \(8\). The corresponding regular sphere-packing floors are \((1,1,2,3,5,9)\). `verification_output.txt` records the exact replay and terminates with `VERIFY_OK profile=1,1,2,2,4,8`.

The computation establishes no statement for \(n>8\). The literature comparison and same-model review are not independent validation.
