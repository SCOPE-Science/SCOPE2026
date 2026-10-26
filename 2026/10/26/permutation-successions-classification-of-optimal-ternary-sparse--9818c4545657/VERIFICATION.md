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

# Reproduction

The standard-library Python 3 checker is `checker.py`. From the directory containing it, run:

```sh
python3 checker.py
```

The checker independently computes one-deletion descendants; tests every signed permutation with direct set-intersection comparisons for \(k\le8\); counts every codebook of size \(n-1\) by direct combination search for \(2\le n\le6\); compares the independent permutation sum to the dynamic recurrence; and tests the displayed family through \(n=100\). It passed these tests when the package was prepared. The implementation uses no external modules, downloaded files or hidden assets.

The *universal* assertions are justified by the capacity bound, coordinate bijection and exact zero-deletion collision lemma in RESULT.md, not by finite exhaustive testing. Earlier priority is not independently certified, and the full text of the 1984 nonbinary-code paper was not available for inspection.
