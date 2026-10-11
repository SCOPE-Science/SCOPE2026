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

The exact symbolic replay checks the moment identities that drive the proof.

For normalized spherical measure,
\[
\mathbb E[u_1^2]=\frac1d,\qquad
\mathbb E[u_1^4]=\frac{3}{d(d+2)},\qquad
\mathbb E[u_1^6]=\frac{15}{d(d+2)(d+4)}.
\]
With
\[
H_2=u_1^2-\frac1d,
\qquad
H_3=u_1^3-\frac{3u_1}{d+2},
\]
the checker verifies
\[
\mathbb E[u_1H_3]=0
\]
and
\[
\mathbb E[u_1H_2H_3]
=
\frac{6(d-1)}
{d(d+2)^2(d+4)}.
\]
Therefore
\[
\int u\,h_\varepsilon^2\,d\mu
=
\frac{12(d-1)}
{d(d+2)^2(d+4)}
\varepsilon^2 e_1.
\]

The implicit-function derivative is then replayed algebraically:
\[
D_xF(0,0)=\frac{p-1}{d}I,
\]
\[
\partial_\delta F(0,0)
=
\frac{(p-1)(p-2)}2
\int u\,h_\varepsilon^2\,d\mu,
\]
so
\[
x'(0)
=
-\frac{6(p-2)(d-1)}
{(d+2)^2(d+4)}
\varepsilon^2e_1.
\]

For \(d=2\), the checker also reduces the two spherical harmonics to
\[
H_2=\frac12\cos(2\theta),
\qquad
H_3=\frac14\cos(3\theta),
\]
and verifies
\[
h_\varepsilon+h_\varepsilon''
=
1-\frac32\varepsilon\cos(2\theta)-2\varepsilon\cos(3\theta).
\]
Hence \(|\varepsilon|<2/7\) is an explicit sufficient planar convexity range.

No finite enumeration is used to infer the theorem. Existence and uniqueness of the optimal translation follow analytically from coercivity and strict convexity, and the radius dependence follows from the proved asymptotic expansion.
