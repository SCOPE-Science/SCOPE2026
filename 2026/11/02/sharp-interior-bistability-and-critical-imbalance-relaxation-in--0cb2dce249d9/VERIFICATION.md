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

Execute `python verify.py` under Python 3.10+ with SymPy 1.12+ installed. The exact checker reconstructs the polynomial vector field, mean/imbalance equations, stationary identities, Jacobian stability invariants, an exact rational example, the critical center-manifold invariance coefficient and the asymptotic amplitudes. It prints `PASS` if every assertion succeeds.

A separate floating-point diagnostic used SciPy's DOP853 solver with relative tolerance \(10^{-10}\) and absolute tolerance \(10^{-12}\). At \(a=3/4\), initial coordinates \((0.9,0.25)\), and \(t=40000\), it produced \(t(x-y)^2\approx5.3351284\) (the predicted limit is \(16/3\)) and \(t(s-2/3)\approx-0.5001968\) (predicted \(-1/2\)). At \(a=13/16\), integrations from \((0.9,0.25)\) and its reversal approached the appropriate exact sink coordinates. These finite experiments do not prove infinite-time claims.

The global convergence proof uses explicit scalar logistic comparisons, the planar Bendixson--Dulac criterion, the classification of equilibria and local invariant-manifold theory. No external proof assistant, independent audit or model validation was performed. Input ranges and exceptional diagonal data are specified in `RESULT.md`.
