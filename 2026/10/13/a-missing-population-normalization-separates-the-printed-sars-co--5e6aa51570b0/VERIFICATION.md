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
The bundled checker uses exact rational arithmetic for the source's terminating-decimal parameters and the exact table identity
\[
\Lambda=\mu N_0.
\]

It verifies
\[
\mathcal R_0^{\mathrm{mass}}
=
N_0\mathcal R_0^{\mathrm{freq}}
\]
for both parameter tables.

For
\[
\beta=0.034
\]
it obtains
\[
\mathcal R_0^{\mathrm{freq}}
=
0.6114991225\ldots,
\]
while the printed mass-action formula gives
\[
36{,}268{,}012.9575\ldots.
\]

For
\[
\beta=0.34
\]
it obtains
\[
\mathcal R_0^{\mathrm{freq}}
=
6.1149912253\ldots,
\]
while the printed mass-action formula gives
\[
362{,}680{,}129.5753\ldots.
\]

The checker also reconstructs the Table 5 initial infectious combination and verifies the per-susceptible force
\[
8{,}563{,}683.19\ {\rm day}^{-1}
\]
under the printed mass-action coefficient, versus
\[
0.1443885212\ {\rm day}^{-1}
\]
after division by \(N_0\).

No trajectory simulation is used as evidence for the algebraic inconsistency.
