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

# Verification notes

The scientific proof is in `RESULT.md`. The separate `verify_work.py` is executable with Python 3 and standard-library modules only. Running `python verify_work.py` on this package yielded `ALL_CHECKS_PASS` after checking four sets of positive parameters: \((D,k,a,b)=(1,1,1,1)\), \((0.7,2.5,0.4,1.3)\), \((1.5,0.9,2.2,0.3)\), and \((1,1,0.1,0.1)\). For these, independent forward propagation of work-position mixed moments gave variance rates approximately \(4.25\), \(3.619320797\), \(51.2379648\), and \(24.50000042\), agreeing with the analytic values \(4.25\), \(3.619320797\), \(51.2379648\), and \(24.5\) within the script's stated tolerances. The mean work rates also matched.

The program checks the stationary second/fourth moment equations, exact Poisson-equation coefficients, and bracket formula with rational arithmetic; it independently integrates twelve coupled deterministic moment equations through fourth spatial moment and second work moment, with both positive and negative work jumps. The deterministic ODE is integrated with fourth-order Runge–Kutta for finite times. Its numerical approximations are **not** proofs of stationarity, martingale CLT, or asymptotic variance; those steps are established analytically in the proof. A different stochastic convention for whether switch-off is counted would change the claim, and is not silently substituted.

Independent audit: not performed. No external validation or certification is asserted.
