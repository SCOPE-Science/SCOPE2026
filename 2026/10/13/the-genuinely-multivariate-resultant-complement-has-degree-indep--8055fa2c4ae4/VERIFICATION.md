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
The checker treats the genuinely multivariate ranges
\[
n=3,
\qquad
1\le d_i\le3,
\]
and
\[
n=4,
\qquad
1\le d_i\le2.
\]

For each degree tuple it constructs every monomial in every coefficient factor.

The common-zero test does not use the pure-power theorem. For each monomial system it enumerates every nonempty subset of coordinate variables and asks whether a projective point with exactly that support can annihilate every monomial. This is compared with the predicted non-resultant count \(n!\).

The checker also verifies directly that the base-weight one-parameter subgroup assigns pairwise distinct weights to all monomials in every tested coefficient factor.

The regression census contains \(43\) parameter tuples, \(45275\) monomial systems, \(546\) non-resultant fixed points, and \(961\) direct weight-separation checks.

Finite checks are not used as an infinite proof. The all-degree theorem follows from the symbolic fixed-point classification in `RESULT.md`.
