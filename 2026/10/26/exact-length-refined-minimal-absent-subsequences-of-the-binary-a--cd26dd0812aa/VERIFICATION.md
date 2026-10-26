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

The enclosed `verify_binary_mas.py` uses standard-library-only, literal scattered-subsequence tests and polynomial recurrence checks. Execute:

`python3 verify_binary_mas.py`

Expected terminal line starts with `ALTERNATING_BINARY_MAS_PASS`. The direct test covers all 1,398,078 binary candidate words of lengths \(1\) through \(2m+1\) for \(m=1,\ldots,9\). It compares literal absence/minimality with the independent greedy-cost/local-pattern criterion. A separate exact count using stars-and-bars run compositions agrees coefficientwise with the rational-function recurrence for \(m=1,\ldots,160\). The first ten source-length totals are \(3,5,9,16,28,49,86,151,265,465\).

The proof for infinitely many values does not rest on these tests. Its critical mathematical steps are the exact greedy embedding position, all positions' deletion effects, an exhaustive maximal-run grammar, and a formal odd-coefficient extraction. No independent mathematical audit was performed. No larger-alphabet or unrestricted-source claim is tested or asserted.
