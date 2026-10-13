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
Set
\[
a=k-1,\qquad b=n-k,\qquad N=ab+a+b.
\]
The checker computes the Segre–Pluecker degree from
\[
D(a,b)
=
\frac{N!\,2^b\prod_{r=0}^{a-1}r!}
{(a+b)!\prod_{r=0}^{a-1}(b+r)!}
\]
and independently from the positive roots of type \(A_{n-1}\) for the highest weight
\[
(2,1,\ldots,1,0,\ldots,0).
\]

It also computes
\[
E(a,b)=\frac{(a+b+1)!}{a!\,b!}
\]
from the parabolic Weyl-group quotient.

The infinite inequality uses the exact identities
\[
\frac{R(a+1,b)}{R(a,b)}
=
\frac{(a+1)!\prod_{j=1}^{b+1}(N+j)}
{(a+b+2)!}
\]
and
\[
\frac{R(a,b+1)}{R(a,b)}
=
\frac{2(b+1)!\prod_{j=1}^{a+1}(N+j)}
{(a+b+2)!}.
\]
Termwise comparison proves both are strictly greater than \(1\) for all positive \(a,b\).

Finite checks are regression evidence only.
