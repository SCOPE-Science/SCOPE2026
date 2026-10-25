---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For an arbitrary nonempty set A with f^2=f (no constants), f^k for k>0 is f, so each arrow justification set is exactly one of five possibilities: full four formal exponent blocks at a fixed diagonal; J00 at a nonfixed diagonal; J01 for (a,f(a)) nonfixed; J10 for the reverse; or empty for unrelated pairs. I inspected the four original Antić directional fixed-target-first-coordinate maximality conditions, including the empty/trivial-rule clause. Same diagonal arrows are maximal because no arrow with a different target second coordinate can contain J00. Within the forward/backward sets intersections are respectively the whole J01/J10 block; unrelated arrows have empty justifications. Cross-class comparisons fail by disjointness, lack of J00, or strict improvement on fixed diagonals, including the required reverse arrow test. This establishes the four classes for infinite A without finite extrapolation; singleton A handled separately. For finite n and q nonfixed points the arrow sizes n,q,q,n(n-1)-2q give n^2+2q^2+[n(n-1)-2q]^2 satisfying ordered quadruples and strict decrease in q via the negative 12q+6-4n(n-1). An independently implemented finite evaluator computed actual maximality under original rules for all idempotent maps n<=4 and verified each equivalence and count; larger packaged tests were read but not represented as our independent infinite proof.

## originality

PASS

The result classifies a natural entire equational subclass of the nontrivial p-transitivity characterization question in Antić’s original monounary semantics and supplies a four-equivalence-class and degree formula. The later similarity-based analogy uses different definitions. Finite term-algebra algorithms and permutation-only analogy do not imply this idempotent-all-cardinality partition: an idempotent permutation is just the identity. Subject to possible unindexed retraction/functional-digraph treatments, best-of-knowledge original.

## value

PASS

This settles all idempotent retractions, a natural algebraic subvariety of a published monounary-transitivity classification problem, including infinite algebras. The four arrow equivalence types and finite n,q satisfying-quadruple formula are independently useful structural and enumeration results rather than isolated examples or a vocabulary change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
