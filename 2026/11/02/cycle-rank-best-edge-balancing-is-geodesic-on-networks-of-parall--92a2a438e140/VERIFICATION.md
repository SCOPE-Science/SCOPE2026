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

The analytical claim is proved in `RESULT.md` without numerical assumptions. The only structural facts required are that a simple cycle stays in one block and, inside an internally disjoint path bundle, is the union of exactly two paths. The rank, minimal-distance, energy-descent, and tie-probability statements then follow algebraically.

Run `python verify_banana.py` with Python 3.10 or later; no packages are needed. It independently enumerates small-host undirected simple cycles, iterates all signs, tests *every* legal maximum-rank edge choice in *every* negative cycle, recomputes the minimum flip distance by Hamming comparison against all balanced signings, and checks the predicted strictly descending potential. The seven host configurations cover 9,168 complete signings and 77,792 legal transitions. Three tie experiments use exact rational arithmetic, yielding \(1/2\), \(134/315\), and \(842/2835\) respectively. They test a nonuniform path-length bias.

Enumeration is finite and not claimed as exhaustive over arbitrary host size. The result is not a claim about the original triangle-only rule, stochastic convergence on arbitrary graphs, or independent validation. Full text of the historical 1978 balancing-process source was not accessible for a decisive priority comparison.
