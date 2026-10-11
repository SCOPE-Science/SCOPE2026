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

Let
\[
L=
\limsup_{r\to\infty}
\frac{N_1(r,f)}{T(r,f)}.
\]
Assume
\[
L<J(\rho)^{-1}
\]
and choose
\[
L<c<J(\rho)^{-1}.
\]

The inspected source gives normalized entire coordinates \(y\) of order at most \(\rho\) and constants with
\[
T(s,f)\le H_y(s+B)+C
\]
and
\[
N_y(t)\le N_{W_f}(t+B)+C_b.
\]
For every fixed
\[
a>1,
\]
these imply, after enlarging a constant,
\[
N_y(t)\le cH_y(at)+C.
\]

For
\[
\rho<\alpha<1,
\]
the source radius-selection proof generalizes directly to
\[
r_\nu\int_0^\infty
\frac{H_y(at)}{(r_\nu+t)^2}\,dt
\le
I_{\alpha,a}H_y(r_\nu),
\]
where
\[
I_{\alpha,a}
=
\int_0^\infty
\frac{\max\{1,(au)^\alpha\}}{(1+u)^2}\,du.
\]

Corollary 6.3 therefore gives
\[
(1-cI_{\alpha,a})H_y(r_\nu)
\le
n\log r_\nu+C.
\]
Because
\[
I_{\alpha,a}\longrightarrow J(\rho)
\]
as
\[
\alpha\downarrow\rho,
\qquad
a\downarrow1,
\]
one can make
\[
cI_{\alpha,a}<1.
\]
The resulting polynomial growth of every \(y_j\) along \(r_\nu\to\infty\) forces all sufficiently high Taylor coefficients to vanish by Cauchy's estimate. Hence every \(y_j\) is a polynomial, making \(f\) rational, contradiction.

For
\[
\rho=\frac12,
\]
substitution \(u=x^2\) gives
\[
J\!\left(\frac12\right)=1+\frac\pi4.
\]
For
\[
\rho\uparrow1,
\]
tail comparison gives
\[
J(\rho)\sim(1-\rho)^{-1}.
\]

No finite experiment, numerical optimization, or unproved classification is used.
