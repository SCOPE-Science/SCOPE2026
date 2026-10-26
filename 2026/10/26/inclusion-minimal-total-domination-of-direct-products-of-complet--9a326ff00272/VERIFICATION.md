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

# Reproduction and boundaries

Run `python3 check_minimal_total.py` with Python 3 using the standard library. The program constructs directly the adjacency relation for the categorical product of two complete graphs; for every candidate vertex subset it checks whether every vertex has a selected **open** neighbor. It then removes each selected vertex in turn to test inclusion-minimality and tallies the size distribution.

The program exhaustively checks \((p,q)=(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(3,6),(4,4)\). All eleven cases passed. The largest enumerated case has \(18\) graph vertices and \(2^{18}\) candidate subsets.

The infinite theorem depends on the incidence edge-set interpretation, the standard bipartite matching--vertex-cover equality, and exact elementary counting, not on extrapolation from finite checks. The results concern inclusion-minimal total domination in a categorical graph product, not ordinary domination, nonminimal total domination, or higher tuple orders. No independent audit is represented by these checks.
