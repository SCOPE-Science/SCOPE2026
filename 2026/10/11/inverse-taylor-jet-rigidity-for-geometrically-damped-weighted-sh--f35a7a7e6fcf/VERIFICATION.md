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

# Verification boundaries
The proof is analytic, not based on finite experiments. It establishes the uniform simple spectral branch for complex parameter near zero, the necessary coordinate order bounds, the leading coordinate products, an operator-norm differentiable interpolation, and an absolutely controlled tail before integration. The special boundary \(k=1\) and finite truncations having zero later weights are included in these estimates.

A supplementary reproducibility check, `verify_jet.py`, uses only the Python 3 standard library and 100-digit decimal arithmetic. It constructs finite Jacobi characteristic polynomials, bisects their largest roots, and checks first-difference orders \(k=1,2,3,4\) at two small positive parameters. On execution it prints `INVERSE_JET_FINITE_TRIDIAGONAL_CHECK_OK`. The finite check does **not** establish coefficient uniqueness for all positive sequences; it supplements the full proof in RESULT.md. The motivating 2026 primary paper's full text could not be inspected, so an originality comparison remains access-limited. No external or independent audit was performed.
