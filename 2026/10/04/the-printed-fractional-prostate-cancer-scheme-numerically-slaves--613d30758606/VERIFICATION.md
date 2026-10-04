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
The analytical defect is exact: if two recurrences have the same increment functional, their difference remains equal to the difference of their initial values.

The bundled checker uses the source's Table 1 values
\[
\gamma_1=\delta_3=\frac{2}{25},
\qquad
a_0=10.
\]
At
\[
X_1=X_2=0,\qquad
A=a_0,\qquad
P=1,\qquad
u=0,
\]
it verifies
\[
H_5=0
\]
and
\[
H_6=-\frac{2}{25}.
\]

It also replays the recurrence invariant with several exact rational increment values. This finite replay is not used as a proof of the general invariant; that proof is direct subtraction.

The verification does not assess unavailable simulation code and does not infer that the published figures were generated with the duplicated component.
