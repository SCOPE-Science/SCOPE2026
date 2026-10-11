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

The exact source equation is
\[
x+2n(1-\alpha)\sum_{m=2}^{\infty}\frac{x^m}{m}
=
1+2n(1-\alpha)\sum_{m=2}^{\infty}\frac{(-1)^{m-1}}{m n^m},
\]
with
\[
x=n r_{n,\alpha}.
\]

The two series are exactly
\[
\sum_{m=2}^{\infty}\frac{x^m}{m}
=
-\log(1-x)-x
\]
and
\[
\sum_{m=2}^{\infty}\frac{(-1)^{m-1}}{m n^m}
=
\log(1+1/n)-1/n.
\]

For
\[
\tau_n=n(1-\alpha_n),
\]
the equation becomes
\[
x_n+2\tau_n\bigl(-\log(1-x_n)-x_n\bigr)
=
1+2\tau_n\bigl(\log(1+1/n)-1/n\bigr).
\]

The right correction is
\[
O(n^{-1}).
\]
Bounded
\[
\tau_n
\]
therefore yields the unique limiting profile by strict monotonicity. Divergent
\[
\tau_n
\]
forces
\[
x_n\to0,
\]
and the quadratic expansion gives
\[
\tau_nx_n^2\to1.
\]

For fixed
\[
a=1-\alpha,
\]
substitution of
\[
x=A n^{-1/2}+B n^{-1}+O(n^{-3/2})
\]
into the exact equation yields
\[
A=a^{-1/2},
\qquad
B=-\frac{5}{6a}.
\]
The exact derivative
\[
1+\frac{2na\,x}{1-x}
\]
has order
\[
n^{1/2}
\]
at this approximation, which gives the stated remainder through the mean-value theorem.

The bundled `verify_bohr_transition.py` file solves the exact equation by bisection using only the standard library. Its stored output checks the fixed-parameter normalization and three finite-transition profiles. The finite computations are sanity checks only.
