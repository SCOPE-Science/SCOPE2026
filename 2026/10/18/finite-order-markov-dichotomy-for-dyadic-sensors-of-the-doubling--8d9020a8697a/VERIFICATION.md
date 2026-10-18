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

# Verification record

The proof covers every positive dyadic cutoff strictly between zero and one and every nonnegative Markov order. Its decisive integer-divisibility lemma is proved directly: if positive integers have an eventually constant rational ratio, the reduced denominator must equal one. In the constructed all-constant-word count family, elementary finite-block constructions force exponential growth faster than one, while disjoint-block omission bounds it by an exponential rate strictly less than two. Hence an eventual integer ratio is impossible.

The executable `verify.py` was run with the standard Python interpreter using integer arithmetic and the `fractions.Fraction` standard-library class. Output:

```
VERIFY_OK 114 thresholds, 570 exact brute/DP comparisons, 3876 finite persistence bounds
```

The first family compares independently coded exhaustive enumeration and a dynamic program; the second family checks upper and lower bounds at longer finite lengths. The verifier also checks one-symbol probabilities and the independent half-threshold normalization. This finite evidence checks implementation and edge cases only; all infinite claims follow from the written argument, not the finite test counts. There has been no independent audit.
