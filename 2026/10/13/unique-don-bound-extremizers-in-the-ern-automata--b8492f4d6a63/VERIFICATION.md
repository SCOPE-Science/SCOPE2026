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

The proof is symbolic and applies to every \(n\ge2\). The executable check is deliberately finite: `verify.py` constructs the power automaton from the stated transitions for every \(2\le n\le12\), computes shortest exact-image distances by BFS, confirms the unique equality subset in every layer, replays the explicit equality word, and checks the cyclic-boundary reverse-extension identity for every nonempty proper subset.

A finite run does not prove the universal theorem. Its role is to detect normalization, indexing, boundary, and recurrence errors in the human proof. The all-\(n\) lower bound rests on the exact characterization of when an inverse \(b\)-step can increase cardinality and on induction through the canonical sets \(S_k\).
