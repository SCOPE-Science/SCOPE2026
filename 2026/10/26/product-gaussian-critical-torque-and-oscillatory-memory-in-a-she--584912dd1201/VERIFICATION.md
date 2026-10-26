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

The standalone `verify.py` uses Python 3 and SymPy, with no external network or downloaded data. Execute `python verify.py` from the same folder. It checks all entries of the Lyapunov equation symbolically, independently solves the six linear covariance equations at three rational shears, verifies the covariance Laurent residue and constant part, exact mean/variance and fourth-cumulant coefficients, the limiting characteristic determinant, and a linear ODE plus three initial derivatives for the claimed fixed-lag covariance. The independently worked Gaussian convergence argument in `RESULT.md` supplies the infinite-dimensional scientific reasoning; finite algebraic checks do not constitute an independent audit.
