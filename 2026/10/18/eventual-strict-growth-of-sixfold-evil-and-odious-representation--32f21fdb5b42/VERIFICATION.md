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

# Reproducibility and limits

Run `python verify.py` with Python 3.8 or later. The checker forms the signed Thue–Morse polynomial of dyadic lengths \(1,2,4,\ldots,128\), computes the exact sixth integral by Parseval on a cubed polynomial, and checks eight results against the independent three-dimensional Laurent transfer. Six integer evaluations certify the sign brackets for its cubic characteristic polynomial. It then forms exact sixfold ordered convolution tables of evil and odious integers through \(n=200\) and records all nonincreasing points in that finite range.

These finite tests are reproducible arithmetic checks of the proof components, not an exhaustive proof of the theorem. The unbounded proof uses the exact Laurent recurrence, strict eigenvalue brackets, the dyadic block triangle inequality, Abel summation, Hölder's inequality, and a Cauchy coefficient estimate. The polynomial and exponents are checked symbolically in `RESULT.md`. The experiment gives **no** independently certified global cutoff. Independent mathematical audit has not been performed.
