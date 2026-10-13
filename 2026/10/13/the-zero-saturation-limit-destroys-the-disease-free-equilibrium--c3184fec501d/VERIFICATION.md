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
The bundled symbolic checker verifies the endpoint algebra without numerical approximation.

For
\[
T_b(I)=\frac{aI}{b+I},
\]
it checks
\[
\lim_{I\downarrow0}T_b(I)=0
\]
for fixed \(b>0\), while after setting \(b=0\) on the positive-\(I\) branch,
\[
\lim_{I\downarrow0}T_0(I)=a.
\]

At
\[
S_0=\frac{A}{\mu_1+\gamma+\delta},
\qquad
B=0,
\]
it substitutes the source's vector field and verifies
\[
\lim_{I\downarrow0}(S',I',B')=(a,-a,0).
\]

It also substitutes \(b=0\) into the source's reproduction-number expression and obtains zero for \(a>0\).

Finally, it checks the regular reparameterized limit
\[
\lim_{b\to\infty}
\frac{rbI}{b+I}
=
rI.
\]

These exact identities are the complete computational content of the finding; no simulation is used.
