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
The bundled checker enumerates local exponent vectors for mixed Segre--Veronese formats.

For a local monomial it computes every catalecticant rank as a coefficient of
\[
\prod_j(1+t+\cdots+t^{\alpha_j}).
\]
It verifies that maximal rank at most two occurs exactly for pure monomials and the stated near-pure degree-two or degree-at-least-three monomials.

For each tested multifactor format it forms every ambient coordinate monomial, multiplies the local maximal ranks, and checks that the resulting rank-at-most-two fixed-point set has cardinality
\[
\prod_i n_i+\sum_i a_i\prod_{j\ne i}n_j.
\]

Finite checks are regression evidence only. The all-parameter theorem follows from the symbolic flattening and tangent-space argument in `RESULT.md`.
