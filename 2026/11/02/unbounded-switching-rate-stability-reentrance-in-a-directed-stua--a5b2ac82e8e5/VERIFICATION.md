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

# Reproducible checks

Execute `python verify_switching.py` with Python 3 standard library. It reconstructs the two complex two-by-two variational blocks for sample strictly positive parameters, forms the half-step exponentials directly, and checks the exact real trace/determinant identity against the product in 60 direct comparisons. It also verifies the analytical discriminant and averaged generator identities, prints and asserts interleaved stable/unstable examples at \(u=1/20\), \(v=1000\), and checks fast-switching stability. The program is a finite numerical *consistency* and exact-to-floating-identity check. The infinite quantified alternation follows from the explicit asymptotic proof in RESULT.md, not the run log.

The global nonlinear dynamics, basin sizes, unit-circle-boundary nonlinear behavior and fixed-reactive-coupling total number of windows are **not** established. Neither source screening nor these computations certify historical priority. Independent audit has not been performed.
