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
The bundled checker reconstructs the source's final-state relation using exact rational arithmetic at the source parameter values.

For
\[
S_0=200,\qquad I_0=2,\qquad
\alpha=2,\qquad \beta=0.2,\qquad
\epsilon=9.8,
\]
it verifies
\[
\sigma=\frac{\alpha\epsilon}{\beta}=98
\]
and
\[
a_\epsilon
=
\frac{\alpha}{\beta S_0}
-\frac1{\epsilon S_0}
=
\frac{97}{1960}.
\]

The exact final-state function is negative at \(x=0\) and positive at \(x=a_\epsilon\), so its unique positive root lies strictly below \(a_\epsilon\), matching the proof's one-sided correction.

The infinite-\(\epsilon\) conclusion is established by the analytic exponential estimate; the finite calculation is only a replay check.
