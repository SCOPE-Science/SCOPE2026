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

The exact source reparameterization is
\[
\ell=2\arccos\sqrt{1-2L},
\qquad
L=\frac{1-\cos\ell}{4}.
\]
The source quotient formula used by the checker is
\[
Q(\ell)=4(2\pi)^{1/3}
\frac{\sin\ell-\ell\cos\ell}
{\left(3\sin\ell+\frac13\sin(3\ell)-4\ell\cos\ell\right)^{2/3}}.
\]

The checker verifies first that
\[
Q\!\left(\frac\pi2\right)=(18\pi)^{1/3}.
\]
Writing
\[
u=\ell-\frac\pi2,
\]
it then obtains symbolically
\[
\frac{Q(\ell)}{(18\pi)^{1/3}}
=
1+\frac{\pi^2-8}{16}u^2
+\frac{\pi(48-5\pi^2)}{96}u^3
+O(u^4).
\]

The exact change of variable is
\[
d=L-\frac14=\frac{\sin u}{4},
\]
so
\[
u=4d+\frac{32}{3}d^3+O(d^5).
\]
Substitution gives
\[
\frac{Q(L)}{(18\pi)^{1/3}}
=
1+(\pi^2-8)d^2
+\frac{2\pi}{3}(48-5\pi^2)d^3
+O(d^4).
\]

The checker also proves the sign statements by exact symbolic inequalities reduced to
\[
\pi^2>8
\]
and
\[
5\pi^2>48.
\]
Both are independently bounded using rational inequalities for \(\pi\) inside the checker rather than floating-point comparison.

No finite numerical sampling is used as proof. Decimal output, if shown, is diagnostic only.
