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
The checker enumerates all degree-\(d\) monomials for
\[
2\le n\le8,
\qquad
3\le d\le10.
\]

For each pair \((n,d)\), it verifies that the diagonal weights
\[
1,(d+1),(d+1)^2,\ldots,(d+1)^{n-1}
\]
induce distinct weights on all degree-\(d\) monomials.

It then counts exactly those monomials whose exponent vector has an entry at least
\[
d-1.
\]
For every tested higher degree, that count is \(n^2\), matching the symbolic UFD classification of the fixed locus.

The checker also evaluates the quadratic boundary and obtains \(\binom{n+1}{2}\), confirming that \(d=2\) has a different fixed-point pattern.

Finite checks are regression evidence only. The theorem for all \(n\ge2\) and \(d\ge3\) follows from the tangent-space formula, unique factorization, and Euler localization in `RESULT.md`.
