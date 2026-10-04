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

The analytic proof is primary. The following checks were replayed against the packaged files.

1. **Exact factorization.** For common delay, multiplying the source characteristic equation by \(e^{2\lambda\tau}\) gives exactly \((\lambda e^{\lambda\tau})^2+P(\lambda e^{\lambda\tau})+Q\).
2. **First-crossing calculation.** For each quadratic root \(z\), an imaginary characteristic root must satisfy \(\omega=|z|\) and \(\arg z=\pi/2+\omega\tau\pmod{2\pi}\). This yields the two stated formulas for \(\tau_c\).
3. **Crossing direction.** Differentiating \(\lambda e^{\lambda\tau}=z\) gives \(d\lambda/d\tau=-\lambda^2/(1+\lambda\tau)\), with positive real part at every simple imaginary crossing.
4. **Figure 2 replay.** The source parameters produce the exact positive equilibrium \(x_1^*=(-9+\sqrt{201})/10\), \(x_2^*=(-11+\sqrt{201})/8\), then \(\tau_c=3.590488585197299\ldots\). Thus the reported equal-delay cases \(\tau=2\) and \(\tau=4\) fall on the stable and unstable sides respectively.
5. **Standalone checker.** `verify.py` checks the equilibrium residuals, algebraic factorization, representative real-root and complex-root threshold cases, the imaginary-root residual at the critical delay, the crossing-sign formula, and the Figure 2 threshold. A successful finite numerical replay is a regression check; the exact proof is not reduced to numerical experiments.

Limits: the verification does not establish nonlinear Hopf criticality, periodic-orbit stability, unequal-delay stability, or global dynamics, and none is claimed.
