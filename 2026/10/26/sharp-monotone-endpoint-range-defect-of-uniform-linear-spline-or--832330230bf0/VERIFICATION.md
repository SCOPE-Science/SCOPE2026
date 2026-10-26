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

# Reproducibility and scope

Run `python3 spline_boundary_verify.py` using Python 3's standard library. It uses `fractions.Fraction` and verifies all endpoint-kernel boundaries and stationary points **exactly**, for each mesh count from 1 through 120. It recomputes the coefficients from the rational Riccati recurrence and checks the terminal tridiagonal relation, positivity, strict decay, exact delta formula, and the sharp global minimum and maximum over one-jump responses.

Separate symbolic calculations simplified the first three delta values, the fixed-point limit, and the inequalities that exclude later-cell extrema for all larger meshes. The mathematical argument, not finite computations, establishes the universal quantified claim. No global interior evaluation or arbitrary-knot range claim has been verified or made. One potentially relevant published chapter was only accessible as an abstract, so its full-text originality comparison remains incomplete.
