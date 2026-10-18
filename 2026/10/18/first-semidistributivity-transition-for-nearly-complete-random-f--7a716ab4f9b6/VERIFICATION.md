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

# Reproducibility and verification

Run `python3 verify_semidistributivity.py` with a normal Python 3 interpreter (standard library only). The source independently constructs formal concept extents from closure for every tree in the finite obstruction range, checks both lattice quasi-identities for every ordered triple, and crosschecks the formal-context/maximal-independent-set correspondence on 576 small labelled incidence patterns.

Recorded output from the actual source program:

```text
TREE_CENSUS [(1, 1, 0, 0), (2, 1, 0, 1), (3, 3, 0, 3), (4, 16, 0, 12), (5, 125, 0, 60), (6, 1296, 0, 360), (7, 16807, 2520, 2520)]
P7_EXTENTS [0, 1, 3, 8, 9, 12, 15]
MIS_FCA_EQUIVALENCE 576
VERIFY_OK
```

The finite census examines 18,249 labelled trees, including all 16,807 labelled trees on seven vertices. Exactly 2,520 seven-vertex trees fail, each a path. The independent correspondence tests concern finite structures, not independent peer verification. The limiting Poisson distribution, the asymptotic probability formula and the first sparse supercritical regime require the analytic counting and second-moment proof in RESULT.md; they cannot be deduced from finite experiments. No independent external audit has occurred.
