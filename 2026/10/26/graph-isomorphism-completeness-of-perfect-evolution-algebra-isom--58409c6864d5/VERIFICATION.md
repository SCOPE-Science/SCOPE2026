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

# Verification record

The theorem is proved symbolically by monomial rigidity, cycle-fiber relational isomorphism, and support-incidence reconstruction. The included `check.py` uses distinct brute-force definitions to compare the monomial coefficient equation to relational isomorphism; it does not assume the theorem in either search.

Executed with Python 3, standard library only:

```
q=2, n=2, matrices=6, tested_pairs=36, isomorphic_pairs=10
q=3, n=2, matrices=48, tested_pairs=2304, isomorphic_pairs=352
q=2, n=3, matrices=168, tested_pairs=1200, isomorphic_pairs=45
q=5, n=2, matrices=480, tested_pairs=100, isomorphic_pairs=6
incidence encoding n=1, simple_graphs=1
incidence encoding n=2, simple_graphs=2
incidence encoding n=3, simple_graphs=8
incidence encoding n=4, simple_graphs=64
incidence encoding n=5, simple_graphs=1024
VERIFY_OK
```

The sampled comparisons are deterministic, and the first two matrix-pair comparisons are exhaustive. The incidence tests validate the determinant and intrinsic indegree partition for all labeled graphs of orders at most five, across three prime fields. General finite-field and arbitrary-dimension correctness rests on the human-readable proof, not on these finite tests. The checker's tested fields are prime fields; the algebraic proof handles all prime powers.
