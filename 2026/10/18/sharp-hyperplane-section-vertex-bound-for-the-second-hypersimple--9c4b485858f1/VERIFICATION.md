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

`checker.py` is a standalone Python 3 checker requiring only the standard library. Running `python3 checker.py` during preparation returned:

```
EXHAUSTIVE_THRESHOLD_WORDS_OK 32764
EXACT_CENTERED_AND_GENERAL_NORMALS_OK 594
HYPERSIMPLEX_MAX_SECTION_OK
```

The checker enumerated every isolated/dominating word for each \(3\le n\le15\), verifying direct triple counts, maximum value, and balanced-suffix equality. For \(3\le n\le35\), it used exact integer, sum-zero normals to check 297 generic centered perturbations and 297 generic unconstrained shapes of normal coordinates, counting all Johnson-edge crossings. It verifies no formulas outside those finite ranges. The all-dimensional proof requires no numerical approximation; it is reconstructed in RESULT.md. Source comparisons are summarized in REVIEW.md and AUDIT.json. Independent mathematical validation has not been performed.
