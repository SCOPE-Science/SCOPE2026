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
The proof is analytic. The bundled checker replays exact identities and the source-rounded numerical witness.

For an endemic unit-determinant boundary,
\[
\Delta
=
1-hd\mathcal R_0
+h^2d(d+r)(\mathcal R_0-1)
=
1
\]
implies
\[
h(d+r)
=
\frac{\mathcal R_0}{\mathcal R_0-1}.
\]
Since
\[
\mathcal R_0>1,
\]
this exceeds \(1\).

The infected update is
\[
I_{n+1}
=
I_n
\left[
1+h(\lambda S_n-(d+r))
\right].
\]
The exact zero of its bracket on the unit-determinant boundary is
\[
S_{\mathrm{crit}}
=
\frac{S_1}{\mathcal R_0}.
\]

For the source's rounded \(1{:}3\) values, exact rational arithmetic gives
\[
\mathcal R_0
=
\frac{909}{640},
\qquad
S_{\mathrm{crit}}
\approx
1.487145414211388.
\]
The global-diagram initial value
\[
S_0=1.4222
\]
lies below this threshold. The exact rational first iterate is
\[
I_1
=
-\frac{10256632066707}{10^{14}}
=
-0.10256632066707.
\]

No finite experiment is used to infer the universal theorem.
