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

# Reproducibility checks

Run `python3 verify.py` using Python 3 and no nonstandard dependencies. The standalone verifier constructs integer Laplacians, uses exact arithmetic modulo the prime 1000000007 for Krylov-rank tests, checks exact forest structure, enumerates all possible actuator subsets of the \(2\)-by-\(2\) network, and enumerates spanning-tree complements for six small bipartite dimensions.

Recorded output, reproduced from this file:

```
EXHAUSTIVE 2 2 256
TREE_COMPLEMENTS 2 2 4 CONTROL_CHECKS 16
TREE_COMPLEMENTS 2 3 12 CONTROL_CHECKS 12
TREE_COMPLEMENTS 2 4 32 CONTROL_CHECKS 15
TREE_COMPLEMENTS 3 3 81 CONTROL_CHECKS 240
TREE_COMPLEMENTS 3 4 432 CONTROL_CHECKS 15
TREE_COMPLEMENTS 4 4 4096 CONTROL_CHECKS 120
SAMPLED_ALL_SUBSETS 2 3 15
SAMPLED_ALL_SUBSETS 3 3 15
SAMPLED_ALL_SUBSETS 3 4 15
SAMPLED_ALL_SUBSETS 4 4 15
VERIFIED 734
```

The positive finite-field ranks and finite enumerations support consistency of examples only; they cannot prove the theorem over real coordinates for all sizes and all subsets. The complete mathematical argument is given in `RESULT.md`, which treats every eigenvalue including the exceptional \(p=q=2\) coincidence. No external audit or independent mathematical certification has been performed.
