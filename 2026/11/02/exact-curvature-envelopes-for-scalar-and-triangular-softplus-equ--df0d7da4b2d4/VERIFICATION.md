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

The included standalone `verify.py` requires SymPy and mpmath. Invoke it as `python verify.py` in the directory containing that file. It checks exact matrix resolvent/chain-rule identities against the closed formulas, the strict interior optimizer, a rational monotonicity identity, 1,500 deterministic high-precision triples, five singular contraction-gap examples, and three independently reconstructed exact-equilibrium finite-difference values. Its output is a diagnostic, not an exhaustive proof over all real parameters.

The analytic proof in `RESULT.md` supplies the actual universal quantifiers: every finite-bias slope is in \((0,1)\); every pair of slopes in \((0,1)^2\) is realizable by finite biases; the second-slope optimum is interior; the remaining expression is strictly increasing; and the one-unit derivative changes sign at a single interior point. The two-dimensional determinant follows from an exactly block-diagonal Hessian, not a numerical determinant estimate.

All claimed suprema are algebraic or asymptotic and require no external fitted parameters or data. The limiting bias sequence is not a fixed network or any finite-trained solver, and no floating-point test certifies actual PDE residuals. Independent audit has not been performed.
