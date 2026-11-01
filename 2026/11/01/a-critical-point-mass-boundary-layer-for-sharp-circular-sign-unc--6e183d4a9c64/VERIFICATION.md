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

# Verification and limits

The stated result concerns the sharp last-sign-change radius under \(\mu_\tau=(dx+\tau\delta_0)/(1+\tau)\) and canonical extremizers (4), with \(m\ge2\). Its external mathematical input is Ismoilov's published universal paraorthogonal-zero theorem, which already supplies the finite-degree sharpness and uniqueness; no new proof of that general theorem is claimed.

Direct checks: exact rational Gram orthogonality, positive-root monotonicity, \(m\tau\) crossover from the tangent equation, Taylor expansion for the fixed-mass \(m^{-3/2}\) regime, and holomorphic removal for the microscopic profiles. The program \(\texttt{check_sign_uncertainty.py}\) ran with Python 3 and mpmath, returning:

`CHECK_OK: rational OPUC Gram identities, critical-window roots, fixed-mass edge scaling`

The script checks finite examples only; infinite conclusions are analytic. Novelty compared with Ismoilov is restricted to parameter-dependent asymptotic regimes and limiting profiles. Historical prior art may still contain these asymptotics implicitly; no independent validation has been performed.
