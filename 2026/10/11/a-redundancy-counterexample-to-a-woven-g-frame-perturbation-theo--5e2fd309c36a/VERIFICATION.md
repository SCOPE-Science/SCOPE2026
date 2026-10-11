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
# Verification

For each original family,
\[
\sum_i\|\Lambda_i f\|^2
=
\sum_i\|\Gamma_i f\|^2
=
16\|f\|^2.
\]
Thus
\[
A_1=B_1=A_2=B_2=16.
\]

The scalar threshold is
\[
\frac1{100}\cdot4
+
\frac1{100}\cdot4
+
\frac34
=
\frac{83}{100}
<
1
=
\frac{16}{2(4+4)}.
\]

For every coefficient family \(c\),
\[
\left(
\sum_i\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
\right)^{1/2}
=
\frac1{\sqrt2}\|c_{\rm act}\|
\le
\frac1{\sqrt2}\|c\|
<
\frac34\|c\|.
\]
Hence the theorem's perturbation inequality holds.

The weave using \(\Lambda_i\) on the first \(64\) active indices and \(\Gamma_i\) on the next \(64\) uses only the \(e_1\)-coordinate. Therefore its energy at \(e_2\) is zero, and it is not a \(g\)-frame.

Finally,
\[
(T_\Lambda-T_\Gamma)c
=
\frac12
\left(
\sum_{i=1}^{64}c_i
-
\sum_{i=65}^{128}c_i
\right)(e_1-e_2),
\]
so
\[
\|T_\Lambda-T_\Gamma\|=8.
\]
The operator appearing in the source hypothesis has norm \(1/\sqrt2\). The ratio is
\[
\sqrt{128},
\]
which verifies the redundancy mechanism exactly.

The publisher PDF was inspected by text and page image at both the theorem statement and the proof step containing the invalid equality.
