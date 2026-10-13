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
The checker enumerates every integer partition for
\[
1\le d\le30.
\]

For each partition
\[
\lambda=(\lambda_1,\ldots,\lambda_e),
\]
it computes the distinct subset-sum set
\[
\Sigma(\lambda)
=
\left\{
\sum_{i\in I}\lambda_i
\right\}
\]
by exact dynamic programming.

For
\[
1\le d\le18,
\]
it independently enumerates all subsets of the labeled parts and verifies membership of every monomial exponent
\[
0\le s\le d.
\]

It also verifies that
\[
|\Sigma(\lambda)|=d+1
\]
is equivalent to
\[
a_1=1,
\qquad
a_j\le1+\sum_{i<j}a_i.
\]

Finite checks are regression evidence only. The infinite theorem is proved by unique factorization, torus fixed-point localization, and interval induction.
