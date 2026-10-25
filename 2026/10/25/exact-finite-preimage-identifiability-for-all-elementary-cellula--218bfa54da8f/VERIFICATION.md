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

Run `python3 verify.py classification.csv` in the directory containing both files. The checker uses the Python standard library and exact integer arithmetic only; no external dependencies or data services are required.

The checker constructs complete reachable capped-count state graphs for all 256 elementary binary rules, proves a finite complete closure (at most 81 formal states), and checks its generated classification byte-for-byte against `classification.csv`. It independently counts all \((n+2)\)-bit predecessor blocks for every rule and output length \(1\le n\le6\), comparing both the exact singleton-predecessor condition and admissible singleton-right-endpair condition. These constitute 32,256 output-word instances; they are confirmatory finite checks, not a substitute for closure over all lengths.

The exact assertions include the histogram \((16,52,56,28,4,8,92)\) for lengths one through six and never, the eight rules requiring length six, the 42 right-boundary-only rules, and the gap-frequency vector \((132,20,8,4)\). Any changed CSV, counting algorithm discrepancy, failed shortest-witness condition or incorrect class statistic aborts with an assertion error. The self-contained complete-closure certificate, not a numerical convergence test, supports the unrestricted conclusions.

No independent audit has been performed; this verification records reproducibility and the limits of the available checks.
