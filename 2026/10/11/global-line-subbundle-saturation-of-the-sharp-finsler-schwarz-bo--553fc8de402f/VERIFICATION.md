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
a_i=\frac{|v_i|}{1-|z_i|^2}.
\]
The source metric is
\[
F_{t,k}^2(z;v)
=
\frac{\sum_i a_i^2+t(\sum_i a_i^{2k})^{1/k}}{1+t}.
\]

For
\[
f_0(z_1,\ldots,z_n)=(z_1,\ldots,z_1),
\]
one has
\[
df_{0,z}v=(v_1,\ldots,v_1),
\]
hence
\[
F_{t,k}^2(f_0(z);df_{0,z}v)
=
\frac{n+t\,n^{1/k}}{1+t}\,a_1^2.
\]
The source sharp factor satisfies
\[
K_{n,t,k}^2
=
\frac{n+t\,n^{1/k}}{1+t}.
\]
Therefore equality in
\[
F_{t,k}(f_0(z);df_0v)
\le
K_{n,t,k}F_{t,k}(z;v)
\]
is equivalent to
\[
a_1^2
=
\frac{\sum_i a_i^2+t(\sum_i a_i^{2k})^{1/k}}{1+t}.
\]

Both quantities
\[
\sum_i a_i^2
\quad\text{and}\quad
\left(\sum_i a_i^{2k}\right)^{1/k}
\]
are at least
\[
a_1^2.
\]
At \(t=0\), equality forces
\[
a_i=0
\quad(i\ge2).
\]
At \(t>0\), equality in the positive weighted average forces the same condition. Since the base denominators are positive, this is exactly
\[
v_2=\cdots=v_n=0.
\]

Thus the nonzero equality locus is precisely
\[
P_n\times(\mathbb C e_1\setminus\{0\}).
\]

The proof is exact and symbolic. No numerical experiment or unverified computational certificate is used.
