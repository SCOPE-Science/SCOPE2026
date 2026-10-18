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

# Finite exact checks and mathematical limits

The companion `verify.py` runs with the Python standard library: `python3 verify.py`. It enumerates all \(2^{2k}\) ordered pairs of digits at depths \(0\le k\le7\), retains values \(n<4^k\), and compares their exact representation counts with the carry recurrence at every position. It checks the support count and maximum against the stated recurrences, and independently enumerates reachable nonnegative carry vectors for \(0\le k\le21\), including explicit Fibonacci attaining words. The observed output is `MOSER_COEFFICIENT_THREE_EXACT_REGRESSION_OK k=0..7 brute; k=0..21 states; pairs= 21845`.

These tests are finite and do not certify the claims for arbitrarily large \(k\). The infinite support count depends on the complete two-carry transition classification; the infinite extremal formula depends on the Fibonacci induction and explicit witnesses. The step from powers of \(4\) to all real \(X\ge1\) depends on monotone bracketing.
