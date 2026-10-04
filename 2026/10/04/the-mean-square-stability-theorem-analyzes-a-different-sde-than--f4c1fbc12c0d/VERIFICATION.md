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
The core verification is analytic.

The original model has diffusion coefficients
\[
g_i(N_i)=\sigma_i(t,N_i)N_i.
\]
At the positive deterministic equilibrium, the four source cases give
\[
(\epsilon N_1^*,\delta N_2^*),\quad
(\epsilon N_1^*,\delta),\quad
(\epsilon,\delta),\quad
(\epsilon,\delta N_2^*),
\]
so every positive immigration intensity leaves nonzero diffusion at the claimed equilibrium.

By contrast, the Section-4 coefficients contain \(N_i-N_i^*\) and therefore vanish at \(P^*\). The two SDEs are not related by the stated centering change of variables.

The bundled checker independently reconstructs
\[
N_1^*=\frac{101}{150},
\qquad
N_2^*=\frac{31}{75},
\]
from the source parameter values and evaluates the four exact coefficients of
\[
\mathbb E\|N_t-P^*\|^2=q\,t+o(t)
\]
at \(\epsilon=0.25\), \(\delta=0.12\).

Finite computation is not used to establish the model mismatch or the equilibrium obstruction.
