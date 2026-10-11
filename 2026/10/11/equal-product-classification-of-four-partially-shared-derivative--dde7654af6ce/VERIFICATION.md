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

The source proof supplies
\[
f'=\kappa(f-a)(f-b),
\qquad
\kappa\ne0,
\]
where
\[
a,b
\]
are the two Picard exceptional values among the four partially shared values.

If
\[
c,d
\]
are the other two values, then they are attained and partial sharing gives
\[
\kappa(c-a)(c-b)=c,
\qquad
\kappa(d-a)(d-b)=d.
\]
Thus they are the roots of
\[
\kappa(y-a)(y-b)-y,
\]
whose root product is
\[
ab.
\]
Therefore
\[
cd=ab.
\]

For the converse assume
\[
ab=cd
\]
with all four values distinct and nonzero. Then
\[
c+d-a-b\ne0,
\]
because equal sum and equal product would otherwise force the two unordered pairs to coincide.

Set
\[
\kappa=(c+d-a-b)^{-1},
\quad
q(z)=\eta e^{\kappa(a-b)z},
\quad
f(z)=\frac{a-bq(z)}{1-q(z)}.
\]
Exact differentiation gives
\[
f'=\kappa(f-a)(f-b).
\]
Moreover,
\[
\kappa(y-a)(y-b)-y
=
\kappa(y-c)(y-d).
\]
Since
\[
q(\mathbb C)=\mathbb C^*,
\]
the function omits exactly
\[
a,b
\]
and attains every other finite value. Hence the finite partially shared values are exactly
\[
a,b,c,d.
\]

All verification is symbolic and exact. No numerical experiment, finite enumeration, or unproved completeness inference is used.
