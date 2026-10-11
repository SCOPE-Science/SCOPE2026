---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The admissible-pair characterization is exactly the finite one-point-extension condition for a poset: transitivity forces downward/upward closure and \(L<U\), and conversely those conditions define a valid extension realized by the random poset. Algebraic types are the parameter equalities. Membership in #P follows from ternary labels. For \(Q_m=P\oplus C_m\), splitting the top-chain status into all-U, an initial incomparable block with no L, and a nonempty L block gives \(c(Q_m)=c(P)+mJ(P)+\binom{m+1}{2}\); subtracting total type counts at \(m=1,2\) recovers \(J(P)\) with two queries, both having greatest elements. The inspected verifier independently checks every naturally labelled poset through five points and the reduction identity for \(m=1,2,3\).

## originality

PASS

The lower-set/upper-set description of finite one-point poset extensions is prior, and #P-completeness of counting antichains/ideals is prior. The new content is the explicit top-chain identity that transfers that hardness to finite-parameter random-poset 1-type counts, including the greatest-element promise. Resultary search found only global tuple-orbit profiles of random-poset reducts, a different invariant with no input parameter poset and no counting-complexity statement.

## value

PASS

Finite-parameter type counting is a natural quantitative model-theoretic task, and the random poset is a canonical homogeneous structure. The theorem gives an exact combinatorial representation and a sharp counting-complexity barrier, including a strong greatest-element promise, so it is useful beyond a small-instance census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
