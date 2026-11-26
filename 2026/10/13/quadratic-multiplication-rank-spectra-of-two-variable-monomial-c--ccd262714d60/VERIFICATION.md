---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For nonzero Q, multiplication blocks below the middle inject since no degree-m relation has yet entered, and the complementary blocks surject by the perfect monomial socle pairing. The order-(m-1) middle block is tridiagonal with diagonal b and off-diagonals a,c. With either off-diagonal nonzero an end-to-end kernel recurrence leaves at most one free coordinate; with both zero the nonzero form is invertible on the block. The total maximal rank is (m-1)^2; xy attains it, and x^2 attains one less. For ac=0 the determinant vanishes just when b=0. For ac≠0 the characteristic-root calculation gives a zero for unequal roots iff their ratio is a nontrivial m_0-th root of unity, and for equal roots iff p divides m. The parameter b²/(ac)=2+xi+xi^(-1) identifies exactly each inverse pair, and Frobenius fixes its value iff xi^(q-1)=1 or xi^(q+1)=1. The two groups intersect exactly at the inversion-fixed roots in their union. This accounts for the half-sum and the deleted identity when p does not divide m. The t=0 fibers take b=0 and arbitrary nonzero a,c; at t≠0 arbitrary nonzero a,b determine c. This works also in characteristic two. Independent ungraded matrix multiplication ranks matched the enumerator in all 21 exhaustively enumerated (m,q) pairs tested over F_2, F_3, F_5 and F_9; for example (m,q)=(8,9) yielded multiplicities (1,272,456) at ranks (0,48,49).

## originality

PASS

The general-m count is the supported distinct claim. The m=3 count is already a mechanical rank projection and homogeneous slice of a same-day indexed Jordan census, with no priority conclusion from that date. The central determinant is also covered at the level of a prior general multiplication determinant after splitting the quadratic. Neither comparison covers the all-m finite-field coefficient enumerator.

## value

PASS

This classifies the full multiplication-rank distribution in the complete space of homogeneous quadratic multipliers, a natural family of Lefschetz operators. It supplies the exact frequency of failure and shows which arithmetic data control it even for nonsplit forms and nonseparable characteristic. The exact formula across all m and q is useful beyond either an isolated census or a determinant test for one form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
