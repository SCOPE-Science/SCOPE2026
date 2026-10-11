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

The primal norm is
\[
N_\omega(s,t)=
\max\{|s|+\omega|t|,\ \omega|s|+|t|\},
\]
and its dual is
\[
N_\omega^*(a,b)=
\max\left\{
|a|,\ |b|,\ \frac{|a|+|b|}{1+\omega}
\right\}.
\]

For facet normals
\[
f_0=(1,\omega),\ f_1=(\omega,1),\
f_2=(-\omega,1),\ f_3=(-1,\omega),
\qquad f_{j+4}=-f_j,
\]
the eight coefficient pairs
\[
\left(
\frac{N_\omega^*(f_0+f_j)}2,
\frac{N_\omega^*(f_0-f_j)}2
\right)
\]
are exactly
\[
(1,0),\ (1,\delta),\ (k,k),\ (\omega,1),\
(0,1),\ (\delta,1),\ (k,k),\ (1,\omega),
\]
where
\[
\delta=\frac{1-\omega}{1+\omega},
\qquad
k=\frac12\max\left\{1+\omega,\frac2{1+\omega}\right\}.
\]

For \(p>1\), Hölder converts a constraint
\[
\alpha a+\beta b\ge1
\]
into
\[
a^p+b^p\ge
(\alpha^{p'}+\beta^{p'})^{1-p}.
\]
Thus the only possible sharp branches are
\[
A=(1+\delta^{p'})^{1-p},
\qquad
B=(1+\omega^{p'})^{1-p},
\]
plus
\[
C=2^{1-p}k^{-p}.
\]

If \(\omega\le\sqrt2-1\),
\[
2\le(1+\omega)^{p'}+(1-\omega)^{p'}
\]
implies \(C\ge A\). If \(\omega\ge\sqrt2-1\),
\[
2\left(\frac{1+\omega}{2}\right)^{p'}
\le1+\omega^{p'}
\]
implies \(C\ge B\). The switch \(A=B\) is exactly
\[
\frac{1-\omega}{1+\omega}=\omega,
\]
hence \(\omega=\sqrt2-1\).

The equality pairs in RESULT.md satisfy the corresponding unit-facet equation and the Hölder equality ratio exactly. No finite enumeration of sample points, timeout, or numerical optimizer is used to establish the theorem.
