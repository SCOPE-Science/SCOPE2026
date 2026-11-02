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

The all-cardinality proof relies on four logically separate steps: a Chebyshev rank-four argument on the first-quadrant unit-circle arc, continuous preservation of positive-definite quadruple interpolants, dense-open avoidance of all five-by-five lifted determinants, and the exclusion of finitely many proper hyperplanes in the constrained coefficient space. The online dimension bound uses an all-positive branch independence argument. No finite enumeration is treated as a proof for unbounded cardinality.

The attached `verify_ellipse_maximum.py` constructs ten explicit distinct rational points and performs exact, nonfloating-point determinant evaluations. It verifies all 210 quadruple interpolation equations have nondegenerate axis-aligned real ellipse solutions with positive quadratic coefficients, and that all 252 five-point lifted determinants are nonzero. The implied trace count is the exact binomial sum 386. The program checks no version outside those ten points; all-size assertion follows only from the mathematical argument.

Run: `python3 verify_ellipse_maximum.py`.

Expected output:

```text
AXIS_ELLIPSE_EXACT_WITNESS_PASS points=10 quadruples=210 quintets=252 traces=386
ALL_DETERMINANT_CHECKS_RATIONAL_PASS
```

Independent replication, additional historical-priority work, and extension to filled ellipses remain unperformed.
