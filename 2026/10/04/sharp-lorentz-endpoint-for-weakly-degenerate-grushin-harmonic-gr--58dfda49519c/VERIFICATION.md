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

The primary proof gives, after normalization of an anchored ball,
\[
|\nabla_Lu(x,y)|
\le
C A |x|^{-\alpha},
\]
where \(A\) is controlled by an outer average of \(|u|\).

For
\[
q_\alpha=\frac1\alpha
\]
and \(t>0\),
\[
\left|
\left\{
|x|^{-\alpha}>t
\right\}
\cap
(-1,1)
\right|
\le
2t^{-1/\alpha}.
\]
Hence
\[
\sup_{\lambda>0}
\lambda
\left(
\frac{
|\{|\nabla_Lu|>\lambda\}|
}{|\text{box}|}
\right)^\alpha
\le
C A.
\]
Intrinsic dilation gives the factor \(r(B)^{-1}\) in the general anchored-ball statement.

For sharpness, the exact profile
\[
u_*(x,y)
=
\operatorname{sgn}(x)|x|^{1-2\alpha}
\]
satisfies
\[
|x|^{2\alpha}\partial_xu_*
=
1-2\alpha
\]
on both sides of \(x=0\), so the conormal flux matches and
\[
Lu_*=0
\]
weakly. Its intrinsic gradient is
\[
|\nabla_Lu_*|
=
(1-2\alpha)|x|^{-\alpha}.
\]

Thus the distribution tail is comparable to
\[
\lambda^{-1/\alpha}.
\]
This proves weak
\[
L^{1/\alpha}
\]
membership. Strong endpoint membership fails because the power becomes
\[
|x|^{-1}
\]
after raising to \(1/\alpha\). For every \(q>1/\alpha\), the weak-\(L^q\) quantity grows like
\[
\lambda^{1-\frac{1}{\alpha q}}
\]
and diverges.

No numerical computation is used as proof, and no endpoint statement for the global Riesz transform is inferred.
