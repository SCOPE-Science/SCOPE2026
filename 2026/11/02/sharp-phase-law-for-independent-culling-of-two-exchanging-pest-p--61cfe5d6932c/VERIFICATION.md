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

Reproduce the arithmetic checks with `python3 check.py` using only the Python 3 standard library. The implementation computes each propagator by independently programmed scaling-and-squaring of the matrix exponential series; it does not insert the proposed trace identity into the monodromy. It verifies 1,500 deterministic random admissible parameter samples for trace, determinant, reflection, phase bounds and discriminant positivity, and performs exact rational matrix multiplication to verify the example's two opposite threshold signs. **Recorded outcome: 9,005 checks passed.**

For the infinite mathematical claim, inspect the algebraic proof in `RESULT.md`: expand the two rank-one diagonal impulses, exploit trace cyclicity and the semigroup law, and use the hyperbolic identity to establish strict phase ordering. The finite checks do not prove the universal parameter statement, and no external audit or empirical field validation is represented.
