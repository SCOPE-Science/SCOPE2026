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

# Reproduction and scope

Run `python3 verify.py` with Python 3.9 or later. It uses only the standard library. It enumerates the strong-matching generators directly from all vertex orders for nine finite complete bipartite graphs, independently builds the proposed closed facet family, compares the entire face sets, verifies every elementary free-face cancellation and the final connected graph, then checks the graph-cycle rank. The expected last line is `VERIFY_OK 9 cases 132624 orderings 738 certified collapses`.

The tested pairs are \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)\). This finite test is not a proof for arbitrary parameters. The theorem for all \(m,n\ge2\) depends on the explicit symbolic facet characterization and descending-size collapse arguments in `RESULT.md`.

There is no independent audit or external validation associated with this package.
