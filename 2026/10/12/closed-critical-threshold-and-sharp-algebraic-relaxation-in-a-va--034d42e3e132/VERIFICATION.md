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
The proof is analytic.

At criticality,
\[
\theta(0)S_0=\mu_1.
\]
The Lyapunov derivative is exactly
\[
\dot L
=
-\frac{\mu_0(S-S_0)^2}{S}
-
S_0E\bigl(\theta(0)-\theta(I)\bigr),
\]
so the disease-free state is globally attracting; \(L\) and the stable \(I\)-filter also give Lyapunov stability.

For positive initial exposure,
\[
\frac{I}{E}\to\frac{\alpha}{\mu_2},
\qquad
\frac{S_0-S}{E}\to\frac{\mu_1}{\mu_0}.
\]
Therefore
\[
-\frac{\dot E}{E^2}
\to
K
=
\frac{\theta(0)\mu_1}{\mu_0}
-
S_0\theta'(0)\frac{\alpha}{\mu_2},
\]
and
\[
tE\to\frac1K.
\]

The bundled checker numerically replays one admissible critical instance with predicted limits
\[
tE\to\frac38,\qquad
tI\to\frac18,\qquad
t(S_0-S)\to\frac34.
\]
The numerical calculation corroborates but does not replace the analytic theorem.
