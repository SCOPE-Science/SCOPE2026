---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The cardinal coefficients sum to 1 and on each half-interval at most one is negative, by at most 1/8. On the upper half, a single-axis interpolation of a monotone row can be written as its minimum plus two nonnegative increments, and lies in [0,9/8]; interpolating those values along the other axis bounds the result below by −9/64. When both half-intervals are lower, write the negative coefficients as −a and −b. The positive-positive interior may be discarded for a lower bound. Each entry multiplying a negative tensor weight is at most f₂₂; retaining the positive corner gives the bound −[a(1+b)+b(1+a)−ab]f₂₂≥−17/64. This covers the continuum and the boundaries. The data that are 1 on the top-index row or column and 0 elsewhere give equality at (1/4,1/4). Reflection in both coordinates and complement transfer the lower extremum to the upper one. Mixing either witness with (i+j)/4 gives strict data without changing the end range, and converges to the witnesses. Thus strict sharpness is limiting only. Affine normalization preserves both sharp constants.

## originality

PASS

The strongest inspected matching indexed statements treat univariate cubic Lagrange interpolation, Jacobi projection or rational interpolation. The available full Floater–Peña paper studies different coefficients, bases and a different property. The exact isotone-data biquadratic nodal range, including its extremizers, is not covered by these or the standard unrestricted Lebesgue-constant calculation.

## value

PASS

The standard uniform biquadratic reconstruction is a natural object for checking whether monotone grid data stay within range. The gain over the unrestricted envelope is numerically modest, but the sharp bound quantifies the required buffer (more than a quarter of the data range on each side), provides an explicit monotone witness and rules out fixing the defect by requiring strict nodal monotonicity alone. The exact coupled-data restriction and witness are useful where a shape- or range-preserving reconstruction is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
