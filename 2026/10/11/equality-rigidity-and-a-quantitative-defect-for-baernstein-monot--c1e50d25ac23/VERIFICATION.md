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

For the global equality statement, let
\[
F_p(r)
=
\log(\|p\|_r/\|Q_n\|_r).
\]
The cited monotonicity theorem gives
\[
F_p(s)\le F_p(t)
\]
for all
\[
0\le s\le t\le\infty.
\]

For every positive exponent,
\[
M_p(r)=\int_{\mathbb T}|p|^r\,dm
\]
is real analytic. Near a zero of multiplicity
\[
m,
\]
the local model is
\[
|\theta-\theta_0|^{mr},
\]
and all parameter derivatives are dominated on compact positive-exponent intervals by integrable logarithmic powers times a fixed positive power of
\[
|\theta-\theta_0|.
\]
Hence
\[
F_p
\]
is real analytic on
\[
(0,\infty).
\]

Equality at any two distinct exponents forces a constant interval by monotonicity, hence global constancy on positive exponents by real analyticity. At
\[
r=2,
\]
the source derivative identity converts
\[
F_p'(2)=0
\]
into equality in the homogeneous entropy inequality. The published equality classification for that inequality gives exactly
\[
p(z)=c(\omega+z^n).
\]

For simple roots, the source area identity reads
\[
\mathcal P_r
=
\frac{M_{Q_n}(r)}{an}
\int_{\mathbb D}
\operatorname{Re}H_a(B)
|g'|^2\,dA,
\qquad
a=r/2,
\qquad
g=q^a.
\]
Harnack's inequality, the source value
\[
\operatorname{Re}H_a(0)=1/(a+1),
\]
and
\[
|B(z)|\le|z|
\]
give
\[
\operatorname{Re}H_a(B(z))
\ge
\frac{1-|z|}{2(a+1)}.
\]

If
\[
g(z)=\sum_{k\ge0}c_k z^k,
\]
normalized area integration gives
\[
\int_{\mathbb D}(1-|z|)|g'(z)|^2\,dA
=
\sum_{k\ge1}\frac{k}{2k+1}|c_k|^2.
\]
Substitution into the source entropy decomposition and exponent-derivative identity yields exactly
\[
F_p'(r)
\ge
\frac{
2M_{Q_n}(r)
}{
n r^2(r+2)M_p(r)
}
\sum_{k\ge1}
\frac{k}{2k+1}|c_k(r)|^2.
\]

Vanishing of the coefficient energy makes
\[
q^{r/2}
\]
constant and hence
\[
q
\]
constant. The coefficient identity
\[
q=p-zp'/n
\]
then removes every intermediate coefficient of the normalized polynomial, leaving
\[
1+z^n.
\]

The verification is analytic; no numerical experiment or finite enumeration is used.
