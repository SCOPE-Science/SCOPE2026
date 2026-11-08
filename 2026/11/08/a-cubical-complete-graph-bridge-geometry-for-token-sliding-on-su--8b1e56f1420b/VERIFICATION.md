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

`check_spider_formula.py` independently enumerates all size-\(m-1\) independent sets on \(S_m\), reconstructs legal single-edge slides, and compares every ordered-pair breadth-first-search distance against the explicit formula for \(3\le m\le7\). It also checks exact vertex and edge counts.

`check_spider_independent.cpp` separately enumerates independent sets using bitmasks, reconstitutes all legal edge slides, and checks every ordered pair for \(3\le m\le9\). It verifies the stated vertex and edge counts and diameter \(2m\).

For both, compile/run from a directory containing the two attached source files:

```sh
python3 check_spider_formula.py
g++ -std=c++17 -O2 check_spider_independent.cpp -o check_spider
./check_spider
```

Observed outcomes after running the packaged source files were `ALL_PAIRS_PASS` in the Python checker and `ALL_PASS` in the C++17 checker, with individual `PASS` reports for every checked arm count. The proof is elementary and independent of finite runs; no conclusion about other token layers follows.
