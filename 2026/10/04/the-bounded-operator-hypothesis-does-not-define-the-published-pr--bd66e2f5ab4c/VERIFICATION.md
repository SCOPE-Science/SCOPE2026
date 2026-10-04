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
The source formula was checked against its stated operator assumptions.

Analytic checks:
- The denominator depends only on the symmetric part \(S=(B+B^*)/2\).
- A zero or skew-adjoint operator makes the quadratic contribution vanish.
- If the quadratic form takes both signs, scaling two states produces exact denominator cancellation.
- Strict one-signedness is equivalent to pointwise nonvanishing on all nonzero state pairs.
- Uniform one-sided coercivity implies \(|v|\le |D+\eta|/\beta\).
- A positive diagonal operator with eigenvalues \(1/n\) is bounded and strictly positive but gives unbounded feedback values on unit basis vectors.

Reproducibility checks:
- `verify.py` evaluates zero, skew, indefinite, and coercive matrix examples exactly.
- It checks exact cancellation for an indefinite form.
- It verifies linear growth of the quotient for finite sections of the \(1/n\) diagonal example.

Limits:
- The computations illustrate explicit witnesses; the general characterization is analytic.
- No independent audit has been performed.
