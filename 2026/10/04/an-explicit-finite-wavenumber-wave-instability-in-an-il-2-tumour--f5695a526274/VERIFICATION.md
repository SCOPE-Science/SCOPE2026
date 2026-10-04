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

`verifier.py` uses only exact rational arithmetic from Python's standard library. It checks the three equilibrium residuals exactly, reconstructs the finite-mode characteristic cubic, verifies homogeneous Routh–Hurwitz stability at \(k=0\), and verifies \(a_2,a_1,a_0>0\) with \(a_2a_1-a_0<0\) at \(k^2=1/4000\). The positive finite-mode coefficients exclude positive real roots, so the Routh–Hurwitz failure certifies an unstable complex pair rather than a stationary positive eigenvalue.

The verification is local and linear. It does not certify nonlinear periodic waves, their criticality, or robustness under parameter perturbation.
