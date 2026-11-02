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

# Exact reproducibility and boundaries

Run `python verify_klein_polar.py` from the directory containing that script. Python 3.10+ and SymPy are required. It uses no inputs, no saved computation state, no network connections, and no external services. It computes the bordered Hessian and the degree-21 Jacobian invariant from their definitions, proves coefficientwise division by 9 and 14, tests cyclic invariance, divides the pullback polynomial over the integer polynomial ring, and checks its degree-42 quotient and characteristic-three square congruence. It then checks all 728 nonzero elements of the explicitly given six-dimensional field have multiplicative inverses; enumerates its 21 roots of the degree-21 polynomial; expands the product of 21 line forms coefficientwise; and enumerates all 210 pairwise intersections and their projective Frobenius degrees.

Expected final marker: `KLEIN_POLAR_CHAR3_FROBENIUS_TOWER_AND_F729_ARITHMETIC_CERTIFICATE_PASS`.

The statement for every integer \(k\ge0\) follows from the algebraic fact that the characteristic-three gradient is cyclic Frobenius and the degree-21 invariant is cyclically symmetric; it is **not** inferred from testing finitely many iterates. The invariant is normalized integrally before reduction, and the claim is about the displayed divisor models only. Independent audit: not performed.
