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

The source coefficient is
\[
C(K)=
C_0\frac{K+1}{2\sqrt K}
+
\frac{kL(K)}2
\left(
\frac{3\sqrt3}{2}+\coth L(K)
\right)
\frac{K-1}{2\sqrt K},
\]
where
\[
k=\frac{K-1}{K+1},
\qquad
L(K)=\frac{2}{1+\sqrt{1-k^2}}.
\]

With
\[
q=\log K,
\qquad
c=\cosh(q/2),
\qquad
s=\sinh(q/2),
\]
one has
\[
k=s/c,
\qquad
L(K)=2c/(1+c),
\]
and therefore
\[
\frac{kL(K)}2
\frac{K-1}{2\sqrt K}
=
\frac{s^2}{1+c}
=
c-1.
\]
This proves the exact reduced formula.

For
\[
\ell(c)=2c/(1+c),
\]
direct differentiation gives
\[
\frac{dC}{dc}
=
C_0+\frac{3\sqrt3}{2}+\coth\ell(c)
-
\frac{2(c-1)}{(c+1)^2}\csch^2\ell(c).
\]
For
\[
c\ge1,
\]
the negative term has magnitude less than \(1/4\), whereas
\[
\coth\ell(c)>1.
\]
Hence the derivative is strictly positive.

Finally,
\[
c=1+\frac{q^2}{8}+O(q^4)
\]
and
\[
\ell(c)=1+\frac{q^2}{16}+O(q^4).
\]
Substitution gives
\[
C(K)
=
C_0+
\frac18
\left(
C_0+\frac{3\sqrt3}{2}+\coth1
\right)q^2
+
O(q^4).
\]

The verification uses exact algebra and Taylor expansion only. No finite enumeration or numerical experiment supports the proof.
