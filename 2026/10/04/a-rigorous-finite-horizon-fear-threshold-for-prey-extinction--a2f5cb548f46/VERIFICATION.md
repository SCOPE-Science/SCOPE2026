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
The proof of finite-time extinction is analytic. The numerical checker only replays the explicit certificate on the motivating source's Figure 6 data.

For
\[
u_0=4.8,\quad
v_0=8.3,\quad
a=2.5,\quad
c=2.5,\quad
d=2,\quad
p=0.2,\quad
m=0.4,
\]
the checker evaluates
\[
R_\infty
=
\frac{(1-p)cv_0^m}
{md\,u_0^{1-p}}
\]
and confirms
\[
R_\infty
\approx
1.661798090950775
>
1.
\]

At
\[
T=1.5,
\]
it computes
\[
R_T
\approx
1.161274124589654
\]
and
\[
K(T)
\approx
15.37918897486502.
\]

For
\[
k=16,
\]
the closed-form normalized margin is approximately
\[
1.005818253780147,
\]
and independent quadrature of the sharper integral gives approximately
\[
1.128993918149717.
\]
Both are strictly above \(1\), so the certificate has a nonzero numerical margin.

No finite experiment is used to infer extinction for arbitrary data, and the checker does not validate the source's \(k=0.03\) trajectory.
