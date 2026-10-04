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

The proof uses the published lemniscate recurrence, its exact shooting criterion, the bound \(\Omega_N>(N+1)^2/\varpi^2\), and the asymptotic law for \(\Omega_N\).

`artifacts/verify_finite_horizon.py` performs two exact certificates with standard integer and rational arithmetic. First, a sixteen-cell monotonicity bound on the defining integral is enclosed outward to prove \(\varpi<27/10\). Second, for each even \(N\) from \(2\) through \(20\), the source one-step map is propagated with outward rational square-root bounds at the threshold \(T_N=(N+2)^2/8\). Before the certified crossing, every lower endpoint remains in the source admissible domain; at the trigger index the upper endpoint is strictly below \(1/T_N\). The source shooting theorem therefore gives \(T_N<\Omega_N\).

The infinite tail is not established by enumeration. For \(N=21+m\), exact expansion yields
\[
800(N+1)^2-729(N+2)^2=71m^2+1666m+1559>0,
\]
which combines with \(\varpi<27/10\) and the source lower bound.

The verifier returns `VERIFY_OK`.
