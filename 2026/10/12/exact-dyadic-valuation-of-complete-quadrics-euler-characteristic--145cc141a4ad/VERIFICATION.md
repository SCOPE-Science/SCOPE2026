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
The checker computes
\[
\kappa(0)=\kappa(1)=1
\]
and
\[
\kappa(n)
=
n\kappa(n-1)+\binom n2\kappa(n-2)
\]
for
\[
2\le n\le1000.
\]

For each
\[
1\le n\le1000,
\]
it verifies
\[
\nu_2(\kappa(n))
=
\left\lceil\frac n2\right\rceil-s_2(n)
+
\begin{cases}
\nu_2(n+1),&n\equiv3\pmod4,\\
0,&\text{otherwise}.
\end{cases}
\]

Independently, it computes
\[
U_0=0,\quad U_1=1,\quad U_m=2U_{m-1}+2U_{m-2}
\]
through
\[
m=1001
\]
and verifies
\[
\nu_2(U_m)
=
\left\lfloor\frac m2\right\rfloor
+
\begin{cases}
\nu_2(m),&4\mid m,\\
0,&4\nmid m.
\end{cases}
\]

It also checks
\[
\kappa(n)=\frac{n!}{2^n}U_{n+1}
\]
exactly at every tested index.

Finite checks are regression evidence only. The infinite theorem follows from the symbolic Lucas-sequence valuation proof and Legendre's identity.
