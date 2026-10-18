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

Run `python3 loop_cycle_verify.py` using Python 3 and only the standard library. The script executes two independently implemented finite semantics: relational program composition and satisfaction on actual vertices, and a quotient calculation using signed displacement residues. The checked cases include tests nested inside Kleene-star programs and formulas using negated loops. A deterministic seed fixes the test family.

Expected and observed output:

```
CYCLE_LOOP_VERIFY_OK formula_semantics=5280 arithmetic=2210
```

The first count is \(240\) randomly generated formulas on each of the \(22\) directed cycles of lengths \(1\) through \(22\). The second count covers explicit divisibility and singleton-recognition formulas on lengths through \(170\). Computations support but cannot establish the infinite theorem; the full proof requires the semilinearity and number-theoretic argument in `RESULT.md`.
