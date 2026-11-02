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

Run the two standard-Python programs from this directory:

```
python verification/verify_gear_direct.py
python verification/verify_gear_metric.py
```

The first checks every standard-zero-forcing triple for rim lengths 4 through 10 and compares it with the proposed five families. It independently builds every token-jump edge from two-element intersections, all-pairs shortest paths, and the claimed exact eccentricities. The second reads the entire included integer table and checks the Bellman inequalities, descending-neighbor condition, all branch transitions, symbolic two-step tail periodicity, the reduction to the nearest two deck translates, every base case from 4 to 27, and all four residues of the induction boundary inequalities. The all-size proof uses mathematical arguments in RESULT.md in addition to these finite symbolic checks. The scripts do not establish independent scholarly priority or external validation.
