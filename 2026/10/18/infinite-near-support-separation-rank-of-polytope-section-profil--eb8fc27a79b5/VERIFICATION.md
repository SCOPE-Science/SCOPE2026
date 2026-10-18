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

# Reproduction and boundaries

The supplied standalone script `checks.py` uses Python 3 and standard-library exact fractions. Run `python3 checks.py` after extracting the files.

The script checks the two-triangle decomposition of a unit square for three rational Euclidean unit normals; exact piecewise-linear section density against the independently known convolution of two uniforms; the nonzero second-highest vertex coefficient; three distinct knots lying in one shared near-support interval; exact zeroth and first integrated moments; and, independently, total volume and first projection moment for the standard tetrahedron using a rational unit normal. The checked geometry also confirms a nonzero coefficient for each generic projected tetrahedron vertex.

These are exact rational tests, not numerical approximations or exhaustive certification of all polytopes. The universal theorem is proved in `RESULT.md`: the sign argument for a vertex exposed by a generic direction is the crucial general noncancellation certificate, and distributional differentiation turns separated moving knot locations into linearly independent functions.

The conclusion is about exact finite separation rank, not approximate separation rank. Source overlap searches were conducted against the cited near-boundary theorem and existing spline formulas; historical priority remains subject to unindexed literature. No independent audit is claimed.
