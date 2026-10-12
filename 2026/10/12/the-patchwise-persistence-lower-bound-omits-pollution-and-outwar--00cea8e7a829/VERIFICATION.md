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
The bundled checker uses exact rational arithmetic.

It verifies that
\[
c_e=\frac12,\qquad
c_0=\frac14
\]
is an equilibrium of the environmental subsystem for
\[
f=g=m=1,\qquad
h=2,\qquad
u_e=1.
\]

It verifies
\[
R_1=\frac74,\qquad
R_2=2,
\]
and both Theorem 4.10 assumptions:
\[
R_1-\frac12=\frac54>0,
\qquad
R_2-\frac12=\frac32>0.
\]

With \(d_{21}=0\), patch 1 is exactly the scalar stochastic logistic equation with effective intrinsic coefficient \(7/4\). Applying the scalar formula stated as Lemma 2.3 gives
\[
\lim\langle x_1\rangle=\frac54.
\]

The checker compares this with
\[
\frac{\bar r_1-\sigma_1^2/2}{a_1}
=
\frac52
\]
from the theorem statement and
\[
\frac{R_1-\sigma_1^2/2}{a_1}
=
\frac54
\]
from the proof.

No trajectory simulation is used.
