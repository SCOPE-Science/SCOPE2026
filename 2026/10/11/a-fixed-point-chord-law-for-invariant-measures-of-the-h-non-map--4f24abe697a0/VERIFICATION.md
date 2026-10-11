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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It checks the invariant first-moment reduction
\[
a\mathbb E[x^2]=1-(1-b)m,
\]
the factorization
\[
a(m-x_-)(m-x_+)
=
a m^2+(1-b)m-1,
\]
and therefore
\[
\operatorname{Var}(x)
=
(x_+-m)(m-x_-).
\]

It also verifies the Euclidean scaling
\[
\operatorname{Var}(x)+\operatorname{Var}(y)
=
(1+b^2)\operatorname{Var}(x)
\]
under
\[
\operatorname{Var}(y)=b^2\operatorname{Var}(x).
\]

At
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
the checker verifies the fixed-point sum and product and the sharp bounds
\[
\operatorname{Var}(x)\le\frac{609}{784},
\]
\[
\int\|(x,y)-\bar p\|^2\,d\mu
\le
\frac{66381}{78400}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure proof is exact and does not rely on finite numerical iteration.
