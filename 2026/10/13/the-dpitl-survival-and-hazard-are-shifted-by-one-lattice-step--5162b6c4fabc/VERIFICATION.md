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
Define
\[
S_c(w)
=
\left[
\frac{1+2w^\eta}{(1+w^\eta)^2}
\right]^\kappa,
\qquad
p_w=S_c(w)-S_c(w+1).
\]
Telescoping gives
\[
\Pr(W\ge w)=S_c(w)
\]
and
\[
\Pr(W>w)=S_c(w+1).
\]

Therefore the correct cell hazard is
\[
h(w)=p_w/S_c(w),
\]
while the source's Eq. (4) uses
\[
p_w/S_c(w+1)=h(w)/(1-h(w)).
\]

At
\[
\kappa=3,\quad w=0,
\]
the two quantities are
\[
37/64
\]
and
\[
37/27.
\]

For the PGF,
\[
G(t)
=
1+(t-1)\sum_{w=1}^\infty t^{w-1}S_c(w).
\]
Replacing \(S_c(w)\) by \(S_c(w+1)\) shifts the series. In particular, whenever the mean is finite,
\[
\mathbb E[W]-\mu_{\mathrm{pub}}
=
S_c(1)
=
(3/4)^\kappa.
\]

The bundled checker verifies the hazard relation, the exact \(w=0\) example, agreement of the direct PMF PGF with the corrected survival identity, and the mean shift for \((\kappa,\eta)=(3,1)\).
