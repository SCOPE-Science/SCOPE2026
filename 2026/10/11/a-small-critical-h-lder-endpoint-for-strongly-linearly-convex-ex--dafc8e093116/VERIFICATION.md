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

The proof uses the actual inequalities appearing in the two primary preprints.

From the September modulus theorem, with
\[
\tau_\delta=\delta^3,
\]
the collar defect obeys
\[
\mathcal D_\delta(z;w)
\ge
-C_0\delta^2
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2
|w|^2.
\]

From the July perturbation lemma, replacing
\[
h_\delta
\]
by
\[
\widetilde h_\delta
=
h_\delta-c\delta^2(1+|z|^2)
\]
adds at least
\[
\frac{c\delta^2}{1+R^2}|w|^2
\]
to the same defect.

Because
\[
\rho(r)
=
\sup_{0<t\le r}
\frac{\omega_\nu(t)}{\sqrt t},
\]
one has
\[
\rho(r)\longrightarrow
\Lambda_\nu
=
\limsup_{t\downarrow0}
\frac{\omega_\nu(t)}{\sqrt t}.
\]

Hence
\[
\Lambda_\nu
<
\left(
\frac{c}{C_0(1+R^2)}
\right)^{1/4}
\]
implies
\[
\frac{c}{1+R^2}
-
C_0
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2
>
0
\]
for every sufficiently small \(\delta\).

The inspected completion of the proof uses
\[
\tau_\delta/\delta=\delta^2\to0
\]
to establish the collar inclusions and nesting. It does not require
\[
\rho(r)\to0
\]
after strict positivity of the defect has been obtained.

No numerical approximation, finite experiment, or external certificate is used.
