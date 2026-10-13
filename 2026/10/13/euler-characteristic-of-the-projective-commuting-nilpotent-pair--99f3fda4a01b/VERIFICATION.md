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
The checker tests the explicit one-parameter weights for
\[
2\le n\le30.
\]

It verifies that all off-diagonal weights within each matrix factor are distinct, that the two factors' off-diagonal weight sets are disjoint, and that neither set collides with a diagonal weight.

It confirms that the predicted number of isolated nilpotent coordinate fixed points is
\[
2n(n-1).
\]

For
\[
2\le n\le12,
\]
it also constructs every off-diagonal matrix unit and verifies directly that its square is zero.

Finite checks are regression evidence only. The theorem for all \(n\) is the symbolic fixed-point and Euler-localization proof in `RESULT.md`.
