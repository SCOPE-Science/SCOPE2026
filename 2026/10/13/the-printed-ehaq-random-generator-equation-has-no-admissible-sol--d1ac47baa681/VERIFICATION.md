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
L_\tau(x)
=
\left((1+\tau)^2+\tau x+\frac12\tau^2x^2\right)e^{-\tau x}.
\]
Then
\[
L_\tau'(x)
=
-\tau^2
\left(2+\tau+\frac{\tau x^2}{2}\right)e^{-\tau x}<0.
\]
Therefore
\[
0<L_\tau(x)\le(1+\tau)^2
\]
for \(x\ge0\).

The printed Eq. (10) requires
\[
L_\tau(x)=(1+\tau)^2(1+z^{1/\delta}),
\]
whose right side exceeds the maximum possible left side whenever \(0<z<1\).

The corrected equation is
\[
L_\tau(x)=(1+\tau)^2(1-z^{1/\delta}),
\]
and has exactly one root.

The bundled checker solves the corrected equation, substitutes the root into the published CDF, and reproduces the Table 1 quartiles.
