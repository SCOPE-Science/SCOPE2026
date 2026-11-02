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

Run `python verify_dual.py` in an environment with Python, NumPy, SciPy and SymPy. The included script has no unpublished input data, inherited run artifacts or remote dependencies.

Executed checks: symbolic generator-inversion identities for stationary second and fourth moments; exact zero-, first-, second-, third- and fourth-lag derivative relations; symbolic fourth-cumulant involution difference; 50 seeded triples with positive diffusivity, switching and stiffness over log-uniform ranges; 5 nonnegative lags per triple; independent `scipy.linalg.expm` two-state propagation compared against closed-form covariance for each twin; explicit two-root and fourth-cumulant inverse reconstructions. Result: all symbolic identities and 1,300 counted numerical comparisons passed. The illustrative twins \((q,k,D)=(1,1,1)\) and \((1/2,2,1)\) have the same covariance (including variance \(3\)) and different fourth cumulants \(15\) and \(42\).

Numerical checks are finite experiments and do not establish uniqueness, infinite-lag identity, or publication novelty. Those scientific claims rest on the finite-dimensional generator proof in `RESULT.md`. The study does not test statistical estimation error from sampled trajectories or higher-order universality beyond the defined model.
