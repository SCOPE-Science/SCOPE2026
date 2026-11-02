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

# Reproduction and scientific limits

Run with Python 3 using only the standard library:

```sh
python3 oa_logic_verify.py
python3 oa_independent_check.py
```

The first check constructs all 2-dimensional affine-linear index-one arrays over explicitly represented fields of orders \(3,4,5,7,8,9,11\) and every row count \(2\le t\le q-1\). For each array it examines every unordered anchor pair, all four third-point adjacency patterns, and the exact table formulas. It then takes a minimum-pattern witness set, deletes it, and checks that no witness remains. Its separate integer loop checks the claimed maximizing row count for all integers from \(3\) through \(299\). The second program independently calculates every two-point pattern count using direct triple loops over prime fields of orders \(3,5,7,11\), and exhibits the first damaging deletion at optimal row count for \(5,7,11\). The recorded outputs in `oa_logic_verify.out` and `oa_independent_check.out` respectively end in `RESULT PASS` and `INDEPENDENT RESULT PASS`.

These tests are finite verification, not an infinite proof. Arbitrary arrays and large prime-power fields are covered by the counting proof. Logical equivalence at every quantifier depth follows from the explicit arbitrarily long three-pebble strategy, not an exhaustive model checker. Historical priority has not been independently certified, and a related 2026 paper was not fully accessible for comparison.
