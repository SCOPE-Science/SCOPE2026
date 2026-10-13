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
For every
\[
1\le m\le20,
\qquad
m\le n\le30,
\]
the checker enumerates all monomial pairs
\[
(x^{m-i}y^i,\ x^{n-j}y^j).
\]

It computes
\[
g(i,j)
=
\min(i,j)+\min(m-i,n-j)
\]
directly from exponents and verifies, for every
\[
1\le k\le m,
\]
that
\[
\#\{(i,j):g(i,j)\ge k\}
=
(m+1)(n+1)-k(k+1).
\]

It also verifies the exact gcd-degree histogram:
\[
\#\{g=0\}=2,
\]
\[
\#\{g=k\}=2(k+1)
\qquad(1\le k<m),
\]
and
\[
\#\{g=m\}
=
(m+1)(n-m+1).
\]

These finite checks are regression evidence only. The infinite theorem follows from the symbolic diagonal-strip count and Euler localization.
