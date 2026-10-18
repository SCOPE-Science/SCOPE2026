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

# Reproducible verification

Run `python verify.py` with a standard Python 3 installation. No third-party libraries or external data are needed. The script reads no external files.

Expected successful output:

```
EXACT_CHECKS_PASS
edge_transitive_labeled_graphs= 174
automorphism_actions= 1508
cut_switches= 2422
balanced_multipartite_pairs= 60
exact_rational_and_integer_arithmetic=True
```

The exact finite script enumerates all simple labeled graphs with two to five vertices, identifies edge-transitive instances through the full permutation group, computes their maximum cuts from all sign assignments, and confirms the uniform automorphism-average and switched reflection identities. It separately verifies the multipartite parity expressions for all tested \(2\le r\le11\) and \(1\le a\le6\); complete max-cut enumeration is also executed when \(ra\le12\). All integer/rational comparisons are exact. These bounded tests do not prove the general classification, center uniqueness or the infinite-parameter closed form; those steps are established in RESULT.md.
