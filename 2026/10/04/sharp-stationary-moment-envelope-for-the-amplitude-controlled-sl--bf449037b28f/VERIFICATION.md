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
The claim was checked directly against the printed three-dimensional vector field.

For every compactly supported invariant probability measure, stationarity of the coordinate observables gives
\[
\langle y^2\rangle=m\langle y\rangle,
\qquad
\langle xy\rangle=-a\langle z^2\rangle,
\qquad
b\langle x^2\rangle=ac\langle z^2\rangle.
\]
The first identity gives \(\operatorname{Var}(y)=\langle y\rangle(m-\langle y\rangle)\). The latter two identities and Cauchy--Schwarz give
\[
\langle z^2\rangle\le \frac c{{ab}}\langle y^2\rangle,
\]
hence the asserted absolute bounds. The zero case was handled separately before cancellation.

The equality cases were checked by solving the equilibrium equations and by using invariance of the support when \(y\) has zero variance. With \(y=m\), the only support points compatible with invariance are
\[
(0,m,0)
\quad\text{{and}}\quad
\left(-\frac{{cm}}b,m,\pm m\sqrt{{\frac c{{ab}}}}\right).
\]
At the source parameters \(a=1/2\), \(b=3/5\), and \(c=6/5\), exact rational arithmetic gives
\[
\frac{{ac}}b=1,
\qquad
\frac c{{ab}}=4,
\qquad
\frac{{c^2}}{{b^2}}=4.
\]

Limits: this verification does not establish compactness of all trajectories, existence of a physical chaotic measure, or ergodicity of the numerically illustrated attractor. No numerical trajectory or finite sampling is used to justify the universal statement.
