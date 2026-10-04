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
The theorem is analytic. The bundled checker replays the critical source-specific calculations.

For the Figure 3 parameters,
\[
\eta=\frac12,\quad
b_2=\frac35,\quad
b_1=\frac12,\quad
c_2=\frac45,\quad
d_3=\frac1{10},\quad
c_3=\frac1{50},
\]
and
\[
P_2(t-\tau_2)=P_3(t)=1,
\]
it verifies
\[
P_3'=\frac{17}{25}=0.68
\]
while the asserted upper expression is
\[
\frac{12}{25}=0.48.
\]

It independently solves the printed nondelayed equilibrium equations at the full Figure 3 parameter set and obtains
\[
P_3^*\approx4.282729940794482,
\]
whereas the printed limiting expression equals \(25\).

It also checks the exact rational witness
\[
r=\frac{11}{10},\quad
d_1=c_1=b_1=\eta=c_2=d_2=1,\quad
b_2=\frac15,\quad
d_3=\frac1{10},
\]
for which
\[
K=\frac1{10},
\qquad
\mathcal R_P=\frac1{11}<1,
\]
although
\[
\frac{\eta b_2}{b_1}>\,d_3.
\]
Thus the corrected theorem genuinely covers parameter values outside the source's simpler sufficient condition.

No finite computation is used to infer the global theorem.
