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

The source identities used are
\[
x_k
=
\frac{
3-k^2-\sqrt{(1-k^2)(9-k^2)}
}{2},
\]
\[
C(k)
=
\frac{2x_k^{3/2}}{k(1+x_k)},
\]
and
\[
r_k=\frac{\sqrt{x_k}}k.
\]

Set
\[
u=K_{\mathrm{aff}}^{-1/2}.
\]
Because
\[
K_{\mathrm{aff}}=\frac{1+k}{1-k},
\]
one has exactly
\[
k=\frac{1-u^2}{1+u^2}.
\]
Substitution gives
\[
x_k
=
\frac{
1+4u^2+u^4
-
2u\sqrt{2+5u^2+2u^4}
}{
(1+u^2)^2
}.
\]

Expanding at
\[
u=0
\]
gives
\[
x_k
=
1
-
2\sqrt2\,u
+
2u^2
+
O(u^3).
\]
This series satisfies the exact source critical equation
\[
x_k^2+(k^2-3)x_k+k^2=0
\]
to the displayed order.

Taking the positive square root and using
\[
1/k=1+2u^2+O(u^4)
\]
gives
\[
r_k
=
1-\sqrt2\,u+2u^2+O(u^3).
\]

Substitution in the exact expression for
\[
C(k)
\]
gives
\[
C(k)
=
1-2\sqrt2\,u+3u^2+O(u^3).
\]

Therefore
\[
\frac{1-C(k)}{1-r_k}\to2.
\]
Finally,
\[
u=K_{\mathrm{aff}}^{-1/2}
=
e^{-r_{\mathrm{aff}}/2},
\]
which yields the intrinsic hyperbolic-radius formulation.

Representative high-distortion numerical evaluations were used only as consistency checks. The proof is the exact algebraic expansion above.
