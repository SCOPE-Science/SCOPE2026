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

Run `python verify.py` (standard library). Actual result:

```
SERIES_OK defects=0..3 semilength=0..80
WORDS_OK semilength=0..11 checked=82500 Dyck_words
COEFFICIENT_OK first two deficiency strata
```

For exact finite symbolic matrix arithmetic, optionally run `python symbolic_certificate.py` with SymPy installed. Actual result: `SYMBOLIC_OK` for each defect 0, 1, 2 and 3, and all four formulas match. The symbolic program recomputes the full transition matrix from two-bit greedy steps and evaluates its rational inverse. The direct enumerator is separate from the matrix evaluator. The proof of infinitely many cases is in `RESULT.md`; tests do not certify an infinite range by themselves.

The source definitions and prior-literature comparisons are recorded in `RESULT.md`, `REVIEW.md` and `AUDIT.json`. This is not an independent scientific audit.
