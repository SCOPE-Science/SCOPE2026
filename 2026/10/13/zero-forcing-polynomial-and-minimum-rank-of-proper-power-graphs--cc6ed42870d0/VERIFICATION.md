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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

For \((p,q,d)=(3,5,2)\) and \((5,3,2)\), it tests every representative initial-white profile having at most one white vertex in each true-twin class and compares the actual zero forcing closure with the criterion “at most one double-white branch.”

It independently constructs the two proper power graphs from the groups themselves by enumerating cyclic subgroups and comparing every pair with the abstract class rule. It expands the weighted profile formula, checks the minimum coefficient, verifies every pairing in the rank witness, and also checks the symbolic formula at \((p,q,d)=(3,5,3)\).

Exact replay output:

```text
p=3, q=5, d=2: profiles=512, vertices=44, Z=38, min_sets=256000, rank_witness=6, direct_group_graph=OK
p=5, q=3, d=2: profiles=8192, vertices=74, Z=66, min_sets=95551488, rank_witness=8, direct_group_graph=OK
p=3, q=5, d=3: symbolic polynomial and rank witness OK; t=13, Z=119
VERIFY_OK
```

The finite checks corroborate, but do not replace, the arbitrary-parameter proof from the cyclic-subgroup decomposition, exact forcing criterion, and explicit Gram representation.
