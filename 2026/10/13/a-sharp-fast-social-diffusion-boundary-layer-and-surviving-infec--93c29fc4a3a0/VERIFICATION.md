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

# Reproducibility and limits

The mathematical argument uses the normalized four-compartment system printed in `RESULT.md`. The exact identity

\[
I_D(t)=(S_0+I_0)e^{-\gamma t}-S_D(t)+\gamma\int_0^t e^{-\gamma(t-u)}S_D(u)\,du
\]

can be checked by differentiation and the initial condition. The scaled risk equation and the two Riccati comparisons are obtained by direct algebraic substitution. Positive-time convergence follows from a monotone susceptible bound plus dominated convergence, not from finite simulation.

The optional numerical experiment `check_sfir_fastdiff.py` solves the transformed stiff ODE in \((\log S,I,w)\) for a fixed positive example at diffusion values \(100,10^4,10^6\), with a Radau integrator. It prints the predicted three limits and errors; it asserts their progressive approximation to the stated values. Run `python check_sfir_fastdiff.py` after installing `requirements.txt` if needed. The analytic proof makes no claim that the solver's floating-point tolerances provide interval-arithmetic or formal certificates.

The verified model limits require a fixed strictly positive initial infectious fraction and exclude the initial instant from outer uniform convergence. No full PDE limit, non-fixed initial data, uniform-in-infinite-time limit, or independent external audit is claimed.
