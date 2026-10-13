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
The checker tests the two finite combinatorial ingredients in the proof.

For
\[
2\le m\le5,
\qquad
2\le d\le8,
\]
it enumerates every exponent vector
\[
(\alpha_0,\ldots,\alpha_{m-1}),
\qquad
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=d,
\]
and confirms that the weights
\[
\sum_i\alpha_iB^i,
\qquad
B=d+1,
\]
are pairwise distinct.

For every integer partition
\[
d=d_1+\cdots+d_r,
\qquad
r\ge2,
\]
the checker explicitly distributes the \(d\) monomial factors into blocks of sizes \(d_i\) and verifies that their exponent vectors sum back to the original monomial.

It also verifies the fixed-point count
\[
\#\{\text{degree-}d\text{ monomials in }m\text{ variables}\}
=
\binom{d+m-1}{m-1}.
\]

Finite checks are regression evidence only. The infinite theorem is proved by base-\(B\) uniqueness, prescribed-degree monomial factorization, and Euler localization.
