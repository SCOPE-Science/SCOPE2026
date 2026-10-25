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

The runnable standalone file `verify_wheel.py` uses breadth-first-search graph distances for the original definition and an independently coded gap predicate. It checks every rim subset for each rim size from \(7\) through \(16\), and both choices of including or omitting the hub. The total is \(130{,}944\) rim subsets, corresponding to \(261{,}888\) full wheel vertex subsets. All cardinality coefficients and metric-basis counts are checked exactly; the residue-class simplifications are additionally checked against the general coefficient formula for rim sizes through \(200\).

Run `python3 verify_wheel.py` and compare standard output byte-for-byte to `verification_output.txt`. The supplied finite checks cannot prove the infinite identities; the separate proof supplies those. No assertion of independent validation is made.
