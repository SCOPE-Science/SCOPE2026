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
1\le n\le7,
\qquad
2\le d\le10.
\]

For each exponent vector it computes the first monomial catalecticant rank as the support size and the second monomial catalecticant rank as the number of degree-two exponent vectors dominated by it.

For \(d\ge3\), every monomial not of the form
\[
x_i^d
\]
or
\[
x_i^{d-1}x_j
\qquad(i\ne j)
\]
is verified to have a first or second catalecticant rank at least three. The number of surviving fixed monomials is checked to be
\[
(n+1)^2.
\]

For \(d=2\), all degree-two monomials survive and their number is checked to be
\[
\binom{n+2}{2}.
\]

The exact-stratum Euler values are checked by subtracting \(n+1\), the Euler characteristic of the Veronese variety.

Finite checks are regression evidence only. The all-parameter result is proved symbolically in the accompanying result.
