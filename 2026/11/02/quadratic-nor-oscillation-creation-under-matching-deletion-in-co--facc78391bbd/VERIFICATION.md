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

# Reproducible checks

The supplied scripts enumerate the complete binary state space for each listed finite graph parameter. Both use the actual neighborhood rule rather than generating transitions from the analytical orbit list.

Run the Python implementation with `python3 checks/check_graph.py`. Its recorded output confirms 105 parameter cases and 86,384 initial configurations for every \(2\le p,q\le6\) and allowed \(k\).

Compile the other implementation with `c++ -O2 -std=c++17 checks/check_bitmask.cpp -o check_bitmask`; then execute `./check_bitmask`. Its recorded output confirms 213 parameter cases and 804,208 configurations for \(2\le p,q\le8\), \(p+q\le14\), and every allowed \(k\).

Each enumerator independently constructs the matching-deleted bipartite graph, evaluates every neighborhood, computes the one-step eventual cycles, and checks orbit counts plus the multiset of attraction-basin sizes. The checks include the boundary case \((p,q,k)=(2,2,2)\) where every state is recurrent. The actual outputs are included beside the source files. Finite checks do not prove the infinite parameter statement; that follows from the one-sided map and preimage counting in the proof.
