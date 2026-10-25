---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

In ZF the generated-neighborhood definition for the fixed term □◇(+) at the least root of a poset produces a compatible certificate exactly when a set-function f:W→P selects f(u)≥u for all u. Ordinary truth is only ∀u∈W ∃v∈P with u≤v. AC supplies such selectors, and conversely an arbitrary family of nonempty sets (A_i) is encoded choice-free in a rooted height-three poset r<m_i<l_(i,a); any corresponding certificate chooses one a from each A_i, yielding full AC. On height≤2 rooted posets all non-root elements are maximal and forced into P, allowing f(u)=u except one explicitly chosen root witness. For all depth≤1 terms, compatible subcertificates for depth-zero terms appear in a fixed finite syntactic list, and choosing the least available index at each successor avoids AC in ZF. Empty family, empty successors and the root boundary were explicitly distinguished. An independent finite model checker enumerated 51 small rooted orders and 1414 valuations and found certificate/truth equivalence in finite cases; it cannot prove the ZF/AC result.

## originality

PASS

Ding–Yang prove soundness/completeness of this particular generated-bundle construction with an AC-dependent Proposition 3.2 and note choice in the proof. The inspected theorem is a sufficiency argument, not the reverse equivalence, sharp depth threshold, or height-three poset reduction to arbitrary choice families. This theorem specifies the necessary strength and exact low-depth/height boundaries.

## value

PASS

It identifies a precise logical strength of a semantic construction: a single depth-two bundled witness condition over a very small structural class already recovers the full axiom of choice, while all depth-one cases are choice-free. This is a natural structural limitation rather than a syntactic reformulation of AC alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
