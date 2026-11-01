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

# Verification and reproducibility

The standalone Python 3 program `verify.py` has no external dependencies. Running `python3 verify.py` enumerates the Boolean majority halfcube for \(d=3,5,7,9,11,13\), constructs the exact Walsh Gram entries as integers (equivalently rationals after dividing by \(2^d\)), checks the degree-one and degree-three Fourier coefficients and all entries of the formula for \(B^*B\). It also checks elementary ratio and ordering identities for 4,999 odd dimensions. The observed standard output is:

```text
VERIFY_OK dimensions=3,5,7,9,11,13 exact_gram_entries=16215 exact_distinct_walsh_moments=2049 dimension_ratios=4999
```

These are exact finite checks, **not** an exhaustive computation over all dimensions. The infinite-dimensional-family theorem follows from the explicit character-coefficient calculation, the finite pair-incidence identity, and the exact singular-vector decomposition in RESULT.md. Particular boundaries: at \(d=3\), three zero eigenvalues occur; only odd dimensions \(d\ge5\) have strictly positive lower restriction bounds. No external independent mathematical audit or noisy-measurement experiment has been performed.
