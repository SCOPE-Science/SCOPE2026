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

Run `python verify_resonance.py` with Python 3 and SymPy installed; it emits `CHECK_OK: exact vector field, Jacobian, resonant forcing, and asymptotic coefficient balances` after checking the precise tuned vector field, the analytic ratio-coordinate identity, Jacobian eigenvalues, the nonlinear forcing coefficient, the prey cubic balance and the resonant ratio balance. The proof of convergence, existence and positivity of the amplitude, integrability of the phase remainder, and all infinite-time limits is supplied analytically in RESULT.md, Sections 3–5. A finite symbolic identity is not by itself an infinite-time theorem.

A direct finite-interval ODE check was additionally performed for \(M=S=1/4\), \(A\in\{1/2,2\}\), \(Q=A(1+M)/2\), and \((u(0),v(0))=(1/8,1/4)\). At nondimensional physical time \(\theta=40\) the normalized ratio diagnostics \((v/u-2)/(\theta u^2)\) were approximately \(-3.05008\) and \(0.81480\), trending toward the exact proved limits \(-3\) and \(0.75\). These computations are corroborative only, and neither finite-time values nor solver tolerances establish the asymptotics. The exceptional surface \(A=1+M\) is excluded. Independent audit has not been performed.
