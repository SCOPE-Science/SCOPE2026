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
The correction is established analytically from the published model.

At the resistant-only equilibrium, the exact two-coordinate invasion block is
\[
J_{IP}
=
\begin{pmatrix}
-(D+\delta)&\kappa kM_2\\
b\delta&-(D+kM_2)
\end{pmatrix}.
\]
The corresponding two-stage next-generation product gives
\[
(\widehat{\mathcal R}_0^M)^2
=
\frac{b\delta\kappa kM_2}
{(D+\delta)(D+kM_2)}.
\]

For the exact witness
\[
D=\delta=1,\quad
b=10,\quad
k=\frac1{100},\quad
\kappa=\frac12,\quad
\mu=\frac12,\quad
m=4,\quad
a=1,\quad
R^0=11,
\]
the bundled checker verifies
\[
\lambda_2=1,\qquad M_2=10,
\]
\[
(\mathcal R_{0,\mathrm{print}}^M)^2=\frac{250}{11}>1,
\]
\[
(\widehat{\mathcal R}_0^M)^2=\frac5{22}<1,
\]
\[
\operatorname{tr}J_{IP}=-\frac{31}{10}<0,
\qquad
\det J_{IP}=\frac{17}{10}>0.
\]

It also checks the source's later identity
\[
-D+kA_2M_2
=
(D+kM_2)
\bigl((\widehat{\mathcal R}_0^M)^2-1\bigr)
=
-\frac{17}{20},
\]
while substituting the printed definition gives
\[
(D+kM_2)
\bigl((\mathcal R_{0,\mathrm{print}}^M)^2-1\bigr)
=
\frac{239}{10},
\]
which is unequal.

Finally, the source's positive-equilibrium condition forces
\[
M_3=\frac{200}{3},
\]
whereas its nutrient balance and positivity condition force
\[
M_3<10.
\]
No simulation or finite enumeration is used to infer the general missing-factor statement.
