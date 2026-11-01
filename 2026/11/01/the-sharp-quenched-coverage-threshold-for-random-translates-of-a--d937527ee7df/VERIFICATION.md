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

# Reproducible finite checks

Run `python verify.py` with Python 3.10 or later. No external packages are required. The verifier calculates the finite expected-coverage identity using exact rational alternating binomial sums, independently evaluates its complete homogeneous symmetric-polynomial form, and confirms nondegenerate rational rectangle-union volumes. It also performs seeded small-dimensional random-union diagnostics and computes numerical gamma/Gumbel crossover values via an integer-shape gamma CDF and deterministic quadrature. It checks the \(d^{-1/2}\) correction and half-volume threshold for selected dimensions and central-window parameters.

The executed check completed successfully with the output:

`PASS: 120 deterministic assertions/cases`

The probabilistic concentration statement and almost-sure limit are **not** verified by finite code. Their evidence is the explicit mathematical proof: exact gamma identity, gamma density expansion, exponential maximum moments, bounded differences, Borel–Cantelli, and monotone threshold inversion. The quadrature uses an asymptotic Gumbel approximation and is diagnostic only. Historical originality is not a computational property; priority comparisons and their limitations are documented separately. Independent mathematical audit has not been performed.
