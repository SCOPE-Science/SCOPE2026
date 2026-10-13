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

The proof uses the Yule generator and a closed moment system. The supplied `verify.py` checks the eleven closed-form expressions against their differential equations at multiple positive times, checks the two covariance signs over a finite grid, and verifies the asymptotic residual-correlation value numerically.

A successful checker run reports 99 differential-equation checks, 10,000 finite sign checks, and a maximum relative differential residual below \(2\times10^{-10}\). The large-time numerical residual correlation agrees with \(-\sqrt{6}/12\).

These computations are deliberately secondary. Finite grids cannot prove signs for all \(t>0\), and numerical ODE residuals cannot replace the symbolic derivation. The continuum claims are justified by the analytic moment equations and the explicit monotonicity arguments in `RESULT.md`.

The verification does not establish novelty, fixed-tip conditional analogues, or extensions to birth-death processes with extinction.
