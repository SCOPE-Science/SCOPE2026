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

# Reproducibility and mathematical limits

Run `python3 verify_polydependence.py` with Python 3.10 or later. The checker has no third-party dependencies and computes all pairs of binary relations over up to three key/value labels, the complete violation histogram, and the independent per-key convolution predicted by the theorem. It also evaluates the endpoint-valid exact zero-event expression at 56 Bernoulli parameter combinations and compares PGFs at three large sizes against the two limiting distributions.

Successful execution produces:

```
EXHAUSTIVE 1 pair_relations 4 satisfying 4 support 1
EXHAUSTIVE 2 pair_relations 256 satisfying 81 support 5
EXHAUSTIVE 3 pair_relations 262144 satisfying 5832 support 18
BERNOULLI_EXACT_OK 56
LIMIT_CHECK 500 compound_abs_error 0.000474 poisson_abs_error 0.010679
LIMIT_CHECK 2000 compound_abs_error 0.000119 poisson_abs_error 0.005242
LIMIT_CHECK 8000 compound_abs_error 3e-05 poisson_abs_error 0.002595
VERIFY_OK
```

This is full finite enumeration only for the stated small sizes, plus numerical examples for the limit; it is not an exhaustive test over every alphabet size or a substitute for the proof's probability estimates. The Poisson limits were established analytically using independent fibers and convergence of probability generating functions. No independently conducted audit is claimed.
