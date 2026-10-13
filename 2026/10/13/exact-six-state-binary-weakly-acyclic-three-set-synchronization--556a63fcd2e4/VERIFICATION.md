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

Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The verifier enumerates every weakly acyclic binary automaton after choosing a topological order: each letter has \(720\) allowed transition maps, hence \(518400\) ordered pairs. For each automaton it builds the complete nonempty subset automaton and computes exact reverse distances from all singleton subsets.

All twenty three-subsets are inspected. The maximum finite distance is checked to be \(7\), with four extremal presentations in the fixed topological order. Every such presentation is replayed independently by a forward BFS. Canonicalization under every state permutation and both letter orders gives one class. The representative `aaabaaa` is replayed and its full labeled symmetry orbit is checked to have size \(1440\).

The computation is exhaustive only for six states, two letters, and three-element distinguished subsets. Independent audit has not been performed.
