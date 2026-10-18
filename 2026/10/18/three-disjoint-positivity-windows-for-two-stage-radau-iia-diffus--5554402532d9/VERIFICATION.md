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

# Verification and scope

The analytic proof in `RESULT.md` derives all four symmetry classes of matrix entries from three mutually orthogonal graph-Laplacian projectors. The denominators are strictly positive, so the sign checks reduce to a quadratic and a quartic. The minimum of the scalar stability function gives the exact threshold of ten versus eleven leaves. Descartes' rule and three strictly located sample signs give the exact count, order, and simplicity of the two positive quartic roots.

The standalone `verify.py` uses rational Gaussian elimination (not floating-point eigenvalue calculations) to compare direct matrix-function computations with the four entry formulas for 192 graph/timestep cases and checks conservation and relevant signs. It also verifies the indicated integer sign identities for parameters up to 1000. These finite checks support the displayed algebra; the proof for every leaf count and real timestep is analytic. Numerical root values are explanatory only.

The result does not assert positivity at Runge–Kutta internal stages, any error tolerance, or extension to arbitrary graph Laplacians or weighted stars. Independent audit: not performed.
