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

# Verification and limits

Run `python3 chord_greedy_verifier.py` with Python 3 and its standard library. It checks exact rational recurrence differences for all \(4\le n\le29\) at chord distance two and all \(6\le n\le29\) at chord distance three. The only exact equalities are \(\Delta_{5,2}=\Delta_{7,3}=0\). A separately implemented permutation enumeration confirms the six examples with \(n=6,7,8\) and both distances. The script also confirms the rational order-twenty-nine values and the bound \(17/1120\).

The recurrence is proved by conditioning on the earliest random priority. The all-order extension requires a separate analytic influence-path lemma; the proof establishes a bound of eight simple paths at each length because the graph has only two degree-three junctions, and a factorial probability for monotone priorities. This is not a computational exhaustion of arbitrarily large graphs. No external proof certification or independent audit is claimed.
