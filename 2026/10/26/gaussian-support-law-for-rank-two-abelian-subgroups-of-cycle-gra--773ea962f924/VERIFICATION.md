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

The executable `verify.py` uses three distinct descriptions: enumerating ordered bases and checking all edge determinants directly over prime fields; counting support subsets via induced components; and calculating a two-state polynomial trace recurrence. It compares all coefficients, not only the totals. Direct exhaustive cases: \((q,n)=(2,3\ldots7),(3,3\ldots5),(5,3\ldots4)\). Exact component/transfer arithmetic comparisons: \(q\in\{2,3,4,5,7,9\}\), \(3\le n\le12\). The run returned `VERIFY_OK`.

The direct checks use prime fields; the component/transfer identities for \(q=4,9\) are integer polynomial evaluations, not implementations of extension-field arithmetic. The theorem covers any finite field because the projective line and nonzero vector counts depend only on q. All limit statements depend on the analytic proof, not on finite checks. A full independent mathematical audit has not been performed.
