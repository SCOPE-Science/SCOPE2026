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

The accompanying `verify.py` uses only the Python standard library.

It checks:

1. The explicit witness matrix
   \[
   N=\begin{pmatrix}i&1\\1&-i\end{pmatrix}
   \]
   is symmetric, nonzero, and satisfies \(N^2=0\), hence has one Jordan block of size \(2\).
2. For every tested \(2\le n\le18\) and \(1\le k\le n-1\), every nontrivial integer partition of \(n\) has coefficient
   \[
   [x^k]\prod_j(1+x^{s_j})
   \le
   [x^k](1+x^2)(1+x)^{n-2}.
   \]
3. The right-hand side equals
   \[
   \binom{n-2}{k}+\binom{n-2}{k-2}.
   \]
4. The exact gap identity
   \[
   \binom{n}{k}
   -
   \left(\binom{n-2}{k}+\binom{n-2}{k-2}\right)
   =
   2\binom{n-2}{k-1}
   \]
   holds throughout the same stress range.
5. The coefficientwise refinement identity
   \[
   (1+x^a)(1+x^b)-(1+x^{a+b})=x^a+x^b
   \]
   is implemented directly at the coefficient-vector level for representative positive integers.

The finite partition enumeration is a stress test only. The proof in `RESULT.md` establishes the inequality for all \(n\) and \(k\) by repeated coefficientwise refinement.

The imported non-elementary premise is Friedman--Hoşten--Rosana Theorem 3.5, which supplies the exact finite count from Jordan-block sizes and the finiteness criterion. Independent audit has not been performed.
