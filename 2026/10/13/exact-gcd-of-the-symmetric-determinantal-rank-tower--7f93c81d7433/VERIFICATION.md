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
The classical symmetric determinantal degree is evaluated as
\[
D_{n,n-q}
=
\prod_{j=0}^{q-1}
\frac{\binom{n+j}{q-j}}{\binom{2j+1}{j}},
\qquad
1\le q\le n-1.
\]

The symbolic proof has two independent parts.

For every prime \(p\mid n\), if
\[
q=p^{\nu_p(n)}<n,
\]
Legendre's factorial valuation formula is expanded scale by scale. At each scale
\[
p^a
\]
the complete floor-sum contribution is zero, proving
\[
p\nmid D_{n,n-q}.
\]

For
\[
n=2^e,
\]
the adjacent-corank ratio gives
\[
\nu_2(A_{2m})
=
m(e-1)-2\sum_{u=0}^{m-1}s_2(u),
\]
and a binary digit-sum inequality yields the lower bound
\[
\nu_2(A_q)\ge e-1
\]
for every proper corank. Corank two attains equality.

The bundled checker evaluates every full symmetric rank tower for
\[
2\le n\le120
\]
and verifies the theorem exactly. It also verifies the prime-primary witnesses in that range and the power-of-two valuation identities through
\[
n=256.
\]

These computations are regression evidence only.
