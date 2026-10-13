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
X_{n,k}=\operatorname{IG}(k,2n),
\qquad
d=\frac{k(4n-3k+1)}2,
\]
the type-\(C_n\) Weyl product gives
\[
D_{n,k}
=
2^{\binom{k}{2}}d!\,
\frac{\prod_{i=0}^{k-1}i!}{\prod_{i=1}^{k}(2n-2i+1)!}.
\]

Applying
\[
\nu_2(m!)=m-s_2(m)
\]
and
\[
s_2(2r+1)=s_2(r)+1
\]
gives
\[
\nu_2(D_{n,k})
=
\frac{k(k+1)}2
-s_2(d)
+\sum_{j=n-k}^{n-1}s_2(j)
-\sum_{j=1}^{k-1}s_2(j).
\]

The bundled checker independently computes the degree from the positive-root factors and from the factorial quotient for every
\[
1\le k\le n\le60.
\]
It verifies the digit-sum valuation by direct exact valuation on all \(1830\) pairs, checks the Catalan edge through \(n=500\), and checks the maximal Lagrangian edge through \(n=200\).

Finite computation is regression evidence only.
