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

# Verification and scope

Execute `python verify.py` with SymPy installed. It verifies the linearization at the positive equilibrium, Hopf pair and adjoint eigenvectors, the full complex cubic contraction, its real and imaginary components, the first Lyapunov coefficient, crossing speed, amplitude-derived frequency coefficient, and a second symbolic Fourier/harmonic-balance computation derived from the scalar jerk equation. The reflection symmetry transfers the computations to the negative equilibrium. All symbolic assertions are over the exact rational function field with \(w=\sqrt b>0\).

Routh–Hurwitz stability, Hopf existence/uniqueness, critical stability and the time-asymptotic limit are proved in RESULT.md using standard analytic theorems rather than exhaustive numerical experiments. No finite sampling is presented as an infinite-parameter proof. The theorem is restricted to fixed \(b>0\) and a neighborhood of \(a=2\). There is no independent audit, and originality remains subject to incompletely indexed literature.
