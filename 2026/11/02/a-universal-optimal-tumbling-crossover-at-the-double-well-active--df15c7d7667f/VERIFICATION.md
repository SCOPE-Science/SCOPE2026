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
# Verification of the analytic asymptotic

The argument's exact input is the zero-current stationary density quoted in RESULT.md. Key independently checkable steps are differentiation of its integral in the flip rate; local Taylor expansion of the force at its interior quadratic maximum; the explicit arctangent integral yielding the inner contribution \(e^z-1\); and the integrated logarithmic boundary layer yielding \(e^z\). Uniformity on compact positive scales and exclusion of optimizers at zero/infinity are explained in RESULT.md.

Run `python verify.py` with NumPy and SciPy installed. The script uses an adaptive ODE for the exact positive-side stationary quadrature and an analytically integrated remote-endpoint tail. It checks four near-critical offsets, local minimization, the endpoint-cutoff approximation and convergence direction of the scaled rates and minimized proxy. The finite numeric samples are diagnostic and not an infinite proof. The exact tail integration is asymptotic in its cutoff, not a verified finite-error certificate. No external review or independent audit is claimed.
