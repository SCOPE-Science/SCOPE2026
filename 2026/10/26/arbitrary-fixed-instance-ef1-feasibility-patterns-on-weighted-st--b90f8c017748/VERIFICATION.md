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

# Reproducibility and limits

The package contains `verify_stars.py`, a standalone Python 3 program. Execute `python3 verify_stars.py` after extracting the embedded file. On its completed test run it printed:

```
Direct-search versus criterion finite tests: 49055
Distinct realization patterns checked: 1022
Six-vertex witness: center=6, leaf weights=[4,5,9,16,23]
Feasibility for 1,...,6 agents: yes,no,yes,no,yes,yes
All finite checks passed.
```

The direct-search branch independently implements the ordered-pair outer-deletion definition and enumerates connected star partitions. The comparison branch applies the proposed sorted-leaf threshold. The construction tests span all binary patterns for star sizes from three through eleven leaves; for the smaller sizes, each outcome is also checked by direct enumeration. No approximations are used for those tests.

The theorem is not inferred from sampling. The general proof appears in RESULT.md: connectivity classifies all partitions, a sharp order-statistic inequality supplies the exact test, and a strict recursive construction realizes every possible bit pattern for all sizes. The six-vertex minimum uses the universal endpoint guarantee for arbitrary connected graphs. Testing does not establish publication priority or independent mathematical validation. There are no external scientific validators or unperformed certificates represented as completed.
