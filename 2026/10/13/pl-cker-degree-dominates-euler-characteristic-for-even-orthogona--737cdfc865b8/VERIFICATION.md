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
The checker evaluates the closed formulas for
\[
4\le n\le200.
\]
For each \(n\) it verifies:
\[
\deg X_n=
\frac{2(4n-7)!}{(n-1)(n-2)(2n-3)!(2n-5)!},
\]
\[
\chi_{\mathrm{top}}(X_n)=2n(n-1),
\]
\[
\frac{\deg X_{n+1}}{\deg X_n}
=
\frac{2(4n-5)(4n-3)}{n(2n-1)},
\]
and strict increase of
\[
\deg X_n/\chi_{\mathrm{top}}(X_n).
\]

A second calculation reconstructs the Weyl denominator directly from the complementary roots
\[
e_1-e_j,\ e_2-e_j,\ e_1+e_j,\ e_2+e_j
\quad(3\le j\le n),
\]
and \(e_1+e_2\), and checks that this root product equals the factorial denominator used in the proof.

Finite computation is only regression evidence. The infinite theorem is established symbolically in `RESULT.md`.
