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

# Reproduction and limits

Use `python verify.py` in a Python 3 environment with `sympy` and `mpmath`. It checks the hyperbolic identities and small-argument coefficient, the positive finite coefficients in two infinite-series proofs, the formulas for mean and variance against independent high-precision derivatives of the first-passage Laplace transform over eight parameter sets, the positive fourth-cumulant formula, published effective diffusivity equivalence, and Taylor-residual checks for the implicit scaled cumulant-generating function.

The coefficient inequalities for arbitrary orders are established by induction in RESULT.md; finitely many code assertions do not replace them. The renewal pole and analyticity argument is mathematical rather than numerical. The code does not simulate full physical Brownian trajectories or independently certify prior-literature priority. No independent audit was conducted.
