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

For
\[
F(x)
=
\sum_{j\ge1}2^{-j}\sin(2^jx_1),
\]
take
\[
J=\lfloor\log_2(1/r)\rfloor.
\]
For every increment of length at most \(r\),
\[
\omega_F(r)
\le
Jr+2^{1-J}
=
\frac{r\log(1/r)}{\log2}+O(r).
\]

At the increment
\[
re_1,
\]
the normalized first \(J\) terms satisfy
\[
\sum_{j\le J}
\frac{\sin(2^jr)}{2^jr}
=
J+O(1),
\]
because
\[
\sum_{j\le J}(2^jr)^2=O(1).
\]
The normalized tail is also \(O(1)\). Hence
\[
F(re_1)/r
=
J+O(1),
\]
which proves
\[
\omega_F(r)
=
\frac{r\log(1/r)}{\log2}+O(r).
\]

For the hyperbolic Poisson extension \(U\), positivity and unit mass of the horizontal Poisson kernel give
\[
\lvert U(x+h,y)-U(x,y)\rvert
\le
\omega_F(\lvert h\rvert).
\]
The primary source gives
\[
\sup\lvert\partial_yU\rvert\le C_d.
\]
Therefore
\[
\omega_U(r)
\le
\omega_F(r)+C_dr.
\]
Since the boundary trace of \(U\) is \(F\),
\[
\omega_U(r)\ge\omega_F(r).
\]
The same exact leading coefficient follows.

The proof is analytic and uniform in small \(r\). No finite computation or numerical experiment is used to infer the limiting statement.
