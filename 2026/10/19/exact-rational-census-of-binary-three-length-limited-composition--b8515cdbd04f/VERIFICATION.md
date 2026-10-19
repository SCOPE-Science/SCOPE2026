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

# Reproduction and scope of verification

Run `python verify.py` with Python 3 and no external packages. The program recomputes coefficients from the displayed rational function via an integer recurrence, then compares them with three independent routes:

1. Literal substring-composition counting on all binary words of each length \(1\) through \(16\), including the exact equivalence to the run-endpoint signature.
2. Structural enumeration of feasible zero and one run counts, singleton status, and allowable boundary counts for lengths \(1\) through \(20\), without enumerating individual words.
3. Incremental last-two-bit dynamic programming through length \(38\), retaining all observed multiplicities without using run decomposition.

Successful output: `VERIFY_OK direct=1..16 structural=1..20 dynamic=1..38`, followed by `COUNTS_1_38=...`. Those ranges are exhaustive over the stated finite state spaces; beyond them the proof, not computation, is the justification. No independent audit was performed, and no claim about another implementation or external certification is made.
