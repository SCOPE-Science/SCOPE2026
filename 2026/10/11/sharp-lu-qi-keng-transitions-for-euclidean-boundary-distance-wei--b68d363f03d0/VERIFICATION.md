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

The proof's mathematical checks are exact and self-contained: the radial beta moments, convergence and completeness of the monomial basis, odd-part binomial identity, Cayley map range, exhaustive integral-index equation, and the derivative nonvanishing at every listed zero.

The accompanying Python script `kernel_check.py` checks coefficients against the closed formula at a finite selection of parameters and scalar points and verifies predicted root locations near the first transitions. This script is not a formal certificate of the infinite-family statement.

The normalization is ordinary planar area, not area divided by \(\pi\). In the zero-count formula, a strict upper bound excludes a zero lying at \(s=-1\) at the critical exponents. All branches are holomorphic principal powers on \(|x|<1\). No independent mathematical audit is included.
