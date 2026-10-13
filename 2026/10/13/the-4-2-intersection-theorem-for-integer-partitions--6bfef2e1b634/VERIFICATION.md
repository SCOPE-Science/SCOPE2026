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

The scientific proof covers every integer \(n\ge4\). In the nontrivial case, it bounds all families by thirteen using an intersection-two witness and an occurrence-label completion argument; this handles \(n\ge30\) since the canonical star then contains at least fourteen partitions. The supplied exact verifier covers **all** remaining orders \(4\le n\le29\), with 26 compatibility-graph maximum-clique computations. For each order it independently verifies the number of ambient four-part partitions through the standard partition recurrence and the pairwise intersections by both multiplicity and labeled-set intersection. An independently implemented Bron--Kerbosch program enumerates all maximal cliques at every order \(4\le n\le29\), with results in `verify_bk_output.txt`. Orders \(4\le n\le13\) are additionally checked by direct enumeration of all subsets in the first verifier. Actual outputs are in `verify_output.txt` and `verify_bk_output.txt`.

The graph branch-and-bound search uses a sound greedy proper-coloring upper bound; no timeout, probabilistic sample, or unexplored node is interpreted as exhaustive. The calculations are exact Python integers. No outside validation, formalization, or generalization to other intersection parameters is claimed.
