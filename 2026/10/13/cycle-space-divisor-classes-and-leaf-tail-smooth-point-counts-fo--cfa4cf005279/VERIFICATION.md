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

`CHECKER.py` uses only Python's standard library. Run from this directory:

```sh
python3 CHECKER.py
```

Expected output is contained verbatim in `CHECKER_OUTPUT.txt`. The program reconstructs facet matrices, finds integral spanning-tree minors of determinant \(\pm1\), compares local class-group ranks to independent frontier/leaf counts, and tests the complete recurrence and smooth-count product on every rooted labeled tree with \(1\le n\le6\) (17,471 filters). It separately checks complete binary trees of heights \(0,1,2,3\).

The determinant tests certify integral saturation only in the finite configurations tested. The proof in `RESULT.md` establishes saturation and the rank formula for every rooted tree by the connected integral incidence-complex argument. No computer enumeration is used as a substitute for this proof.

Self-review has passed for the stated theorem. Independent audit has not been performed.
