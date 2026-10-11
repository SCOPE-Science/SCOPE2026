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

For
\[
a>0
\]
define
\[
\phi_a(z)=\max\{0,\log|z_1|+a\}.
\]

The two entries of the maximum are plurisubharmonic, so
\[
\phi_a
\]
is plurisubharmonic. It is identically zero on
\[
|z_1|\le e^{-a}
\]
and equals
\[
\log|z_1|+a
\]
outside that cylinder, proving boundedness and continuity.

For a unit direction
\[
\xi,
\]
\[
\phi_a(w\xi)
=
\max\{0,\log|w|+\log|\xi_1|+a\}.
\]
This is harmonic on the full unit disc exactly when
\[
|\xi_1|\le e^{-a}.
\]
Otherwise its radial derivative jumps at
\[
|w|=e^{-a}/|\xi_1|.
\]

For normalized surface measure on
\[
S^{2n-1},
\]
the squared coordinate
\[
X=|\xi_1|^2
\]
has density
\[
(n-1)(1-x)^{n-2}
\]
on
\[
[0,1].
\]
Hence
\[
\begin{aligned}
\sigma\{|\xi_1|>e^{-a}\}
&=
\int_{e^{-2a}}^1
(n-1)(1-x)^{n-2}\,dx
\\
&=
(1-e^{-2a})^{n-1}.
\end{aligned}
\]

This quantity is positive for every
\[
a>0
\]
and tends to zero with
\[
a.
\]
Therefore every positive exceptional-measure tolerance admits a bounded continuous finite plurisubharmonic nonpluriharmonic example below that tolerance.

The verification is symbolic and exact; no finite experiment or numerical approximation is used.
