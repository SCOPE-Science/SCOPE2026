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

Run `python3 verify.py` using only Python's standard library. The program performs exact arithmetic with `fractions.Fraction`; it does not need web access, numerical packages, reference tables, or unpublished data. The expected output is:

```
Grid denominator 2: 7966 nondegenerate instances passed
Grid denominator 3: 107205 nondegenerate instances passed
Sharp 3/2 mode separation witness passed
```

The finite verifier enumerates all independent probability triples from two rational simplex grids through five factors, checks the full CDF sandwich `Pr(K <= k) <= Pr(J <= k) <= Pr(K <= k+1)` and the cross-modal bound, and checks the exact two-factor sharpness example. It tests 115,171 nondegenerate instances, which are **not** an exhaustive test over arbitrary real parameters or arbitrarily many independent factors. The theorem's infinite-family justification is the explicit Hurwitz-stability/interlacing/coupling proof in `RESULT.md`, with its boundary limit argument. The cited strict Hermite–Biehler theorem and Darroch's theorem are external mathematical premises stated with references, not independently re-proved here.
