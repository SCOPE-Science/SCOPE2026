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
The proof uses the exact identity
\[
\deg X^\vee
=
\left(\prod_i d_i\right)
h_n(d_1-1,\ldots,d_c-1).
\]

For the first parity layer, the generating function
\[
\sum_{m\ge0}h_m(x_1,\ldots,x_c)t^m
=
\prod_i(1-x_it)^{-1}
\]
is reduced modulo \(2\). If \(e\) of the shifted degrees are odd, its reduction is
\[
(1-t)^{-e},
\]
so the relevant coefficient is
\[
\binom{n+e-1}{n}.
\]
Kummer--Lucas makes this odd exactly when
\[
n\mathbin{\&}(e-1)=0.
\]

If all defining degrees are odd, then every shifted degree has a factor \(2\), producing the exact factor \(2^n\); the argument is then repeated after dividing by \(2\).

The bundled checker computes complete homogeneous symmetric polynomials using integer dynamic programming and verifies the valuation equalities, lower bounds, universal evenness, and mod-\(4\) classifications over a bounded grid. Those finite checks are not used to infer the infinite theorem.

Limits: characteristic zero, smooth positive-dimensional nonlinear complete intersections, and only the first \(2\)-adic layer after the forced power of \(2\).
