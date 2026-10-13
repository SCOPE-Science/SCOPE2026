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
3\le d\le12.
\]

For each exponent vector it computes support size and catalecticant ranks by counting degree-\(k\) divisor monomials. It verifies the symbolic fixed-point classification:
\[
\underline{\operatorname{rank}}\le3
\]
occurs only for pure powers and two-variable monomials whose smaller exponent is at most two, except that the three-support cubic is explicitly excluded by the Aronhold check.

It then confirms the three fixed-point totals and their differences from the border-rank-two total
\[
(n+1)^2.
\]

For the torus action, it uses
\[
B=d+1
\]
and checks that every degree-\(d\) exponent vector has a distinct weight
\[
\sum_i\alpha_iB^i.
\]

Finite enumeration does not prove the all-parameter theorem. The proof is the symbolic catalecticant, Aronhold, degeneration, and Euler-localization argument in `RESULT.md`.
