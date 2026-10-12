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
The bundled checker verifies the state-space identities exactly.

On
\[
P=\frac1\delta,
\]
it symbolically simplifies the predator derivative to
\[
P'
=
\frac{\delta r_2-r_2e/K-q_2E}{\delta^2}.
\]

For the counterexample it verifies
\[
\delta=\frac15,
\qquad
\frac eK+\frac{q_2E}{r_2}
=
\frac3{50},
\]
and
\[
P'(1,5)=\frac72>0.
\]

For the source Dataset (24) it verifies
\[
\delta=\frac1{20},
\qquad
\frac eK+\frac{q_2E}{r_2}
=
\frac14,
\]
so the repaired condition holds.

Finally, at \(P=10\) for the counterexample parameters, the checker verifies that
\[
N=2
\]
makes the predator denominator zero and
\[
N=3
\]
makes the prey denominator zero.

No simulation is used to infer the theorem.
