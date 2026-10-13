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
The bundled checker verifies the invariant-region correction symbolically and replays the source parameter table with exact rational arithmetic.

For a general environmental cap \(E\le H\), the largest possible derivative on its top face under
\[
0\le I_m\le K_m
\]
is
\[
\alpha_EK_m-\mu_EH.
\]
Thus the smallest rectangular cap is
\[
H_*=\frac{\alpha_EK_m}{\mu_E}.
\]

At the source values
\[
\Lambda_m=2,\qquad
\mu_m=\frac1{365\cdot60},\qquad
\alpha_E=\mu_E=\frac1{14},
\]
the checker obtains
\[
K_m=43800,\qquad
E_{\mathrm{pub}}=1,\qquad
H_*=43800.
\]

For the exact boundary witness
\[
(S_m,I_m,S_v,I_v,E)=(1,2,1,1,1),
\]
it verifies both population-cap inequalities and
\[
\dot E=\frac1{14}>0.
\]

No simulation or finite parameter search is used.
