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

The analytic computation uses the normalized Bergman reproducing kernel and the two-point Gram inverse. The independent algebraic identities used to locate the maximum are reproduced by `checker.py` with SymPy installed according to `requirements.txt`.

Checks made: two-by-two Gram identity; rational simplification; exact two-variable derivative factorization; polynomial resultant; lexicographic elimination of common roots; exact Sturm counts and rational isolating brackets; exact upper bounds on all angular boundary points; and the strictly larger rational interior test. Decimal values were additionally evaluated but are not proof of uniqueness. Only equal-modulus pairs and the specified quadratic target are covered.

The self-review is complete. No independent mathematical audit or validation has been performed. Historical-priority risk outside inspected sources remains.
