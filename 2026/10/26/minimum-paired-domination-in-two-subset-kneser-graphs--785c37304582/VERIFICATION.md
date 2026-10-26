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

Run `python3 verify.py` with standard Python 3. It independently reconstructs the underlying two-subset disjointness graphs and tests domination and matching by different combinatorial predicates. In particular, it enumerates all even-size candidate sets for the two small boundaries, all four-vertex candidate sets through ten ground symbols, all five-symbol automorphism actions, and the three support-shape embedding counts.

Expected checked output:

```
small 4 minimum 6 count 1
small 5 minimum 6 count 125
four 4 0
four 5 0
four 6 180
four 7 1575
four 8 7665
four 9 27405
four 10 80325
VERIFY_OK
```

The arbitrary-parameter theorem is not deduced from these tests. Its proof uses an exact cover reduction and a complete four-edge component classification. This program does not certify independent scientific review or priority.
