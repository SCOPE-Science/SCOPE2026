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
For a length-three partition \(\lambda\), Hilbert's formula is evaluated exactly as
\[
\deg(\Delta_\lambda)
=
\frac{3!}{\prod_j e_j!}\prod_j j^{e_j}.
\]

The proof uses the following exact witnesses:
\[
\deg(\Delta_{(1,1,d-2)})=3(d-2)
\]
for \(d\ge4\), and
\[
\deg(\Delta_{(1,2,d-3)})=12(d-3)
\]
for \(d\ge6\).

These imply that the common gcd has no prime factor above \(3\). The remaining \(2\)- and \(3\)-adic minima are proved by exhausting the three symmetry types of a three-part partition.

The bundled checker enumerates every partition
\[
1\le a\le b\le c,\qquad a+b+c=d
\]
for all
\[
3\le d\le500,
\]
computes the exact degree and gcd, and verifies
\[
G_d=2^{\alpha(d)}3^{\beta(d)}.
\]

The computation is regression evidence only; no finite search is used as proof of the infinite theorem.
