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

The included `verify_cyclic_good.py` is a Python standard-library checker. It was run directly from the package directory and returned:

`CYCLIC_ANTISQUARE_PASS exhaustive_n=1..15 test_words=65534 trace_n=1..60 rational_and_formula_n=1..120`

Independent finite paths: literal periodic-factor comparison against a direct cyclic-difference criterion on every binary word of lengths \(1\) through \(15\); a state-transition closed-walk enumerator of all admissible difference words for lengths through \(60\); and algebraic coefficient extraction from the claimed rational series against the explicit binomial count for lengths through \(120\). The code checks source words, not merely previously saved numerical tables.

Finite verification does not independently establish the all-length theorem. The infinite proof additionally relies on the published minimal-forbidden-antisquare and exceptional-bi-infinite-factor results explicitly identified in `RESULT.md`. Those external facts were read in an accessible full-text version. No independent audit or external formal certification was performed.
