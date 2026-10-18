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

# Verification notes

Run `python3 check_weight_two_deletion.py` with Python 3 and no third-party dependencies. It constructs complete deletion-output sets independently of the closed-form theorem for every weight-two source word at lengths \(2\le n\le84\), checks each output's weight-one projected coordinate, and verifies collision-freedom and exact cardinality of the proposed optimal family at each length.

A separate compatibility-graph search builds the graph directly from overlapping deletion balls and computes exact independence numbers for all lengths \(2\le n\le11\). It agrees with the formula at each length. The actual run printed:

```
WEIGHT_TWO_DELETION_ALL_CHECKS_PASS
construction_n=2..84; direct_source_balls= 98770 ; deck_outputs= 479906
independent_exact_n=2..11: {2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 4, 8: 5, 9: 6, 10: 7, 11: 7}
```

Proof for *all* \(n\ge2\): the upper bound is supplied by two deletion-descendant capacity constraints and the matching construction is checked by a complete case distinction of one-weight and two-weight outputs. Finite program runs supplement but do not replace the proof. The result does not cover larger input Hamming weights or more deletions.
