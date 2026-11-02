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

The uniform theorem is established by an exact color-class partition decomposition, followed by the three-way shared-color case distinction and the distinguished-doubleton counting bijection in `RESULT.md`. This is a mathematical proof; finite experiments are supplementary.

Run `python3 verify.py` using Python 3, with no external libraries. The checker constructs each graph \(K_{m,n}-M_t\) by its actual adjacency and tests every proper coloring over a named palette for an exactly-once color in each open neighborhood. It compares counts grouped by the number of shared matched-pair colors with the independently implemented Stirling formula for every \(2\le m,n\le4\), \(0\le t\le\min(m,n)\), \(1\le q\le4\), and eight further parameter cases. The total number of exact profile comparisons is **136**.

For every \(2\le m,n\le10\) and allowable \(t\), the coefficient formula was checked against the stated chromatic threshold and minimum-color counts; this gives **447** tested parameter triples. The exact four-color four-pair crown profile is \(216+144u^2+24u^4\).

Actual successful execution:
```
EXACT_PROFILE_COMPARISONS 136
CHROMATIC_CLASSIFICATION_CHECKS 447
CROWN_FOUR_COLOR_PROFILE {0: 216, 1: 0, 2: 144, 3: 0, 4: 24}
VERIFY_OK
```

No result concerning arbitrary deleted-edge graphs, list variants, or independent mathematical audit is asserted.
