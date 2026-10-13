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

The scientific theorem is proved by an exact critical Lyapunov identity followed by spectral projection onto a simple infected zero mode and forced-response asymptotics.

At criticality \(Ak=a\),
\[
\dot V=-\mu(S-\rho)^2/S
-\mu(L-(1-\rho))^2/L
+\sigma R[1-\rho^2/S-(1-\rho)^2/L]\le0.
\]
The constraint \(S+L\le1\) gives the last sign by Cauchy–Schwarz. This proves global convergence. With \(W=E+(A/b)I\),
\[
(1/W)'\to K/H>0,
\quad K=\frac{k(kB-GA)}{\mu H}.
\]
The remainder of the proof gives all compartment ratio limits and signed susceptible deficits. The heterogeneity comparison uses the exact identity \(B=A^2+\rho(1-\rho)(\alpha-\beta)^2\).

The bundled standalone checker verifies the Lyapunov derivative symbolically for arbitrary parameters and uses the exact rational critical parameter instance
\[
\rho=1/2,\quad\mu=\sigma=\delta=\gamma=1,\quad\alpha=5/3,\quad\beta=1.
\]
It verifies \(K=45/16\) and the predicted five-component scaled limits, then integrates the full normalized ODE to large finite time with a relative comparison tolerance of one percent. These computations corroborate but do not certify the analytic infinite-time claim. No external independent audit has been carried out.
