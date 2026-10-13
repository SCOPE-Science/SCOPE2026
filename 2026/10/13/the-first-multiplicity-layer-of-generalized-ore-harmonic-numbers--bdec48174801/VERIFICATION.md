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

The symbolic proof is unrestricted.

The attached checker evaluates the defining divisibility condition exactly for every
\[
1\le k\le10
\]
and every
\[
2\le n\le50000
\]
with
\[
\Omega(n)\le2.
\]
It computes prime factorizations, \(\tau(n)\), and
\[
\sigma_k(n)=\prod_{p^a\parallel n}\frac{p^{k(a+1)}-1}{p^k-1}
\]
using integer arithmetic.

The complete observed hit list is asserted to be
\[
[(1,6)].
\]

The checker additionally evaluates the algebraic semiprime branches:
\[
(x-1)(y-1)=2
\]
has the unique positive solution pair \(\{x,y\}=\{2,3\}\), while
\[
(x-3)(y-3)=12
\]
has only the candidate pairs \((4,15),(5,9),(6,7)\) up to order, none compatible with two prime powers sharing the same exponent.

Finite replay is corroborative only. The proof in `RESULT.md` establishes the theorem for all \(k\) and all \(n\) in the stated multiplicity range.
