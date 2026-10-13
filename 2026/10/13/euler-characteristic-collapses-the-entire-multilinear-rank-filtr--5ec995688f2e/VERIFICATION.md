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
The checker tests the finite combinatorics of the proof.

For every tensor format
\[
3\le t\le5,
\qquad
2\le a_i\le4,
\]
it sets
\[
B=\max_i a_i
\]
and assigns a coordinate tensor indexed by
\[
(j_1,\ldots,j_t)
\]
the weight
\[
\sum_i j_iB^{i-1}.
\]
It verifies that all coordinate weights are distinct and that their number is
\[
N=\prod_i a_i.
\]

For every positive bound vector \(\mathbf r\), the checker assigns cumulative Euler value \(N\) and reconstructs the exact-rank values by finite poset subtraction. In every tested format the only nonzero exact-stratum value is
\[
e(1,\ldots,1)=N.
\]

Finite checks are regression evidence only. The infinite theorem follows from mixed-radix uniqueness, Euler localization, and constructible additivity.
