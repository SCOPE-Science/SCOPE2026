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
The complete proof is analytic and does not depend on finite sampling.

The local characteristic determinant splits into \(\det(\lambda I-A)\) and \(\lambda+h-pe^{-\lambda\tau}\). The prey block has negative trace and positive determinant. The exact scalar modulus, real-root monotonicity, and imaginary-phase identities give the stability trichotomy and all crossings. At each crossing,
\[
\Re\lambda'(\tau_j)=\frac{\omega^2}{(1+h\tau_j)^2+(\omega\tau_j)^2}>0.
\]
Thus the right-half-plane root count rises by two at each crossing; a positive real eigenvalue persists when \(p>h\). Any sufficiently nearby periodic orbit with nonnegative predator abundance would contradict \(0=\int_0^T(q-h)z\,dt\) because the local predator birth multiplier satisfies \(q>h\); hence no such biological Hopf offspring exists.

The nonlinear result assumes positive infected-prey history throughout the delay interval, avoiding the indeterminate ratio at simultaneous infected-prey/predator extinction; positivity subsequently persists. The nonlinear result uses
\[
\dot x\le rx(1-x/K),\qquad
\dot z\le q_\varepsilon z(t-\tau)-hz,
\]
and chooses \(\eta>0\) satisfying
\[
\eta+q_\varepsilon e^{\eta\tau}<h.
\]
Exponential comparison then guarantees predator extinction for any fixed finite delay.

The bundled `verify.py` checks the rational parameter example's equilibrium, full prey Jacobian, sharp local threshold, global sufficient threshold, and first six imaginary-root residuals and crossing velocities. This replay is corroborative only. In particular, it does not imply nonlinear convergence at the equality threshold or optimality of the global bound.
