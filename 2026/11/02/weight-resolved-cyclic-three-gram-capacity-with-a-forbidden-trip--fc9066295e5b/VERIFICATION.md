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

The standalone `verify.py` was executed against its embedded source contents with Python 3. It exhaustively generated permitted cyclic indexed binary words of all lengths from 1 to 16, compared their weight-stratified three-gram profile classes to the closed count, generated constructive witnesses for every parameter class through length 70, checked the bivariate generating function coefficients through length 70, and confirmed saturation through weight 39.

Observed output:

```
VERIFY_OK literal_max_n=16 literal_words=37592 literal_profiles=394 constructive_max_n=70 constructed_distinct_profiles=93573 bivariate_gf_verified=True constant_weight_saturation_verified=True
```

The verification is finite and makes no claim of exhaustive checking beyond these lengths. The all-length formulas, phase law, and period statement follow from the mathematical proof in `RESULT.md`. No independent audit has been performed.
