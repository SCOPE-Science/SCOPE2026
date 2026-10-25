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

# Verification scope

The all-parameter theorem is proved in `RESULT.md` by explicit equidistance counting, a coefficientwise Vandermonde argument, and an exact treatment of antipodal pairs. The separately included `verify.py` uses integer arithmetic and the Python standard library.

Reproduce with `python3 verify.py`. The verified output includes:

```
COEFFICIENT_LEMMA_PASS r=1..150
JOHNSON_CLASSIFICATION_PASS n=2..80, cases= 1600
EXHAUSTIVE_PASS 4 2 vertices 6 threshold 5
EXHAUSTIVE_PASS 8 4 vertices 70 threshold 37
ALL_PASS
```

The coefficientwise test covers a finite range of polynomial degrees and dimensions. The classification test checks 1,600 pairs of integer parameters using the derived closed equidistance expression. The separate small-graph check constructs actual vertices and measures all pairwise distance profiles, rather than using the binomial summation. Neither finite test can by itself establish the infinite theorem. Only the supplied symbolic proof supplies that inference.

No independent external verification has been performed.
