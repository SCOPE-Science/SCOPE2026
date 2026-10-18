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

# Reproducible finite certificate

Execute `python3 evidence/verify_mk_morse.py` and `python3 evidence/verify_mk_independent.py` from the extracted package. The first script establishes a complete discrete-Morse certificate by enumerating all \(65,536\) candidate vertex subsets and all \(218,672\) nonempty-face covering incidences; every node is consumed by a topological sort after matched arrows are reversed. It then computes all eight signed simplicial Lefschetz traces. It reports `Morse and cyclic character verification: PASS` only if every internal assertion succeeds.

The second script independently realizes the graph through the cyclic eight-point/eight-line incidence configuration and uses a fixed explicit vertex isomorphism. It enumerates all dominating complements without using the first program's forbidden-mask method. It reports `Independent cyclic configuration check: PASS` only after verifying the full face vector and reduced Euler characteristic.

These exact finite checks support the proved single-graph classification; neither program proves any claim for an infinite graph family. The scripts do not provide an independent mathematical audit.
