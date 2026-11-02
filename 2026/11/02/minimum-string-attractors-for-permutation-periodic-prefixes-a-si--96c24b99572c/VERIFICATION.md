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

# Reproducibility

The standalone verifier uses only Python 3 standard-library modules. Execute `python verify.py` after extracting the embedded files into one directory. It constructs full literal words and verifies every substring occurrence, then compares each size-\(q\) selection with the claimed finite-parameter characterization and count. It additionally verifies the occurrence starts of the proposed critical boundary factor.

Observed output:

```
VERIFY_OK parameter_cases=88 candidate_sets=52430 valid_sets=51595 invalid_sets=835 alphabet_sizes=2..6 complete_factors=True
```

The finite computation examines \(q=2,3,4,5\) with \(m=1,\ldots,5\) and \(q=6\) with \(m=1,2,3\), and all legal \(r\) in each case. It makes no assertion for untested parameters or about originality. Universal correctness depends on the exhaustive mathematical cases in RESULT.md.
