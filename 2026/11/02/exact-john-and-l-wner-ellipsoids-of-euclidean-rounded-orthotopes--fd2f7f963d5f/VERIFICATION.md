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

# Verification record

The proof checks are analytic: the John candidate is explicitly included in the Minkowski sum, any contained ellipsoid is bounded by the product of the squared coordinate projection radii, the positive scalar contact parameter exists uniquely, the outer containment deficit is a nonpositive sum with strictly positive quadratic coefficients, and unrestricted Löwner optimality follows from sign averaging and the matrix arithmetic–geometric mean inequality.

`VERIFY.py` was executed from the extracted research artifact. It reported `PASS: 150 parameter instances; 30,000 independently sampled points; product KKT, contact isotropy, numerical optimization`. It compares the scalar root to independent constrained numerical optimization and tests the contact design in dimensions 3, 4, 5, 8, 12. The random sampler is not exhaustive; the proof is necessary for the universal statement.

No independent review, external formal proof certification, or independent priority certification was performed. The claim is limited to positive half-lengths and Euclidean balls, as specified in the result.
