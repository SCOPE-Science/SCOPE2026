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

# Verification protocol and scope

The standalone `CHECK.py` works with the Python 3 standard library; invoke `python3 CHECK.py`. It builds the Petersen graph canonically as \(KG(5,2)\), lists all fifteen edges, and exhaustively checks all \(2^{15}\) directed assignments, rejecting exactly the cyclic ones. Each surviving orientation's Hasse-arc count is computed via DAG reachability and independently via DFS after reversal of each original edge; the methods agree at every case. All \(120\) permutations of five symbols are enumerated and every orientation orbit checked. The certificate separately enumerates all nine-edge spanning trees, checks all nine-edge orientation assignments for coherent chord paths, and verifies all five symmetry-orbit sizes. It terminates with `VERIFY_OK` if and only if the asserted counts match.

Expected outputs include \(16680\) acyclic orientations, the seven local degree coefficients \(1080,2280,3600,3120,3120,2160,1320\), \(168\) orientation orbits, \(2000\) trees, \(540\) coherent trees in five orbits, and \(100080\) total invariant curves.

The finite enumeration is complete for this particular graph; it is not a sampling experiment. Geometric use of the enumeration requires the chamber–orientation dictionary, the characterization of reversible arcs, and the unimodularity of oriented tree-incidence matrices, all supplied in the mathematical result. Source overlap was compared only against accessible literature and records; an unindexed equivalent census remains possible. No independent audit or external validation has been undertaken.
