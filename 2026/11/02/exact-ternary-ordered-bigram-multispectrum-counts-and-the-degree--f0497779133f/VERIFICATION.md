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
# Verification information

## Reproduction

Run `python3 verify_ternary_profiles.py` using Python 3.8 or later and its standard library. A successful run prints:

```
VERIFY_OK word_lengths=2..11 literal_words=265716 sum_distinct_profiles=14404 matrix_degrees=1..10 rational_coefficients=1..20 Euler_criterion_vs_literal=TRUE
```

The program enumerates every ternary word with between one and ten adjacent pairs and computes its ordered-bigram multiplicity vector. Separately, it enumerates all nonnegative integer nine-vectors of each tested weight and applies the degree-balance/weak-connectivity directed Eulerian-trail criterion. It compares the two complete finite sets and checks the coefficients of the rational expression using exact integer arithmetic. It additionally checks the empty bigram observation for single-character source words.

## Limits

All tests are finite. They do not independently certify the general Eulerian theorem, the formal generating-function derivation, or completeness of the literature comparison. The proof in `RESULT.md` is intended to establish those all-length statements. No independent audit has been performed.
