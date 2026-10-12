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

# Reproducibility and boundaries

Execute `python3 verify.py` from this directory with Python 3 and SymPy available. Expected terminal line: `VERIFY_OK`.

The program independently constructs the source-to-target polynomial relations and a graded Gröbner basis, computes all sixteen entries of the rank-four trace Gram matrix, and tests its determinant against the exact claimed factorization. It also verifies the source Jacobian, the quartic discriminant with its extra chart factor, the two ramification-plane parametrizations, the coordinate change to the Whitney umbrella, and explicit nondegenerate fold points on each ramification component.

The proof's global claims that each factor is irreducible, the finite birational parametrizations are normalizations, and geometric monodromy is \(S_4\) are supported by algebraic and topological arguments in `RESULT.md`. No finite symbolic test by itself establishes those statements; no independent external verification has been performed.
