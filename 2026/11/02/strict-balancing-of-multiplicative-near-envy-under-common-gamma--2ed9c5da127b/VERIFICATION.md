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

The standalone `verify.py` executable uses Python 3's standard library, computes exact rational probabilities for integer Gamma shapes at rational tolerances using a finite integral expansion, and exhaustively compares positive bundle-count multisets over the documented finite parameter grid. It also cross-checks two-agent Beta binomial-tail probabilities and the sharp small-tolerance coefficient formula. The observed output after execution was:

```
VERIFY_OK exact_profile_comparisons=306 strict_comparisons=216 beta_reductions=108 small_tolerance_coefficients=checked
```

The all-shape and all-real-tolerance claims rest on the analytical Beta-Gamma, monotone likelihood-ratio and dominated-convergence arguments in `RESULT.md`. The executable does not purport to exhaust continuous shapes or prove historical novelty. Independent audit has not been performed.
