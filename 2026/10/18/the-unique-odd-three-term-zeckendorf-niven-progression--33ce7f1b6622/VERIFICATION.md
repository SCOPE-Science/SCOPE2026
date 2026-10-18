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

# Verification procedure

Execute `python3 VERIFY.py` (Python standard library only) from the directory containing this file. The verifier reconstructs greedy Fibonacci summand counts, exhaustively checks the 34 initial induction cases, both exact four-offset boundary base tables, all boundary parity cases for both Fibonacci-index parities and auxiliary parameter parities, and an additional 100000 consecutive start values. It also confirms that the only odd three-term Zeckendorf–Niven start below 100000 is 1. The expected final status is `VERIFY_OK`.

The infinite statement does not rely on finite enumeration. Its essential steps are the exact greedy decomposition recurrence, the two-step boundary recurrence, four boundary offset cases, and the divisibility argument in `RESULT.md`. The calculation provides a reproducible cross-check of those finite identities only. The scientific review is not an independent audit.
