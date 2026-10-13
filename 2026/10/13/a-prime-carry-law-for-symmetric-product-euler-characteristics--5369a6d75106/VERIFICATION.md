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
The geometric input is
\[
\sum_{n\ge0}\chi_c(\operatorname{Sym}^nX)t^n
=
(1-t)^{-\chi_c(X)}.
\]

If \(c=\chi_c(X)>0\), this gives
\[
E_n=\binom{c+n-1}{n}.
\]
If \(c=-m<0\), it gives
\[
E_n=(-1)^n\binom mn
\]
for \(0\le n\le m\), followed by zeros.

For a prime \(p\), Legendre's formula yields
\[
\nu_p\binom NK
=
\frac{s_p(K)+s_p(N-K)-s_p(N)}{p-1}.
\]
The numerator divided by \(p-1\) is independently identified with the number of carries in the base-\(p\) addition \(K+(N-K)\).

For a genus-\(g\) curve, \(N=2g-2\). The common divisor of the interior binomial coefficients is a prime \(p\) exactly when \(N\) is a power of \(p\), and then one coefficient has valuation exactly one. Since \(N\) is even, only \(p=2\) can occur.

The bundled checker replays all three descriptions—direct valuation, digit sums, and explicit carry counting—and independently verifies the curve gcd criterion for the stated finite test ranges. The finite computation is regression evidence only.
