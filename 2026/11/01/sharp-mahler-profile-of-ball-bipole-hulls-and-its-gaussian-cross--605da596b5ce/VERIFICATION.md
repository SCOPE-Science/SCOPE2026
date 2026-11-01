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

The self-contained `check.py` requires Python 3 and only its standard library. Execution command: `python3 check.py`.

The checker exercises these separately designed checks: exact rational integration in dimension three at \(t=1/2\); numerical monotonicity and endpoint agreement in six dimensions; direct geometric convex hulls of thousands of points approximating planar ball–bipole hulls, checked against a separately evaluated polar disk-slab area; leading nonzero coefficients at both endpoint regimes; Gaussian rescaling and independent numerical quadrature in dimensions 500 and 1000. All reported tests passed in this package.

Proof verification must still inspect the analytical differentiation and slicing arguments in `RESULT.md`. The tests are finite diagnostics rather than an infinite-dimensional proof or an independent audit. The near-ball numerical endpoint calculation is ill-conditioned at very small deficits and deliberately tested at moderate distances.
