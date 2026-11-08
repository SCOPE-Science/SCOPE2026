---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The original RESULT.md contains a false numerical inequality 1+ab >= (a+1)+(b+1)-1 for arbitrary a,b (a=b=1 is a counterexample), so it cannot stand unchanged as a valid proof of the minimum. The fully staged replacement RESULT.md repairs the minimum proof: if subtrees have i and m-1-i keys, a>=i+1 and b>=m-i by induction, whence 1+ab>=1+(i+1)(m-i)=m+1+i(m-1-i)>=m+1, with equality exactly at an endpoint root and minimum nonempty subtree (m>=2), giving 2^(m-1) minimizers. The original componentwise commuting criterion, uniqueness of root, and product recursion are structurally checked against Demazure-idempotent classification; independent recursive size arithmetic gives f4(5)=8, f4(6)=2, f4(7)=4. The corrected final claim holds for every m>=1, with finite rank tests as checks not proofs.

## originality

PASS

After independent comparison of statement/implication and the source inspections below, the final claim is original to the best of present knowledge, subject to the named residual risks. The corrected classification is distinct from the established general idempotent classification and Kiselman quotient Catalan count.

## value

PASS

Classifying maximal pairwise commuting idempotent sets (not maximal commutative monoid subalgebras) by labeled binary search trees yields a complete natural class of semilattices and a nontrivial full size spectrum. The sharp Catalan count, minimum and recurrence have intrinsic algebraic/combinatorial meaning and are not a mere parameter substitution into the distinct Kiselman quotient result. The corrected minimum proof preserves the same valuable classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
