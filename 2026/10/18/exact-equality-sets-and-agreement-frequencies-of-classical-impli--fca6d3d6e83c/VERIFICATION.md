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

# Finite verification and proof boundary

Run `python3 implication_spectrum_verify.py` with Python 3.9 or later and only the standard library. The script directly generates all implication-only term functions by closure on truth tables for arities \(1,2,3\), then independently enumerates candidate forcing-coordinate truth tables and positive-face supersets and compares the resulting sets.

Observed output:

```
arity=1 closure_rounds=2 distinct_terms=2 equality_sets=2 numerator_range=[1,2]
arity=2 closure_rounds=3 distinct_terms=6 equality_sets=8 numerator_range=[1,4]
arity=3 closure_rounds=5 distinct_terms=38 equality_sets=112 numerator_range=[2,8]
IMPLICATION_SPECTRUM_VERIFY_OK
```

The exhaustive checks run for three finite arities only. The general all-arity theorem is derived by structural induction for the forcing coordinate, an explicit recursive encoding of Boolean functions in the implication-only fragment, and pointwise construction of two functions whose equality set is prescribed. The computational checks neither establish originality nor prove the general theorem. The lower-bound witness \(p_1\approx(p_1\to p_2)\) is a direct truth-table calculation.
