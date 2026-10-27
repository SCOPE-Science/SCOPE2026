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

# Verification of the inverse classification

The proof works for every \(L>0\), \(T_1,T_2>0\) with \(T_1\ne T_2\), and every symmetric SPD \(K\) with \(\operatorname{tr}K=L\); the proof and formulas are in `RESULT.md`.

The standalone numerical checker `bg_inverse_checker.py` uses a separate numerical Lyapunov solver and evaluates the actual ensemble stationary-current angular integral by one-dimensional quadrature. With the documented fixed seed it passed 1,200 forward comparisons, 1,200 inverse reconstructions, 12 boundary/interior cases, three impossibility tests and three zero-torque inversions. To replay: install `numpy` and `scipy` and execute `python bg_inverse_checker.py`.

The numerical experiments are not a proof of the complete feasible image or global uniqueness. Those follow analytically by the explicit covariance equations, determinant inequalities and strict zero-torque derivative. The square-root fold holds for fixed nonzero torque approaching the maximal-frequency boundary, not uniformly near the origin. Independent scientific audit and external replication have not been performed.
